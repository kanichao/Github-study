import pathlib
import os

# 1. デスクトップにあるフォルダの場所を特定する
# ユーザー名に依存しないように「ホームディレクトリ」を起点にします
desktop_path = pathlib.Path.home() / "Desktop" / "pathlib_test"

print(f"--- 探索開始: {desktop_path} ---")

# 2. フォルダ内のファイルをスキャンする
for file_path in desktop_path.iterdir():
    if file_path.is_file():
        # ここで pathlib の属性（Property）を取り出す
        print(f"見つけたファイル: {file_path.name}")
        print(f"  - 名前（拡張子なし）: {file_path.stem}")
        print(f"  - 拡張子: {file_path.suffix}")
        print(f"  - 親フォルダ: {file_path.parent.name}")
        print("-" * 30)

# 3. 新しいファイルを作ってみる（自動化の第一歩）
new_file = desktop_path / "test_output.md"
new_file.write_text("# Hello Pathlib\nこれは自動生成されたファイルです。", encoding="utf-8")

print(f"\n[成功] {new_file.name} を作成しました。")
