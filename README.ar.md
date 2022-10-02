# خطوات ما قبل الانحدار ، نموذج الانحدار ، تحليل ما بعد الانحدار

في الانحدار (المعروف أيضًا باسم تقريب الوظيفة) ، نحن مهتمون بالتنبؤ بمتغير واحد (تابع) من متغير واحد أو أكثر (مستقل) (من أي نوع بيانات). إذا كان لدينا متغير مستقل واحد فهو انحدار بسيط ، على سبيل المثال ، توقع الارتفاع من الوزن. إذا كان هناك أكثر من واحد ، فهو انحدار متعدد ، على سبيل المثال. توقع الطول من الوزن والعمر.

الانحدار يعني السببية. التغيير في المتغير التابع يرجع إلى التغيير في المتغير المستقل.

Linear regression implies that the relationship between the dependent variable and independent variable is linear and thus can be described by a straight line known as the **خط الانحدار**. نحن بصدد البحث عن خط انحدار يناسب (يلامس) الحد الأقصى لعدد نقاط البيانات (عدد نقاط البيانات = عدد السجلات في مجموعة البيانات).

يُطلق على عدم قدرة خط الانحدار على لمس جميع نقاط بيانات التدريب اسم التحيز. لا يولي نموذج التعلم الآلي ذو التحيز العالي اهتمامًا كبيرًا لبيانات التدريب ويبسط النموذج بشكل مفرط.[click to tweet](https://clicktotweet.com/6Rcfz)

عند تشغيل نموذج الانحدار نفسه على مجموعة بيانات الاختبار ، تتم إعادة تقييم مقياس أداء النموذج. إذا كانت القيمة المترية لبيانات الاختبار أقل من تلك التي تم الحصول عليها في بيانات التدريب ، فيُقال إن النموذج كذلك**overfitting**. إذا كان الأمر مختلفًا ، فيُقال إن النموذج كذلك**غير مناسب**. This difference in fits (bias) between different datasets (training and testing dataset in our case) is called **التباين**. يرتبط التباين بنموذج لا يلائم مجموعة بيانات الاختبار. النموذج ذو التباين العالي لا يعمم جيدًا على مجموعة بيانات الاختبار ويقال إنه مُجهز بشكل زائد.

أكمل القراءة في[ينكدين](https://www.linkedin.com/pulse/simple-linear-regression-overview-nitin-malik/)

ال[كود بيثون](https://github.com/drnitinmalik/simple-linear-regression/blob/main/predict-GPA-from-SAT.py)و ال[ملف البيانات](https://github.com/drnitinmalik/simple-linear-regression/blob/main/SAT-GPA.csv)موجود على جيثب.

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)**هل تعمل على أول طلب سحب لك؟**يمكنك أن تتعلم كيف من هذا_مجانا_سلسلة[كيفية المساهمة في مشروع مفتوح المصدر على GitHub](https://kcd.im/pull-request)
