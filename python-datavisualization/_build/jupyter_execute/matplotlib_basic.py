#!/usr/bin/env python
# coding: utf-8

# # Matplotlib（基礎編）
# 
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kentakom1213/practice-datavisualization/blob/main/matplotlib_basic.ipynb)
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
# **一定区間に等間隔で散らばった点を生成**
# 
# `np.arange(開始, 終了, 間隔)`

# In[2]:


x = np.arange(-1, 1, 0.1)  # -1から1まで、0.1刻みで点を生成する

x


# **関数にわたす**
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
# **データの生成**
# 
# $1〜6$ までの数字をランダムに $1000$ 回選んで平均を求めます。  
# これを $1000$ 回繰り返して、どんな分布になっているかをみてみます。

# In[6]:


from random import randint

data = []

for i in range(1000):

    # 1~6までの数字をランダムに選んで足す x 1000回
    sum_of_dice = 0
    for j in range(1000):
        sum_of_dice += randint(1, 6)
    
    ave_of_dice = sum_of_dice / 1000  # 1000で割って平均を出す
    data.append(ave_of_dice)


print(data[:10])  # 10個目までを見る


# **ヒストグラムを作成**
# 
# `plt.hist(データ)`
# 
# 自動的に階級の幅を決めてプロットしてくれます。
# この場合は $10$ 個の階級に分けられていました。

# In[7]:


plt.hist(data)


# ### パラメータの調整
# 
# `hist`関数にオプションで `bins=100` を渡すと、階級を $100$ 個に分けることができます。

# In[8]:


plt.hist(data, bins=100)


# ```{tip}
# 実は**中心極限定理**によって、この分布は正規分布に近づいていくらしいです。（よくわかってない）
# 
# [中心極限定理 - 統計WEB](https://bellcurve.jp/statistics/course/8543.html)
# ```

# ## 箱ひげ図
# 
# **データの生成**
# 
# 確率90%、60%、30%で表が出るコインを用意して、何回連続で表が出るかを調べます。  
# それぞれ1000回ずつ試行します。

# In[9]:


from random import randint


# In[10]:


prob_90 = []
prob_60 = []
prob_30 = []

for i in range(1000):

    # 90%が何回連続で出るか
    count_90 = 0
    while randint(1, 100) <= 90:
        count_90 += 1
    prob_90.append(count_90)

    # 60%が何回連続で出るか
    count_60 = 0
    while randint(1, 100) <= 60:
        count_60 += 1
    prob_60.append(count_60)

    # 30%が何回連続で出るか
    count_30 = 0
    while randint(1, 100) <= 30:
        count_30 += 1
    prob_30.append(count_30)

print("90%: ", prob_90[:20])
print("60%: ", prob_60[:20])
print("30%: ", prob_30[:20])


# In[11]:


plt.boxplot((prob_90, prob_60, prob_30))


# 90%だと70回以上出ることもあるのに対して、
# 30%だと10回以上連続で出ることはほとんどないですね。

# ## 参考
# - [Chainerチュートリアル](https://tutorials.chainer.org/ja/12_Introduction_to_Matplotlib.html)
