#!/usr/bin/env python3
"""Check package structure and selected disclosure risks, not model behavior."""
from pathlib import Path
import re
import sys

try:
    import yaml
except ImportError:
    raise SystemExit("需要 PyYAML；请自行确认后安装 requirements-dev.txt 中的验证依赖。未自动下载。")

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
NAMES = {
    "author-first-person-fiction", "r01-author-feedback", "novel-logic-review",
    "novel-reader-review", "novel-quality-check", "novel-boring-detect",
    "novel-scene-director", "novel-reveal-control", "novel-opening-check",
    "novel-character-check", "novel-concept-check", "novel-character-voice",
    "novel-chapter-state",
    "novel-reference-study", "novel-setting-research", "novel-character-design",
    "novel-spatial-design", "novel-horror-design", "novel-delivery-check",
}
errors = []


def fail(path, message):
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def load_yaml(path, text):
    try:
        value = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        fail(path, f"YAML 无法解析：{exc}")
        return {}
    if not isinstance(value, dict):
        fail(path, "YAML 必须为映射")
        return {}
    return value


actual = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
if actual != NAMES:
    errors.append(f"技能目录差异：缺失 {sorted(NAMES - actual)}，多余 {sorted(actual - NAMES)}")

for name in sorted(actual):
    path = ROOT / "skills" / name / "SKILL.md"
    content = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.S)
    if not match:
        fail(path, "缺 YAML frontmatter")
        continue
    meta = load_yaml(path, match[1])
    if meta.get("name") != name:
        fail(path, "声明名称与目录不同")
    metadata = meta.get("metadata", {})
    if not isinstance(metadata, dict) or metadata.get("version") != VERSION:
        fail(path, "metadata.version 与包版本不同")
    description = meta.get("description")
    if not isinstance(description, str) or not description.strip():
        fail(path, "缺非空描述")

for path in (ROOT / "skills").glob("*/agents/openai.yaml"):
    data = load_yaml(path, path.read_text(encoding="utf-8"))
    ui = data.get("interface")
    if not isinstance(ui, dict):
        fail(path, "缺 interface 映射")
        continue
    for field in ("display_name", "short_description"):
        if not isinstance(ui.get(field), str) or not ui[field].strip():
            fail(path, f"缺 interface.{field}")
    if 'default_prompt' in ui:
        prompt = ui['default_prompt']
        if not isinstance(prompt, str) or f"${path.parents[1].name}" not in prompt:
            fail(path, "default_prompt 应含当前技能的 $调用名")

private_path = re.compile(r"(?:/Users/[^/\s]+/|/home/[^/\s]+/|[A-Za-z]:\\Users\\)")
thread_id = re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.I)
for path in sorted(ROOT.rglob("*")):
    relative = path.relative_to(ROOT)
    if any(part in {".git", "__pycache__", ".venv"} for part in relative.parts):
        continue
    if path.is_symlink():
        fail(path, "发布源不允许符号链接")
        continue
    if not path.is_file():
        continue
    if any(part in {"private", "backups", "local-results", ".skill-index"} for part in relative.parts):
        fail(path, "本地运行数据不应在发布源中")
    if path.name.startswith(".env") or path.suffix.lower() in {".jsonl", ".zip", ".sqlite", ".db"}:
        fail(path, "需要人工检查的私有/运行归档文件")
    if path.suffix not in {".md", ".yaml", ".txt"}:
        continue
    content = path.read_text(encoding="utf-8")
    if private_path.search(content) or thread_id.search(content):
        fail(path, "发现私人绝对路径或疑似会话ID")
    if path.suffix == ".md":
        for target in re.findall(r"\]\(([^)]+)\)", content):
            if re.match(r"(?:[a-z]+:|#)", target):
                continue
            target = target.strip("<>").split("#", 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                fail(path, f"无效或越界相对链接：{target}")

version = VERSION
if not re.fullmatch(r"\d+\.\d+\.\d+", version):
    errors.append("VERSION 应为 major.minor.patch")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"PASS: {len(actual)} skills，版本 {version}；结构、相对引用及限定隐私模式检查通过。")
print("未验证：模型行为、全部隐私信息、许可完备性、运行时权限或实际费用控制。")
