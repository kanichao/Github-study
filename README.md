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

$$ J = \frac{nΔW}{Δt} = \vec{E} ・(-ne\vec{v} = \vec{i} ・ \vec{E} = σ/vec{E} ・　/vec{E} = σE^2 = \frac{i^2}{σ} $$

#### correct formula by gemini

$$J = \frac{n \Delta W}{\Delta t} = \vec{E} \cdot (-ne\vec{v}) = \vec{i} \cdot \vec{E} = \sigma \vec{E} \cdot \vec{E} = \sigma E^2 = \frac{i^2}{\sigma}$$

#### findings

* Δ: \Delta
* σ: \sigma
* ・: \cdot

#### retry

$$\vec{D} = \epsilon \vec{E} \rightleftharpoons \vec{i} = \sigma \vec{E}$$







