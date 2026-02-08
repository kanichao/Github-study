# ---


import os
import datetime
from google.colab import userdata

import pathlib
from datetime import datetime


# ---


# やり直すとき用

!rm -rf Github-study
!git clone {auth_url}


# ---


# 1. 認証情報とパスの設定

# 前回の手順で Colab の「鍵アイコン」に保存した名前（GITHUB_TOKEN）を呼び出します

token = userdata.get('GITHUB_TOKEN')
username = "kanichao"  # あなたのユーザー名
repo_name = "Github-study"
auth_url = f"https://{token}@github.com/{username}/{repo_name}.git"


# ---


# 2. リポジトリのクローン（存在しない場合のみ）
if not os.path.exists(repo_name):
    !git clone {auth_url}
    print("Cloned repository.")
else:
    print("Repository already exists.")


# ---


# today,today_str,filenameの箱を作る
today = datetime.now()
today_str = today.strftime("%Y%m%d")
filename = f"{today_str}.md"

# 現在の年月（YYYY-MM）を取得してディレクトリ名にする
# 2026-02とかのフォルダ名になるはず

dir_name = today.strftime("%Y-%m")

# いったんtoday_str,dir_nameを表示させる
# 正しく表示されていれば次へ
# メモ：ここで、{}を使わなかったことにより日付が表示されなかったが、
# 上記プログラムを見て自分で解決した

print(f"{today_str}")
print(f"{dir_name}")


# ---


# まず、その日の日付のDailylog用ファイルを作る

target_dir = pathlib.Path(f".{repo_name}/{dir_name}")

# 名づけ

test_file = target_dir / filename

if not test_file.exists():

    # 新規作成プロセス

    test_file.write_text("automated generation", encoding="utf-8")

    # 読み込んでヘッダーを付与

    content = test_file.read_text(encoding="utf-8")
    header = f"# {test_file.stem}\n\n"
    test_file.write_text(header + content, encoding="utf-8")

    print(f"success: {test_file.name} was created in {target_dir.name}!")
else:
    # 既に存在する場合は何もしない
    print(f"skip: {test_file.name} already exists in {target_dir.name}.")
   

# ---


# リンクを作る

new_link = f"* [{today_str}](./{dir_name}/{today_str}.md)"

# リンクがあっているか確認するためにいったん表示
# 正しく表示されたら、アンカーを探して挿入

print(f"{new_link}")


# ---


# readme_pathがGithub-study/README.mdになる
# アンカーを<!-- LOG_START -->に指定する

readme_path = f"{repo_name}/README.md"
part1 = "<" + "!" + "-- "
part2 = "LOG_START"
part3 = " --" + ">"
anchor = part1 + part2 + part3


print(f"DEBUG: 現在のアンカーは [{anchor}] です") # 確認用
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()
# アンカーを探して、その直後に新しいリンクを挿入する論理

if anchor in content:
    # 既に今日の日付が含まれていないかチェック（二重追加防止）
    if new_link not in content:
      
        # replace を使い「アンカー」を「アンカー + 改行 + 新しいリンク」に置き換える
        updated_content = content.replace(anchor, f"{anchor}\n{new_link}")
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print(f"Success: {today_str} を README に追加しました。")
    else:
        print("Notice: 今日のリンクは既に存在します。")
else:
    print("Error: README 内に が見つかりません。")


# ---


# --- GitHub へ成果を送信するセル ---

# 1. ディレクトリをリポジトリへ移動

%cd {repo_name}

# 2. Git のユーザー設定（コミットの「署名」になります）

!git config user.email "kanichao@example.com"
!git config user.name "kanichao"


# 3. 変更をステージング（「このファイルを送るよ」という宣言）

!git add README.md



# 4. コミット（「何を変えたか」のメッセージを添えて記録）

!git commit -m "Automated: Update README with daily log link for $(date +%Y-%m-%d)"



# 5. プッシュ（GitHub のサーバーへ送信）

# 既に auth_url が設定されている origin を使います

!git push origin main



# 6. 元のディレクトリに戻る

%cd ..



print("\n🚀 全ての工程が完了しました！GitHub のリポジトリページをリロードして確認してください！")



# ---
