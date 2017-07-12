# これまでの授業解説では抜けてた補足

- ＜目次＞
  - <a href="#break">break文</a>
  - <a href="#continue">continue文</a>
  - <a href="#pass">pass文</a>
  - <a href="#del">del文</a>
  - <a href="#__name__">\_\_name\_\_変数</a>
  - <a href="#ref">参考サイト</a>

<hr>

## <a name="break">break文</a>
- ループ処理中break文が実行されると、反復処理を中断（それ以降のループ処理を行わない）し、ループから抜ける。
```
for x in range(5):
    if x == 3:
        break
    print('x = {0}'.format(x))
```

<hr>

## <a name="continue">continue文</a>
- ループ処理中continue文が実行されると、その後のブロック内の処理を行わず、ループ文冒頭に戻る。
```
for x in range(5):
    if x == 3:
        continue
    print('x = {0}'.format(x))
```

<hr>

## <a name="pass">pass文</a>
- 何もしない（ということの明示）。
  - 詳細な記述は後回しにし、形だけ揃えておきたい（実行できるようにしておきたい）場合に使うことが多い。

```
def add(x, y):
    pass
```

<hr>

## <a name="del">del文</a>
- 定義した名前（変数や関数）を明示的に削除したい時に用いる。
  - e.g., 大規模なデータセットを読み込んで処理していた。その後、処理は終わったが、プログラム自体はまだ継続している。メモリ上に不要なデータセットが残ってると無駄にリソースを食ってしまうから消そう。

```
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
# -> [1, 66.25, 333, 333, 1234.5]

del a
print(a)
# -> NameError: name 'a' is not defined
```

<hr>

## <a name="__name__">\_\_name\_\_変数</a>
- \_\_name\_\_ は「モジュール名」が設定される。
  - case 1) ``python3 hoge.py`` のように実行すると、モジュール名「\_\_main\_\_」が代入されている。
  - case 2) ``python3`` とインタプリタを起動すると、「\_\_main\_\_」が代入されている。
  - case 3) ``import hoge`` のようにモジュールを読み込むと、hoge.\_\_name\_\_ の中身は「hoge」が代入されている。
    - importすると\_\_name\_\_にはモジュール名が代入されている。デフォルトの \_\_main\_\_ にはならない。このため、case1, case2と、case3とで実行結果が異なるケースがある。
  - 何故こうなっているのか？
    - 「スクリプトファイルを実行する場合（上記のcase 1）」と「モジュールとして利用する場合（上記のcase 3）」とで、動作を変えたいから。
      - 例えば、random.randint()を使って乱数生成したことを振り返ってみよう。
        - 「import random」しただけで、プログラムが実行されたら邪魔じゃない？（上記case 3に相当）

- コード例: hoge.py

```
# コード例 (hoge.py という名前で保存しよう)
if __name__ == '__main__':
    print('__name__ の中身は __main__ でした！')
```

- 実行例

```
# case 1: 普通にプログラムを実行した際の動作。
oct:tnal% python3 hoge.py
__name__ の中身は __main__ でした！

# case 2:
oct:tnal% python3
>>> __name__
'__main__'

# case 3: hogeをimportしても、print文が実行されていない。
>>> import hoge
>>> print(hoge.__name__)
'hoge'
```

<hr>

## <a name="ref">参考サイト</a>
- [4.4. break and continue Statements, and else Clauses on Loops](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) by 公式ドキュメント
- [4.5. pass Statements](https://docs.python.org/3/tutorial/controlflow.html#pass-statements)
- [5.2. The del Statement](https://docs.python.org/3/tutorial/datastructures.html#the-del-statement)
- [29.4. \_\_main\_\_ — Top-level script environment](https://docs.python.org/3/library/__main__.html#module-__main__)
