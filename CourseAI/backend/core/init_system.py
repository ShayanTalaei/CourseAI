from model.student import *
from model.question import *

def initialize_system():
    student = Student("شایان")
    # load questions into all questions
    
    Question.all_questions = animal_questions + fruit_questions + music_questions + countries_questions + clothing_questions + sports_questions
    #[Question.generate_random_question() for _ in range(100)]

    return student






### Sample questions, 6 topics: animals, fruits, music, countries, clothing, sports

animal_questions = []

# سوال 1
question1 = Question(
    "توضیح دهید که چرا گوزن‌ها در پرواز نمی‌پرند؟",
    ["چون بال‌های آن‌ها برای پرواز مناسب نیست.", "چون پرواز برای آن‌ها ضروری نیست.", "چون وزن زیادی دارند.", "چون مهارت پرواز ندارند."],
    correct_option_id=1,
    hardness=4,
    importance=5,
    chapter=1,
    section=0,
    subsection=1,
    page=5,
    tags=["حیوانات"]
)
animal_questions.append(question1)

# سوال 2
question2 = Question(
    "استراتژی دفاعی مورچه‌ها در مقابل حشرات دیگر چگونه است؟",
    ["توسط دفاع شخصی", "توسط ترکیبات شیمیایی", "توسط شمشیر", "توسط پریدن"],
    correct_option_id=1,
    hardness=3,
    importance=4,
    chapter=1,
    section=1,
    subsection=0,
    page=7,
    tags=["حیوانات"]
)
animal_questions.append(question2)

# سوال 3
question3 = Question(
    "تفاوت بین خرگوش‌های وحشی و خرگوش‌های خانگی چیست؟",
    ["خرگوش‌های وحشی دارای رنگ‌های مختلف هستند.", "خرگوش‌های وحشی به صورت انفرادی زندگی می‌کنند.", "خرگوش‌های وحشی از نوع پرندگان هستند.", "خرگوش‌های وحشی از نوع آبزیان هستند."],
    correct_option_id=1,
    hardness=4,
    importance=3,
    chapter=1,
    section=0,
    subsection=2,
    page=9,
    tags=["حیوانات"]
)
animal_questions.append(question3)

# سوال 4
question4 = Question(
    "میگوییم گرگ‌ها جلوی چه حیوانی نمی‌روند؟",
    ["خرگوش", "شیر", "زرافه", "گربه"],
    correct_option_id=1,
    hardness=2,
    importance=4,
    chapter=1,
    section=1,
    subsection=1,
    page=12,
    tags=["حیوانات"]
)
animal_questions.append(question4)

animal_questions = []

# سوال 6
question6 = Question(
    "چگونه فرآیند تغذیه در گرگ‌ها اتفاق می‌افتد و چگونه این حیوانات جلوی شکار می‌روند؟",
    ["فرآیند تغذیه گرگ‌ها برای تامین انرژی برای شکار بسیار بهینه‌سازی شده است و آن‌ها با استفاده از تاکتیک‌های شکار مختلف، شکار می‌کنند.", "گرگ‌ها تنها از شکارچی‌های حرفه‌ای کمک می‌گیرند تا شکار را انجام دهند.", "گرگ‌ها هیچگاه جلوی شکار نمی‌روند و به صورت تصادفی شکار می‌کنند.", "گرگ‌ها فقط از شکارهایی که به آن‌ها حمله می‌کنند جلویی می‌روند."],
    correct_option_id=0,
    hardness=4,
    importance=5,
    chapter=1,
    section=2,
    subsection=1,
    page=14,
    tags=["حیوانات", "شکار"]
)
animal_questions.append(question6)

# سوال 7
question7 = Question(
    "چرا مهاجمان در مقابل خرگوش‌ها شکار نمی‌کنند؟",
    ["چون خرگوش‌ها دارای سرعت بسیار بالا هستند و از آن‌ها دشوار است فرار کنند.", "خرگوش‌ها دارای دفاعات مختلفی هستند که مهاجمان را از خود دور نگه می‌دارند.", "مهاجمان تنها در شب شکار می‌کنند و در روز به خرگوش‌ها حمله نمی‌کنند.", "خرگوش‌ها به طور تاریکی روشنایی‌های نقلی تولید می‌کنند که مهاجمان را از خود دور نگه می‌دارند."],
    correct_option_id=1,
    hardness=3,
    importance=4,
    chapter=1,
    section=2,
    subsection=2,
    page=16,
    tags=["حیوانات", "دفاع"]
)
animal_questions.append(question7)

# سوال 8
question8 = Question(
    "چرا زرافه‌ها گردن بلند دارند؟",
    ["برای نمایش اجتماعی", "برای به دست آوردن غذاهای بالا", "برای دفاع در برابر حیوانات مهاجم", "برای جلب نرهای دیگر"],
    correct_option_id=1,
    hardness=4,
    importance=3,
    chapter=1,
    section=0,
    subsection=1,
    page=19,
    tags=["حیوانات", "مورفولوژی"]
)
animal_questions.append(question8)

# سوال 9
question9 = Question(
    "چرا مورچه‌ها توده‌های بزرگی از مورچه‌های کوچک جمع می‌کنند؟",
    ["برای مهاجمت به حشرات دیگر", "برای ایجاد ساختارهای پیچیده", "برای ذخیره غذا", "برای ایجاد حمله گروهی به دشمنان خود"],
    correct_option_id=2,
    hardness=4,
    importance=5,
    chapter=1,
    section=1,
    subsection=0,
    page=22,
    tags=["حیوانات", "اجتماعیت"]
)
animal_questions.append(question9)



# لیست سوالات جدید با تمرکز بر روی میوه‌ها
fruit_questions = []

# سوال 11
question11 = Question(
    "میوه آناناس اصلیاً در کدام منطقه جهان کشت می‌شود؟",
    ["آمریکای جنوبی", "آفریقا", "آسیا", "استرالیا"],
    correct_option_id=0,
    hardness=3,
    importance=4,
    chapter=2,
    section=0,
    subsection=1,
    page=10,
    tags=["میوه‌ها", "آناناس"]
)
fruit_questions.append(question11)

# سوال 12
question12 = Question(
    "میوه خیار از چه خانواده‌ای است؟",
    ["خانواده گلابی", "خانواده خربزه", "خانواده بادمجان", "خانواده کدو"],
    correct_option_id=3,
    hardness=2,
    importance=3,
    chapter=2,
    section=1,
    subsection=0,
    page=12,
    tags=["میوه‌ها", "خیار"]
)
fruit_questions.append(question12)

# سوال 13
question13 = Question(
    "کدام میوه از دسته میوه‌های خشک به شمار می‌آید؟",
    ["سیب", "هلو", "خرمالو", "خرما"],
    correct_option_id=3,
    hardness=2,
    importance=3,
    chapter=2,
    section=0,
    subsection=2,
    page=15,
    tags=["میوه‌ها", "خشکبار"]
)
fruit_questions.append(question13)

# سوال 14
question14 = Question(
    "عناصر غذایی اصلی در میوه توت فرنگی چیستند؟",
    ["ویتامین C و کلسیم", "پتاسیم و فیبر", "آهن و ویتامین A", "مگنز و ویتامین D"],
    correct_option_id=1,
    hardness=3,
    importance=4,
    chapter=2,
    section=1,
    subsection=1,
    page=18,
    tags=["میوه‌ها", "توت فرنگی"]
)
fruit_questions.append(question14)

# سوال 15
question15 = Question(
    "کدام میوه اصلیاً در نیمکره شمالی کشت می‌شود؟",
    ["پرتقال", "مانگو", "پاپایا", "کیوی"],
    correct_option_id=0,
    hardness=2,
    importance=3,
    chapter=2,
    section=2,
    subsection=0,
    page=20,
    tags=["میوه‌ها", "پرتقال"]
)
fruit_questions.append(question15)

# سوال 16
question16 = Question(
    "میوه گلابی از کدام خانواده میوه‌ای می‌آید؟",
    ["خانواده سیب", "خانواده گلابی", "خانواده زردآلو", "خانواده انار"],
    correct_option_id=0,
    hardness=2,
    importance=3,
    chapter=2,
    section=0,
    subsection=1,
    page=23,
    tags=["میوه‌ها", "گلابی"]
)
fruit_questions.append(question16)

# سوال 17
question17 = Question(
    "عنصر غذایی اصلی در میوه بلوبری چیست؟",
    ["کلسیم", "پروتئین", "فیبر", "آهن"],
    correct_option_id=2,
    hardness=3,
    importance=4,
    chapter=2,
    section=1,
    subsection=2,
    page=26,
    tags=["میوه‌ها", "بلوبری"]
)
fruit_questions.append(question17)

# سوال 18
question18 = Question(
    "میوه انار چه مزایای بهداشتی دارد؟",
    ["افزایش حافظه", "کاهش کلسترول خون", "افزایش قدرت بینایی", "افزایش انرژی"],
    correct_option_id=1,
    hardness=3,
    importance=5,
    chapter=2,
    section=0,
    subsection=2,
    page=29,
    tags=["میوه‌ها", "انار"]
)
fruit_questions.append(question18)

# سوال 19
question19 = Question(
    "کدام میوه برای تقویت سیستم ایمنی بدن مفید است؟",
    ["خرما", "اناناس", "توت فرنگی", "توت"],
    correct_option_id=0,
    hardness=2,
    importance=4,
    chapter=2,
    section=2,
    subsection=1,
    page=32,
    tags=["میوه‌ها", "خرما"]
)
fruit_questions.append(question19)

# سوال 20
question20 = Question(
    "چرا توت فرنگی به عنوان یک میوه سوزانده معروف است؟",
    ["چون میوه‌های آن به راحتی سوخته و می‌سوزند.", "چون توت فرنگی دارای طعم تند و حاره‌ای است.", "چون توت فرنگی تنها در تابستان رشد می‌کند.", "چون توت فرنگی دارای رنگ قرمز زیبایی است."],
    correct_option_id=0,
    hardness=3,
    importance=3,
    chapter=2,
    section=1,
    subsection=2,
    page=35,
    tags=["میوه‌ها", "توت فرنگی"]
)
fruit_questions.append(question20)



# لیست سوالات با موضوع موسیقی
music_questions = []

# سوال 21
question21 = Question(
    "چه نامی به ساز پیانو داده می‌شود؟",
    ["کیبورد", "کلارینت", "پیانو", "گیتار"],
    correct_option_id=2,
    hardness=3,
    importance=4,
    chapter=3,
    section=0,
    subsection=1,
    page=10,
    tags=["موسیقی", "پیانو"]
)
music_questions.append(question21)

# سوال 22
question22 = Question(
    "کدام آهنگساز معروف برای آثارش در زمینه موسیقی کلاسیک شناخته می‌شود؟",
    ["لودویگ فان بتهوون", "مایکل جکسون", "باب مارلی", "تایلور سویفت"],
    correct_option_id=0,
    hardness=3,
    importance=4,
    chapter=3,
    section=1,
    subsection=0,
    page=12,
    tags=["موسیقی", "آهنگساز"]
)
music_questions.append(question22)

# سوال 23
question23 = Question(
    "کدام نوع موسیقی به عنوان موسیقی ملل شناخته می‌شود و معمولاً با استفاده از سازهای مختلف جهانی اجرا می‌شود؟",
    ["پاپ", "راک", "موسیقی کلاسیک", "جهانی"],
    correct_option_id=3,
    hardness=4,
    importance=5,
    chapter=3,
    section=0,
    subsection=2,
    page=15,
    tags=["موسیقی", "موسیقی جهانی"]
)
music_questions.append(question23)

# سوال 24
question24 = Question(
    "چه نامی به ترکیبی از نت‌های موسیقی به منظور ایجاد تغییر در ارتفاع صدا داده می‌شود؟",
    ["آکورد", "ملودی", "هارمونی", "ترانزیشن"],
    correct_option_id=0,
    hardness=3,
    importance=4,
    chapter=3,
    section=1,
    subsection=1,
    page=18,
    tags=["موسیقی", "آکورد"]
)
music_questions.append(question24)

# سوال 25
question25 = Question(
    "آهنگ 'بوهمیان راپسدی' اثر کدام گروه موسیقی معروف است؟",
    ["رولینگ استونز", "بیتلز", "کوئین", "پینک فلوید"],
    correct_option_id=2,
    hardness=2,
    importance=3,
    chapter=3,
    section=2,
    subsection=0,
    page=20,
    tags=["موسیقی", "آهنگ"]
)
music_questions.append(question25)

# سوال 26
question26 = Question(
    "چه نامی به ترکیبی از دسته‌های ریتمیک و صداها داده می‌شود که به صورت خلاقانه در موسیقی مورد استفاده قرار می‌گیرد؟",
    ["آهنگ", "همخوانی", "ساز", "صداپیشه"],
    correct_option_id=3,
    hardness=3,
    importance=4,
    chapter=3,
    section=1,
    subsection=2,
    page=23,
    tags=["موسیقی", "صداپیشه"]
)
music_questions.append(question26)

# سوال 27
question27 = Question(
    "کدام ساز موسیقی چندگانه و چندصدا است و به کمک دست‌ها و پاها برای تولید صداها استفاده می‌شود؟",
    ["پیانو", "ترومبون", "سازهای کوبه‌ای", "ویولن"],
    correct_option_id=2,
    hardness=3,
    importance=4,
    chapter=3,
    section=0,
    subsection=1,
    page=26,
    tags=["موسیقی", "سازهای کوبه‌ای"]
)
music_questions.append(question27)

# سوال 28
question28 = Question(
    "آهنگساز مشهور 'لودویگ وان بتهوون' چه کدام اثر را به نام خود ساخته است؟",
    ["سونات برای ویولن و پیانو", "پیانوسونات دیالیچین برای دو پیانو", "نخستین سمفونی", "کنسرتو برای کلارینت و ارکستر"],
    correct_option_id=2,
    hardness=4,
    importance=5,
    chapter=3,
    section=1,
    subsection=0,
    page=29,
    tags=["موسیقی", "لودویگ وان بتهوون"]
)
music_questions.append(question28)

# سوال 29
question29 = Question(
    "موسیقی راک در دهه 1960 در کدام کشور شروع شد؟",
    ["انگلستان", "آمریکا", "کانادا", "آسترالیا"],
    correct_option_id=1,
    hardness=3,
    importance=4,
    chapter=3,
    section=2,
    subsection=1,
    page=32,
    tags=["موسیقی", "راک"]
)
music_questions.append(question29)

# سوال 30
question30 = Question(
    "کدام موسیقی‌دان معروف به عنوان 'ملکه پاپ' شناخته می‌شود؟",
    ["مایکل جکسون", "مدونا", "ویتنی هیوستون", "التون جان"],
    correct_option_id=1,
    hardness=2,
    importance=3,
    chapter=3,
    section=0,
    subsection=2,
    page=35,
    tags=["موسیقی", "ملکه پاپ"]
)
music_questions.append(question30)

# لیست سوالات با موضوع کشورها
countries_questions = []

# سوال 31
question31 = Question(
    "کدام کشور بزرگترین کشور جهان از لحاظ مساحت است؟",
    ["کانادا", "آمریکا", "روسیه", "چین"],
    correct_option_id=2,
    hardness=3,
    importance=4,
    chapter=4,
    section=0,
    subsection=1,
    page=10,
    tags=["کشورها", "روسیه"]
)
countries_questions.append(question31)

# سوال 32
question32 = Question(
    "کدام کشور به عنوان 'کشور پناهندگی' شناخته می‌شود و بسیاری از پناهندگان از سرزمین‌های دیگر در آن می‌پناهند؟",
    ["آلمان", "کانادا", "استرالیا", "سوئد"],
    correct_option_id=0,
    hardness=3,
    importance=4,
    chapter=4,
    section=1,
    subsection=0,
    page=12,
    tags=["کشورها", "آلمان"]
)
countries_questions.append(question32)

# سوال 33
question33 = Question(
    "کشوری که شهرت دارد به عنوان 'کشور زرع و دیزاین' چیست؟",
    ["ایتالیا", "فرانسه", "هلند", "آلمان"],
    correct_option_id=2,
    hardness=3,
    importance=4,
    chapter=4,
    section=0,
    subsection=2,
    page=15,
    tags=["کشورها", "هلند"]
)
countries_questions.append(question33)

# سوال 34
question34 = Question(
    "در کدام قاره جمعیت کمتری دارد؟",
    ["آفریقا", "آسیا", "اروپا", "آمریکا شمالی"],
    correct_option_id=2,
    hardness=3,
    importance=4,
    chapter=4,
    section=1,
    subsection=1,
    page=18,
    tags=["کشورها", "اروپا"]
)
countries_questions.append(question34)

# سوال 35
question35 = Question(
    "کدام کشور به عنوان 'کشور آفتابگردان' شناخته می‌شود؟",
    ["کره جنوبی", "ترکیه", "مکزیک", "ارمنستان"],
    correct_option_id=0,
    hardness=2,
    importance=3,
    chapter=4,
    section=0,
    subsection=1,
    page=20,
    tags=["کشورها", "کره جنوبی"]
)
countries_questions.append(question35)

# سوال 36
question36 = Question(
    "کدام کشور دارای بیشترین تعداد جمعیت در جهان است؟",
    ["چین", "هند", "آمریکا", "اندونزی"],
    correct_option_id=0,
    hardness=3,
    importance=4,
    chapter=4,
    section=2,
    subsection=0,
    page=22,
    tags=["کشورها", "چین"]
)
countries_questions.append(question36)

# سوال 37
question37 = Question(
    "کدام کشور به عنوان 'کشور آتشفشان‌ها' شناخته می‌شود و دارای تعداد زیادی آتشفشان است؟",
    ["ژاپن", "ایسلند", "ایتالیا", "اندونزی"],
    correct_option_id=1,
    hardness=3,
    importance=4,
    chapter=4,
    section=1,
    subsection=2,
    page=25,
    tags=["کشورها", "ایسلند"]
)
countries_questions.append(question37)

# سوال 38
question38 = Question(
    "کدام کشور دارای بیشترین تعداد زبان ملی است؟",
    ["هند", "پاکستان", "کانادا", "جمهوری چین"],
    correct_option_id=0,
    hardness=3,
    importance=4,
    chapter=4,
    section=2,
    subsection=1,
    page=28,
    tags=["کشورها", "هند"]
)
countries_questions.append(question38)

# سوال 39
question39 = Question(
    "کدام کشور به عنوان 'کشور قهوه' شناخته می‌شود و معروف به تولید و مصرف قهوه است؟",
    ["کلمبیا", "بازیل", "کوبا", "اتیوپی"],
    correct_option_id=1,
    hardness=2,
    importance=3,
    chapter=4,
    section=0,
    subsection=2,
    page=30,
    tags=["کشورها", "بازیل"]
)
countries_questions.append(question39)

# سوال 40
question40 = Question(
    "کدام کشور به عنوان 'کشور کلاه‌ها' شناخته می‌شود و تولید کلاه‌های مختلف معروف است؟",
    ["ایتالیا", "فرانسه", "پرو", "کره جنوبی"],
    correct_option_id=1,
    hardness=2,
    importance=3,
    chapter=4,
    section=1,
    subsection=1,
    page=33,
    tags=["کشورها", "فرانسه"]
)
countries_questions.append(question40)


# لیست سوالات با موضوع تولید لباس
clothing_questions = []

# سوال 41
question41 = Question(
    "چه نامی به فرآیند تولید لباس از مواد اولیه چون پارچه و پوشاک داده می‌شود؟",
    ["بافت", "دوخت", "ژاکار", "بخیه"],
    correct_option_id=1,
    hardness=3,
    importance=4,
    chapter=5,
    section=0,
    subsection=1,
    page=10,
    tags=["لباس تولید کردن", "فرآیند تولید لباس"]
)
clothing_questions.append(question41)

# سوال 42
question42 = Question(
    "کدام ماده اولیه معمولاً به عنوان پایه برای تولید لباس‌های نخی استفاده می‌شود؟",
    ["پنبه", "پلی‌استر", "شلتون", "لینن"],
    correct_option_id=0,
    hardness=3,
    importance=4,
    chapter=5,
    section=1,
    subsection=0,
    page=12,
    tags=["لباس تولید کردن", "پنبه"]
)
clothing_questions.append(question42)

# سوال 43
question43 = Question(
    "کدام فرآیند تولید لباس به معنای برش و دوخت قطعات پارچه به یکدیگر است؟",
    ["بافت", "رنگ‌آمیزی", "تراش و دوخت", "آبکاری"],
    correct_option_id=2,
    hardness=3,
    importance=4,
    chapter=5,
    section=0,
    subsection=2,
    page=15,
    tags=["لباس تولید کردن", "دوخت"]
)
clothing_questions.append(question43)

# سوال 44
question44 = Question(
    "کدام پرده میانی در فرآیند تولید لباس برای تقویت و پایداری بیشتر پارچه استفاده می‌شود؟",
    ["پرده زیرکمری", "پرده میانی", "پرده زیربغلی", "پرده اصلی"],
    correct_option_id=1,
    hardness=3,
    importance=4,
    chapter=5,
    section=1,
    subsection=1,
    page=18,
    tags=["لباس تولید کردن", "پرده میانی"]
)
clothing_questions.append(question44)

# سوال 45
question45 = Question(
    "کدام ماشین یا ابزار در فرآیند تولید لباس برای اتصال دو قطعه پارچه با هم استفاده می‌شود؟",
    ["ماشین دوخت", "ماشین بافت", "ماشین برش", "ماشین رنگ‌آمیزی"],
    correct_option_id=0,
    hardness=3,
    importance=4,
    chapter=5,
    section=0,
    subsection=2,
    page=20,
    tags=["لباس تولید کردن", "ماشین دوخت"]
)
clothing_questions.append(question45)

# سوال 46
question46 = Question(
    "کدام نوع الیاف پلیمری برای تولید لباس‌های بدون چروک به کار می‌رود؟",
    ["پلی‌استر", "پنبه", "نایلون", "لینن"],
    correct_option_id=0,
    hardness=3,
    importance=4,
    chapter=5,
    section=1,
    subsection=0,
    page=22,
    tags=["لباس تولید کردن", "پلی‌استر"]
)
clothing_questions.append(question46)

# سوال 47
question47 = Question(
    "کدام پارچه از مواد طبیعی مانند پنبه تولید می‌شود و به عنوان پارچه معمولی استفاده می‌شود؟",
    ["ساتن", "لینن", "تافته", "شلتون"],
    correct_option_id=1,
    hardness=3,
    importance=4,
    chapter=5,
    section=0,
    subsection=1,
    page=25,
    tags=["لباس تولید کردن", "لینن"]
)
clothing_questions.append(question47)

# سوال 48
question48 = Question(
    "چه نامی به فرآیند افزودن رنگ به پارچه‌ها در تولید لباس می‌دهند؟",
    ["رنگ آمیزی", "پارچه‌پاشی", "رنگ تراشی", "رنگ میکسی"],
    correct_option_id=0,
    hardness=3,
    importance=4,
    chapter=5,
    section=1,
    subsection=2,
    page=28,
    tags=["لباس تولید کردن", "رنگ آمیزی"]
)
clothing_questions.append(question48)

# سوال 49
question49 = Question(
    "کدام جزء اصلی در تولید لباس‌های جین استفاده می‌شود و معمولاً با طراحی‌های جین معروف است؟",
    ["سیکس‌پنس", "زیپ", "جیب", "چرم"],
    correct_option_id=0,
    hardness=3,
    importance=4,
    chapter=5,
    section=0,
    subsection=2,
    page=30,
    tags=["لباس تولید کردن", "لباس جین"]
)
clothing_questions.append(question49)

# سوال 50
question50 = Question(
    "کدام فرآیند تولید لباس به معنای افزودن پتروشیمیکال‌ها به پارچه‌ها به منظور افزایش کیفیت و عمر مفید پارچه است؟",
    ["شستشو", "پردازش نهایی", "پردازش شیمیایی", "دوخت"],
    correct_option_id=2,
    hardness=3,
    importance=4,
    chapter=5,
    section=1,
    subsection=1,
    page=33,
    tags=["لباس تولید کردن", "پردازش شیمیایی"]
)
clothing_questions.append(question50)

# لیست سوالات با موضوع ورزش
sports_questions = []

# سوال 51
question51 = Question(
    "ورزش فوتبال با چند نفر در هر تیم انجام می‌شود؟",
    ["10 نفر", "11 نفر", "9 نفر", "8 نفر"],
    correct_option_id=1,
    hardness=3,
    importance=4,
    chapter=6,
    section=0,
    subsection=1,
    page=10,
    tags=["ورزش", "فوتبال"]
)
sports_questions.append(question51)

# سوال 52
question52 = Question(
    "چه کشوری به عنوان مکان تولد بازی‌های المپیک در سال 2020 انتخاب شد؟",
    ["آمریکا", "ژاپن", "فرانسه", "آلمان"],
    correct_option_id=1,
    hardness=3,
    importance=4,
    chapter=6,
    section=1,
    subsection=0,
    page=12,
    tags=["ورزش", "بازی‌های المپیک"]
)
sports_questions.append(question52)

# سوال 53
question53 = Question(
    "کدام مسابقه ورزشی در آب انجام می‌شود و شامل انجام موزیک و حرکات هنری است؟",
    ["شنا", "آب‌نشانکری", "قایق‌رانی", "پارکور آبی"],
    correct_option_id=1,
    hardness=3,
    importance=4,
    chapter=6,
    section=0,
    subsection=2,
    page=15,
    tags=["ورزش", "آب‌نشانکری"]
)
sports_questions.append(question53)

# سوال 54
question54 = Question(
    "کدام تنیس با چه تعداد نفر در هر تیم انجام می‌شود؟",
    ["تنیس رومی", "تنیس میز", "تنیس والیبال", "تنیس پیاده"],
    correct_option_id=0,
    hardness=3,
    importance=4,
    chapter=6,
    section=1,
    subsection=1,
    page=18,
    tags=["ورزش", "تنیس رومی"]
)
sports_questions.append(question54)

# سوال 55
question55 = Question(
    "در چه ورزشی از تیمی که توپ را به طرف تیم حریف می‌فرستد به عنوان 'تیم تهاجمی' یاد می‌شود؟",
    ["فوتبال آمریکایی", "بسکتبال", "فوتبال", "هاکی"],
    correct_option_id=2,
    hardness=3,
    importance=4,
    chapter=6,
    section=0,
    subsection=2,
    page=20,
    tags=["ورزش", "فوتبال"]
)
sports_questions.append(question55)

# سوال 56
question56 = Question(
    "کدام ورزش به عنوان ورزش 'شاخه‌چی' نیز شناخته می‌شود؟",
    ["گلف", "پینگ پنگ", "اتاق بازی", "بسکتبال"],
    correct_option_id=0,
    hardness=3,
    importance=4,
    chapter=6,
    section=1,
    subsection=0,
    page=22,
    tags=["ورزش", "گلف"]
)
sports_questions.append(question56)

# سوال 57
question57 = Question(
    "کدام ورزشی شناخته می‌شود به عنوان 'پادل تنیس' که با یک توپ کوچک و راکت انجام می‌شود؟",
    ["تنیس میز", "بسکتبال", "پادل تنیس", "تنیس رومی"],
    correct_option_id=2,
    hardness=3,
    importance=4,
    chapter=6,
    section=0,
    subsection=1,
    page=25,
    tags=["ورزش", "پادل تنیس"]
)
sports_questions.append(question57)

# سوال 58
question58 = Question(
    "چه ورزشی به عنوان 'برزیلیایی جیگر' شناخته می‌شود و شامل حرکات رقصی است؟",
    ["بوکس", "کراته", "کاپوئیرا", "تایکواندو"],
    correct_option_id=2,
    hardness=3,
    importance=4,
    chapter=6,
    section=1,
    subsection=1,
    page=28,
    tags=["ورزش", "کاپوئیرا"]
)
sports_questions.append(question58)

# سوال 59
question59 = Question(
    "ورزشی که در آن با استفاده از دسته‌ها توپ به طرف زمین حریف می‌فرستند چه نام دارد؟",
    ["تنیس رومی", "بسکتبال", "هاکی", "پینگ پنگ"],
    correct_option_id=3,
    hardness=3,
    importance=4,
    chapter=6,
    section=0,
    subsection=2,
    page=30,
    tags=["ورزش", "پینگ پنگ"]
)
sports_questions.append(question59)

# سوال 60
question60 = Question(
    "کدام ورزش به عنوان 'ورزش شناخته شده فضا' شناخته می‌شود و در فضا انجام می‌شود؟",
    ["فوتبال فضایی", "بسکتبال فضایی", "شنا فضایی", "تنیس رومی فضایی"],
    correct_option_id=1,
    hardness=3,
    importance=4,
    chapter=6,
    section=1,
    subsection=0,
    page=33,
    tags=["ورزش", "بسکتبال فضایی"]
)
sports_questions.append(question60)


for q in animal_questions:
    q.chapter = 1
    q.section = 1

for q in fruit_questions:
    q.chapter = 1
    q.section = 2

for q in music_questions:
    q.chapter = 1
    q.section = 3

for q in countries_questions:
    q.chapter = 1
    q.section = 4

for q in clothing_questions:
    q.chapter = 1
    q.section = 5

for q in sports_questions:
    q.chapter = 1
    q.section = 5

