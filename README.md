# Pre-regression steps, Regression model, Post-regression analysis

In regression (also known as function approximation), we are interested in predicting one (dependent) variable from one or more (independent) variables (of any datatype). If we have one independent variable it is simple regression e.g, predicting height from the weight. If there are more than one, it is multiple regression e.g. predicting height from weight and age.

Regression implies causation. Change in the dependent variable is due to the change in the independent variable.

Linear regression implies that the relationship between the dependent variable and independent variable is linear and thus can be described by a straight line known as the **regression line**. We are in the process of finding a regression line that fits (touches) the maximum number of data points (no. of data points = no. of records in dataset).

The inability of the regression line to touch all the training data points is called bias. A machine learning model with high bias pays little attention to the training data and oversimplifies the model. [click to tweet](https://clicktotweet.com/6Rcfz)

When the same regression model is run on the test dataset, the model performance metric is reevaluated. If the metric value on test data is less than that obtained on training data, the model is said to be **overfitting**. If it's other way around, then the model is said to be **underfitting**. This difference in fits (bias) between different datasets (training and testing dataset in our case) is called **variance**. Variance is related to a model failing to fit the test dataset. A model with high variance does not generalises well on the test dataset and is said to be overfitted.

Continue reading at [linkedin](https://www.linkedin.com/pulse/simple-linear-regression-overview-nitin-malik/) 

The [python code](https://github.com/drnitinmalik/simple-linear-regression/blob/main/predict-GPA-from-SAT.py) and the [data file](https://github.com/drnitinmalik/simple-linear-regression/blob/main/SAT-GPA.csv) is on github.
