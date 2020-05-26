'''画像データを平滑化するプログラム。
画像データはピクセルごとに0〜255のグレイスケール値を取る。
'''
import matplotlib.pyplot as plt
import copy

data = [[ 0.,  0., 0., 0.,15., 0., 0., 0.],
        [ 0.,  0., 0.,15.,15., 0., 0., 0.],
        [ 0.,  0.,15.,15.,15., 0., 0., 0.],
        [ 0.,  0., 0.,15.,15., 0., 0., 0.],
        [ 0.,  0., 0.,15., 0., 0., 0., 0.],
        [ 0.,  0., 0.,15.,15., 0., 0., 0.],
        [ 0.,  0., 0.,15.,15., 0., 0., 0.],
        [ 0.,  0.,15.,15.,15.,15., 0., 0.]]

def plot_image(image1, image2):
    '''2つの画像を横に並べて描画。

    Argments:
        image1 (list): 横方向に並んだピクセル値を一つのリストとして保持し、そのリストを複数保持した2重リスト。
        image2 (list): 同上。
    '''
    plt.subplot(2,2,1)
    plt.imshow(image1, cmap="gray_r")
    plt.subplot(2,2,2)
    plt.imshow(image2, cmap="gray_r")
    plt.show()

def averaging(img, w, h, window_size):
    '''対象画素値を周囲画素値の平均値に置き換えることで滑らかにする（平滑化）。

    Argments:
        img (list): 画像データ。plot_image参照。
        w (int): 平滑化する中心の横座標（横インデックス）。
        h (int): 平滑化する中心の縦座標（縦インデックス）。
        window_size (int): 平滑化サイズ。
    Returns:
        result (float): 平滑化した値。
    '''
    count = 0
    sum = 0.0
    relative_index = range(-window_size, window_size+1)
    for relative_x in relative_index:
        for relative_y in relative_index:
            x = w + relative_x
            y = h + relative_y
            if 0 <= x and x < len(img[0]) and 0 <= y and y < len(img):
                sum += img[y][x]
                count += 1
    result = sum / count
    return result

def blur_filter(image, window_size=1):
    """平滑化フィルタ。

    Arguments:
        image (list): 画像データ。plot_image参照。
        window_size (int): 平滑化時の周辺参照サイズ。
    Returns:
        new_image (list): 平滑化した画像データ。形式はimageと同一。
    """

    width = len(image[0])
    height = len(image)
    new_image = copy.deepcopy(image)
    for w in range(width):
        for h in range(height):
            new_image[h][w] = averaging(image, w, h, window_size)
    #print(new_image)
    return new_image

if __name__ == '__main__':
    print('data:', data[0])
    new_img = blur_filter(data)
    print('data:', data[0])
    print('new_img:', new_img[0])
    plot_image(data, new_img)
