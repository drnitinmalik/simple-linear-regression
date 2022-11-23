## 目錄

-   [簡單線性回歸](https://github.com/drnitinmalik/simple-linear-regression#simple-linear-regression)
-   [代碼和數據集](https://github.com/drnitinmalik/simple-linear-regression#code-and-dataset)
-   [錯誤和功能請求](https://github.com/drnitinmalik/simple-linear-regression#bugs-and-feature-requests)
-   [提交拉取請求](https://github.com/drnitinmalik/simple-linear-regression#submitting-a-pull-request)
-   [版權](https://github.com/drnitinmalik/simple-linear-regression#copyright)

## 簡單線性回歸

在回歸（也稱為函數逼近）中，我們感興趣的是根據一個或多個（獨立）變量（任何數據類型）預測​​一個（因）變量。如果我們有一個自變量，它就是簡單回歸，例如，根據體重預測身高。如果有多個，則為多元回歸，例如根據體重和年齡預測身高。

回歸意味著因果關係。因變量的變化是由於自變量的變化。

線性回歸意味著因變量和自變量之間的關係是線性的，因此可以用稱為**回歸線**.我們正在尋找適合（接觸）最大數據點數（數據點數 = 數據集中記錄數）的回歸線。

回歸線無法觸及所有訓練數據點稱為偏差。具有高偏差的機器學習模型很少關注訓練數據並過度簡化了模型。[點擊鳴叫](https://clicktotweet.com/6Rcfz)

當在測試數據集上運行相同的回歸模型時，將重新評估模型性能指標。如果測試數據上的度量值小於訓練數據上獲得的度量值，則稱該模型是**過擬合**.如果它是相反的，那麼模型就是**欠擬合**.不同數據集（在我們的案例中是訓練和測試數據集）之間的這種擬合差異（偏差）稱為**方差**.方差與無法擬合測試數據集的模型有關。具有高方差的模型不能很好地概括測試數據集，並且被稱為過度擬合。

繼續閱讀[領英](https://www.linkedin.com/pulse/simple-linear-regression-overview-nitin-malik/)

## 代碼和數據集

這[蟒蛇代碼](https://github.com/drnitinmalik/simple-linear-regression/blob/main/predict-GPA-from-SAT.py)和[數據文件](https://github.com/drnitinmalik/simple-linear-regression/blob/main/SAT-GPA.csv)在github上。

## 錯誤和功能請求

識別代碼中的錯誤或功能請求，[請打開一個新問題](https://github.com/drnitinmalik/simple-linear-regression/issues/new/choose)

## 提交拉取請求

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)**正在處理您的第一個 Pull Request？**你可以從中學習如何_自由的_系列[如何為 GitHub 上的開源項目做出貢獻](https://kcd.im/pull-request)

## 版權

代碼和文檔版權所有 2020–2022[作者](https://github.com/drnitinmalik/simple-linear-regression/graphs/contributors).根據 MIT 許可證發布的代碼。下發布的文檔[創作共用](https://creativecommons.org/licenses/by/3.0/).
