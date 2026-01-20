import pathlib
from datetime import datetime

# 1. 日付からファイル名を決定
today = datetime.now()
today_str = today.strftime("%Y%m%d")
filename = f"{today_str}.md"

# 2. パスの動的指定とディレクトリ作成（ここを修正）
# 現在の年月（YYYY-MM）を取得してディレクトリ名にする
dir_name = today.strftime("%Y-%m")
target_dir = pathlib.Path(f"./{dir_name}")

# ディレクトリの存在確認と作成を一行で実行
# parents=True: 親ディレクトリ（Github-study等）がなくても作成する
# exist_ok=True: すでにフォルダが存在していてもエラーを出さず、そのまま進む
target_dir.mkdir(parents=True, exist_ok=True)

test_file = target_dir / filename

# 3. 冪等性の確保（存在しない時だけ新規作成）
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
    