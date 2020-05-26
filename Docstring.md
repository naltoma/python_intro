# Docstring（ドキュメンテーション）
- ＜目次＞
  - <a href="#intro">コメントとドキュメントの違い、外観</a>
  - <a href="#exercise">ドキュメントを書いてみよう</a>
  - <a href="#sample">参考：ドキュメント付きソースコードと生成したドキュメントの例</a>

<hr>

## <a name="intro">コメントとドキュメントの違い、外観</a>
- コメント
  - コードに対する補足。
  - 書き方
    - 1行コメントなら ``#`` で記述。
    - 複数行コメントなら ``'''〜'''``` で記述。（ダブルクォートも可）
- ドキュメント
  - 補足する文という点ではコメントと一緒。「マニュアル」としての側面が強い。
  - 書き方
    - 複数行コメントを「**特定の場所**」に書く。
      - 対象の冒頭に記述。
      - ファイル全体についてのドキュメントなら、ファイル冒頭。
      - 関数についてのドキュメントなら、関数冒頭。
    - 書き方の例
      - [Example Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
      - [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
  - 参照方法
    - 方法1：pydocコマンドで参照。
      - ソースコードが ``test.py`` なら、ターミナル上で ``pydoc test`` として参照。拡張子 .py を付けずに指定する点に注意。この拡張子を取り除いた名前を「モジュール名」と呼ぶ。
        - 以前利用した random モジュールや、random.randint 関数についても pydoc からドキュメントを参照できる。試してみよう。
      - pydoc を終了するには ``q`` を入力しよう。quit（終了）の頭文字。
    - 方法2：HTML形式でドキュメントを生成し、ブラウザで参照。
      - pydocコマンド実行時に、-wオプション付きで実行。エラーが無ければ「モジュール名.html」が生成される。
      - 生成されたHTMLファイルを open コマンドで開くか、Finderからダブルクリックで開くと参照できる。

<hr>

## <a name="exercise">ドキュメントを書いてみよう</a>
- コード例
  - 参考：[画像の平滑化](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_filtering/py_filtering.html)

```Python
import matplotlib.pyplot as plt
import copy #for deepcopy

data = [[ 0.,  0., 0., 0.,15., 0., 0., 0.],
        [ 0.,  0., 0.,15.,15., 0., 0., 0.],
        [ 0.,  0.,15.,15.,15., 0., 0., 0.],
        [ 0.,  0., 0.,15.,15., 0., 0., 0.],
        [ 0.,  0., 0.,15., 0., 0., 0., 0.],
        [ 0.,  0., 0.,15.,15., 0., 0., 0.],
        [ 0.,  0., 0.,15.,15., 0., 0., 0.],
        [ 0.,  0.,15.,15.,15.,15., 0., 0.]]

def plot_image(image1, image2):
    plt.subplot(2,2,1)
    plt.imshow(image1, cmap="gray_r")
    plt.subplot(2,2,2)
    plt.imshow(image2, cmap="gray_r")
    plt.show()

def averaging(img, w, h, window_size):
    count = 0
    sum = 0.0
    relative_index = range(-window_size, window_size+1)
    for x in relative_index:
        for y in relative_index:
            relative_x = w + x
            relative_y = h + y
            if 0 <= relative_x and relative_x < len(img[0]) and 0 <= relative_y and relative_y < len(img):
                sum += img[relative_y][relative_x]
                count += 1
    result = sum / count
    return result

def blur_filter(image, window_size=1):
    width = len(image[0])
    height = len(image)
    new_image = copy.deepcopy(image)
    for w in range(width):
        for h in range(height):
            new_image[h][w] = averaging(image, w, h, window_size)
    return new_image

if __name__ == '__main__':
    new_img = blur_filter(data)
    plot_image(data, new_img)
```

- 手順0：環境構築。
  - matplotlibのインストール。
    - 赤嶺先生授業で pip を使った学生は、``pip install -U matplotlib``
    - 上記以外の学生は、``conda install matplotlib``
- 手順1：コードの準備。
  - 上記コードを averaging.py として保存。
- 手順2：ドキュメント生成＆参照。（docstring書く前の状態を確認）
  - ``pydoc -w averaging``
  - ``open averaging.html``
- 手順3-1：ドキュメント記述1（ファイル全体）
  - ファイル冒頭に下記を記述。
  - 保存したらドキュメント生成し、どのように反映されるか確認してみよう。

```Python
'''画像データを平滑化するプログラム。
画像データはピクセルごとに0〜255のグレイスケール値を取る。
'''
```

- 手順3-2：ドキュメント生成2（関数plot_image）
  - 関数plot_image冒頭に下記を記述。インデントを関数ブロックに揃えること。
  - 保存したらドキュメント生成し、どのように反映されるか確認してみよう。

```Python
  '''2つの画像を横に並べて描画。

  Argments:
    image1 (list): 横方向に並んだピクセル値を一つのリストとして保持し、そのリストを複数保持した2重リスト。
    image2 (list): 同上。
  Returns:
    なし。
  '''
```

-　手順3-3：ドキュメント生成3（関数averaging）
  - 関数averaging冒頭に下記を記述。インデントを関数ブロックに揃えること。
  - 保存したらドキュメント生成し、どのように反映されるか確認してみよう。

```Python
  '''対象画素値を周囲画素値の平均値に置き換えることで滑らかにする（平滑化）。

  Argments:
    img (list): 画像データ。plot_image参照。
    w (int): 平滑化する中心の横座標（横インデックス）。
    h (int): 平滑化する中心の縦座標（縦インデックス）。
    window_size (int): 平滑化サイズ。
  Returns:
    result (float): 平滑化した値。
  '''
```

<hr>

## <a name="sample">参考：ドキュメント付きソースコードと生成したドキュメントの例</a>
- [averaging.py](./samples/averaging.py)
- [averaging.html](./samples/averaging.html)
