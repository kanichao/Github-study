import os
import pathlib
from datetime import datetime

# 1. 変数の定義（環境変数から取得する設計）
repo_name = "." # Actionsではリポジトリ内にいるためカレントディレクトリ
today = datetime.now()
today_str = today.strftime("%Y%m%d")
dir_name = today.strftime("%Y-%m")
filename = f"{today_str}.md"

# 2. 日記ファイルの作成
target_dir = pathlib.Path(dir_name)
target_dir.mkdir(parents=True, exist_ok=True)
test_file = target_dir / filename

if not test_file.exists():
    header = f"# {today_str}\n\n"
    test_file.write_text(header + "automated generation", encoding="utf-8")
    print(f"Created: {test_file}")

# 3. README へのリンク挿入
readme_path = pathlib.Path("README.md")
anchor = "<!-- LOG_START -->"
new_link = f"* [{today_str}](./{dir_name}/{today_str}.md)"

if readme_path.exists():
    content = readme_path.read_text(encoding="utf-8")
    if anchor in content and new_link not in content:
        updated_content = content.replace(anchor, f"{anchor}\n{new_link}")
        readme_path.write_text(updated_content, encoding="utf-8")
        print("README updated.")
