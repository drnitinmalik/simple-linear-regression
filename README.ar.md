## جدول المحتويات

-   [الانحدار الخطي البسيط](https://github.com/drnitinmalik/simple-linear-regression#simple-linear-regression)
-   [الكود ومجموعة البيانات](https://github.com/drnitinmalik/simple-linear-regression#code-and-dataset)
-   [طلبات البق والميزات](https://github.com/drnitinmalik/simple-linear-regression#bugs-and-feature-requests)
-   [تقديم طلب سحب](https://github.com/drnitinmalik/simple-linear-regression#submitting-a-pull-request)
-   [حقوق النشر](https://github.com/drnitinmalik/simple-linear-regression#copyright)

## الانحدار الخطي البسيط

في الانحدار (المعروف أيضًا باسم تقريب الوظيفة) ، نحن مهتمون بالتنبؤ بمتغير واحد (تابع) من متغير واحد أو أكثر (مستقل) (من أي نوع بيانات). إذا كان لدينا متغير مستقل واحد فهو انحدار بسيط ، على سبيل المثال ، توقع الارتفاع من الوزن. إذا كان هناك أكثر من واحد ، فهو انحدار متعدد ، على سبيل المثال. توقع الطول من الوزن والعمر.

الانحدار يعني السببية. التغيير في المتغير التابع يرجع إلى التغيير في المتغير المستقل.

يشير الانحدار الخطي إلى أن العلاقة بين المتغير التابع والمتغير المستقل هي علاقة خطية وبالتالي يمكن وصفها بخط مستقيم يعرف باسم**خط الانحدار**. نحن بصدد العثور على خط انحدار يناسب (يلامس) الحد الأقصى لعدد نقاط البيانات (عدد نقاط البيانات = عدد السجلات في مجموعة البيانات).

يُطلق على عدم قدرة خط الانحدار على لمس جميع نقاط بيانات التدريب اسم التحيز. لا يولي نموذج التعلم الآلي ذو التحيز العالي اهتمامًا كبيرًا لبيانات التدريب ويبسط النموذج بشكل مفرط.[انقر للتغريد](https://clicktotweet.com/6Rcfz)

عند تشغيل نموذج الانحدار نفسه على مجموعة بيانات الاختبار ، تتم إعادة تقييم مقياس أداء النموذج. إذا كانت القيمة المترية لبيانات الاختبار أقل من تلك التي تم الحصول عليها في بيانات التدريب ، فيُقال إن النموذج كذلك**overfitting**. إذا كان الأمر مختلفًا ، فيُقال إن النموذج كذلك**غير مناسب**. يسمى هذا الاختلاف في النوبات (التحيز) بين مجموعات البيانات المختلفة (مجموعة بيانات التدريب والاختبار في حالتنا)**التباين**. يرتبط التباين بنموذج لا يلائم مجموعة بيانات الاختبار. النموذج ذو التباين العالي لا يعمم جيدًا على مجموعة بيانات الاختبار ويقال إنه مُجهز بشكل زائد.

Continue reading at [ينكدين](https://www.linkedin.com/pulse/simple-linear-regression-overview-nitin-malik/)

## الكود ومجموعة البيانات

ال[كود بيثون](https://github.com/drnitinmalik/simple-linear-regression/blob/main/predict-GPA-from-SAT.py)و ال[ملف البيانات](https://github.com/drnitinmalik/simple-linear-regression/blob/main/SAT-GPA.csv)موجود على جيثب.

## طلبات البق والميزات

حددت الخلل في التعليمات البرمجية أو طلبات الميزات ،[الرجاء فتح عدد جديد](https://github.com/drnitinmalik/simple-linear-regression/issues/new/choose)

## تقديم طلب سحب

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)**هل تعمل على أول طلب سحب لك؟**يمكنك أن تتعلم كيف من هذا_مجانا_سلسلة[كيفية المساهمة في مشروع مفتوح المصدر على GitHub](https://kcd.im/pull-request)

## حقوق النشر

حقوق النشر الخاصة بالتعليمات البرمجية والتوثيق 2020-2022[المؤلف](https://github.com/drnitinmalik/simple-linear-regression/graphs/contributors). تم إصدار الرمز بموجب ترخيص MIT. تم إصدار المستندات بموجب[Creative Commons](https://creativecommons.org/licenses/by/3.0/).
