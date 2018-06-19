# Chapter 5.5, Strings, Tuples, Ranges and Lists (文字列、タプル、リストの整理と文字列操作)

- 教科書5.5節の補足。
- ＜目次＞
  - <a href="#fig5.6">シーケンス集合に共通する操作（図5.6）</a>
  - <a href="#fig5.7">タプル・リスト・文字列の比較（図5.7）</a>
  - <a href="#fig5.8">strオブジェクトの操作（図5.8）</a>

<hr>

## <a name="fig5.6">シーケンス集合に共通する操作（図5.6）</a>

- 「シーケンス集合への操作」は、シーケンス集合（タプル・リスト・文字列）に共通している操作一覧。
- コード例
  - [リスト](https://docs.python.org/3.6/tutorial/introduction.html#lists)
  - [タプル・文字列](https://docs.python.org/3.6/tutorial/datastructures.html#tuples-and-sequences)
- 注意点
  - []と()の使い分け。
    - []: シーケンス集合に対する処理で用いる。
    - (): 下記2通りで使用。
      - タプルを記述する際には、()の前に変数名等を書かない。
      - 関数呼び出しを記述する際には、「関数名()」の形式で記述する。

|シーケンス集合への操作|操作の意味|
|-:|:-|
|``seq[i]``|シーケンス集合seqのi番目の要素を返す。|
|``len(seq)``|シーケンス集合seqの長さを返す。長さとは、文字列の場合は文字数、リストやタプルの場合は要素数のこと。|
|``seq1 + seq2``|2つのシーケンス集合seq1, seq2を結合したシーケンス集合を返す。|
|``n * seq``|シーケンス集合seqをn回繰り返したシーケンス集合を返す。|
|``seq[start:end]``|シーケンス集合seqのstartからendまでをスライス（切り出し）したシーケンス集合を返す。|
|``e in seq``|シーケンス集合内にオブジェクトeが存在する時にTrue、存在しない時にはFalseを返す。|
|``e not in seq``|シーケンス集合内にオブジェクトeが存在しない時にTrue、存在する時にはFalseを返す。|
|``for e in seq``|シーケンス集合各々を取り出して反復処理する|

<hr>

## <a name="fig5.7">シーケンス集合の比較（図5.7）</a>

|型|要素の型|リテラル例|可変か否か|
|:-|:-|:-|:-|
|str|文字のみ|'', 'a', 'abc'|No|
|tuple|任意の型|(), (3,), ('abc', 4)|No|
|range|int型のみ|range(10), range(1, 10, 2)|No|
|list|任意の型|[], [3], ['abc', 4]|Yes|

<hr>

## <a name="fig5.8">strオブジェクトの操作（図5.8）</a>

- コード例: [convert_text2html](https://github.com/naltoma/python_intro/blob/master/samples/convert_text2html.py)

|strオブジェクトへの操作|操作の意味|
|-:|:-|
|s.count(s1)|strオブジェクトsに、「s1」が出現する回数を返す。|
|s.find(s1)|strオブジェクトsを前から調べ、「s1」が初めて出現するインデックスを返す。もし出現しないならば-1を返す。|
|s.rfind(s1)|strオブジェクトsを後ろから調べ、「s1」が初めて出現するインデックスを返す。もし出現しないならば-1を返す。|
|s.index(s1)|s.find(s1)とほぼ同じだが、存在しない場合にエラーValueErrorを返す。|
|s.rindex(s1)|s.rfind(s1)とほぼ同じだが、存在しない場合にエラーValueErrorを返す。|
|s.lower()|strオブジェクトsを、lowercase(アルファベット小文字)に変換したオブジェクトを返す。（s自身は変換されない）|
|s.replace(old, new)|strオブジェクトsを前から調べ、文字列oldが見つかったら文字列newへ置き換えたstrオブジェクトを返す。（s自身は変換されない）|
|s.rstrip()|strオブジェクトsの最後尾にホワイトスペースがあれば、削除したオブジェクトを返す。ホワイトスペースとは半角スペースや、改行。（何を削除するか指定することも可能）|
|s.split(d)|strオブジェクトsを、指定した文字dを区切り文字と判断して複数のstrオブジェクトに分割したリストオブジェクトを返す。例えば[CSV形式](https://ja.wikipedia.org/wiki/Comma-Separated_Values)（コンマ区切り文字列）ならコンマをdで指定すると、個々の情報に分割できる。|
