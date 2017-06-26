# Chapter 5.5 Dictionaries (dict型オブジェクト)

- 教科書5.5節の補足。
- ＜目次＞
  - <a href="#definition">Definition（定義）</a>
  - <a href="#init">dict型オブジェクトの作成方法</a>
  - <a href="#dict_methods">dict操作（図5.10）</a>
  - <a href="#looping">dictに対するfor文の例</a>
  - <a href="#ref">参考サイト</a>

<hr>

## <a name="definition">Definition (定義)</a>
- 呼称
  - dict型オブジェクト: dict, 辞書型オブジェクト、辞書
- 定義
  - 辞書とは「順序付けられていない集合」であり、各々の要素(value)を参照するには鍵(key)を指定する必要がある。
  - key指定には、int, str, tuple等の「immutableなオブジェクト」なら利用することができる。リストや、変数そのものといったmutableなオブジェクトはkeyとして指定することができない。
  - keyはユニークである必要がある。（重複したkeyを異なるvalueに割り当てることはできない）
- 主な用途
  - 順番を気にせず、(1)ある値を何らかのキーを付けて記憶させたい場合、(2)キーを指定して値を取り出したい場合に利用することが多い。
    - 例
      - 「アカウントe175701の最終成績は？」「e175701のレポートの提出状況は？」
      - 身の回りのデータ構造の多くは、順序よりも「keyを指定してvalueを参照する」方が都合がいい。
- list, tupleとの違い
  - list, tupleには順番があるが、**dictには順番はない**。
    - Warnings
      - for文のシーケンス集合指定のように「in dict」として辞書型を指定することは可能だが、**どの順番でkey,valueが参照されるかは「定義されていない」**。
        - 対策例
          - 順番を指定したいなら、指定順通りに並べた（ソートした）keyシーケンス集合を用意し、そのkeyシーケンス集合を指定して反復処理する。
  - リストやタプルの場合は「参照したい要素の順番(int型オブジェクト)」をインデックスとして指定することで目的の要素を参照するが、辞書の場合は「任意のオブジェクト」で指定することで目的の要素を参照する。

<hr>

## <a name="init">dict型オブジェクトの作成方法</a>
- dict型オブジェクトを作るには、大別して次の2通りの手続きで行う。考え方はリストと同じ。
  - (1) 辞書として作成したいオブジェクトを``key:value``の形式で用意し、そのオブジェクト群をカンマ(,)で列挙し、``{``〜``}``で囲う。
  - (2) 空の辞書``{}``を代入した変数を予め用意しておき、その変数に追加・削除する形で辞書を用意(更新)する。

- リストの作成例(1): ``key:value``の形で予め列挙する。

```
>>> month_numbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
>>> month_numbers['Jan']
1
>>> month_numbers[1]
'Jan'
```

- リストの作成例(2): 空の辞書を用意して、更新する。

```
>>> month_numbers = {}
>>> len(month_numbers)
0
>>> month_numbers['Jan'] = 1
>>> len(month_numbers)
1
>>> print(month_numbers)
{'Jan': 1}
>>> print(month_numbers['Jan'])
1
>>> month_numbers[1] = 'Jan'
>>> len(month_numbers)
2
>>> print(month_numbers)
{'Jan': 1, 1: 'Jan'}
>>> print(month_numbers[1])
Jan
```

<hr>

## <a name="dict_methods">dict操作（図5.10）</a>
|dict型オブジェクトへの操作|操作の意味|
|-:|:-|
|``len(d)``|dict型オブジェクトdが持つ要素数を返す。要素数は「key:value」で1件とカウント。|
|``d.keys()``|dict型オブジェクトdが持つkey一覧を返す。一覧はdict_keys型であり、list()やtuple()で型変換も可能。|
|``d.values()``|dict型オブジェクトdが持つvalue一覧を返す。一覧はdict_values型。d.keys()と同様に型変換可能。|
|``k in d``|dict型オブジェクトdの中にkというキーがある場合にTrueを返す。|
|``d[k]``|dict型オブジェクトdにおいて、キーkで参照できる値を返す。存在しない場合にはKeyErrorを返す。|
|``d.get(k, other)``|dict型オブジェクトdにおいて、キーkで参照できる値を返す。存在しない場合にはotherを返す（KeyErrorを返さない）。|
|``d[k] = value``|dict型オブジェクトdにおいて、キーkで参照できる値をvに紐付ける。既に存在する場合には置き換えられる（上書きされる）。|
|``del d[k]``|dict型オブジェクトdにおいて、キーkを削除する。（kに紐付けられていたvalueも削除される）|
|``for k in d``|dict型オブジェクトdに対して反復処理をする。|

<hr>

## <a name="looping">dictに対するfor文の例</a>
- tupleやlistと異なり、dictは「key:value」の組で1要素を表現している。この要素をkey,valueに取って反復処理させるには次のように書こう。
  - month_numbers.itemsが何を意味するかはhelpで確認してみよう。

```
>>> month_numbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
>>> for key, value in month_numbers.items():
...     print('key = {0}, value= {1}'.format(key,value))
...
key = Jan, value= 1
key = Mar, value= 3
key = 2, value= Feb
key = 3, value= Mar
key = Apr, value= 4
key = 5, value= May
key = 1, value= Jan
key = 4, value= Apr
key = May, value= 5
key = Feb, value= 2
>>>
```

- 上記以外にも、``d.keys()``でキー一覧を用意し、それを使って反復処理参照する等、同じループ処理を書くにしても様々な書き方があります。

<hr>

## <a name="ref">参考サイト</a>
- [公式ドキュメント: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
