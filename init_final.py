import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

# パラメータの設定
sf = 100
n = np.linspace(0, 1, sf + 1)
unistep = np.ones(sf + 1)

# 最初のフィルタ
a1 = [3, -2, -1]
b1 = [1]
y1 = lfilter(b1, a1, unistep)

# 初期値の確認
plt.subplot(2, 2, 1)
plt.stem(n, y1)
plt.xlim([0, 0.1])
plt.ylim([0, 0.5])
plt.title('Initial values (Filter 1)')

# 最終値の確認
plt.subplot(2, 2, 2)
plt.stem(n, y1)
plt.title('Final values (Filter 1)')

# 2つ目のフィルタ
a2 = [2, -0.5, 0, -0.3]
b2 = [3]
y2 = lfilter(b2, a2, unistep)

# 初期値の確認
plt.subplot(2, 2, 3)
plt.stem(n, y2)
plt.xlim([0, 0.1])
plt.ylim([0, 2])
plt.title('Initial values (Filter 2)')

# 最終値の確認
plt.subplot(2, 2, 4)
plt.stem(n, y2)
plt.title('Final values (Filter 2)')

plt.tight_layout()
plt.show()
