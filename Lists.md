# リスト型オブジェクトの基本

- 教科書 Chapter 5.2, Lists and Mutability
- ＜目次＞
  - <a href="#mutable">Immutable vs. Mutable (不変 vs 可変)</a>
  - <a href="#definition">Definition（定義）</a>
  - <a href="#list_methods">リスト操作（図5.4）</a>
  - <a href="#note_clone">リスト操作時の注意点（chap 5.2.1 cloning)</a>
  -  <a href="#list_includings">リスト参照を含むリスト（図5.1〜5.3）</a>
  - <a href="#list_comprehension">リスト内包表記</a>
  - <a href="#ref">参考サイト</a>

<hr>

## <a name="mutable">Immutable vs. Mutable (不変 vs 可変)</a>
- ここでいう可変・不変は「一度紐付けたオブジェクトの**一部**を変更できるか、できないか」。
  - オブジェクト**全体**なら、``=``を使って紐付け直す（代入し直す）ことが可能。
- 不変（変更できない）オブジェクトの例
  - strings, tuples

```
# strオブジェクトで一部を変更しようとしても、出来ないことの確認。
>>> name = 'naltoma'
>>> name[0]
'n'
>>> name[0] = 'b'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

# 変数を新しく assign (紐付け) し直すことは可能。
>>> name = 'hoge'
>>> print(name)
hoge
```

- 可変（変更できる）オブジェクトの例
  - lists (今回の対象)

<hr>

## <a name="definition">Definition (定義)</a>
- リストとは「順序付けられたシーケンス集合」。オブジェクトは任意の要素を取りうる。リスト内の各objectはindexにより紐付けられる。
  - リストを作るには、大別して次の2通りの手続きで行う。
    - (1) リストとして作成したいオブジェクトをカンマ(,)で列挙し、``[``〜``]``で囲う。
    - (2) 空のリスト``[]``を代入した変数を予め用意しておき、そのリストに追加・削除する形でリストを用意(更新)する。
- リストの作成例(1): 最初から必要なオブジェクトを列挙して用意する。
```
# リストの作成例(1): 最初から必要なオブジェクトを列挙して用意する。
# 教科書 p.58 のコード例を少し修正
>>> list_ex = ['I did it all', 4, 'love']
>>> len(list_ex)
3
>>> print(list_ex[0])
I did it all
>>> print(list_ex[-1])
love
>>> print(list_ex)
['I did it all', 4, 'love']
>>> for i in range(len(list_ex)):
...     print(list_ex[i])
...
I did it all
4
love
>>> for i in list_ex:
...     print(i)
...
I did it all
4
love
# リストの一部分（ここではlist_ex[0]）を変更してみる
>>> list_ex[0] = 3
>>> print(list_ex[0])
3
>>> print(list_ex)
[3, 4, 'love']
```
- リストの作成例(2): 空のリストに、オブジェクトを追加する。
```
# リストの作成例(2): 空のリストに、オブジェクトを追加する。
>>> list_ex2 = []
>>> len(list_ex2)
0
>>> list_ex2.append(1)
>>> len(list_ex2)
1
>>> print(list_ex2)
[1]
>>> list_ex2.append('hoge')
>>> len(list_ex2)
2
>>> print(list_ex2)
[1, 'hoge']
```

<hr>

## <a name="list_methods">リスト操作（図5.4＋α）</a>
- リスト同士の結合（+演算子）
```
>>> list_ex3 = [1, 2, 3]
>>> list_ex4 = [4, 5, 6]
>>> list_ex5 = list_ex3 + list_ex4
>>> print(list_ex5)
[1, 2, 3, 4, 5, 6]
```
- list.append(object): listの後ろにobjectを追加。
```
>>> list_ex3 = [1, 2, 3]
>>> list_ex3.append(1)
>>> print(list_ex3)
[1, 2, 3, 1]
```
- list.count(object): list内にobjectがある個数を返す。
```
>>> list_ex3.count(1)
2
```
- list.insert(i, object): listのi番目にobjectを追加する。
```
>>> list_ex3.insert(0, 'hoge')
>>> print(list_ex3)
['hoge', 1, 2, 3, 1]
```
- list.extend(other_list): listの後ろに、別のリストother_listを追加する。
```
>>> list_ex3.extend(list_ex4)
>>> print(list_ex3)
['hoge', 1, 2, 3, 1, 4, 5, 6]
```
- list.remove(object): listの頭から探していき、初めに見つかったobjectを削除 する。
```
>>> list_ex3.remove(1)
>>> print(list_ex3)
['hoge', 2, 3, 1, 4, 5, 6]
```
- list.index(object): listの頭から探していき、初めに見つかったobjectのインデックスを返す。もし見つからなければErrorを返す。
```
>>> list_ex3.index(1)
3
```
- list.pop(index): list[index]の値を削除しつつ、返す。
```
>>> list_ex3.pop(0)
'hoge'
>>> print(list_ex3)
[2, 3, 1, 4, 5, 6]
```
- list.sort(): listを小さい順 (ascending order) に並べ直す。
```
>>> list_ex3.sort()
>>> print(list_ex3)
[1, 2, 3, 4, 5, 6]
```
- list.reverse(): listを逆順に並べ直す。
```
>>> list_ex3.reverse()
>>> print(list_ex3)
[6, 5, 4, 3, 2, 1]
```
- リスト要素の検索
```
>>> 3 in list_ex3
True
>>> 10 in list_ex3
False
```

<hr>

## <a name="note_clone">リスト操作時の注意点（chap 5.2.1 cloning)</a>
- 注意点: for文で反復処理をするオブジェクトとしてリストを指定している最中に、そのリスト自身に変更を加えると動作がおかしくなる。
  - 何故か？
    - for文はリストの全要素に対して反復処理する際に、インデックスを内部で参照しているため。
  - 対処法
    - (a) 反復処理対象のシーケンスとして該当リストを指定しない。
    - (b) 反復処理前にリストを複製し、反復対象のリストと、編集用のリストを分けて利用する。

- 問題のあるケース

```
def remove_dups(list1, list2):
    for e1 in list1:
        if e1 in list2:
            list1.remove(e1)

l1 = [1, 2, 3, 4]
l2 = [1, 2, 5, 6]
remove_dups(l1, l2)
print(l1)
# -> 想定では[3,4]になって欲しいが、実際には[2, 3, 4]になってしまう。
```

- 事前にリストを複製してから反復処理する例
  - 下記コード中の``list1[:]``は、「list1の最初から最後まで」を省略した書き方。
  - 教科書にある通り``for e1 in list1[:]:``に変更するだけでもOK。

```
def remove_dups(list1, list2):
    duplicate = list1[:]
    for e1 in list1:
        if e1 in list2:
            duplicate.remove(e1)
    return duplicate

l1 = [1, 2, 3, 4]
l2 = [1, 2, 5, 6]
result = remove_dups(l1, l2)
print(result)
print(l1)
```

<hr>

## <a name="list_includings">リスト参照を含むリスト（図5.1〜5.3）</a>
- リストには任意のオブジェクトを含めることができる。
  - 教科書の図5.1〜5.3は「リストが別のリストを参照している」場合に、片方のリストへの操作が別リストにも影響を及ぼすことを可視化している例。

![図5.2: univs1はtechsリストとivysリストを参照しているので、techsリストを修正するとその影響を受ける。univs2は他のリストを参照していないので、影響を受けない。](https://raw.githubusercontent.com/naltoma/python_intro/master/figs/fig5.2.png)

```
# 2つのリスト techs, ivys を用意。
>>> techs = ['MIT', 'Caltech']
>>> ivys = ['Harvard', 'Yale', 'Brown']
# 別のリスト univs1, univs2 を用意。
# このうち univs1 は、先ほど用意したリストオブジェクト techs と ivys を要素とする。
# これに対し univs2 は、既存変数とは無関係に新しくstr型オブジェクトを列挙したリストを要素とする。
>>> univs1 = [techs, ivys]
>>> univs2 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]
>>> univs1 == univs2
True
# 上記補足:
# 　リスト同士の``==``は、「順番通りに保持している値が等しいか」だけを判定。
# 　メモリ空間上は異なる部分を参照していても、保持している値が等しければ True になる。
>>> print(univs1)
[['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]
>>> print(univs2)
[['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]
# techs を編集（下記では techs[0] を違う値に変更）すると、
# techsリストを参照している univs1 にも影響が及ぶ。
>>> techs[0] = 'hoge'
>>> print(techs)
['hoge', 'Caltech']
>>> print(univs1)
[['hoge', 'Caltech'], ['Harvard', 'Yale', 'Brown']]
>>> print(univs2)
[['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]
# techs を編集（ここではtechsの後ろに新しいオブジェクトを追加）すると、
# techsリストを参照している univs1 にも影響が及ぶ。
>>> techs.append('RPI')
>>> techs
['hoge', 'Caltech', 'RPI']
>>> univs1
[['hoge', 'Caltech', 'RPI'], ['Harvard', 'Yale', 'Brown']]
>>> univs2
[['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]
```

<hr>

## <a name="list_comprehension">リスト内包表記</a>
- 演算結果をリストとして保存したい場合、リストの中に演算を書くことができる。
- 下記のコードは、どちらも同じ処理になる。
- (case 1) 通常のfor文で計算する書き方。

```
squares = []
for x in range(1,7):
    squares.append(x**2)

print(squares)
# -> [1, 4, 9, 16, 25, 36]
```

- (case 2) リスト内包表記での書き方。

```
squares = [x**2 for x in range(1,7)]
print(squares)
# -> [1, 4, 9, 16, 25, 36]
```

<hr>

## <a name="ref">参考サイト</a>
- [チュートリアル, リスト型 (list)](http://docs.python.jp/3/tutorial/introduction.html#lists)
- [チュートリアル, リストの内包表記](http://docs.python.jp/3/tutorial/datastructures.html#list-comprehensions)
