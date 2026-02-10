# ADR: Actionsを使った自動化

**＜概要＞** 

Dailylog作成・READMEへのリンク追加を行う[20260208.py](../Python-trial/Automation/20260208-03.py)をGitHub Actionsを用いて自動化する。

<br>
<br>

### 20260210

## ＜一回目＞

   * Geminiに提案されたコードを打ち込み、Pythonファイルの[update_log.py](../update_log.py)と
     YAMLファイルの[daily_log.yml](../.github/workflows/daily_log.yml)を作成
     * このとき、Geminiのコードをコピペするとanchor判定に失敗する事象があったことから、
       Geminiのコードの **anchor = ""** の "" の部分を **＜!-- LOG_START --＞** (表示が消えてしまわないよう＜＞は全角)に変更した。
     * 参考事例：[20260207.md](../202602/20260207.md)
       
   * Actions > Daily log Automation > Run workflow から実行
   * "Workflow run was successfully requested."と出た
   * [20260210.md](../202602/20260210.md)ができていることを確認した
   * Geminiによると、

     > もし今実行して成功した場合、今日の日付（20260210.md）のファイルがすでに作成されてしまいます。<br>
     > すると、今日の夜 0 時（UTC 15:00）に自動実行される際、「既に存在する場合は何もしない」 という 冪等性（ばくとうせい） が
     > 正しく機能し、二重にファイルが作られることはありません。<br>


   * このことから、**もう一度Run workflowをすれば、ファイル作成を回避する何かしらの事象が起こるのではないか？** と判断した。
     
<br>

## ＜二回目＞

   * 一回目と同様の手順で実行した
     
   * "Workflow run was successfully requested."と出た
     
   * README上及び202602フォルダに"20260210"は一つしかなかった <br>
     $\rightarrow$ 二重に作成されることはなかった
     
   * コミット履歴も、一回目に実行した時間のままだった
     $\rightarrow$ 上書きされてもいなかった



