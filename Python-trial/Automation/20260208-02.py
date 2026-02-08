# Geminiに提案されたコード

import os
import pathlib
from datetime import datetime
from google.colab import userdata

# 1. 認証と変数の定義
token = userdata.get('GITHUB_TOKEN')
username = "kanichao"
repo_name = "Github-study"
auth_url = f"https://{token}@github.com/{username}/{repo_name}.git"

# 2. リポジトリの準備
if not os.path.exists(repo_name):
    !git clone {auth_url}
else:
    # 常に最新の状態を Pull してから作業を開始する（競合回避の論理）
    %cd {repo_name}
    !git pull origin main
    %cd ..

# 3. 日付とディレクトリの計算
today = datetime.now()
today_str = today.strftime("%Y%m%d")
dir_name = today.strftime("%Y-%m")
filename = f"{today_str}.md"

# 4. ディレクトリとファイルの生成
target_dir = pathlib.Path(repo_name) / dir_name
target_dir.mkdir(parents=True, exist_ok=True) # ★ディレクトリ作成の保証

test_file = target_dir / filename

if not test_file.exists():
    header = f"# {today_str}\n\n"
    body = "automated generation content\n"
    test_file.write_text(header + body, encoding="utf-8")
    print(f"Success: {test_file.name} created.")

# 5. README のリンク更新
readme_path = pathlib.Path(repo_name) / "README.md"
anchor = ""
new_link = f"* [{today_str}](./{dir_name}/{today_str}.md)"

content = readme_path.read_text(encoding="utf-8")

if anchor in content:
    if new_link not in content:
        # 状態遷移: anchor -> anchor + \n + new_link
        updated_content = content.replace(anchor, f"{anchor}\n{new_link}")
        readme_path.write_text(updated_content, encoding="utf-8")
        print("Success: README updated.")

# 6. GitHub への同期
%cd {repo_name}
!git config user.email "kanichao@users.noreply.github.com" # プライバシー保護
!git config user.name "kanichao"
!git add . # ★すべての変更（READMEと日記ファイル）を対象にする
!git commit -m "Automated update: {today_str}"
!git push origin main
%cd ..
