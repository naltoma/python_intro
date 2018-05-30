# ユニットテスト演習（doctest on Python3）

- ＜目次＞
  - <a href="#pre">コード例を準備<a>
  - <a href="#dir">作業ディレクトリに移動</a>
  - <a href="#doctest">対象ファイルを開き、ユニットテストを書き加える</a>
  - <a href="#tips">Tips: doctest内のテストコードの書き方</a>
  - <a href="#howto">ユニットテストの一般的な使い方</a>

<hr>

## <a name="pre">コード例を準備<a>
- コードをダウンロード。
  - [github:python_demo_module](https://github.com/naltoma/python_demo_module)へアクセス。
  - 右端にある「背景緑のClone or download」をクリック。
  - 「Doownload ZIP」をクリック。
- 解凍して作業ディレクトリに移動。
  - ダウンロードしたファイル python_demo_module-master.zip を、ダブルクリックして展開（解凍）する。
  - ダウンロードしたディレクトリ上で展開したはずなので、上記コードは ``~/Downloads/python_demo_module-master/`` フォルダにあるはずだ。
  - ``~/Downloads/python_demo_module-master/`` を、``~/prog1/python_demo_module-master/`` に移動しよう。

<hr>

## <a name="dir">作業ディレクトリに移動</a>
- ターミナルを起動して、``~/prog1/python_demo_module-master`` に移動。
  - 移動先ディレクトリを指定する際、``cd ~/prog1/py`` まで入力した状態でTabキーを押すと、 ``*~/prog1/python_demo_module/*`` まで補完されるはず。**Tabキーによる補完** を使いこなそう。
  - pyから始まるフォルダが複数ある場合、候補を出力してくれるはずなので、候補を見てユニークになるまで文字を入力してからTabキーを押そう。

<hr>

## <a name="doctest">対象ファイルを開き、ユニットテストを書き加える</a>
- 今回の目的
  - my_math.pyには階乗を計算するfactR()関数が定義されている。この関数が正しく動作することを検証するコードを、doctestで書いてみよう。
- [手順1] my_math.pyをエディタで開く。
- [手順2] factR()の中にdocstring形式のコメント欄を用意する。
- [手順3] 用意したコメント欄にdoctestを記述する。
  - 注意点
    - インデントを揃えよう。
      - my_math.factR関数内のインデントは「半角スペース4つ」になっている。docstring形式のコメント欄も、その中のdoctestも同じインデントで揃える必要がある。
      - Pythonインタプリタ上では「>>> 」のように半角スペース付きプロンプト。ここでもそうなるように記述しよう。その他、スペースの有無がテスト結果に影響していくるので注意。
    - Pythonインタプリタ上で実行している状況をイメージし、実行する内容と得られる結果を列挙する必要がある。

```
def factR(n):
    """
    ここはdocstring形式の、複数行に跨るコメント欄。
    単にコメントを書くためだけではなく、以下のようにdoctestを書くこともできる。

    >>> factR(3)
    6
    >>> factR(4)
    24

    以下は「doctestとして駄目な例」。>>>の次にスペースが入っていません。
    >>>factR(3)
    6
    """
    if n == 1:
        return n
    else:
        return n * factR(n-1)
```
- [手順4] doctestを実行する。
  - コード内にdoctestモジュール読み込みを予め記述する方法（先週の授業ページ参照）と、実行時にオプション指定する方法がある。今回はオプション指定の方法で実行してみよう。

```
# 以下はターミナル上で実行。
# case 1: テストに失敗したときだけテスト結果を出力。
python -m doctest my_math.py

# case 2: 常にテスト結果を出力。
python -m doctest my_math.py -v
```

<hr>

## <a name="tips">Tips: doctest内のテストコードの書き方</a>
- ある機能をテストしたい時、そのテストを1行のコードとして書く必要はない。複数行に跨って書いて良い。

```
def factR(n):
    """
    例1: 「factR(3) の結果が0より大きい数値であること」を検証するテストコード。
    >>> factR(3) > 0
    True
    >>> result = factR(3)
    >>> result > 0
    True

    例2: 「factR(3) の結果が0より大きい数値であり、かつ、int型であること」を検証するテストコード。
    >>> result = factR(3)
    >>> result > 0
    True
    >>> type(result)
    <class 'int'>
    >>> result > 0 and type(result) == int
    True
    """
    if n == 1:
        return n
    else:
        return n * factR(n-1)
```


<hr>

## <a name="howto">ユニットテストの一般的な使い方</a>
- 関数の仕様（入力と出力）を検討する際に、使い方の例示のためにテストを記載しておく。ここで書いたテストが通るように関数を仕上げていく。（テスト駆動開発）
  - 発展的な使い方: 中身は空のままで、先に関数名・引数・戻り値だけを決めていく。必要な関数群を列挙して全体が動く見通しを立てる。見通しが立ってから、中身の実装に入る。
- 以前書いたコードに機能追加したくなった時、コード修正に伴い出力結果が変わっては困る。動作確認を自動化するためにテストを書いておく。
