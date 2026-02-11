import pathlib
from datetime import datetime, timedelta, timezone

# --- 1. タイムゾーンの設定 (JST) ---
# サーバー時刻(UTC)に関わらず、常に日本時間で計算する
JST = timezone(timedelta(hours=+9), 'JST')
today = datetime.now(JST)

today_str = today.strftime("%Y%m%d")
dir_name = today.strftime("%Y-%m")
filename = f"{today_str}.md"

# --- 2. 基準ディレクトリ（Root）の特定 ---
# スクリプトの場所が深くても、常にリポジトリのルートを起点にする
# .resolve().parents[0] はこのファイルがあるフォルダ (Automation)
# .resolve().parents[2] でリポジトリのルート (Github-study) に到達
BASE_DIR = pathlib.Path(__file__).resolve().parents[2]

# --- 3. 日記ファイルの作成 ---
target_dir = BASE_DIR / dir_name
target_dir.mkdir(parents=True, exist_ok=True)
test_file = target_dir / filename

if not test_file.exists():
    header = f"# {today_str}\n\n"
    # ここに昨日の自動化成功の証を初期テキストとして入れることも可能です
    test_file.write_text(header + "automated generation", encoding="utf-8")
    print(f"Created: {test_file}")
else:
    print(f"Skip: {test_file.name} already exists.")

# --- 4. README へのリンク挿入 ---
readme_path = BASE_DIR / "README.md"
# ADRで修正した全角のアンカーを使用
anchor = "＜!-- LOG_START --＞"
new_link = f"* [{today_str}](./{dir_name}/{today_str}.md)"

if readme_path.exists():
    content = readme_path.read_text(encoding="utf-8")
    
    # アンカーが存在し、かつ新しいリンクがまだ書かれていない場合のみ更新
    if anchor in content:
        if new_link not in content:
            updated_content = content.replace(anchor, f"{anchor}\n{new_link}")
            readme_path.write_text(updated_content, encoding="utf-8")
            print("Success: README updated with JST date.")
        else:
            print("Notice: Link already exists in README.")
    else:
        # アンカーが見つからない場合の警告（観測容易性のため）
        print(f"Warning: Anchor '{anchor}' not found in README.md")
else:
    print("Error: README.md not found at root.")
