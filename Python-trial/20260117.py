# 20260117

# 動機
# 　pythonを用いた試行錯誤と2026年1月のdailylogsとでフォルダを別にしたかった
# 実践１
#  1. 20260116のファイル作成命名1行目挿入プログラムを、別フォルダで再度作成する
#  2. プログラムを動作させて、動作結果が2026-01(Dailylogsがある方のフォルダ)に反映されるか確かめる
#  3. 動作結果が反映されていれば、20260115/0116のプログラムもPython-trialフォルダに移す
#     反映されなければ、再度検討し直す
# 仮説１
# 　ターミナルに入力する"Python..."の部分を"Python Python-trial/20260117.pyにすればできる
# 結果１
# 　できなかったのでコードを読み直す
# 　いったんコードをコミットして、実践２に移る
# 仮説２
# 　current_dir = pathlib.Path("./2026-01")で位置情報の取得に失敗した？
# 実践２
# 　./2026-01を./Python-trialに変えてみる(Python-trial内にファイルができてしまうかも、、)
# 結果２
# 　command not foundだったのでgeminiに相談
# Geminiアドバイス
# 　実行のための"Python..."のPythonは小文字のpython
# 　コードに二重動作がある(ファイル作成を指示した後に「ファイルがなければ…」の指示はおかしい)
# 実践３
# 　いったんコミットして、プログラムをコピペ、ターミナルに正しく入力
# 結果３
# 　2026-01の中に20260117.mdが作成された(動機を満たした)
# 考察
# 　直接の原因はターミナルへの記入ミス
# 　コードの二重動作が改善できたのは良かった
# 実践４
# 　いったんコミット
# 　動作結果が反映されたため、20260115/0116のプログラムもPython-trialフォルダに移す




import pathlib
from datetime import datetime

# 1. 日付からファイル名を決定
today_str = datetime.now().strftime("%Y%m%d")
filename = f"{today_str}.md"

# 2. パスの指定（動機に基づき、2026-01 を指定）
# プログラムが Python-trial にあっても、ルートから実行するならこれでOK
target_dir = pathlib.Path("./2026-01")
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