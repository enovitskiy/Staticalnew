from django.db import models
from django.db.models import CharField



class Common(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название раздела', help_text='название основного раздела')
    slug = models.SlugField(null=True, unique=True, blank=True, verbose_name='URL адрес', help_text='название url адреса')
    section = models.TextField(null=True, verbose_name='Название секции', help_text='название секции, необязательно')
    template_name: CharField = models.CharField(max_length=30, null=True, verbose_name='Название html', help_text='название html файла' )
    hreflogo = models.CharField(max_length=100, blank=True, verbose_name='URL картинка', help_text='URL картинка')
    title = models.CharField(max_length=300, blank=True, verbose_name='Заголовок', help_text='описание заголовка в строке браузера')
    descrtionmeta = models.TextField(max_length=300, blank=True, verbose_name='Описание страницы', help_text='описание страницы в поискаовика')
    keywordsmeta = models.TextField(max_length=300, blank=True, verbose_name='Ключевые слова', help_text='ключевые слова для поисковика')

    class Meta:
        abstract = True

class Navconstruct(Common):
    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Основное меню"

    def __str__(self):
        return self.name

class Subnavigator(Common):
    class Meta:
        verbose_name = "Подраздел"
        verbose_name_plural = "Подменю"
    subname = models.ForeignKey('Navconstruct', on_delete=models.CASCADE, related_name="sub", null=True, blank=True, verbose_name='Основное меню', help_text='привязка к основному меню')
    projname = models.ForeignKey('Footercont', on_delete=models.CASCADE, related_name="project", null=True, blank=True, verbose_name='Тип подвала', help_text='привязка к подвалу')
    def __str__(self):
        return self.name

class Subsubnav(Common):
    class Meta:
        verbose_name = "Подраздел подраздела"
        verbose_name_plural = "Подменю подменю"
    subname = models.ForeignKey('Subnavigator', on_delete=models.CASCADE, related_name="sub", null=True, verbose_name='Подменю', help_text='привязка к подменю')
    def __str__(self):
        return self.name

class Social(models.Model):
    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети и данные заголовка"
    title = models.CharField(max_length=30, verbose_name='Название', help_text='название подменю')
    href = models.URLField(null=True, verbose_name='URL компании', help_text='URL сети или сайта')
    classname = models.CharField(max_length=30, verbose_name='стиль иконки', help_text='стиль выбирается из https://fontawesome.ru/all-icons/ ')
    text = models.TextField(blank=True, verbose_name='Описание', help_text='Описание компании или сети')
    social = models.BooleanField( verbose_name='Соц сети', help_text='Если соц сеть,то ставим галочку')
    def __str__(self):
        return self.title

class Footercont(models.Model):
    class Meta:
        verbose_name = "Тип подвала"
        verbose_name_plural = "Тип подвала"

    title = models.CharField(max_length=30, verbose_name='Наименование', help_text='название типа подвала')
    classname = models.CharField(max_length=100, verbose_name='Стиль', help_text='указать стиль')
    classdiv= models.CharField(max_length=100, blank=True, verbose_name='Стиль', help_text='Стиль контейнера')

    def __str__(self):
        return self.title

class Footer(models.Model):
    class Meta:
        verbose_name = "Данные подвала"
        verbose_name_plural = "Данные подвала"

    type = models.ForeignKey('Footercont', on_delete=models.CASCADE, related_name="type", null=True, verbose_name='Тип подвала', help_text='выбрать тип подвала')
    title = models.CharField(max_length=30, verbose_name='Наименование', help_text='название раздела подвала')
    hreflogo = models.CharField(max_length=100, blank=True, verbose_name='URL лого', help_text='URL лого')
    classul = models.CharField(max_length=100, blank=True, verbose_name='Стиль', help_text='указать стиль')
    classdir = models.CharField(max_length=100, blank=True, verbose_name='Стиль', help_text='Стиль контейнера')

    def __str__(self):
        return self.title

class Text(models.Model):
    class Meta:
        verbose_name = "Информация подвала"
        verbose_name_plural = "Информация подвала"
    subname = models.ForeignKey('Footer', on_delete=models.CASCADE, related_name="textsub", null=True, verbose_name='Данные подвала', help_text='привязка к данным подвала')
    title = models.CharField(max_length=30, blank=True, verbose_name='Наименование', help_text='название раздела подвала')
    footertext = models.TextField(blank=True, verbose_name='Текст', help_text='описание подвала')
    def __str__(self):
        return self.title

class Page(models.Model):
    class Meta:
        verbose_name = "Информация страницы"
        verbose_name_plural = "Информация страницы"
    subname = models.ForeignKey('Navconstruct', on_delete=models.CASCADE, related_name="text", null=True,verbose_name='Основное меню', help_text='привязка к основному меню')
    projname = models.ForeignKey('Subnavigator', on_delete=models.CASCADE, related_name="subtext", null=True, blank=True, verbose_name='Подменю', help_text='привязка к подменю')
    title = models.CharField(max_length=30, blank=True,verbose_name='Заголовок', help_text='название заголовка')
    textup = models.TextField(blank=True,verbose_name='Текст', help_text='текст')
    quote = models.TextField(blank=True,verbose_name='Текст1', help_text='текст')
    textdown = models.TextField(blank=True,verbose_name='Текст2', help_text='текст')
    def __str__(self):
        return self.title

class Slider(models.Model):
    class Meta:
        verbose_name = "Картинки слайдера страницы"
        verbose_name_plural = "Картинки слайдера страницы"
    projname = models.ForeignKey('Subnavigator', on_delete=models.CASCADE, related_name="subslider", null=True, blank=True, verbose_name='Подменю', help_text='привязка к подменю')
    name = models.CharField(max_length=30 ,verbose_name='Имя картинки', help_text='имя картинки на слайдере')
    hreflogo = models.CharField(max_length=100, blank=True ,verbose_name='URL картинки', help_text='URL картинки')

    def __str__(self):
        return self.name



class Projects(models.Model):
    class Meta:
        verbose_name = "Типы примеров на странице"
        verbose_name_plural = "Типы примеров на странице"
    subname = models.ForeignKey('Navconstruct', on_delete=models.CASCADE, related_name="proj", null=True, verbose_name='Основное меню', help_text='привязка к основному меню')
    projname = models.ForeignKey('Subnavigator', on_delete=models.CASCADE, related_name="subproj", null=True, blank=True, verbose_name='Подменю', help_text='привязка к подменю')
    title = models.CharField(max_length=100, blank=True, verbose_name='Наименование', help_text='название тимпа примеров')
    href = models.CharField(max_length=100, blank=True, verbose_name='Ссылка', help_text='ссылка на страницу, если на той же, по умолчанию #')
    dafilter = models.CharField(max_length=100, blank=True, verbose_name='Обозначени типа', help_text='обозначается через ., пример .type1')

    def __str__(self):
        return self.title

class Example(models.Model):
    class Meta:
        verbose_name = "Пример"
        verbose_name_plural = "Примеры"
    example = models.ForeignKey('Projects', on_delete=models.CASCADE, related_name="example", null=True, verbose_name='Тип примеров', help_text='привязка к типу примера')
    title = models.CharField(max_length=100, blank=True, verbose_name='Тип примеров', help_text='обозначается без ., пример type1')
    href = models.CharField(max_length=200, blank=True, verbose_name='URL картинки', help_text='URL картинки в приблежениии')
    src = models.CharField(max_length=200, blank=True, verbose_name='URL картинки', help_text='URL картинки')
    slug = models.SlugField(null=True, unique=True, blank=True, verbose_name='URL адрес', help_text='название url адреса')
    alt = models.CharField(max_length=150, blank=True, verbose_name='Alt картинка', help_text='описание картинки')
    projectname = models.CharField(max_length=200, blank=True, verbose_name='Название проекта', help_text='название проекта')
    description = models.TextField(max_length=300, blank=True, verbose_name='Описание страницы', help_text='описание страницы в поискаовика')
    keywords = models.TextField(max_length=300, blank=True, verbose_name='Ключевые слова', help_text='ключевые слова для поисковика')
    def __str__(self):
        return self.projectname


class Pictures(models.Model):
    class Meta:
        verbose_name = "Фото примера"
        verbose_name_plural = "Фото примера"
    name = models.ForeignKey('Example', on_delete=models.CASCADE, related_name="pictures", null=True, verbose_name='Пример', help_text='привязка к примеру')
    href1 = models.CharField(max_length=200, blank=True, verbose_name='URL фото', help_text='URL фото примера')
    alt = models.CharField(max_length=150, blank=True, verbose_name='Alt картинка', help_text='описание картинки')
    def __str__(self):
        return self.name.projectname

class Short(models.Model):
    class Meta:
        verbose_name = "Краткая информация примера"
        verbose_name_plural = "Краткая информация примера"
    name = models.ForeignKey('Example', on_delete=models.CASCADE, related_name="short", null=True, verbose_name='Пример', help_text='привязка к примеру')
    predescription = models.TextField(blank=True, verbose_name='Краткое описание', help_text='Краткое описание')
    namecategory = models.CharField(max_length=30, verbose_name='Название категории', help_text='Название категории')
    caregory = models.CharField(max_length=100, verbose_name='Категория', help_text='Категория')
    namefokus = models.CharField(max_length=30, verbose_name='Название фокус', help_text='Название фокус')
    fokus = models.CharField(max_length=100, verbose_name='Фокус', help_text='Фокус')
    namesite = models.CharField(max_length=30, verbose_name='Название адреса', help_text='Название адреса')
    site = models.CharField(max_length=100, verbose_name='Адрес проекта', help_text='Адрес проекта')
    nameduration = models.CharField(max_length=30, verbose_name='Название сроков', help_text='Название сроков')
    duration = models.CharField(max_length=100, verbose_name='Сроки выполнения', help_text='Сроки выполнения')
    def __str__(self):
        return self.name.projectname

class CommonInfo(models.Model):
    urlvideo = models.URLField(max_length=100, blank=True, verbose_name='URL видео с ютуба', help_text='URL видео с ютуба')
    blockquote = models.TextField(blank=True,verbose_name='Текст', help_text='текст')
    paragraph = models.TextField(blank=True,verbose_name='Текст1', help_text='текст')
    titlenext = models.CharField(max_length=30, blank=True,verbose_name='Заголовок', help_text='заголовок')
    textnext = models.TextField(blank=True,verbose_name='Текст2', help_text='текст')
    titlecoloumn = models.CharField(max_length=100, blank=True,verbose_name='Заголовок1', help_text='заголовок')
    titleparagraph = models.CharField(max_length=100, blank=True,verbose_name='Заголовок2', help_text='заголовок')

    class Meta:
        abstract = True

class Pagenext(CommonInfo):
    class Meta:
        verbose_name = "Иинформация страницы"
        verbose_name_plural = "Иинформация страницы"
    subname = models.ForeignKey('Navconstruct', on_delete=models.CASCADE, related_name="next", null=True, verbose_name='Основное меню', help_text='привязка к основному меню')
    projname = models.ForeignKey('Subnavigator', on_delete=models.CASCADE, related_name="subnext", null=True, blank=True, verbose_name='Подменю', help_text='привязка к подменю')
    title = models.CharField(max_length=100, blank=True,verbose_name='Заголовок3', help_text='заголовок')
    urljpg = models.CharField(max_length=100, blank=True, verbose_name='URL фото', help_text='URL фото')
    alt = models.CharField(max_length=150, blank=True, verbose_name='Alt картинка', help_text='описание картинки')
    textup = models.TextField(blank=True,verbose_name='Текст3', help_text='текст')
    quote = models.TextField(blank=True,verbose_name='Текст4', help_text='текст')
    textdown = models.TextField(blank=True,verbose_name='Текст5', help_text='текст')
    def __str__(self):
        return self.title

class Pageproject(CommonInfo):
    class Meta:
        verbose_name = "Иинформация страницы"
        verbose_name_plural = "Иинформация страницы"
    name = models.ForeignKey('Example', on_delete=models.CASCADE, related_name="pageproject", null=True, verbose_name='Пример', help_text='привязка к примеру')
    def __str__(self):
        return self.name.projectname

class Faqblock (models.Model):
    class Meta:
        verbose_name = "Всплвающие списки на старнице"
        verbose_name_plural = "Всплвающие списки на старнице"
    name = models.CharField(max_length=100, verbose_name='Название списка', help_text='название списка и страница')
    def __str__(self):
        return self.name

class Faq (models.Model):
    class Meta:
        verbose_name = "Наполнение списка"
        verbose_name_plural = "Наполнение списка"
    name = models.ForeignKey('Faqblock',on_delete=models.CASCADE, related_name="faq", null=True, verbose_name='Основное меню', help_text='привязка к основному меню')
    question = models.CharField(max_length=200, verbose_name='Имя списка', help_text='имя списка')
    answer = models.TextField(blank=True, verbose_name='Ответ списка', help_text='ответ списка')
    def __str__(self):
        return self.question

class Commoncontact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя списка', help_text='имя списка')
    answer = models.TextField(blank=True, verbose_name='Ответ списка', help_text='ответ списка')
    class Meta:
        abstract = True

class Contact (Commoncontact):
    class Meta:
        verbose_name = "Контактная информация для контакты"
        verbose_name_plural = "Контактная информация для контакты"
    icon = models.CharField(max_length=50, blank=True, verbose_name='стиль иконки', help_text='стиль выбирается из https://fontawesome.ru/all-icons/ ')
    def __str__(self):
        return self.name

class Etapy(Commoncontact):
    class Meta:
        verbose_name = "Этапы работ на главной странице"
        verbose_name_plural = "Этапы работ на главной странице"
    namenext = models.CharField(max_length=50, blank=True, verbose_name='Имя списка', help_text='имя списка')
    answernext = models.TextField(blank=True, verbose_name='Ответ списка', help_text='ответ списка')
    href = models.CharField(max_length=200, blank=True, verbose_name='URL фото', help_text='URL фото примера')
    href1 = models.CharField(max_length=200, blank=True, verbose_name='URL фото1', help_text='URL фото примера')
    alt = models.CharField(max_length=150, blank=True, verbose_name='Alt картинка', help_text='описание картинки')
    alt1 = models.CharField(max_length=150, blank=True, verbose_name='Alt картинка', help_text='описание картинки')
    def __str__(self):
        return self.name

class Contdecr (models.Model):
    class Meta:
        verbose_name = "Загловки на странице контакты"
        verbose_name_plural = "Загловки на странице контакты"
    title1 = models.CharField(max_length=100, blank=True, verbose_name='Загловок на стр контакты', help_text='Загловок на стр контакты')
    title2 = models.CharField(max_length=100, blank=True, verbose_name='Загловок на стр контакты', help_text='Загловок на стр контакты')
    title3 = models.CharField(max_length=100, blank=True, verbose_name='Загловок на стр контакты', help_text='Загловок на стр контакты')

    def __str__(self):
        return self.title1

class Pictslider(models.Model):
    class Meta:
        verbose_name = "Слайдер на главной странице"
        verbose_name_plural = "Слайдер на главной странице"
    hreflogo = models.CharField(max_length=100, verbose_name='URL фото', help_text='URL фото')

    def __str__(self):
        return self.hreflogo

class Textslider(models.Model):
    class Meta:
        verbose_name = "Слайдер текст на главной странице"
        verbose_name_plural = "Слайдер текст на главной странице"
    picture = models.ForeignKey('Pictslider',on_delete=models.CASCADE, related_name="picture", null=True, verbose_name='Слайдер главной страницы', help_text='привязка к слайдеру главной страницы')
    textblock =models.TextField(blank=True,verbose_name='Текст слайедра', help_text='текст')
    textbldown = models.TextField(blank=True,verbose_name='Текст слайедра', help_text='текст')
    clas = models.CharField(max_length=20, blank=True,verbose_name='Класс текста слайдера', help_text='текст')


    def __str__(self):
        return self.picture.hreflogo

class Mpage(models.Model):
    class Meta:
        verbose_name = "Информации для главной"
        verbose_name_plural = "Информации для главной"
    name = models.CharField(max_length=30, blank=True, verbose_name='Заголовок', help_text='заголовок')
    title = models.CharField(max_length=100, blank=True, verbose_name='Заголовок1', help_text='заголовок')
    textblock =models.TextField(blank=True, verbose_name='Текст', help_text='текст')
    title1 = models.CharField(max_length=100, blank=True, verbose_name='Заголовок2', help_text='заголовок')
    textblock1 = models.TextField(blank=True, verbose_name='Текст1', help_text='текст')

    def __str__(self):
        return self.title

class Values (Commoncontact):
    class Meta:
        verbose_name = "Список информации для главной"
        verbose_name_plural = "Список информации для главной"
    icon = models.CharField(max_length=50, blank=True, verbose_name='стиль иконки', help_text='стиль выбирается из https://fontawesome.ru/all-icons/ ')
    def __str__(self):
        return self.name


# Create your models here.
