# 回归前步骤、回归模型、回归后分析

In regression (also known as function approximation), we are interested in predicting one (dependent) variable from one or more (independent) variables (of any datatype). If we have one independent variable it is simple regression e.g, predicting height from the weight. If there are more than one, it is multiple regression e.g. predicting height from weight and age.

回归意味着因果关系。因变量的变化是由于自变量的变化。

Linear regression implies that the relationship between the dependent variable and independent variable is linear and thus can be described by a straight line known as the **回归线**.我们正在寻找适合（触及）最大数据点数（数据点数 = 数据集中记录数）的回归线。

回归线无法触及所有训练数据点称为偏差。具有高偏差的机器学习模型很少关注训练数据并且过度简化了模型。[点击发推文](https://clicktotweet.com/6Rcfz)

当在测试数据集上运行相同的回归模型时，会重新评估模型性能指标。如果测试数据上的度量值小于训练数据上的度量值，则称该模型为**过拟合**.如果它是其他方式，那么模型被称为**欠拟合**.不同数据集（在我们的例子中是训练和测试数据集）之间的拟合（偏差）差异称为**方差**.方差与无法拟合测试数据集的模型有关。具有高方差的模型不能很好地在测试数据集上泛化，并且被称为过度拟合。

继续阅读[链接素](https://www.linkedin.com/pulse/simple-linear-regression-overview-nitin-malik/)

这[蟒蛇代码](https://github.com/drnitinmalik/simple-linear-regression/blob/main/predict-GPA-from-SAT.py)和[数据文件](https://github.com/drnitinmalik/simple-linear-regression/blob/main/SAT-GPA.csv) is on github.

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)**处理你的第一个拉取请求？**你可以从中学习如何_自由的_ series [如何为 GitHub 上的开源项目做出贡献](https://kcd.im/pull-request)
