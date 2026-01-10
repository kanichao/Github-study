# Github-study
to get used to using Github

<br>

---
<br>

## 2026/01/06

<br>

### purpose
* to get used to Github 
* to be able to use various techniques
* to get used to writing code in English
<br>

### method
* Asking Gemini
* Writing for myself
* Trying to take note in Psychology in English lesson

### note
<br>

> using reading material "the task of love"

<br>

#### words that I didn't know

| word | meaning |
| :--- | :--- |
| hitherto | これまで |
| sublimation | 昇華 |
| womanhood | 女性らしさ |
| reinforce | △評価 |
| dichotomy | 二分法 |
| obedient | △従順 |
| servile | 卑屈 |
<br>

#### comment to the reading material

The other day, I saw the post that said "Becoming "man" is easy. It is hard but it is only to get fame and much money and to be active in the various field but how can I become "woman" ? To praise the boring things and the boring stories?"

Certainly, I have wanted to be "man", to get wealth and fame while keep doing what I like such as wearing cute clothes and collecting stuffed toy. 

By reading today's reading material, I remenber this, and feel that this is also little proof that women are "opposite" to men.

<br>
<br>

> * comparison thinking is neutral
> * Existential vacuum
> * will to power
> * the Unheard Cry for Meaning: Psychotherapy and Humanism

<br>
<br>

---

## 20260107

<br>

### purpose
* to get used to writing code
* 可能であれば数式の書き方を身に着ける
<br>

### method
* taking note in the analytical chemistry class
* asking Gemini how to write formula
<br>

### note

$K_{a} = \frac{[H^+][A^-]}{[HA]}$

$HA_{(w)}\rightleftharpoonsH^+_{(w)}+A^-_{(w)}$

#### ↑失敗

Gemini


> 問題点: 矢印コマンドの直後に文字が続いている点です。
>
> 原因： \rightleftharpoonsH と書くと、LaTeXは \rightleftharpoonsH という名前の一つのコマンド（命令）だと解釈しようとします。しかしそのようなコマンドは存在しないため、描画エラー（あるいは無視）が発生します。

> 修正： コマンドの終わりを明示するために、半角スペースを入れる必要があります。
>
> 問題点： 数式モード $ ... $ の中では、英字はデフォルトで**斜体（Italic）になります。しかし、IUPAC（国際純正・応用化学連合）の規定では、「元素記号は直立体（アップライト）で書く」**と定められています。斜体（$H$）：物理量や変数（例: $x$, $y$, プランク定数 $h$ など）直立体（$\text{H}$）：元素記号（例：$\text{H}, \text{O}, \text{Ca}$ など）修正： \text{...} または \mathrm{...} を使って囲みます。

> 問題点： (w) はおそらく "water" の略と思われますが、化学の国際標準では aq (aqueous：水溶液の) を使用します。
>
> 添え字の是非： 状態表記を _{(aq)} のように下付きにするか、\text{HA(aq)} のようにそのまま横に並べるかは流派がありますが、現在の分析化学の主流（Harrisの教科書など）では、下付きにせずそのまま横に書くのが一般的です。

#### 修正

$\text{HA(aq)} \rightleftharpoons \text{H}^+\text{(aq)} + \text{A}^-\text{(aq)}$

<br>

### result
* too difficult
* hand-writing is much much much much easier
* I should thank gemini and people who created these mathmatical notation systems

<br>
<br>

---

## 20260108

<br>

### purpose

* to get used to writing formula

<br>

### method

* taking note in physics class
* asking gemini

<br>

### note

#### gemini
> 基本コマンド： \vec{A}

> 長い矢印（複数の文字）： \overrightarrow{AB}

#### formula by myself

$$
J = \frac{nΔW}{Δt} = \vec{E} ・(-ne\vec{v} = \vec{i} ・ \vec{E} = σ/vec{E} ・　/vec{E} = σE^2 = \frac{i^2}{σ}
$$

#### correct formula by gemini

$$
J = \frac{n \Delta W}{\Delta t} = \vec{E} \cdot (-ne\vec{v}) = \vec{i} \cdot \vec{E} = \sigma \vec{E} \cdot \vec{E} = \sigma E^2 = \frac{i^2}{\sigma}
$$

#### findings

| name | how it see | how to write |
| :--- | :---: | ---: |
| デルタ | $\Delta$ | \Delta |
| シグマ | $\sigma $ | \sigma |
| ・ | $\cdot$ | \cdot |

#### retry

$$
\vec{D} = \epsilon \vec{E} \rightleftharpoons \vec{i} = \sigma \vec{E}
$$

#### correct formula

$$
\vec{D} = \epsilon \vec{E} \quad \longleftrightarrow \quad \vec{i} = \sigma \vec{E}
$$

#### findings

| name | how it see | how to write |
| :--- | :---: | ---: |
| 対応、類似 | $\longleftrightarrow$ | \longleftrightarrow |
| 同値 | $\iff$ | \iff |
| 平衡 | $\rightleftharpoons$ | \rightleftharpoons |

### gemini

#### findings

| name | how it see | how to write |
| :--- | :---: | :--- |
| デルタ | $\Delta$ | `\Delta` |
| シグマ | $\sigma$ | `\sigma` |
| ・ | $\cdot$ | `\cdot` |

#### retry

$$
\vec{D} = \epsilon \vec{E} \rightleftharpoons \vec{i} = \sigma \vec{E}
$$

#### correct formula

$$
\vec{D} = \epsilon \vec{E} \quad \longleftrightarrow \quad \vec{i} = \sigma \vec{E}
$$

#### findings

| name | how it see | how to write |
| :--- | :---: | :--- |
| 対応、類似 | $\longleftrightarrow$ | `\longleftrightarrow` |
| 同値 | $\iff$ | `\iff` |
| 平衡 | $\rightleftharpoons$ | `\rightleftharpoons` |

#### comment
うまくいかなかったけど原因がわからないので、もう少しGithubを理解してからやり直したい

<br>
<br>
    
---

## 20260109

<br>

### week summary

$\text{chemistry formula} \rightarrow \text{OK}$

$\text{physics formula} \rightarrow \text{fault}$

$\text{taking note in English} \rightarrow \text{OK}$

↑上手くいかなかったが、今日は忙しいため、一旦明日以降に回す

<br>
<br>

---

## 20260110

<br>

今日は連日の疲労が溜まり、一日中寝込んでいた

Geminiにエンジニア関連の仕事に必要なことについて教えてもらったため、コピペして記録を残す

<br>

### Gemini's summary

# 2026/01/10: Carrier Vision and Science-oriented Python

<br>

## 1. Roles in Software Engineering (Library Metaphor)
将来のキャリアパスを理解するために、エンジニアの職種を「巨大な自動図書館」に例えて整理。

* **Backend Engineer (The Librarian):** * 図書館の「司書」と「貸出システム」を構築する役割。
    * 利用者のリクエストに対し、裏側の書庫（データベース）から情報を探し出し、適切な論理（Logic）で加工して届ける。
* **Infrastructure Engineer (The Building):** * 図書館の「建物」や「電気・水道」を管理する役割。
    * サーバー（計算資源）やネットワークを整え、システムが動く土台を作る。
* **SRE - Site Reliability Engineer (The Maintenance Robot):** * 図書館の「自動メンテナンス・ロボット」を作るエンジニア。
    * 「信頼性（故障なく動き続ける確率）」を、人手ではなく「プログラムによる自動化」で向上させる。

<br>

## 2. Action Plan for the Future
エンジニアの求人票（SRE/Backend）から逆算した、今の自分にできること。

* **Python Development:** * 単なる文法習得に留まらず、Django等のフレームワークを用いた「仕組み作り」へ。
* **Infrastructure Knowledge:** * プログラムが動く土台（Linuxやクラウド環境）への理解。
* **Team Development Mindset:** * GitHubを通じた「コードレビュー（他者による査読）」に耐えうる、論理的で透明性の高い記述。

<br>

## 3. Mastering "Science-oriented Python" on GitHub
理系学生がGitHubでPythonを学ぶことは、単なるプログラミング学習を超えた「科学的作法」の習得である。

* **Reproducibility (再現性の担保):** * コミット履歴により、物理定数や計算モデルの変更過程をすべて記録し、検証可能にする。
* **Analyzing OSS (設計図の解剖):** * NumPyやSciPy等の世界的な理系ライブラリのソースコードをGitHubで読み、論理の実装を学ぶ。
* **Logical Documentation (論理的記述):** * READMEにLaTeX（数式）とコードを併記し、「理論と実装」を一致させる訓練。

<br>

## 4. Personal Reflection
* **Health & Sustainability:** * 体調に波がある自分にとって、リモートワークが可能なエンジニア職は合理的な選択肢。
    * GitHubによる「非同期学習（自分のペースでの積み上げ）」は、自分を守る武器になる。
* **Goal:** * 「手書きの方が楽」という直感を越えて、デジタルで論理を構築する「難しさ」に慣れていく。

<br>
<br>

### 自分の今までのMarkdown形式に合うように同様の内容を修正

#### 1. Roles in Software Engineering (Library Metaphor)
将来のキャリアパスを理解するために、エンジニアの職種を「巨大な自動図書館」に例えて整理。

* **Backend Engineer (The Librarian):** 
    * 図書館の「司書」と「貸出システム」を構築する役割。
    * 利用者のリクエストに対し、裏側の書庫（データベース）から情報を探し出し、適切な論理（Logic）で加工して届ける。
* **Infrastructure Engineer (The Building):** 
    * 図書館の「建物」や「電気・水道」を管理する役割。
    * サーバー（計算資源）やネットワークを整え、システムが動く土台を作る。
* **SRE - Site Reliability Engineer (The Maintenance Robot):** 
    * 図書館の「自動メンテナンス・ロボット」を作るエンジニア。
    * 「信頼性（故障なく動き続ける確率）」を、人手ではなく「プログラムによる自動化」で向上させる。

<br>

#### 2. Action Plan for the Future
エンジニアの求人票（SRE/Backend）から逆算した、今の自分にできること。

* **Python Development:** * 単なる文法習得に留まらず、Django等のフレームワークを用いた「仕組み作り」へ。
* **Infrastructure Knowledge:** * プログラムが動く土台（Linuxやクラウド環境）への理解。
* **Team Development Mindset:** * GitHubを通じた「コードレビュー（他者による査読）」に耐えうる、論理的で透明性の高い記述。

<br>

#### 3. Mastering "Science-oriented Python" on GitHub
理系学生がGitHubでPythonを学ぶことは、単なるプログラミング学習を超えた「科学的作法」の習得である。

* **Reproducibility (再現性の担保):** 
    * コミット履歴により、物理定数や計算モデルの変更過程をすべて記録し、検証可能にする。
* **Analyzing OSS (設計図の解剖):** 
    * NumPyやSciPy等の世界的な理系ライブラリのソースコードをGitHubで読み、論理の実装を学ぶ。
* **Logical Documentation (論理的記述):** 
    * READMEにLaTeX（数式）とコードを併記し、「理論と実装」を一致させる訓練。











