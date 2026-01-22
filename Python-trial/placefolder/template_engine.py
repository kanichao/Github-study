# Geminiにコードを書いてもらってPlacefolderの動作確認をする
# 結果：
# $ python Python-trial/placefolder/template_engine.py
# Error: Template file not found.
# 考察：
# Python-trial内にplacefolderのフォルダを作ったから？
# Pathlib-path(".")はPython-trial内のことを指しているはずだから、Pathlib-path("./placefolder")にしたらどうだろう
# 一回コミットしてやり直す






import pathlib
from datetime import datetime

# 1. パスの定義
current_dir = pathlib.Path(".")
template_file = current_dir / "README_template.md"
output_file = current_dir / "README_actual.md"

# 2. 挿入するデータの生成
today_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
new_log = "- 2026-01-22: プレースホルダ置換の実験に成功\n[INSERT_HERE]"

# 3. テンプレートの読み込み（非破壊的読み込み）
if template_file.exists():
    template_content = template_file.read_text(encoding="utf-8")
    
    # 4. 置換ロジック（論理的変換）
    # [INSERT_HERE] を「新しいログ + 次回用の[INSERT_HERE]」に置き換えることで、
    # 次回も同じプレースホルダが使える状態（再帰的構造）を維持します。
    updated_content = template_content.replace("[INSERT_HERE]", new_log)
    updated_content = updated_content.replace("[LAST_UPDATE]", today_str)
    
    # 5. 出力（新規ファイルとして保存）
    output_file.write_text(updated_content, encoding="utf-8")
    print(f"Success: {output_file} has been generated/updated!")
else:
    print("Error: Template file not found.")
