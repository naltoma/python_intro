# 課題レポート6: 平均値・標準偏差値の算出

- ＜目次＞
  - <a href="#abst">課題概要</a>
  - <a href="#howto">取り組み方</a>
  - <a href="#report">レポートに含める内容</a>
  - <a href="#level1">課題詳細</a>
  - <a href="#upload">提出方法</a>

<hr>

## <a name="abst">課題概要</a>
- [Iris Data Set](https://archive.ics.uci.edu/ml/datasets/iris)で提供されているデータファイルを読み込み、4変数（sepal length, sepal width, petal length, petal width）の平均値・標準偏差値を求めよ。
  - データファイルは以下のようにしてダウンロードすること。
  - データファイルの読み方
    - 1行に1サンプル分のデータが並んでいる。
    - 各サンプルは「sepal length, sepal width, petal length, petal width, name」の5項目のデータで構成される。
      - 例えば、1サンプル目は「speal length=5.1, sepal width=3.5, petal length=1.4, petal width=0.2, name=Iris-setosa」である。
    - 合計150サンプル分のデータが並んでいる。このファイルを読み込み、4変数（sepal length, sepal width, petal length, petal width）の平均値・標準偏差値を求めよ。

```
curl https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data -O
```

- 達成目標
  - ファイル処理（読み込み）に慣れよう。
  - リスト操作・数値演算に慣れよう。
  - 変数名、関数名、コメントの大切さに気付こう。
  - レポート4で読んだ[tic_tac_toe.py](https://github.com/naltoma/python_intro/blob/master/report/tic_tac_toe.py)を参考に、ドキュメントを書いてみよう。

<hr>

## <a name="howto">取り組み方</a>
- ペアや友人らと話し合って取り組んで構わないが、**自分自身の言葉で述べること。試して分かったこと、自身で解決できなかった部分等についてどう取り組んだか、といった過程がわかるように示すこと**。（考えを図表や文章を駆使して表現して報告する練習です）

<hr>

## <a name="report">レポートに含める内容</a>
- レポート作成は当面「googleドキュメント」を使うこと。
- レポートには下記を含めること。
  - **タイトル**
    - 今回は【プログラミング1、レポート課題6: 「平均値・標準偏差値の算出」】。
  - **提出日**: yyyy-mm-dd
  - **報告者**: 学籍番号、氏名
    - 複数人で相談しながらやった場合、相談者らを「協力者: 学籍番号、氏名」として示そう。
  - **課題説明**
    - 1,2行程度で課題の内容を説明しよう。
  - **書いたコード**
  - **実行結果**
  - **考察**
    - 課題への取り組みを通し、課題の意義、課題から分かったこと、今後の展望などを述べる。失敗やつまづきがあれば、それらについての失敗分析を含めること。
  - 参考リンク: [実験レポートの書き方](http://www.report.gusoku.net/jikken/jikkenreport.html)
  - その他
    - 通常は感想等をレポートには含めませんが、練習なので課題に取り組みながら何か感じたこと、悩んでいること等、書きたいことがあれば自由に書いてください。（なければ省略OK）

<hr>

## <a name="level">課題詳細</a>
- 以下に示す条件を満足しつつ、「実行イメージ」のように結果を出力するプログラムを書け。
- 実行イメージ

```
oct:tnal% python report6.py
iris.dataには150個のサンプルデータが列挙されています。
4変数について平均値・標準偏差値を求めた結果を以下に示します。
sepal length: average = 5.84, standard deviation = 0.83
 sepal width: average = 3.05, standard deviation = 0.43
petal length: average = 3.76, standard deviation = 1.76
 petal width: average = 1.2, standard deviation = 0.76
```

- ヒント
  - CSVファイルの読み込みには、(1)[csvモジュール](https://docs.python.jp/3/library/csv.html)を使うか、もしくは、(2)通常のファイル読み込み後に[str.split](https://docs.python.jp/3/library/stdtypes.html#str.split)で分割しよう。
  - [標準偏差の求め方](https://en.wikipedia.org/wiki/Standard_deviation#Uncorrected_sample_standard_deviation)
  - 平方根は[math.sqrt](https://docs.python.jp/3/library/math.html#power-and-logarithmic-functions)を利用しよう。
  - 四捨五入には、[numpy.around](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.around.html#numpy.around)を利用しよう。
    - 四捨五入を使う理由について。
      - 平均値や標準偏差を求める際に、単にfloatのまま処理すると膨大な桁数が発生してしまう。それに対して、今回扱うデータは小数点第1位までしかない。丸め誤差もあるため、小数点第3位で四捨五入し、小数点第2位までで保存＆出力するようにしよう。
      - なお、言語によって実装が異なるが、PythonやNumpyのround関数は、厳密には四捨五入とは異なる。このことは上記ドキュメントにも「Evenly round to the given number of decimals.」と書いてある通りである。何故このような仕様になっているのかは、例えば[JIS, ISO 式四捨五入](http://www.okadajp.org/RWiki/?JIS%2CISO式四捨五入)を参照すると理解しやすいかも。
    - 四捨五入をどのタイミングで使うかにより、多少結果が異なる。このため、厳密に上記と同じ結果でなくても構わない。
- 条件
  - **使用して良い外部モジュールは、上記で示したもののみとする。（csv, math.sqrt, np.around以外の外部モジュールや関数を使うのは駄目）**
  - 実装について。
    - スクリプトファイル名は「report6.py」とすること。
    - 最低1つは関数定義して利用すること。
      - どの処理を関数として定義するかは自由。
      - 引数・戻り値の設定に注意。例えば、引数として渡していないにも関わらず、関数内から外部の変数へアクセスするような書き方は減点対象。
    - docstring形式でドキュメントを書くこと。（参考: [tic_tac_toe.py](https://github.com/naltoma/python_intro/blob/master/report/tic_tac_toe.py)）

<hr>

## <a name="upload">提出方法</a>
- 提出物は「レポート」、「作成したスクリプトファイル」の2点である。
  - もしそれ以外に作成したものがあるなら、それも提出しよう。
- レポートは電子ファイルで提出するものとする。
- 提出先＆〆切: 授業ページを参照。
