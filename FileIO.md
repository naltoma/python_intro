# File I/O（ファイル入出力）処理の基本

- 教科書 Chapter 4.6, Files
- ＜目次＞
  - <a href="#abst">概要</a>
  - <a href="#write-ex1">コード例1（write1.py）：ファイルに書き込んでみる</a>
  - <a href="#read-ex1">コード例2（read1.py）：ファイルの中身を1行ずつ読み込んでみる</a>
  - <a href="#others">代表的な読み書きのための関数</a>
  - <a href="#ref">出典</a>

<hr>

## <a name="abst">概要</a>
- 教科書の4.6節。
- File I/O = File Input/Output
  - 「ファイル、アイ、オー」
- ソースコードとは別に用意されたファイルを利用（ファイルを読み込む、ファイルへ書き込む）する方法を学ぶ。
  - Step1: 「ファイルハンドラ (file handle)」を準備する。ファイルオブジェクトとも呼ばれる。
  - Step2: ハンドラに対して読み書きする。
  - Step3: 読み書きし終えたらハンドラを閉じる。

<hr>

## <a name="write-ex1">コード例1（write1.py）：ファイルに書き込んでみる</a>
```Python
filename = 'test.txt'
with open(filename, 'w') as fh:
  name = input('あなたの名前は何ですか？ => ')
  fh.write(name + '\n')
print('ファイル書き込み終了')
```
- コード概要
  - 1行目
    - 書き込むためのファイル名を指定。
  - 2行目
    - [open()](https://docs.python.org/3/library/functions.html?highlight=open#open)は、ファイルを開き、そのファイルを処理するためのファイルハンドラを返す関数。``'w'``は、ファイルを書き込み(write)モードで開くという指定。読み込みたい場合には``'r'``。
    - ``with open() as fh:``は、(1)ファイルをopen()で開き、(2)そのファイルハンドラをfhという変数に保存する。(3)withブロック内で、fhに対する処理を記述し、(4)ブロックを抜けると、自動的にファイルを閉じる（ちゃんと保存する）。
      - with構文を使わずに書くことも可能。教科書にある最初のコード例がそれ。この場合には、(4)のfh.close()を記述し忘れることがあり、また、これだけだと様々な理由での例外時の処理をしてくれないことから、with構文の利用を推奨している。
  - 3行目
    - input()は、プログラム実行者からの入力を受け付けたい場合に利用できる関数。pydocで調べてみよう。
  - 4行目
    - ``fh.write()``は、指定したファイルハンドラ（fh）に対して、書き込むための関数。単に ``fh.write(name)``でも書き込み可能。この場合には「名前」のみ書き込むことになる。ここでは単に改行も加えたい（例えば複数人の名前をループ処理して取得したい場合には改行加えて列挙したい）という意図で、最後に ``\n`` を追加している。
  - 5行目
    - withブロックを抜けているため、ここでは既にfh.close()が自動的に実行された後。fhに対する処理をすることはできない。更にファイル操作したいなら、もう一度openし直す必要がある。
- Tips
  - ファイル操作時の注意
    - open()時の代表的なオプションは、read 'r', write 'w', append 'a' あたり。'w'は、「上書きモードで開く」点に注意。もし既にファイルの中身が存在している場合には、中身を削除した上で書き込むことになる。
  - ファイルへの書き込み方。
    - 上記コード例の通り、ファイルオブジェクトに対して wirte 関数を実行することで、指定ファイルへ書き込むことができる。これ以外にもファイルオブジェクトを指定して書き込むことは可能。例えば ``print(name, file=fh)`` としてprint関数の引数fileにファイルオブジェクトを指定すると、標準出力ではなくファイルに対して出力する（＝書き込む）ことができる。

<hr>

## <a name="read-ex1">コード例2（read1.py）：ファイルの中身を1行ずつ読み込んでみる</a>
- 事前準備
  - 中身は何でも構わないので、2〜5行程度のテキストファイルを用意する。そのファイル名を target.txt としよう。

```Python
filename = 'target.txt'
with open(filename, 'r') as fh:
  line_no = 1
  for line in fh.readlines():
    print('{}行目の中身: {}'.format(line_no, line))
    line_no += 1
print('ファイル読み込み終了')
```

-　コード概要
  - 1行目
    - ファイル名の指定。
  - 2行目
    - with構文にて、readモードでファイルハンドラを用意。
  - 3行目
    - 読み込んだ行数を表示するための変数を用意。
  - 4行目
    - ファイルハンドラから「1行を1str型オブジェクト」「そのstr型オブジェクトを要素として持つリスト」として読み込む。この要素を変数lineに保存した上で、forブロックで処理していく。
  - 5行目
    - ちゃんと読み込めてることを確認するために、出力しているだけのコード例。何もない空の行も出力されることに注意。これは「行末ある改行文字」もそのまま読み込んでいるため。改行文字を取り除きたいなら [str.rstrip()](https://docs.python.org/ja/3/library/stdtypes.html?highlight=split#str.rstrip) を使おう。
  - 6行目
    - 行番号を更新。
  - 7行目
    - withブロックを抜けているため、処理がここに辿り着いた時点でfhに対する処理は終了。
- Tips
  - ファイル読み込みには [readline関数, readlines関数](https://docs.python.org/3/library/io.html?highlight=readlines#io.IOBase.readline) が用意されている。
    - ``readline(size=-1)``
      - 引数sizeを省略した場合には、ストリーム（ここではファイルハンドラ）から1行読んで返す。
    - ``readlines(hint=-1)``
      - 引数hintを省略した場合には、ストリームからファイル全体を読んでリストとして返す。各行はstr型オブジェクトとして保存されている。ファイルサイズが巨大な場合にはメモリを超えてしまうため、readlineを使うことを検討しよう。

```Python
# readlineを使った例。
# iris.data は以下からダウンロード。
# https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
filename = 'iris.data'
with open(filename, 'r') as fh:
  line_no = 1
  while True:
    line = fh.readline()
    if line == "":
        break
    else:
        print('{}行目の中身: {}'.format(line_no, line))
        line_no += 1
print('ファイル読み込み終了')
```

<hr>

## <a name="others">代表的な読み書きのための関数</a>
- [io --- ストリームを扱うコアツール](https://docs.python.org/ja/3/library/io.html)
  - 中でも、 read(), readline(), readlines(), write(), writelines(), flush() あたりは使う可能性高いかも。

## <a name="ref">出典</a>
- 教科書4.6節。図4.12。
- [7.2. Reading and Writing Files / Python Tutorial](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Dive Into Python 3, 第11章 ファイル](http://diveintopython3-ja.rdy.jp/files.html)
- [Python3: open()](https://docs.python.org/3/library/functions.html#open)
- [io --- ストリームを扱うコアツール](https://docs.python.org/ja/3/library/io.html)
