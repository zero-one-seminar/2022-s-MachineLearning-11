#!/usr/bin/env python
# coding: utf-8

# # Matplotlibを使ったプロット
# 
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]()
# 
# まずは、[Chainerチュートリアル](https://tutorials.chainer.org/ja/12_Introduction_to_Matplotlib.html)通りプロット。
# 簡単なグラフはこれで十分です。
# 
# ここでは、numpyでデータを作成しつつプロットを行います。

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# ## numpyの使い方
# 
# #### 一定区間に等間隔で散らばった点を生成
# `np.arange(開始, 終了, 間隔)`

# In[2]:


x = np.arange(-1, 1, 0.1)  # -1から1まで、0.1刻みで点を生成する

x


# #### 関数にわたす
# 
# `np.array`を関数に渡すと、その要素全てに同じ操作が加えられます。
# 
# 例）
# ```python
# np.array([1, 2, 3]) ** 2
# 
# # array([1, 4, 9])
# ```
# 
# その他、`numpy`で定義されている関数
# 
# - `sin`
# - `cos`
# - `tan`
# - `log`
# - `exp`
# 
# も使えます。

# In[3]:


y = np.sin(x)  # 生成した点をsin関数に渡す

y


# ## 散布図
# 
# `plt.scatter(xの配列, yの配列)`
# 
# 平面状に点を打ちます。
# 

# In[4]:


x = np.arange(-1, 1, 0.1)
y = x ** 2

plt.scatter(x, y)


# ## 折れ線グラフ
# 
# `plt.plot(xの配列, yの配列)`
# 
# 散布図と異なり、隣り合った点をつなげます。

# In[5]:


x = np.arange(-3, 3, 0.5)
y = np.sin(x)

plt.plot(x, y)


# ## ヒストグラム
# 
# ### データの生成
# $1〜6$ までの数字をランダムに $1000$ 回選んで平均を求めます。
# 
# これを $1000$ 回繰り返して、どんな分布になっているかをみてみます。

# In[6]:


from random import randint

data = []

for i in range(1000):

    # 1~6までの数字をランダムに選んで足す x 100回
    sum_of_dice = 0
    for j in range(1000):
        sum_of_dice += randint(1, 6)
    
    ave_of_dice = sum_of_dice / 1000
    data.append(ave_of_dice)


print(data[:10])  # 10個目までを見る


# ### ヒストグラムを作成
# 自動的に階級の幅を決めてプロットしてくれるみたいです。
# この場合は $10$ 個の階級に分けられていました。

# In[7]:


plt.hist(data)


# ### パラメータの調整
# 
# `hist`関数にオプションで `bin=100` を渡すと、階級を $100$ 個に分けることができます。

# In[8]:


plt.hist(data, bins=100)


# ```{tip}
# 実は**中心極限定理**によって、この分布は正規分布に近づいていきます。
# 
# [中心極限定理 - 統計WEB](https://bellcurve.jp/statistics/course/8543.html)
# ```
