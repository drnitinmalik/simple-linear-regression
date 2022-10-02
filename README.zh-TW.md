# 回歸前步驟、回歸模型、回歸後分析

In regression (also known as function approximation), we are interested in predicting one (dependent) variable from one or more (independent) variables (of any datatype). If we have one independent variable it is simple regression e.g, predicting height from the weight. If there are more than one, it is multiple regression e.g. predicting height from weight and age.

回歸意味著因果關係。因變量的變化是由於自變量的變化。

線性回歸意味著因變量和自變量之間的關係是線性的，因此可以用一條稱為**回歸線**.我們正在尋找一條適合（觸及）最大數據點數（數據點數 = 數據集中記錄數）的回歸線。

The inability of the regression line to touch all the training data points is called bias. A machine learning model with high bias pays little attention to the training data and oversimplifies the model. [點擊推文](https://clicktotweet.com/6Rcfz)

當在測試數據集上運行相同的回歸模型時，會重新評估模型性能指標。如果測試數據上的度量值小於訓練數據上的度量值，則稱該模型為**過擬合**.如果它是其他方式，那麼模型被稱為**欠擬合**.不同數據集（在我們的例子中是訓練和測試數據集）之間的擬合（偏差）差異稱為**方差**.方差與無法擬合測試數據集的模型有關。具有高方差的模型不能很好地在測試數據集上泛化，並且被稱為過度擬合。

繼續閱讀[鏈接素](https://www.linkedin.com/pulse/simple-linear-regression-overview-nitin-malik/)

The [蟒蛇代碼](https://github.com/drnitinmalik/simple-linear-regression/blob/main/predict-GPA-from-SAT.py)和[數據文件](https://github.com/drnitinmalik/simple-linear-regression/blob/main/SAT-GPA.csv)在github上。

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)**處理你的第一個拉取請求？**你可以從中學習如何_自由的_系列[如何為 GitHub 上的開源項目做出貢獻](https://kcd.im/pull-request)
