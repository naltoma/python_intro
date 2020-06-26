# Jupyter Lab を使ってみよう

- ＜目次＞
  - <a href="#whatis">JupyterLab とは？</a>
  - <a href="#install">インストール</a>
  - <a href="#sample">サンプルを試してみる</a>
  - <a href="#newfile">ゼロから新規作成してみる</a>
  - <a href="#shutdown">JupyterLab を終了する</a>
  - <a href="#others">ノートの例を探してみる</a>

<hr>

## <a name="whatis">Jupyter Lab とは？</a>
- [公式サイト](http://jupyter.org)
  - JupyterLab is a web-based interactive development environment for Jupyter notebooks, code, and data.
  - ノート、コード、実行結果等を一つのノートにまとめることができる「インタラクティブな開発環境」。
- Jupter Notebook vs JupyterLab
  - 厳密には異なるもの。元々はNotebookが安定版として広く使われていて、Labは拡張を含む開発版というニュアンスが強かった。特に大きな違いは「LabはNotebookを内包する次世代UI」として開発されていること。
  - 単にインタラクティブなノートとして使うだけならばNotebookでも十分。今回は拡張版であるLabを使ってみよう。

<hr>

## <a name="install">インストール</a>
- 赤嶺先生授業で pip3 を使っている人: ``pip3 install jupyterlab``
- 上記以外の人: ``conda install -c conda-forge jupyterlab``

## <a name="sample">サンプルを試してみる</a>
- ``~/prog1/`` に移動し、サンプルファイルをダウンロード。
```
curl https://ie.u-ryukyu.ac.jp/~tnal/2016/prog1/jupyter_example.ipynb -O
```

- JupyterLabの起動。
  - ターミナルで``jupyter lab``を実行。自動的にブラウザが立ち上がり、コマンドを実行したディレクトリの中身が左パネルに表示される。
    - もしブラウザが自動で立ち上がらない場合には、ターミナル上に ``Or copy and paste one of these URLs: http://localhost:8888/?token=長い文字列`` という出力があるはずなので、そのURLをコピーしよう。その後、ブラウザで新規ウィンドウか新規タブを用意し、URLを貼り付けて開こう。
    - ブラウザで「JupyterLab」タイトルが見え、実行したディレクトリの一覧が表示されてるなら、正常に起動している。これ以降はブラウザ内で操作する。
- サンプルファイルを操作してみる。
  - ダウンロードしたファイル「jupyter_example.ipynb」を開こう。
    - Jupyterではセル（Cell）と呼ばれる論理構造でノートを編集していく。ダウンロードしたノート例は5つの「Cell」で構成されている。
      - 1つ目, 4つ目のCell: Markdown形式のテキスト。Markdown cell。
        - [Markdownとは](http://www.markdown.jp/what-is-markdown/)
      - 2,3,5つ目のCell(灰色背景): Python3で実行可能なコード。Code cell。
  - Cellの編集
    - 編集したいCellをダブルクリック。
      - ここでは1つ目のCellを編集してみよう。
    - Cellを新しく追加するには、左上の「＋」アイコンをクリック。
    - 上下の矢印アイコンで、現在選択肢ているセルの並びを変更可能。
  - Cellの実行
    - Cell単位で実行
      - 編集し終えたら「Shift + return」で実行。
        - Markdownセルなら、viewの更新。
        - Codeセルなら、コードを実行し、実行結果をセルの下に出力。
    - ファイルに含まれる全てのCellを実行
      - Cellメニューから「Run All」を選択。

<hr>

## <a name="newfile">ゼロから新規作成してみる</a>
- 全体の流れ
  - JupyterLabの起動。（起動済みならそのまま）
  - 一時的な作業用ディレクトリ ``~/prog1/`` に移動。（移動済みならそのまま）
  - 新規ノート ``test.ipynb`` を作成。
  - ノートを編集・実行してみる。
- 新規ノート ``test.ipynb`` を作成。
  - 左パネル上部にある File メニューから ``New => Notebook`` を選択。
  - Select Kernel と問われたら ``Python 3`` を選択。
  - 右パネルのタブに ``Untitled.ipynb`` と表示されたらOK。これがノートブック。
  - 左パネルから ``Untitled.ipynb`` を探し、Ctrl+クリック。サブメニュー出るので、``Rename`` を選んで ``test.ipynb`` にファイル名を変更しよう。
- ノートを編集・実行してみる。
  - [Numpyを使ったベクトル・行列演算入門](https://github.com/naltoma/python_intro/blob/master/Numpy.md)を参考に、numpyによるベクトル・行列演算のコードを記述し、動作確認してみよう。
- **注意点**
  - Jupyterでノートを開いてコードを実行すると、「ノート毎にPythonインタプリタを起動」している状態になります。このインタプリタは「Jupyter本体を停止する」か、「個別にインタプリタを停止」するまで起動しっぱなしになります。CPU/メモリ等のリソースを食いまくるので、不要なインタプリタは停止するようにしよう。
    - インタプリタが起動中かどうかを確認する方法
      - 左パネルファイル名の左側に緑●が付いていたら起動中。
    - インタプリタの停止方法
      - 停止させたいファイルを開き、Kernelメニューから「Shutdown」を選択。

<hr>

## <a name="shutdown">JupyterLab を終了する</a>
- ブラウザはいつ閉じてもOK。ただし、**ブラウザを閉じただけではJupyterは終了しません**。
- ``jupyter lab`` を実行したターミナルを開き、「Ctrl+C」。
- 終了(shutdown)するか聞いてくるので、「y」。
  - 入力無い状態が5秒続くと、自動でアプリ実行を継続するので、そうなったらまた「Ctrl+C」しよう。

<hr>

## <a name="others">ノートの例を探してみる</a>
- [nbviewer](http://nbviewer.jupyter.org): A simple way to share Jupyter Notebooks
