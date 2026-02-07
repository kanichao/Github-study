import datetime
import os

# アンカーの設定
part1 = "<" + "!" + "-- "
part2 = "LOG_START"
part3 = " --" + ">"
anchor = part1 + part2 + part3

today_id = datetime.date.today().strftime("%Y%m%d")
today_label = datetime.date.today().strftime("%Y-%m-%d")
new_link = f"* [{today_label}](./Daily-Log/2026/02/{today_id}.md)"

readme_path = "README.md"

if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    if anchor in content and new_link not in content:
        updated_content = content.replace(anchor, f"{anchor}\n{new_link}")
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print("README updated.")