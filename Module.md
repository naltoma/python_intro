# モジュールの利用
- 目次
  - <a href="#whatis">モジュールとは何か</a>
  - <a href="#howto">モジュールを作成し、利用してみよう</a>
  - <a href="#ref">参考文献</a>

<hr>

## <a name="whatis">モジュールとは何か</a>
- [公式ドキュメント](https://github.com/naltoma/python_demo_module)
  - 要約
    - 「Python では定義をファイルに書いておき、スクリプトの中やインタプリタの対話インスタンス上で使う方法があります。このファイルを モジュール (module) と呼びます。モジュールにある定義は、他のモジュールや main モジュール (実行のトップレベルや電卓モードでアクセスできる変数の集まりを指します) に import (取り込み) することができます。」
- 補足
  - 第三者が作成したモジュールを、再利用しやすくするために「モジュール」という機能が用意されている。
    - 関数だけだと、同一ファイル内でしか再利用できない。これに対しモジュールなら、別ファイルからでも再利用できる。モジュール（別ファイル）として利用するなら、少なくともファイル編集に伴うバグは発生しない。
- 別のコード例
  - [Pythonの「モジュール」を理解するためのコード例。](https://github.com/naltoma/python_demo_module)

<hr>

## <a name="howto">モジュールを作成し、利用してみよう</a>
- 手順1：モジュールを作成。（今回はコピペで用意）
  - モジュールの保存場所：``~/prog1/``
  - モジュール名：``cards``
  - ファイル名：``cards.py``　＊モジュール名に.py拡張子を付けたもの。
    - ファイル名は原則として「**英数字、アンダースコア(_) + .py**」とすること。これ以外の要素を含むと、モジュールとして利用できないことがあるため。
    - 例えば「test-3.py」というファイルのモジュール名は ``test-3`` になりそうだ。だが、Python言語仕様からすると test-3 は「testという変数に保存されているオブジェクトからint型の3を引く」ことを指すため、モジュール名として解釈されない。「test(2).py」のようなファイル名も同様の理由で避けよう。
  - 補足
    - ``__name__`` は、プログラム実行時に自動設定される特殊変数。``python cards.py`` のようにファイル実行すると ``__main__`` と設定され、main関数とかmain実行等と呼ばれる。これに対し、手順2でやる import 時にはそのモジュール名が設定される。具体的には、``import cards`` とすると ``cards`` が保存される。このようにファイル実行時とimport時とで ``__main__`` の中身が異なるため、同じソースファイルを用いていても動作が異なる点に注意しよう。

```Python
import random

def initialize_deck():
    """ready for a card deck.

    Args:
        None
    Returns:
        deck (list): a set of cards which consist of a suite and a number.

    >>> deck = initialize_deck()
    >>> print(len(deck))
    52
    >>> print(deck[0])
    S1
    """
    suites = ['S', 'H', 'D', 'C'] #Spade, Heart, Diamond, Club
    deck = []
    for suite in suites:
        for number in range(1,14):
            card = suite + str(number)
            deck.append(card)
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)

def get_one_card(deck):
    return deck.pop()

if __name__ == '__main__':
    # デッキを初期化、シャッフルして1枚目を確認。
    print("# デッキを初期化、シャッフルして1枚目を確認。")
    deck = initialize_deck()
    shuffle_deck(deck)
    print(deck[0])

    # デッキから1枚取り出す。
    print("# デッキから1枚取り出す。")
    card = get_one_card(deck)
    print(len(deck))
    print(card)

    # デッキから1枚取り出す。
    print("# デッキから1枚取り出す。")
    card = get_one_card(deck)
    print(len(deck))
    print(card)
```

- 手順2：モジュールを利用。
  - 前提
    - モジュールを保存したディレクトリと同じディレクトリから利用する。もしくは、[モジュール検索パス](https://docs.python.org/ja/3/tutorial/modules.html#the-module-search-path)で検索可能なパスにモジュールを用意しておくこと。今回は、モジュールを保存したディレクトリと同じディレクトリから利用しよう。
  - 方法1：importを使う。
    - 方法1-1：importで指定モジュールを読み込む。
    - 方法1-2：importで指定モジュールを読み込み、別称を付ける。

```Python
# 方法1−1： importで指定モジュールを読み込む。
import cards
deck = cards.initialize_deck()
print(deck)

# 方法1−2: importで指定モジュールを読み込み、別称を付ける。
import cards as trump
deck = trump.initialize_deck()
print(deck)
```

- 方法2：fromとimportを使う。
  - importだけ使う場合との違い
    - import
      - モジュール全体を読み込む。
    - from
      - モジュールの一部を指定して読み込むことも可能。
      - モジュール内関数等を利用する際に、モジュール名を省略できる。
  - 注意点
    - 多数モジュールをfrom読み込みしている場合には、「どのモジュールを利用しているのか」を判断しづらくなる。

```Python
# cards.initialize_deck だけを読み込む。
from cards import initialize_deck
deck = initialize_deck()
print(deck)
```

<hr>

## <a name="ref">参考文献</a>
- [6. モジュール](https://github.com/naltoma/python_demo_module) by 公式ドキュメント
