# Chapter 6 Testing and Debugging（テストとデバッグ）の補足

- ＜目次＞
  - <a href="#abst">概要</a>
  - <a href="#6.1">Chapter 6.1 Testing</a>
    - <a href="#testsuit">テストスイートの考え方の例</a>
    - <a href="#6.1.1">Chapter 6.1.1 Black-Box Testing</a>
    - <a href="#6.1.2">Chapter 6.1.2 Glass-Box Testing</a>
    - <a href="#6.1.3">Chapter 6.1.3 Conducting Tests（テストの管理）</a>
  - <a href="#6.2">Chapter 6.2 Debugging</a>
    - <a href="#debug_hint">デバッグのヒント</a>
    - <a href="#6.2.3">6.2.3 When the Going Gets Tough (しんどい状況に陥ったら)</a>
    - <a href="#6.2.4">Chapter 6.2.4 And When You Have Found "The" bug（目的のバグを見つけた時）</a>
  - <a href="#ref">参考サイト</a>

<hr>

## <a name="abst">概要</a>
- Testing is the process of running a program to try and ascertain whether or not it works as intended.
  - プログラムが想定通りに動くことを検証するプロセスのこと（検証するためにプログラムを走らせる行程）を**Testing（テスト）**と呼ぶ。
- Debugging is the process of trying to fix a program that you already know does not work as intended.
  - 想定通りに動かないことが判明しているプログラムを修正するプロセスを**debugging（デバッグ）**と呼ぶ。
- 理想的には、
  - テストとデバッグは、プログラムが組み上がってから考えるのではなく、プログラムを設計しながら（テストやデバッグが）やりやすくなるように考える。
  - ヒント
    - **<font color="red">（理想的には）プログラムをいくつかの要素（関数）に分解し、実装・テスト・デバッグを他の要素から独立した形で行えるようにする。</font>**

<!--
- At this point in this book, we have discussed only one mechanism for modularizing programs, the function. So, for now, all of our examples will be based around functions.
  - ここでは1つのメカニズム「プログラムをモジュール化するための関数」についてのみ取り扱う。
  -->

<hr>

## <a name="6.1">Chapter 6.1 Testing</a>
- its purpose is to show that bugs exist, not show that a program is bug-free.
  - テストは、バグがあることを示すことが目的。バグがないことを示すためではない。バグフリー（存在しない）であることを証明することは不可能。
- test suite: the key to testing finding a collection of inputs, that has a high likelihood of revealing bugs, yet does not take too long to run.
  - テストのための入力集合をテストスイート(test suite)と呼ぶ。バグを見つけ出す可能性が高く、（実行が）長すぎないようなテストスイートが望ましい。

<hr>

### <a name="testsuit">テストスイートの考え方の例</a>
- 検討例（教科書コード）

```
def isBigger(x, y):
  """Assumes x and y are ints
      Returns True if x is less than y
      and False otherwise."""
```

- 入力x, yがint型であることを想定している。
  - int型が取りうる値を列挙（カテゴライズ）してみると、、、
    - 正か負か
      - x=正, y=正
      - x=正, y=負
      - x=負, y=正
      - x=負, y=負
    - 0か否か
      - x=0, y=0
      - x=0, y≠0
      - x≠0, y≠0
  - このように「想定できる値」をカテゴライズして列挙し、それらを入力として用意することでバグを見つける可能性を高めることができる。
  - より一般的には、コードと仕様の組み合わせから異なる経路を取る入力セットを用意する等の工夫がとられる。
    - 指標の例
      - カバー率（コード100%のうちどれだけテストで動かしたか）

- **black-box testing**: コードを見ずにテストすること。
- **glass-box testing (white-box testing)**: コードを見れる前提でテストすること。

<hr>

## <a name="6.1.1">Chapter 6.1.1 Black-Box Testing</a>
- 実装に関する知識がない状態で想定通りに動作することを確認する。

<hr>

## <a name="6.1.2">Chapter 6.1.2 Glass-Box Testing</a>
- コードを見ながらテストすること。
  - コードが見れるなら、if文, for文, while文等の条件部がどのように判定されてるかを確認できる。条件部が正しく動作するかのテスト。
- path-complete
  - あらゆるパス（実行経路）を通るようにテストすること

<hr>

## <a name="6.1.3">Chapter 6.1.3 Conducting Tests</a>
- unit testing: ユニットテスト、単体テスト。（関数単位でやるテスト）
- integration testing: 統合テスト、結合テスト。（システム全体でやるテスト）
- software quality assurance (SQA): ソフトウェアをリリースする前に、ソフトウェアの質（想定通りに機能すること）を担保する
- test drivers (**doctest, tox等のテストツール**)
  - set up the environment needed to invoke the program (or unit)to be tested, (テストに必要な環境を整える機能)
  - invoke the program (or unit) to be tested with a predefined or automatically generated sequence of inputs, (前もって用意された入力や、自動生成された入力を用いてテストする機能)
  - save the results of these invocations, (テスト結果を保存する機能)
  - check the acceptability of the results of the tests, (テスト結果へのアクセスを容易にする機能)
  - prepare an appropriate report. (適切なレポートを準備する機能)
- **stubs (スタブ)**: simulate parts of the program used by the unit being tested.
  - あるテストをするための前処理が必要な場合、その前処理の関数が完成してるなら利用したら良いが、完成していない場合には代替機能を用意する。代替機能を用意する機能をスタブと呼ぶ。

<hr>

## <a name="6.2">Chapter 6.2 Debugging</a>
- バグの種別
  - overt bug (顕在的なバグ) <-> covert bug (潜在的なバグ)
    - 顕在的なバグ: 明らかな兆候があるケース。
    - 潜在的なバグ: 明らかな兆候がないケース。
  - persistent bug (継続的なバグ) <-> intermittent bug (断続的なバグ)
    - 継続的なバグ: 再現性が明らかで、同じ入力で毎回発生するケース。
    - 断続的なバグ: 再現性が不確かで、同じ入力でも発生する場合としない場合があるケース。

<hr>

### <a name="debug_hint">デバッグのヒント</a>
- デバッグを一貫して効率よく行うには、「問題点探し」をシステマティックに管理しよう。
  - 利用可能なデータは？
  - テストの結果は？
  - どのテストが正常に通り、どのテストが失敗するのか？

<hr>

### <a name="6.2.3">6.2.3 When the Going Gets Tough (しんどい状況に陥ったら)</a>
- 一般的に疑わしいところを探ろう
  - 関数へ渡す引数の順番は誤っていないか？
  - 変数名、関数名等をスペルミスしていないだろうか？
  - 変数の初期化に失敗していないか？
  - 2つの浮動小数点数の値を「近似的に等しい」と判断するつもりで、数学の意味で「==」を使っていないか？（==は完全一致）
  - オブジェクトが等しいこと（e.g., id(L1)==id(L2)）を判断するつもりで、値だけで判定（e.g., L1==L2）していないか？
  - ビルトイン関数に副作用があることを忘れていないか？
    - 副作用がある≒同じ入力で同じ結果を返すとは限らない
  - 関数型オブジェクトの参照を、関数呼び出しへ変えるための()を付け忘れていないか？
  - 意図的でないエイリアスを作成していないか？
  - あなたがやりがちな過ちを犯していないか？
- **「何故思い通りに動かないのか？」ではなく、「何故こう動くのか？」を問え（確認せよ）。**
- バグは想定したところには恐らく存在しない可能性が高い。（想定しているならもっと早く気づくはず）
- **他の誰かに問題を説明してみよう。**
  - **テディベア効果。第三者に説明しようとするだけで気づくことが少なくない。**
- **書かれているコードやドキュメントを信用しすぎるな。コメント通りに動くとは限らない。**
- デバッグに行き詰まったら、デバッグをやめてドキュメントを書こう。
  - これまでと違う観点から物事を整理するのに役立つ。
- **一旦やめて、明日もう一度やってみよう。**
  - 没頭し過ぎるとケアレスミスであっても気づかないことがある。

<hr>

### <a name="6.2.4">Chapter 6.2.4 And When You Have Found "The" bug（目的のバグを見つけた時）</a>
- ケースバイケースだが、
  - 見つけたバグをすぐに治そうとするのではなく、そのバグの影響を理解するよう心がけよう。バグだったとしてもそれを正しい動作と見做して実装されてる機能があるかもしれない。このバグを直接修正するのが良いのか、新しい関数を用意するのが良いのか、関数を分割して実装するべきなのか、どのような代替案が良さそうか見積もろう。
  - 古いバージョンは残しておこう（バージョン管理しよう）
    - 後日やります。

<hr>

### <a name="ref">参考サイト</a>
- [ソフトウェアテスト基本テクニック](http://gihyo.jp/dev/serial/01/tech_station) by gihyo.jp
- [ソフトウェアテスト](https://ja.wikipedia.org/wiki/ソフトウェアテスト) by wikipedia
