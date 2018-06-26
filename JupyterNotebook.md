# Jupyter Notebook を使ってみよう

- ＜目次＞
  - <a href="#whatis">Jupyter Notebook とは？</a>
  - <a href="#install">インストール</a>
  - <a href="#sample">サンプルを試してみる</a>
  - <a href="#newfile">ゼロから新規作成してみる</a>
  - <a href="#shutdown">Jupyter Notebook を終了する</a>
  - <a href="#others">ノートの例を探してみる</a>

<hr>

## <a name="whatis">Jupyter Notebook とは？</a>
- [公式サイト](http://jupyter.org)
  - The Jupyter Notebook is **a web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text**. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, machine learning and much more.
  - コード、実行結果、コメント等を一つのノートにまとめることができる。

## <a name="install">インストール</a>
- ターミナルで以下を実行。（Anacondaインストール時には不要）
```
pip install jupyter
pip install matplotlib
```

## <a name="sample">サンプルを試してみる</a>
- サンプルファイルをダウンロード。
```
curl https://ie.u-ryukyu.ac.jp/~tnal/2016/prog1/jupyter_example.ipynb -O
```
- Jupyter Notebookの起動。
  - ターミナルで``jupyter notebook``を実行。
  - 指定されたURLをブラウザで開く。
    - 「Copy/paste this URL into your browser when you connect for the first time, to login with a token: http://localhost:8888/（略）」という指示が出力されるなら、その次に示されているURLをコピーして、ブラウザに貼り付けてアクセス。
    - ブラウザで「Jupyter」タイトルが見え、実行したディレクトリの一覧が表示されてるなら、正常に起動している。これ以降はブラウザ内で操作する。
- サンプルファイルを操作してみる。
  - ダウンロードしたファイル「jupyter_example.ipynb」を開こう。
    - 5つの「Cell」で構成されている。
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
        - Codeセルなら、実行結果をセルの下に出力。
    - ファイルに含まれる全てのCellを実行
      - Cellメニューから「Run All」を選択。

<hr>

## <a name="newfile">ゼロから新規作成してみる</a>
- Jupyterのトップ画面（ファイル一覧画面）からなら、右上の「New」アイコンからPython3を選択。
- ファイルを開いているウィンドウからなら、Fileメニューから「New Notebook」を選択。
- **注意点**
  - Jupyterでノートを開いてコードを実行すると、「ノート毎にPythonインタプリタを起動」している状態になります。このインタプリタは「Jupyter本体を停止する」か、「個別にインタプリタを停止」するまで起動しっぱなしになります。CPU/メモリ等のリソースを食いまくるので、不要なインタプリタは停止するようにしよう。
    - インタプリタの停止方法
      - 開いてるノート画面にいる場合: Kernelメニューから「Shutdown」を選択。
      - ファイル一覧画面にいる場合: 停止したいファイル名の左にある「チェックボックス」を選択し、「Shutdown」を選択。

<hr>

## <a name="shutdown">Jupyter Notebook を終了する</a>
- ブラウザはいつ閉じてもOK。ただし、**ブラウザを閉じただけではJupyterは終了しません**。
- ``jupyter notebook`` を実行したターミナルを開き、「Ctrl+C」。
- 終了(shutdown)するか聞いてくるので、「y」。
  - 入力無い状態が5秒続くと、自動でアプリ実行を継続するので、そうなったらまた「Ctrl+C」しよう。

<hr>

## <a name="others">ノートの例を探してみる</a>
- [nbviewer](http://nbviewer.jupyter.org): A simple way to share Jupyter Notebooks
