# ADR: Actionsを使った自動化

**概要:** 

Dailylog作成・READMEへのリンク追加を行う[20260208.py](./20260208-03.py)をGitHub Actionsを用いて自動化する。

<br>

---

<br>

### 20260210

## 一回目の実行

   * Geminiに提案されたコードを打ち込み、Pythonファイルの[update_log.py](../../update_log.py)と
     YAMLファイルの[daily_log.yml](../../.github/workflows/daily_log.yml)を作成
     * このとき、Geminiのコードをコピペするとanchor判定に失敗する事象があったことから、
       Geminiのコードの **anchor = ""** の "" の部分を **＜!-- LOG_START --＞** (表示が消えてしまわないよう＜＞は全角)に変更した。
     * 参考事例：[20260207.md](../../2026-02/20260207.md)
       
   * Actions > Daily log Automation > Run workflow から実行
   * "Workflow run was successfully requested."と出た
   * [20260210.md](../../2026-02/20260210.md)ができていることを確認した
   * Geminiによると、

     > もし今実行して成功した場合、今日の日付（20260210.md）のファイルがすでに作成されてしまいます。<br>
     > すると、今日の夜 0 時（UTC 15:00）に自動実行される際、「既に存在する場合は何もしない」 という 冪等性（ばくとうせい） が
     > 正しく機能し、二重にファイルが作られることはありません。<br>


   * このことから、**もう一度Run workflowをすれば、ファイル作成を回避する何かしらの事象が起こるのではないか？** と判断した。
     
<br>

## 二回目の実行

   * 一回目と同様の手順で実行した
     
   * "Workflow run was successfully requested."と出た
     
   * README上及び202602フォルダに"20260210"は一つしかなかった <br>
     $\rightarrow$ 二重に作成されることはなかった
     
   * コミット履歴も、一回目に実行した時間のままだった
     $\rightarrow$ 上書きされてもいなかった

<br>

---

<br>

### 20260211

## 日付が変わった後の変化

   * 本来起こるべき事象：
     * AM0:00(JST)に20260211.mdファイルが作られ、READMEにリンクが作られる
  
   * 実際に起こった事象：
     * 20260211.mdファイルおよびリンクがなく、コミット履歴にも実行記録がない状態
     * Actionsには、今日(20260211)のAM1:08(JST)にAutomationが実行されたとある
       
       $\rightarrow$ **(仮説)** 20260211に実行されたプログラムでは20260210.mdが作られてしまった？

     <br>
     
以下：参考画像のActionsの履歴

<img width="1813" height="1178" alt="image" src="https://github.com/user-attachments/assets/2c10ed22-43d3-47eb-bf35-e50b7926ce66" />

<br>
<br>

   * **疑問**
     * なぜ20260211.mdは作られなかった？
     * なぜ1:00に実行された？
    
  <br>
  
   * **仮説**
     * YAMLファイルの時刻設定の部分に問題があるのではないか？ <br>
       $\rightarrow$ Geminiに聞いてみる

<br>

   > **プログラムは動いたが、条件分岐によって意図的に『何もしない』を選択した** 状態 <br>
   > 2026-02-11 00:00 (JST) は **2026-02-10** 15:00 (UTC) のため、20260210.mdを作成しようとした　<br>
   > $\rightarrow$ **インフラ(UTC)の制約を認めつつ、アプリケーション(Python)層でJSTへ変換する**べき
   > なお、GitHubのキュー待ちによる約1時間の遅延が発生しているため、AM1:00に実行されている

<br>

   * **手法**
     * [update_log.py](../../update_log.py)のはじめのプログラムを以下に変更する

<br>


> ＃ update_log.py <br>
> from datetime import datetime, timedelta, timezone <br>
> ＃ タイムゾーンを明示的に指定 (UTC+9) <br>
> JST = timezone(timedelta(hours=+9), 'JST') <br>
> today = datetime.now(JST) ＃ サーバーがどこにあっても「日本時間」を取得 <br>
> today_str = today.strftime("%Y%m%d") <br>
> ＃ 以降の処理はそのまま

<br>


   * **仮説**
     * Pythonファイルで日本時間を取得するようにしたら、
       YAMLファイルの実行時間を0:00に変えないといけないのでは？ <br>
       $\rightarrow$ Geminiに聞いてみる

   <br>
   
   > **YAMLを変える必要はなく、Pythonだけ変えればよい** <br>
   > 実行時刻の管理は YAML に任せ、日付の判定は Python に任せている。<br>
   > $\rightarrow$ Python側が「日付を日本時間を基に正しく判断」できれば問題ない　<br>
   > これがエンジニアリングにおける **「関心の分離（Separation of Concerns）」**

<br>

  * **結論**
    * PythonファイルがJSTを取得できるよう書き換えると、プログラム内での「日付の取得」が成功するため、問題が解決する。
   
<br>
<br>

## 修正後の実行

   * Geminiに提案を受けて、[update_log.py](../../update_log.py)を書き換えた
     
   * Actionsの run workflow から手動で実行した
     
   * "Workflow run was successfully requested."と出て、アクション履歴もあるが、<br>
     コミット履歴はなく、20260211.mdファイルとREADME上のリンクはどちらも作成されなかった。<br>

     $\rightarrow$ 何も思い浮かばないのでGeminiに相談

<br>

   > 「実行は成功したのに、何も起きていない」**サイレントスキップ**の状態　<br>
   > * parents[2] とスクリプトの配置場所の不一致
   > * アンカー文字の「全角・半角」の不一致
   > * GitHub Actions の「ログ」に答えがある

   * **仮説**
     * Geminiの説明を読むに、<br>
       私は前述の ＜!-- LOG_START --＞における全角への変更をこのADR内のみで行っている認識だったが、 <br>
       GeminiはPythonファイルでもその変更をしていると捉えているようす
     * これは保守性の欠如ともいえるので、きちんと記述すべきだった。

  <br>

   * **検証**
     * Actionsの履歴を見ると、ファイルはCreatedなのに存在していないことになっていたので、アンカーの不一致が確実になった
     * Pythonファイルのアンカーが＜＞(全角)になっていた

  <br>

   * **実践**
     * アンカーを半角の＜＞に書き換えてコミットした
     * もう一度run workflowから実行

  <br>
  <br>

## アンカー変更後の実行

   * "Workflow run was successfully requested."と出たが、再び失敗 <br>
     $\rightarrow$ Geminiに相談

<br>

---

<br>

### 20260214


   * BASE_DIRの修正、正しいアンカーになっているかの確認、デバック情報を追加するプログラムの追加を行った。

   * parents[2]には「二回さかのぼる」の意味があるため、ファイルの位置をふまえた設定をするべきだった。
   * プログラムは階層順に実行されるため、一部コードの書き換えを終えた後、定義順序の確認を行う必要があった。

<br>
<br>

## 最終的な実行

   * 本日分(20260214)のファイルは正常に作成された。
   * 翌日分のファイルがうまくいくかはわからない。
     


       
