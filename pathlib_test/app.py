import pathlib

# 現在の場所（pathlib_test）を取得
current_dir = pathlib.Path("./pathlib_test")

# 1. 新しいファイルを作成してみる
test_file = current_dir / "20260113.md"
test_file.write_text("これはテストファイルです。", encoding="utf-8")

# 2. 作成したファイルを pathlib で読み取り、1行目を上書きする
if test_file.exists():
    content = test_file.read_text(encoding="utf-8")
    # ファイル名（20260113）をヘッダーとして追加
    header = f"# {test_file.stem}\n\n"
    test_file.write_text(header + content, encoding="utf-8")
    
    print(f"成功: {test_file.name} を作成し、ヘッダーを挿入しました。")