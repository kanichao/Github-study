import pathlib

current_dir = pathlib.Path("./2026-01")

test_file = current_dir / "20260116.md"
test_file.write_text("using trial01.py", encoding="utf-8")

if test_file.exists():
    content = test_file.read_text(encoding="utf-8")
    header = f"# {test_file.stem}\n\n"
    test_file.write_text(header + content, encoding=("utf-8"))
    print(f"success: {test_file.name}")
