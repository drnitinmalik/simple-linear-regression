# خطوات ما قبل الانحدار ، نموذج الانحدار ، تحليل ما بعد الانحدار

In regression (also known as function approximation), we are interested in predicting one (dependent) variable from one or more (independent) variables (of any datatype). If we have one independent variable it is simple regression e.g, predicting height from the weight. If there are more than one, it is multiple regression e.g. predicting height from weight and age.

الانحدار يعني السببية. التغيير في المتغير التابع يرجع إلى التغيير في المتغير المستقل.

يشير الانحدار الخطي إلى أن العلاقة بين المتغير التابع والمتغير المستقل هي علاقة خطية وبالتالي يمكن وصفها بخط مستقيم يعرف باسم**خط الانحدار**. نحن بصدد البحث عن خط انحدار يناسب (يلامس) الحد الأقصى لعدد نقاط البيانات (عدد نقاط البيانات = عدد السجلات في مجموعة البيانات).

يُطلق على عدم قدرة خط الانحدار على لمس جميع نقاط بيانات التدريب اسم التحيز. لا يولي نموذج التعلم الآلي ذو التحيز العالي اهتمامًا كبيرًا لبيانات التدريب ويبسط النموذج بشكل مفرط.[انقر للتغريد](https://clicktotweet.com/6Rcfz)

عند تشغيل نموذج الانحدار نفسه على مجموعة بيانات الاختبار ، تتم إعادة تقييم مقياس أداء النموذج. إذا كانت القيمة المترية لبيانات الاختبار أقل من تلك التي تم الحصول عليها في بيانات التدريب ، فيُقال إن النموذج كذلك**overfitting**. إذا كان الأمر مختلفًا ، فيُقال إن النموذج كذلك**underfitting**. يسمى هذا الاختلاف في النوبات (التحيز) بين مجموعات البيانات المختلفة (مجموعة بيانات التدريب والاختبار في حالتنا)**التباين**. يرتبط التباين بنموذج لا يلائم مجموعة بيانات الاختبار. النموذج ذو التباين العالي لا يعمم جيدًا على مجموعة بيانات الاختبار ويقال إنه مُجهز بشكل زائد.

أكمل القراءة في[ينكدين](https://www.linkedin.com/pulse/simple-linear-regression-overview-nitin-malik/)

ال[كود بيثون](https://github.com/drnitinmalik/simple-linear-regression/blob/main/predict-GPA-from-SAT.py)و ال[ملف البيانات](https://github.com/drnitinmalik/simple-linear-regression/blob/main/SAT-GPA.csv)موجود على جيثب.

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)**هل تعمل على أول طلب سحب لك؟**يمكنك أن تتعلم كيف من هذا_مجانا_سلسلة[كيفية المساهمة في مشروع مفتوح المصدر على GitHub](https://kcd.im/pull-request)
