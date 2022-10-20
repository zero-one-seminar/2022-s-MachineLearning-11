# Pythonの可視化ライブラリまとめ

## 汎用ツール
### [matplotlib](https://matplotlib.org/)
一番メジャーなライブラリ、ほとんどのグラフはこのライブラリで描画することが可能です。  
多機能であることも特徴の一つで、3Dプロットやアニメーションなどもサポートしています。

```{figure} ./images/e_potential.png
matplotlibの例
```

- [matplotlib でアニメーションを作る - Qiita](https://qiita.com/yubais/items/c95ba9ff1b23dd33fde2)

### [seaborn](https://seaborn.pydata.org/)
matplotlibよりも少しのコードで、より洗練された図を書くことができます。

```{figure} ./images/seaborn.png
seabornの例

[seaborn](https://seaborn.pydata.org/examples/scatterplot_matrix.html)より引用
```

### [plotly](https://plotly.com/python/)
手で動かすことのできる（インタラクティブな）グラフをかけるのが特長です。

[こんなかんじ](https://plotly.com/python/3d-axes/#:~:text=Range%20of%20axes,-3D%20figures%20have)

- [[Python] Plotlyでぐりぐり動かせるグラフを作る - Qiita](https://qiita.com/inoory/items/12028af62018bf367722)

### [Altair](https://altair-viz.github.io/)
こちらも、インタラクティブにデータを可視化できるライブラリです。  
直接htmlなどにレンダリングして、ファイルとして送ったりできるのが売りみたい。

- [可視化ライブラリAltairの便利な使い方](https://sakizo-blog.com/298/)

### [Bokeh](http://docs.bokeh.org/en/latest/)
またまた、インタラクティブです。Pythonの可視化ライブラリは群雄割拠ですね。  
これは使うのが多少簡単らしいです。


## 地理情報可視化ツール
位置情報と紐付いたデータを地図上に表示するツールです。

### [GeoPandas](https://geopandas.org/en/stable/)
地理データをPandasっぽく扱えるのが売りらしいです。

[こんなかんじ](https://qiita.com/c60evaporator/items/ac6a6d66a20520f129e6#:~:text=%E3%81%A8%E6%80%9D%E3%81%84%E3%81%BE%E3%81%99%E3%80%82-,GeoPandas%E3%81%A8%E3%81%AF,-GIS%EF%BC%88%E5%9C%B0%E7%90%86%E6%83%85%E5%A0%B1)

- [GeoPandas入門](https://sorabatake.jp/20510/)

## ネットワーク可視化ツール
グラフ（グラフ理論の方）を可視化できるツールです。  
グラフというとあまり馴染みがないかもしれませんが、たとえば、「SNSでユーザー同士がどう繋がっているのか」
みたいな情報を表したものです。

### [networkX](https://networkx.org/)
可視化だけでなく、データ処理も行えるツールです。

### [Graphviz](https://graphviz.readthedocs.io/en/stable/manual.html)
こちらは、フローチャートチックなプロットができます。  
オートマトンをいい感じに表示するのに向いてるかも！

```{figure} ./images/Q1.png
graphvizの例
```

- [Python上でGraphvizを使って綺麗なグラフを描く](https://programgenjin.hatenablog.com/entry/2019/02/26/075121)
