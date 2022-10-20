#!/usr/bin/env python
# coding: utf-8

# # Pythonによるデータ可視化入門
# 
# ## ライブラリ
# 
# ### 汎用
# #### ┣ matplotlib
# 一番メジャーなライブラリ、ほとんどのグラフはこのライブラリで描画することが可能。  
# 多機能であることも特徴の一つで、3Dプロットやアニメーションなどもサポートしている
# 
# - [matplotlib でアニメーションを作る - Qiita](https://qiita.com/yubais/items/c95ba9ff1b23dd33fde2)
# - [matplotlib.animationでグラフをアニメーションさせる - Qiita](https://qiita.com/studio_haneya/items/891c4ea6a7326919e381)
# 
# #### ┣ seaborn
# 
# #### ┣ plotly
# 
# #### ┗ Altair
# 
# ### 特定の機能に特化したもの
# #### ┣ networkX
# 
# #### ┣ Graphviz
# 
# #### ┗ Folium
# 

# In[1]:


# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


x = np.arange(-3, 3, 0.01)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1)
plt.show()

plt.plot(x, y2)
plt.show()

