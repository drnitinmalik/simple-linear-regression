# خطوات ما قبل الانحدار ، نموذج الانحدار ، تحليل ما بعد الانحدار

في الانحدار (المعروف أيضًا باسم تقريب الوظيفة) ، نحن مهتمون بالتنبؤ بمتغير واحد (تابع) من متغير واحد أو أكثر (مستقل) (من أي نوع بيانات). إذا كان لدينا متغير مستقل واحد فهو انحدار بسيط ، على سبيل المثال ، توقع الارتفاع من الوزن. إذا كان هناك أكثر من واحد ، فهو انحدار متعدد ، على سبيل المثال. توقع الطول من الوزن والعمر.

الانحدار يعني السببية. التغيير في المتغير التابع يرجع إلى التغيير في المتغير المستقل.

يشير الانحدار الخطي إلى أن العلاقة بين المتغير التابع والمتغير المستقل هي علاقة خطية وبالتالي يمكن وصفها بخط مستقيم يعرف باسم**خط الانحدار**. نحن بصدد البحث عن خط انحدار يناسب (يلامس) الحد الأقصى لعدد نقاط البيانات (عدد نقاط البيانات = عدد السجلات في مجموعة البيانات).

The inability of the regression line to touch all the training data points is called bias. A machine learning model with high bias pays little attention to the training data and oversimplifies the model. [انقر للتغريد](https://clicktotweet.com/6Rcfz)

When the same regression model is run on the test dataset, the model performance metric is reevaluated. If the metric value on test data is less than that obtained on training data, the model is said to be **overfitting**. إذا كان الأمر مختلفًا ، فيُقال إن النموذج كذلك**غير مناسب**. يسمى هذا الاختلاف في النوبات (التحيز) بين مجموعات البيانات المختلفة (مجموعة بيانات التدريب والاختبار في حالتنا)**التباين**. يرتبط التباين بنموذج لا يلائم مجموعة بيانات الاختبار. النموذج ذو التباين العالي لا يعمم جيدًا على مجموعة بيانات الاختبار ويقال إنه مُجهز بشكل زائد.

أكمل القراءة في[ينكدين](https://www.linkedin.com/pulse/simple-linear-regression-overview-nitin-malik/)

ال[كود بيثون](https://github.com/drnitinmalik/simple-linear-regression/blob/main/predict-GPA-from-SAT.py)و ال[ملف البيانات](https://github.com/drnitinmalik/simple-linear-regression/blob/main/SAT-GPA.csv)موجود على جيثب.

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
**هل تعمل على أول طلب سحب لك؟**يمكنك أن تتعلم كيف من هذا_مجانا_سلسلة[كيفية المساهمة في مشروع مفتوح المصدر على GitHub](https://kcd.im/pull-request)
