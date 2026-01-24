import pathlib
from datetime import datetime

# 1. パスの定義
current_dir = pathlib.Path(__file__).parent
target_file = current_dir / "test_log.md"
today_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def insert_line_after_match(file_path, target_text, new_line):
    # ファイルが存在しない場合は処理を中断
    if not file_path.exists():
        print(f"Error: {file_path} does not exist.")
        return

    # 2. 全行をリストとして読み込む（シーケンス化）
    lines = file_path.read_text(encoding="utf-8").splitlines()

    # 3. インデックスの探索
    target_index = -1
    for idx, line in enumerate(lines):
        if target_text in line:
            target_index = idx
            break  # 最初に見つかった時点でループを抜ける（効率化）

    # 4. 挿入と書き出し（注釈1）
    if target_index != -1:
        # 見つかった行の「次」に挿入するため +1 する
        lines.insert(target_index + 1, new_line)
        
        # リストを文字列に戻して上書き保存
        file_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"Success: '{new_line}' was inserted at index {target_index + 1}.")
    else:
        print(f"Warning: '{target_text}' not found in the file.")

# 実行例
insert_line_after_match(
    target_file, 
    "## 現在の時間", 
    "- {today_str}"
)