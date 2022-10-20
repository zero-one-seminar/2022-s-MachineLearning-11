#!/usr/bin/env python
# coding: utf-8

# # 演習問題
# 
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kentakom1213/practice-datavisualization/blob/main/matplotlib_practice.ipynb)
# 
# 演習問題です。
# 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


# 日本語対応
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']


# In[3]:


df = pd.read_csv('sample_data/california_housing_train.csv')

print(df.head(5))


# In[4]:


# カリフォルニアの気象データ
# ソース: https://www.data.jma.go.jp/cpd/monitor/climatview/graph_mkhtml_nrm.php?n=72494&m=1

# california_temp = pd.read_csv('sample_data/climat_72494_nrm.csv')

california_temp = pd.DataFrame(
    {
        "month": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "average_temperature": [10.7, 11.8, 13.0, 13.9, 15.4, 16.9, 17.7, 18.2, 18.2, 16.9, 13.4, 10.7],
        "precipitation_amount": [98.8, 100.2, 69.4, 35.2, 13.3, 3.8, 0.0, 1.0, 1.9, 20.0, 50.3, 105.9],
    }
)

california_temp


# ## 課題
# 
# 穴埋めで、下の図を完成させよう。
# 
# 1. 左上に`df['total_rooms']`と`df['total_bedrooms']`の箱ひげ図をプロット
# 2. 右上に`df['total_rooms']`と`df['total_bedrooms']`のヒストグラムを重ねてプロット  
#    `bins=100`を指定すること
# 3. 左下にカリフォルニアの雨温図をプロット  
#    （横軸:月, 縦軸:気温、降水量の折れ線グラフ）
# 4. 右下にカリフォルニアのハイサーグラフをプロット  
#    （(x, y) = (気温, 降水量)のグラフ）
# 
# ↓こんな感じ
# 
# ```{figure} images/california_stats.png
# ```

# In[5]:


### 問題 ###
# ... に当てはまるコードを入れてね

fig = plt.figure(figsize=(12, 10), dpi=100)

ax1 = ...
ax2 = ...
ax3 = ...
ax4 = ...

# ax1 (左上)
ax1. ...

# ax2 (右上)
ax2. ...  # label='total_rooms'
ax2. ...  # label='total_bedrooms'
ax2.legend(loc='upper right')

# ax3 (左下)
ax3. ... # label='temperature'
ax3. ... # label='precipitation'
ax3.legend(loc='upper right')

# ax4 (右下)
ax4. ...

#### タイトル
fig.suptitle('カリフォルニアの各種統計', fontsize=20)

ax1.set_title('total_rooms and total_bedrooms')
ax2.set_title('total_rooms and total_bedrooms')
ax3.set_title('temperature and precippitation')
ax4.set_title('hythergraph of california')

plt.show()


# ## 解答
# 
# <details><summary>解答</summary>
# <div>
# 
# ```python
# fig = plt.figure(figsize=(12, 10), dpi=100)
# 
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
# 
# # ax1 (左上)
# ax1.boxplot((df['total_rooms'], df['total_bedrooms']), labels=('total_rooms', 'total_bedrooms'))
# 
# # ax2 (右上)
# ax2.hist(df['total_rooms'], bins=100, label='total_rooms')
# ax2.hist(df['total_bedrooms'], bins=100, label='total_bedrooms')
# ax2.legend(loc='upper right')
# 
# # ax3 (左下)
# ax3.plot(california_temp['month'], california_temp['average_temperature'], label="temperature")
# ax3.plot(california_temp['month'], california_temp['precipitation_amount'], label="precipitation")
# ax3.legend(loc='upper right')
# 
# # ax4 (右下)
# ax4.plot(california_temp['average_temperature'], california_temp['precipitation_amount'])
# 
# #### タイトル
# fig.suptitle('カリフォルニアの各種統計', fontsize=20)
# 
# ax1.set_title('total_rooms and total_bedrooms')
# ax2.set_title('total_rooms and total_bedrooms')
# ax3.set_title('temperature and precippitation')
# ax4.set_title('hythergraph of california')
# 
# plt.show()
# ```
# 
# </div>
