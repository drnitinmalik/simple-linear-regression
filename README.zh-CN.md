## 目录

-   [简单线性回归](https://github.com/drnitinmalik/simple-linear-regression#simple-linear-regression)
-   [代码和数据集](https://github.com/drnitinmalik/simple-linear-regression#code-and-dataset)
-   [错误和功能请求](https://github.com/drnitinmalik/simple-linear-regression#bugs-and-feature-requests)
-   [版权](https://github.com/drnitinmalik/simple-linear-regression#copyright)

## 简单线性回归

在回归（也称为函数逼近）中，我们感兴趣的是根据一个或多个（独立）变量（任何数据类型）预测一个（因）变量。如果我们有一个自变量，它就是简单回归，例如，根据体重预测身高。如果有多个，则为多元回归，例如根据体重和年龄预测身高。

回归意味着因果关系。因变量的变化是由于自变量的变化。

线性回归意味着因变量和自变量之间的关系是线性的，因此可以用称为**回归线**.我们正在寻找适合（接触）最大数据点数（数据点数 = 数据集中记录数）的回归线。

回归线无法触及所有训练数据点称为偏差。具有高偏差的机器学习模型很少关注训练数据并过度简化了模型。[点击鸣叫](https://clicktotweet.com/6Rcfz)

当在测试数据集上运行相同的回归模型时，将重新评估模型性能指标。如果测试数据上的度量值小于训练数据上获得的度量值，则称该模型是**过拟合**.如果它是相反的，那么模型就是**欠拟合**.不同数据集（在我们的案例中是训练和测试数据集）之间的这种拟合差异（偏差）称为**方差**.方差与无法拟合测试数据集的模型有关。具有高方差的模型不能很好地概括测试数据集，并且被称为过度拟合。

继续阅读[领英](https://www.linkedin.com/pulse/simple-linear-regression-overview-nitin-malik/)

## 代码和数据集

这[蟒蛇代码](https://github.com/drnitinmalik/simple-linear-regression/blob/main/predict-GPA-from-SAT.py)和[数据文件](https://github.com/drnitinmalik/simple-linear-regression/blob/main/SAT-GPA.csv)在github上。

## 错误和功能请求

识别代码中的错误或功能请求，[请打开一个新问题](https://github.com/drnitinmalik/simple-linear-regression/issues/new/choose)

## 版权

代码和文档版权所有 2020–2022[作者](https://github.com/drnitinmalik/simple-linear-regression/graphs/contributors).根据 MIT 许可证发布的代码。下发布的文档[创作共用](https://creativecommons.org/licenses/by/3.0/).

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)**正在处理您的第一个 Pull Request？**你可以从中学习如何_自由的_系列[如何为 GitHub 上的开源项目做出贡献](https://kcd.im/pull-request)
