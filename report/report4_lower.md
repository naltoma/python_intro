# 課題レポート4: テキストファイルの統計処理その1

- ＜目次＞
  - <a href="#abst">課題概要</a>
  - <a href="#howto">取り組み方</a>
  - <a href="#report">レポートに含める内容</a>
  - <a href="#level1">課題詳細</a>
  - <a href="#upload">提出方法</a>

<hr>

## <a name="abst">課題概要</a>
- テキストファイル[target2.txt](./target2.txt)を読み込み、段落数・単語総数・ユニークな単語数を各々カウントせよ。
  - target2.txtは以下のようにしてダウンロードすること。

```
curl -O https://raw.githubusercontent.com/naltoma/python_intro/master/report/target2.txt
```

- 達成目標
  - ファイル処理（読み込み）に慣れよう。
  - リスト操作に慣れよう。
  - 変数名、関数名、コメントの大切さに気付こう。
  - docstring形式でドキュメントを書いてみよう。

<hr>

## <a name="howto">取り組み方</a>
- ペアや友人らと話し合って取り組んで構わないが、**自分自身の言葉で述べること。試して分かったこと、自身で解決できなかった部分等についてどう取り組んだか、といった過程がわかるように示すこと**。（考えを図表や文章を駆使して表現して報告する練習です）

<hr>

## <a name="report">レポートに含める内容</a>
- レポート作成は当面「googleドキュメント」を使うこと。
- レポートには下記を含めること。
  - **タイトル**
    - 今回は【プログラミング1、レポート課題4: 「テキストファイルの統計処理その1」】。
  - **提出日**: yyyy-mm-dd
  - **報告者**: 学籍番号、氏名
    - 複数人で相談しながらやった場合、相談者らを「協力者: 学籍番号、氏名」として示そう。
  - **課題説明**
    - 1,2行程度で課題の内容を説明しよう。
  - **書いたコード（関数のみでOK）**
    - 作成した関数について説明すること。
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
oct:tnal% python report4.py target2.txt
target2.txtには段落が9つ含まれています。
単語総数は322個ありました。そのうちユニークな単語数は184個です。
```

- 条件
  - 数え方について。
    - 段落数を数える際には、空行（改行だけの行）は無視して数えること。今回の例では、2行目、4行目、6行目、、が空行なので、カウントしないように。
    - 単語総数を数える際には、スペースを区切り文字として数えること。例えば4行目の「learn,」は、「learn,」という1つの単語があるものとして数えよ。
    - ユニークな単語数を数える際には、大文字小文字は同じものとして扱うこと。例えば「the」と「The」は同一単語とする。
  - 実装について。
    - スクリプトファイル名は「report4.py」とすること。
    - 最低1つは関数定義して利用すること。
      - どの処理を関数として定義するかは自由。
      - 引数・戻り値の設定に注意。例えば、引数として渡していないにも関わらず、関数内から外部の変数へアクセスするような書き方は減点対象。
    - docstring形式で「ファイル全体」と「関数」の2点について、ドキュメントを書くこと。（参考: [tic_tac_toe.py](https://github.com/naltoma/python_intro/blob/master/report/tic_tac_toe.py)）
- ヒント
  - スペースを区切り文字として単語集合に切り出すには、[str.split](https://docs.python.jp/3/library/stdtypes.html#str.split)を使おう。以下、実行例。
```
>>> hoge = 'Python is a widely'
>>> hoge
'Python is a widely'
>>> hoge.split(' ')
['Python', 'is', 'a', 'widely']
>>> fuga = hoge.split(' ')
>>> fuga
['Python', 'is', 'a', 'widely']
>>> len(fuga)
4
```
  - 大文字・小文字を同一単語として扱うには、「予め、全ての単語を大文字に変換するか、もしくは小文字に変換する」することで、後の処理を記述しやすくなる。小文字に変換するには [str.lower](https://docs.python.jp/3/library/stdtypes.html#str.lower) を使おう。以下、実行例。
```
>>> hoge = 'The the'
>>> print(hoge.lower())
the the
```
  - 行末の改行文字を削除したいのであれば、[str.rstrip()](https://docs.python.org/3/library/stdtypes.html?highlight=str.rstrip#str.rstrip) を使おう。以下、実行例。

```
>>> hoge = 'hello\n'  # '\n'は改行文字。
>>> print(hoge)   # 改行文字が含まれているため、プロンプトの前に改行だけの行が出力されている。
hello

>>> hoge.rstrip()
'hello'
>>> print(hoge.rstrip())  # 改行文字が削除されている。
hello
```
  - プログラム実行時に、コマンドラインからファイル名を指定するには sys ライブラリの [sys.args](https://docs.python.org/3/library/sys.html?highlight=sys.arg#sys.argv) を使おう。以下、コード＆実行例。exit()は、ここでは不要な命令だが、本来のプログラム上は「ファイル名が指定されていない場合には、ここでプログラムの処理を終える」ために使いことを想定した例。

```Python
# test.py として以下のコードを保存。
import sys
if len(sys.argv) == 2:
  filename = sys.argv[1]
  print('filename = {}'.format(filename))
else:
  print('Usage: python {} textfile'.format(sys.argv[0]))
  exit()
```

```
# ターミナル（シェル）で target2.txt を用意しているなら、以下の通り実行可能。
prompt % python test.py
Usage: python test.py textfile
prompt % python test.py target2.text
filename = target2.text
```

<hr>

## <a name="upload">提出方法</a>
- 提出物は「レポート」、「作成したスクリプトファイル」の2点である。
  - もしそれ以外に作成したものがあるなら、それも提出しよう。
- レポートは電子ファイルで提出するものとする。
- 提出先＆〆切: 授業ページを参照。
