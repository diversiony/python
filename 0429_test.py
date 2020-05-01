import matplotlib.pyplot as plt
import numpy as np

# 平均50、分散20の乱数を10万個作成する
x = np.random.normal(50, 20, 100000)

# 画像のプロット先の準備
fig = plt.figure()

# ヒストグラムの描画
plt.hist(x, bins=100, ec='black')

# グラフの指定
plt.title("normal histogram")
# x方向のラベル
plt.xlabel("x")
# y方向のラベル
plt.ylabel("y")
# グラフの表示範囲(x方向)
plt.xlim(-50, 150)
# グリッドを表示する
#plt.grid()

# グラフをファイルに保存する
fig.savefig("C:\\Users\\diver\\img.png")