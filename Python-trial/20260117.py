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
# 　いったんコードをコミットして、仮説２の検証に移る
# 仮説２
# 　current_dir = pathlib.Path("./2026-01")で位置情報の取得に失敗した？



import pathlib
from datetime import datetime

today_str = datetime.now().strftime("%Y%m%d")
filename = f"{today_str}.md"

current_dir = pathlib.Path("./2026-01")
test_file = current_dir / filename

test_file.write_text("automated generation", encoding="utf-8")
if test_file.exists():
    content = test_file.read_text(encoding="utf-8")
    header = f"# {test_file.stem}\n\n"
    test_file.write_text(header + content, encoding="utf-8")
    print(f"success: {test_file.name} was created!")


if not test_file.exists():
    test_file.write_text("automated generation", encoding="utf-8")
    print(f"success: create new file! {test_file.name} ")
else:
    print(f"skip: {test_file.name} already exists.")

