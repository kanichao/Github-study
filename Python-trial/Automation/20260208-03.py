# 最終的に完成させたもの

# ---


# 初期設定

import os
import datetime
from google.colab import userdata

import pathlib
from datetime import datetime

token = userdata.get('GITHUB_TOKEN')
username = "kanichao"
repo_name = "Github-study"
auth_url = f"https://{token}@github.com/{username}/{repo_name}.git"

if not os.path.exists(repo_name):
    !git clone {auth_url}
else:
    %cd {repo_name}
    !git pull origin main
    %cd ..


# ---


# Dailylog用ファイル作成

today = datetime.now()
today_str = today.strftime("%Y%m%d")
filename = f"{today_str}.md"
dir_name = today.strftime("%Y-%m")


target_dir = pathlib.Path(repo_name) / dir_name
target_dir.mkdir(parents=True, exist_ok=True)

test_file = target_dir / filename

if not test_file.exists():
    test_file.write_text("automated generation", encoding="utf-8")
    content = test_file.read_text(encoding="utf-8")
    header = f"# {test_file.stem}\n\n"
    test_file.write_text(header + content, encoding="utf-8")
    print(f"success: {test_file.name} was created in {target_dir.name}!")
else:
    print(f"skip: {test_file.name} already exists in {target_dir.name}.")


# ---


# READMEにファイルのリンクを挿入

new_link = f"* [{today_str}](./{dir_name}/{today_str}.md)"

readme_path = f"{repo_name}/README.md"
part1 = "<" + "!" + "-- "
part2 = "LOG_START"
part3 = " --" + ">"
anchor = part1 + part2 + part3

print(f"DEBUG: 現在のアンカーは [{anchor}] です")

with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

if anchor in content:
    if new_link not in content:
        updated_content = content.replace(anchor, f"{anchor}\n{new_link}")

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print(f"Success: {today_str} を README に追加しました。")
    else:
        print("Notice: 今日のリンクは既に存在します。")
else:
    print("Error: README 内に が見つかりません。")


# ---


# コミット

%cd {repo_name}

!git config user.email "253000329+kanichao@users.noreply.github.com"
!git config user.name "kanichao"

!git add .

!git commit -m "Automated: Update README with daily log link for $(date +%Y-%m-%d)"

!git push origin main

%cd ..

print("\n 全ての工程が完了しました！GitHub のリポジトリページをリロードして確認してください！")

