# 回歸前步驟、回歸模型、回歸後分析

在回歸（也稱為函數逼近）中，我們感興趣的是從一個或多個（獨立）變量（任何數據類型）預測​​一個（因）變量。如果我們有一個自變量，那就是簡單的回歸，例如，根據體重預測身高。如果有多個，則為多元回歸，例如根據體重和年齡預測身高。

回歸意味著因果關係。因變量的變化是由於自變量的變化。

線性回歸意味著因變量和自變量之間的關係是線性的，因此可以用一條稱為**回歸線**.我們正在尋找適合（觸及）最大數據點數（數據點數 = 數據集中記錄數）的回歸線。

回歸線無法觸及所有訓練數據點稱為偏差。具有高偏差的機器學習模型很少關注訓練數據並且過度簡化了模型。[點擊發推文](https://clicktotweet.com/6Rcfz)

當在測試數據集上運行相同的回歸模型時，會重新評估模型性能指標。如果測試數據上的度量值小於訓練數據上的度量值，則稱該模型為**過擬合**.如果它是其他方式，那麼模型被稱為**欠擬合**.不同數據集（在我們的例子中是訓練和測試數據集）之間的擬合（偏差）差異稱為**方差**.方差與無法擬合測試數據集的模型有關。具有高方差的模型不能很好地在測試數據集上泛化，並且被稱為過度擬合。

繼續閱讀[鏈接素](https://www.linkedin.com/pulse/simple-linear-regression-overview-nitin-malik/) 

這[蟒蛇代碼](https://github.com/drnitinmalik/simple-linear-regression/blob/main/predict-GPA-from-SAT.py)和[數據文件](https://github.com/drnitinmalik/simple-linear-regression/blob/main/SAT-GPA.csv)在github上。

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)**處理你的第一個拉取請求？**你可以從中學習如何_自由的_系列[How to Contribute to an Open Source Project on GitHub](https://kcd.im/pull-request)
