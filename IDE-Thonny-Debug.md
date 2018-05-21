# Thonny によるデバッガの利用

- ＜目次＞
  - <a href="#abst">概要</a>
  - <a href="#whatis_IDE">IDE（統合開発環境）とは</a>
  - <a href="#goal">達成目標</a>
  - <a href="#install">インストール</a>
  - <a href="#run">起動〜新規作成〜実行</a>
  - <a href="#debug1">デバッグ実行1</a>
  - <a href="#debug2">デバッグ実行2（演習）</a>

<hr>

## <a name="abst">概要</a>
- 初心者向けIDE [Thonny](http://thonny.org)を使ってみよう。
- 物足りなくなってきたら、もしくは細かすぎて面倒になってきたら、 [PyCharm](https://www.jetbrains.com/pycharm/) を試してみよう。
  - 行単位でのデバッグ実行。
  - テストやバージョン管理にも対応。

<hr>

## <a name="whatis_IDE">IDE（統合開発環境）とは</a>
- [Wikipedia:統合開発環境](https://ja.wikipedia.org/wiki/統合開発環境)より抜粋。
>統合開発環境（とうごうかいはつかんきょう）、IDE (Integrated Development Environment) は、ソフトウェアの開発環境。
>従来、コンパイラ、テキストエディタ、デバッガなどがばらばらで利用していたものをひとつの対話型操作環境（多くはGUI）から利用できるようにしたもの。
- Thonny は「Python IDE for beginners」ということでプログラミング初学者向けのIDE。
  - Easy to get started. (簡単に始められる)
  - No-hassle variables. (変数確認の手間削減)
  - Simple debugger. (シンプルなデバッガ)
  - Step through expression evaluation. (表記評価しながら進む)
  - Faithful representation of function calls. (関数呼び出しの直感的な表現)

<hr>

## <a name="goal">達成目標</a>
- Thonnyを起動し、プログラムを作成・保存し、実行することができる。
- デバッグ実行（debug-run, step-in）することができる。
- Thonnyを起動し、演習や課題など新しいコードを書くために利用（保存・通常実行・デバッグ実行）することができる。

<hr>

## <a name="install">インストール</a>
- ターミナル上で以下を実行。pipは、Python用のパッケージ管理ツール。
```
pip install thonny
```

<hr>

## <a name="run">起動〜新規作成〜実行</a>
- Thonnyを起動する。```python -m thonny```
  - 3つのタブ「&lt;untitled&gt;, Variables, Shell」で構成される大きなウィンドウが表示されるはず。
- コードの作成。
  - &lt;untitled&gt;タブに、以下のコードを手打ちで入力しよう。

```
# textbook, p.40
def max_val(x, y):
    if x > y:
        return x
    else:
        return y

result = max_val(3, 4)
print(result)
```
- （コード作成時に気づくであろう）多くのIDEに共通する特徴
  - ハイライト表示による見やすさ。
    - 関数の引数xにカーソルを移動させるとどうなるか観察してみよう。同様に関数名や他の変数にカーソルを合わせるとどうなるだろうか。
  - インデント対応。
    - **Tabキー** でインデント追加。**複数行同時に変更** することも可能。
    - **Shift+Tabキー** でインデント削除。
  - スコープ対応。
- コードの保存。
  - Command+Sか、FileメニューからSaveを選び、ファイル名「max_val.py」として保存。
  - 一度ファイル名を付けて保存すると、今後は「実行」する際に自動で上書き保存される。
- コードの実行。
  - 「右向き三角」アイコンをクリックするか、Runメニューから「Run Current Script」を選択して実行。
  - 特に問題なければ、「Shellタブ」に実行結果の「4」が出力され、Pythonインタプリタのプロンプト「>>>」が出力されているはずだ。また、「Variablesタブ」のName欄にmaxが掲載されているはず。
    - インタプリタモードになっているため、追加確認もしやすい。
    - ShellタブやVariablesタブに上記内容が掲載されていない場合、コードに誤りがある可能性が高い。同じ結果になるまで「目視チェック->修正->実行」を繰り返そう。（誤り箇所を発見できないなら質問しよう）
  - Shellタブでは、上記で書いたコードを実行した直後の状態。すなわち、(1)関数max_valを定義し、(2)print(result)を実行し終えた状態である。
    - 利点1: Pythonインタプリタを直接使うと、コードが残らないため再利用しづらいが、Thonnyではコードを保存しているので再利用しやすい。
    - 利点2: この状態でインタプリタモードになっているため、「コードを明示的に残す部分と、インタプリタで確認したい部分」とを**同時**に使うことができる。

<hr>

## <a name="debug1">デバッグ実行1</a>
- そもそもデバッグ(debug)とは？
  - [Wikipedia:Debugging](https://en.wikipedia.org/wiki/Debugging)より引用
> Debugging is the process of finding and resolving of defects that prevent correct operation of computer software or a system.

- これからやること
  - 正常に動作しない要因を発見し、解決するプロセスをデバッグと呼ぶ。
  - 要因発見の一手段として、デバッグ実行が用いられる。このデバッグ実行は「コードを読む」ためにも使える。今回はコード読みのためにデバッグ実行してみよう。
- デバッガを起動する。
  - 「（右向き三角の隣りにある）虫アイコン」をクリックするか、Runメニューから「Debug current script」を選択して実行。
    - max_val関数を定義しているエリアが囲われ、ハイライトされた状態で停止する。
      - **ハイライトされた箇所=これから実行する箇所**
  - Step into実行してみる。（1回目）
    - デバッグ実行が一時停止している状態で「**Step into実行**」してみよう。3つ矢印が並んでる箇所の真ん中にある「➘アイコン」をクリック。
      - (1) Variablesタブに「max_val」が登録され、(2)ハイライト表示が関数定義を抜けて「result = max_val(3, 4)」の行に移動したはずだ。
      - これは、(1)def文が関数定義をするだけで実行を伴わないこと、(2)後から参照できるようにmax_val関数を定義している場所を登録していること、(3)関数定義を終えたら、次に実行する行は「result = max_val(3,4)」であること、を意味している。
      - デバッグ実行を最初からやり直したくなったら、停止（赤い四角をクリック）して、もう一度デバッグ実行しよう。
        - Thonnyは初心者向けのため、冒頭で停止し、細かく1ステップずつ実行することになる。これは細部確認時には便利だが、慣れてくると「見たい場所」に辿り着くまでの手間がかかる。これに対し、一般的なIDEだと、どこで一時停止するか（breakpoints）を指定することが可能。（後日やります）
  - Step into実行してみる。（2回目）
    - Step intoアイコンをもう一度クリック。
    - 「val_max(3, 4)」がハイライトされて、停止したはずだ。
  - Step into実行してみる。（3〜7回目）
    - 実行する度に「次に処理すべき箇所」をハイライト表示し、処理結果が確定したら次に進む。このように一時停止しながら実行することを「デバッグ実行」と呼ぶ。
      - Step into以外にも幾つか種別があるが、今はこれだけで良い。
  - Step into実行してみる。（8回目〜: 関数呼び出し）
    - 「max(3,4)」として関数maxが呼び出されると、新しくウィンドウが作られ、関数maxの中がハイライト表示される。このウィンドウ下部には「**Local variablesタブ**」があり、引数x,yの中身が表示されているはずだ。この変数x,yは、元の大きなウィンドウには記録されていない点に注意。（スコープが異なる）
    - この状態でもう一度Step into実行すると、if文の条件を確認し、その結果に応じてTrueブロック/Falseブロックに移動して処理を行う。
    - return文にたどり着くと、指定された値を返して関数の処理を終了する。このタイミングで関数maxのウィンドウが無くなるため、先程の局所変数x,yも失われる。
  - デバッグ実行のまとめと補足。
    - 処理を一時停止し、実行の様子（変数の中身等）を確認しながら実行できるため、動作を確認しやすい。
    - Step into実行は、一般的には「行単位」で実行される。Thonnyの場合「細切れ」にして実行してくれてるが、これはThonny独自の仕様。（なので、for beginners）

<hr>

## <a name="debug2">デバッグ実行2（演習）</a>
- 以下のコードを「scoping.py」という名前で保存し、デバッグ実行（Step into実行）してみよう。実行の様子からソースコードの動作を理解してみよう。

```
# textbook, p.43
def f(x):
    y = 1
    x = x + y
    print('x = {0}'.format(x))
    return x

x = 3
y = 2
z = f(x)
print('z = {0}'.format(z))
print('x = {0}'.format(x))
print('y = {0}'.format(y))
```
