import pathlib
from datetime import datetime, timedelta, timezone

# --- 1. タイムゾーンの設定 ---
JST = timezone(timedelta(hours=+9), 'JST')
today = datetime.now(JST)
today_str = today.strftime("%Y%m%d")
dir_name = today.strftime("%Y-%m")
filename = f"{today_str}.md"

# --- 2. 基準ディレクトリ（Root）の特定 ---
# スクリプト自体がルートにあるため、.parent で OK
BASE_DIR = pathlib.Path(__file__).resolve().parent

# 【デバッグ用】定義した「後」に print する
print(f"DEBUG: Current Script: {pathlib.Path(__file__).resolve()}")
print(f"DEBUG: Calculated Root: {BASE_DIR.resolve()}")
print(f"DEBUG: Target date: {today_str}")

# --- 3. 日記ファイルの作成 ---
target_dir = BASE_DIR / dir_name
target_dir.mkdir(parents=True, exist_ok=True)
test_file = target_dir / filename

if not test_file.exists():
    header = f"# {today_str}\n\n"
    test_file.write_text(header + "automated generation", encoding="utf-8")
    print(f"Created: {test_file.name} in {target_dir.name}")
else:
    print(f"Skip: {test_file.name} already exists.")

# --- 4. README へのリンク挿入 ---
readme_path = BASE_DIR / "README.md"
anchor = "<!-- LOG_START -->" # READMEに合わせて適宜修正してください
new_link = f"* [{today_str}](./{dir_name}/{today_str}.md)"

if readme_path.exists():
    content = readme_path.read_text(encoding="utf-8")
    if anchor in content:
        if new_link not in content:
            updated_content = content.replace(anchor, f"{anchor}\n{new_link}")
            readme_path.write_text(updated_content, encoding="utf-8")
            print("Success: README updated.")
        else:
            print("Notice: Link already exists.")
    else:
        print(f"Warning: Anchor '{anchor}' not found.")
else:
    print("Error: README.md not found.")
