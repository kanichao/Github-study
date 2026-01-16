# 20260116
# Geminiに書いてもらったコードを参考に、日付を参照してファイルを作成・命名・一行目を作成するコードを書いた。

import pathlib
from datetime import datetime

today_str = datetime.now().strftime("%Y%m%d")
filename = f"{today_str}.md"

current_dir = pathlib.Path("./2026-01")
test_file = current_dir / filename

test_file.write_text("automated generation", encoding="utf-8")
if test_file.exists():
    content = test_file.read_text(encoding="utf-8")
    header = f"# {test_file.stem}\n\n"
    test_file.write_text(header + content, encoding="utf-8")
    print(f"success: {test_file.name} was created!")


if not test_file.exists():
    test_file.write_text("automated generation", encoding="utf-8")
    print(f"success: create new file! {test_file.name} ")
else:
    print(f"skip: {test_file.name} already exists.")
