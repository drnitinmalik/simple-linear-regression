# Étapes de pré-régression, modèle de régression, analyse de post-régression

Dans la régression (également connue sous le nom d'approximation de fonction), nous sommes intéressés à prédire une variable (dépendante) à partir d'une ou plusieurs variables (indépendantes) (de n'importe quel type de données). Si nous avons une variable indépendante, il s'agit d'une simple régression, par exemple, prédire la taille à partir du poids. S'il y en a plusieurs, il s'agit d'une régression multiple, par ex. prédire la taille à partir du poids et de l'âge.

La régression implique la causalité. Le changement de la variable dépendante est dû au changement de la variable indépendante.

Linear regression implies that the relationship between the dependent variable and independent variable is linear and thus can be described by a straight line known as the **ligne de régression**. Nous sommes en train de trouver une droite de régression qui correspond (touche) au nombre maximum de points de données (nombre de points de données = nombre d'enregistrements dans l'ensemble de données).

L'incapacité de la droite de régression à toucher tous les points de données d'apprentissage est appelée biais. Un modèle d'apprentissage automatique avec un biais élevé accorde peu d'attention aux données d'apprentissage et simplifie à l'extrême le modèle.[cliquez pour tweeter](https://clicktotweet.com/6Rcfz)

When the same regression model is run on the test dataset, the model performance metric is reevaluated. If the metric value on test data is less than that obtained on training data, the model is said to be **sur-ajustement**. Si c'est l'inverse, alors on dit que le modèle est**sous-équipement**. Cette différence d'ajustement (biais) entre différents ensembles de données (ensemble de données d'entraînement et de test dans notre cas) est appelée**variance**. La variance est liée à un modèle qui ne correspond pas à l'ensemble de données de test. Un modèle à forte variance ne se généralise pas bien sur le jeu de données de test et est dit surajusté.

Continuez à lire sur[LinkedIn](https://www.linkedin.com/pulse/simple-linear-regression-overview-nitin-malik/)

La[code Python](https://github.com/drnitinmalik/simple-linear-regression/blob/main/predict-GPA-from-SAT.py)et le[fichier de données](https://github.com/drnitinmalik/simple-linear-regression/blob/main/SAT-GPA.csv)est sur github.

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)**Vous travaillez sur votre première pull request ?**Vous pouvez apprendre comment de ceci_libre_série[Comment contribuer à un projet Open Source sur GitHub](https://kcd.im/pull-request)
