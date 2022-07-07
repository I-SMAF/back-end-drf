# back-end-drf

- [GIT(git ignore, main comands, rules)](#gitgit-ignore-main-comands-rules)
- [Virtual Environment(virtual variables)](#virtual-environmentvirtual-variables)
- [Class (remember the python)](#class-remember-the-python)
- [ORM (sqllite)](#orm-sqllite)
- [Internet](#internet)
- [OS & General Knowledge](#os--general-knowledge)
- [APIs](#apis)
- [Django Rest Framework](#django-rest-framework)
- [Models Django](#models-django)
- [Manager Django](#manager-django)
- [Model Serializers](#model-serializers)
- [View Django(NO INFO WHILE)](#view-django)
- [APIView(NO INFO WHILE)](#apiview)
- [URL Manager](#url-manager)
- [Routers](#routers )

# Learning...

## GIT(git ignore, main comands, rules)

__Git__ — система управления версиями с распределенной архитектурой. Таким образом, каждая рабочая копия кода сама по
себе является репозиторием, что позволяет разработчикам хранить всю историю изменений проекта в полном объёме. Данная
система является деревом с возможностью ветвления (удобство данного процесса является отличительной чертой Git). Для
работы с Git существуют следующие команды:

*git add*

Команда `git add` добавляет содержимое рабочего каталога в индекс (staging area) для последующего коммита (снимка
текущего состояния изменений). По умолчанию `git commit` использует лишь этот индекс, так что вы можете
использовать `git add` для сборки слепка вашего следующего коммита.

*git status*

Команда `git status` показывает состояния файлов в рабочем каталоге и индексе: какие файлы изменены, но не добавлены в
индекс; какие ожидают коммита в индексе. Вдобавок к этому выводятся подсказки о том, как изменить состояние файлов.

*git diff*

Команда `git diff` используется для вычисления разницы между любыми двумя Git деревьями. Это может быть разница между
вашей рабочей копией и индексом (собственно `git diff`), разница между индексом и последним
коммитом (`git diff --staged`), или между любыми двумя коммитами (`git diff master branchB`).

*git commit*

Команда `git commit` берёт все данные, добавленные в индекс с помощью `git add`, и сохраняет их слепок во внутренней
базе данных, а затем сдвигает указатель текущей ветки на этот слепок.

*git rm*

Команда `git rm` используется в Git для удаления файлов из индекса и рабочей копии. Она похожа на `git add` с тем лишь
исключением, что она удаляет, а не добавляет файлы для следующего коммита.

*git mv*

Команда `git mv` — это всего лишь удобный способ переместить файл, а затем выполнить `git add` для нового файла
и `git rm` для старого.

*git reset*

Команда `git reset`, как можно догадаться из названия, используется в основном для отмены изменений. Она изменяет
указатель *__HEAD__* (дерево коммитов) и, опционально, состояние индекса. Также эта команда может изменить файлы в
рабочем каталоге при использовании параметра __--hard__, что может привести к потере наработок при неправильном
использовании, так что убедитесь в серьёзности своих намерений прежде чем использовать его.

*git clean*

Команда `git clean` используется для удаления мусора из рабочего каталога. Это могут быть результаты сборки проекта или
файлы конфликтов слияний.

*git branch*

Команда `git branch` — это своего рода "менеджер веток". Она умеет перечислять ваши ветки, создавать новые, удалять и
переименовывать их.

*git stash*

Команда `git stash` используется для временного сохранения всех незафиксированных изменений с целью очистки рабочего
каталога без необходимости фиксировать незавершённую работу в текущей ветке.

*git fetch*

Команда `git fetch` связывается с удалённым репозиторием и забирает из него все изменения, которых у вас пока нет и
сохраняет их локально.

*git merge*

Команда `git merge` используется для слияния одной или нескольких веток в текущую. Затем она устанавливает указатель
текущей ветки на результирующий коммит.

*git pull*

Команда `git pull` работает как комбинация команд `git fetch` и `git merge`, т. е. Git вначале забирает изменения из
указанного удалённого репозитория, а затем пытается слить их с текущей веткой.

*git push*

Команда `git push` используется для установления связи с удалённым репозиторием, вычисления локальных изменений
отсутствующих в нём, и собственно их передачи в вышеупомянутый репозиторий. Этой команде нужно право на запись в
репозиторий, поэтому она использует аутентификацию.

## Virtual Environment(virtual variables)

__Виртуальная среда__ - это дерево каталогов, которое содержит исполняемые файлы Python и другие файлы, указывающие на
то, что это виртуальная среда.

В виртуальной среде мы всё также можем использовать стандартные средства установки (setuptools и pip).

Модуль `sys` обеспечивает доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором Python.

Во время работы с виртуальной средой, чтобы получить необходимые данные модуля `sys`, мы используем:
`sys.prefix` - папка установки интерпретатора Python.
`sys.exec_prefix` - каталог установки Python. Чтобы сделать аналогичные действия, но для корневого Python, за счёт
которого работает виртуальная среда, используем:
`sys.base_prefix` и `sys.base_exec_prefix`. Если виртуальная среда не активна, то `sys.prefix` совпадает
с `sys.base_prefix`, а sys.exec_prefix совпадает с `sys.base_exec_prefix`.

В поставку Python входит `distutils`, пакет, отвечающий за создание дистрибутивов — архивов кода, которые могут быть
распакованы в целевом окружении и установлены так, чтобы интерпретатор Python "увидел" распакованный код. Когда
виртуальная среда активна, любые параметры, изменяющие путь установки, будут игнорироваться во всех файлах конфигурации
distutils, чтобы предотвратить непреднамеренную установку проектов за пределами виртуальной среды.

При работе в командной оболочке пользователи могут сделать виртуальную среду активной, запустив сценарий активации в
каталоге исполняемых файлов виртуальной среды (точное имя файла и команда для использования файла зависят от оболочки),
который добавляет каталог виртуальной среды для исполняемых файлов к переменной окружения PATH для запущенной оболочки.
В других обстоятельствах не должно быть необходимости активировать виртуальную среду; скрипты, установленные в
виртуальных средах, имеют строку “shebang”, которая указывает на интерпретатор Python виртуальной среды. Это означает,
что скрипт будет выполняться с этим интерпретатором независимо от значения PATH. В Windows обработка строк “shebang”
поддерживается, если у вас установлена программа запуска Python для Windows (она была добавлена в Python в версии 3.3 -
подробнее см. PEP 397). Таким образом, двойной щелчок по установленному скрипту в окне проводника Windows должен
запустить скрипт с правильным интерпретатором без необходимости какой-либо ссылки на его виртуальную среду в PATH.

|Platform|Shell|Command to activate virtual environment|
|--------|-----|---------------------------------------|
|POSIX|bash/zsh|source <venv>/bin/activate|
||fish|source <venv>/bin/activate.fish|
||csh/tcsh|source <venv>/bin/activate.csh|
||PowerShell Core|<venv>/bin/Activate.ps1|
|Windows|cmd.exe|<venv>\Scripts\activate.bat|
||PowerShell|<venv>\Scripts\Activate.ps1|

## Class (remember the python)

__Класс__ — тип, описывающий устройство объектов. Объект — это экземпляр класса. Класс можно сравнить с чертежом, по
которому создаются объекты. Python соответствует принципам объектно-ориентированного программирования. В python всё
является объектами - и строки, и списки, и словари, и всё остальное.

__Пример простейшего класса, который ничего не делает__

```
class A:
    pass
    
a = A()
b = A()
a.arg = 1  # у экземпляра a появился атрибут arg, равный 1
b.arg = 2  # а у экземпляра b - атрибут arg, равный 2
print(a.arg)
 >>1
print(b.arg)
 >>2
c = A()
print(c.arg)  # а у этого экземпляра нет arg
 >>SomeException
```

__Классу возможно задать собственные методы:__

```
class A:
    def g(self): # self - обязательный аргумент, содержащий в себе экземпляр
                 # класса, передающийся при вызове метода,
                 # поэтому этот аргумент должен присутствовать
                 # во всех методах класса.
        return 'hello world'

a = A()
a.g()
 >>'hello world'
```

__Наследование__ позволяет выделить общее для нескольких классов поведение и вынести его в отдельную сущность.
Наследование позволяет получить новый класс, немного отличающийся от старого, при этом нам не нужно иметь доступ к коду
исходного класса.

```
 # Класс 'A', который мы уже создали.
    class A:
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1

# 'B' - новый класс. Наследник 'A'.
class B(A):  # в скобках указан класс-предок
    def dec(self):
        pass
```

## ORM (sqllite)

__Для подключения к SQLite нужно выполнить следующие шаги:__

- Использовать метод `connect()` из модуля *__sqlite3__* и передать в качестве аргумента название базы данных.
- Создать объект cursor с помощью объекта соединения, который вернул прошлый метод для выполнения SQLite-запросов из
  Python.
- Закрыть объект cursor после завершения работы.
- Перехватить исключение базы данных, если в процессе подключения произошла ошибка.

```
import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    sqlite_select_query = "select sqlite_version();"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print("Версия базы данных SQLite: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
```

__Шаги для создания таблицы в SQLite с помощью Python:__

- Соединиться с базой данных с помощью `sqlite3.connect().` Речь об этом шла в первом разделе.
- Подготовить запрос создания таблицы.
- Выполнить запрос с помощью `cursor.execute(query)`.
- Закрыть соединение с базой и объектом `cursor`.

```
import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    sqlite_create_table_query = '''CREATE TABLE sqlitedb_developers (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                email text NOT NULL UNIQUE,
                                joining_date datetime,
                                salary REAL NOT NULL);'''

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблица SQLite создана")

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
```

__Получение и вывод данных__

```
for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)
```

## Internet

- __Интернет:__ это глобальная сеть компьютеров, соединенных друг с другом, которые взаимодействуют с помощью
  стандартизированного набора протоколов
- __HTTP:__ это протокол связи прикладного уровня на основе __TCP/IP__, который стандартизирует взаимодействие клиента и
  сервера друг с другом. Он определяет, как контент запрашивается и передается через Интернет.
- __Доменное имя:__ это уникальный, легко запоминающийся адрес, используемый для доступа к веб-сайтам, таким
  как `google.com`, и `facebook.com`. Пользователи могут подключаться к веб-сайтам, используя доменные имена, благодаря
  системе __DNS__.
- __Система доменных имен (DNS):__ это телефонная книга Интернета. Люди получают доступ к информации в Интернете через
  доменные имена, такие как nytimes.com или espn.com . Веб-браузеры взаимодействуют через адреса Интернет-протокола
  (__IP__). __DNS__ преобразует доменные имена в __IP-адреса__, чтобы браузеры могли загружать интернет-ресурсы.
- __Веб-хостинг:__ это онлайн-сервис, который позволяет вам публиковать файлы вашего веб-сайта в Интернете. Итак, любой,
  у кого есть доступ к Интернету, имеет доступ к вашему веб-сайту.

## OS & General Knowledge

- __Операционная система:__ это программа, которая управляет ресурсами компьютера, особенно распределением этих ресурсов
  между другими программами. Типичные ресурсы включают центральный процессор (__CPU__), память компьютера, файловое
  хранилище, устройства ввода/вывода (I/O) и сетевые подключения.
- __Терминал:__ позволяет нам выполнять и автоматизировать задачи на компьютере без использования графического
  пользовательского интерфейса.
- Управление процессами включает в себя различные задачи, такие как создание, планирование, завершение процессов и
  взаимоблокировка. __Процесс:__ это программа, находящаяся в процессе выполнения, которая является важной частью
  современных операционных систем. Операционная система должна выделять ресурсы, позволяющие процессам совместно
  использовать и обмениваться информацией. Он также защищает ресурсы каждого процесса от других методов и обеспечивает
  синхронизацию между процессами.
- __Поток:__ это наименьшая единица обработки, которая может быть выполнена в операционной системе. В большинстве
  современных операционных систем поток существует внутри процесса, то есть один процесс может содержать несколько
  потоков. Параллелизм относится к одновременному выполнению нескольких потоков. Это происходит в операционной системе,
  когда несколько потоков процесса выполняются одновременно. Эти потоки могут взаимодействовать друг с другом через
  общую память или передачу сообщений. Параллелизм приводит к совместному использованию ресурсов, что вызывает такие
  проблемы, как взаимоблокировки и нехватка ресурсов. Это помогает с такими методами, как координация процессов,
  распределение памяти и расписание выполнения, чтобы максимизировать пропускную способность.
- __Основные команды Терминала:__
  Работа в терминале является обычной практикой для любого серверного разработчика, и существует множество команд и
  утилит, которые могут помочь вам более эффективно решать ваши задачи. Лучший способ выучить эти команды -
  попрактиковаться в них на вашей собственной машине / среде. В частности, они связаны с командами / утилитами Linux,
  которые являются наиболее распространенными на рынке. Чтобы понять эти команды, прочтите страницы руководства,
  используя `man command`, например `man grep`, `man awk` и т.д. После достаточного ознакомления и практики с этими
  командами вам станет легче использовать их на практике
  [`linux-commands`](https://www.tutorialworks.com/linux-commands/)
- Термин __"Память"__ может быть определен как набор данных в определенном формате. Он используется для хранения
  инструкций и обработки данных. Память содержит большой массив или группу слов или байтов, каждый из которых имеет свое
  собственное местоположение. Основным мотивом компьютерной системы является выполнение программ. Эти программы вместе с
  информацией, к которой они обращаются, должны находиться в основной памяти во время выполнения. Центральный процессор
  извлекает инструкции из памяти в соответствии со значением счетчика программ. Для достижения определенной степени
  мультипрограммирования и правильного использования памяти важно управление памятью. Существует несколько методов
  управления памятью, отражающих различные подходы, и эффективность каждого алгоритма зависит от ситуации.

## APIs

- __Объектная нотация JSON или JavaScript:__ это схема кодирования, разработанная для устранения необходимости в
  специальном коде для каждого приложения для взаимодействия с серверами, которые взаимодействуют определенным образом.
  Модуль `API JSON` предоставляет реализацию для хранилищ данных и структур данных, таких как типы сущностей, пакеты и
  поля.
- __REST:__, или Передача репрезентативного состояния, - это архитектурный стиль для обеспечения стандартов между
  компьютерными системами в Интернете, облегчающий взаимодействие систем друг с другом.

## Django Rest Framework

[__Project structure__](https://github.com/I-SMAF/back-end-drf/blob/main/project_structure.md)

## Models Django

__Модель__ является единственным источником информации о ваших данных. Она содержит основные поля и поведение данных,
которые вы храните. Как правило, каждая модель отображается в одну таблицу базы данных. сновы:

Каждая модель представляет собой класс Python, который является подклассом `django.db.models.Model`. Каждый атрибут
модели представляет поле базы данных. При этом Django предоставляет вам автоматически сгенерированный API доступа к базе
данных; смотрите Создание запросов.

__Быстрый пример__
Этот пример модели определяет `Person`, который имеет `first_name` и `last_name`:

```
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
first_name и last_name являются fields модели. Каждое поле указывается как атрибут класса, и каждый атрибут отображается в столбец базы данных.
```

Приведенная выше модель `Person` создаст таблицу базы данных следующим образом:

```
CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
```

Некоторые технические примечания:

Имя таблицы, `myapp_person`, автоматически выводится из некоторых метаданных модели, но может быть переопределено.
Смотрите Названия таблиц для более подробной информации. Поле id добавляется автоматически, но это поведение может быть
переопределено. Смотрите Автоматические поля первичного ключа.
`SQL CREATE TABLE` в этом примере отформатирован с использованием синтаксиса `PostgreSQL`, но стоит отметить,
что `Django` использует SQL с учетом серверной части базы данных, указанной в вашем файле settings.

__Использование моделей__
После того, как вы определили свои модели, вам нужно сообщить Django, что вы собираетесь использовать эти модели.
Сделайте это, отредактировав файл настроек и изменив параметр `INSTALLED_APPS`, чтобы добавить имя модуля, который
содержит ваш `models.py`.

Например, если модели для вашего приложения находятся в модуле `myapp.models` (структура пакета, которая создается для
приложения сценарием `manage.py startapp`), `INSTALLED_APPS` следует читать частично:

```
INSTALLED_APPS = [
    #...
    'myapp',
    #...
]
```

Когда вы добавляете новые приложения в `INSTALLED_APPS`, обязательно запустите `manage.py migrate`, при необходимости
сначала сделав миграцию для них с помощью `manage.py makemigrations`.

## Manager Django

`class Manager`
`Manager` - это интерфейс, через который для моделей Django предоставляются операции запросов к базе данных. По крайней
мере, один `Manager` существует для каждой модели в приложении Django.

Принцип работы классов `Manager` задокументирован в Создание запросов; этот документ специально касается параметров
модели, которые настраивают поведение `Manager`.

__Имена менеджеров__
По умолчанию Django добавляет `Manager` с именем `objects` в каждый класс модели Django. Однако, если вы хотите
использовать `objects` в качестве имени поля или если вы хотите использовать имя, отличное от `objects` для `Manager`,
вы можете переименовать его для каждой модели. Чтобы переименовать `Manager` для данного класса, определите атрибут
класса типа `models.Manager()` для этой модели. Например:

```
from django.db import models

class Person(models.Model):
    #...
    people = models.Manager()
```

Используя этот пример модели, `Person.objects` сгенерирует исключение `AttributeError`, а `Person.people.all()`
предоставит список всех объектов `Person`.

__Изменение начального QuerySet менеджера__
Базовый `QuerySet Manager` возвращает все объекты в системе. Например, используя эту модель:

```
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
```

…оператор `Book.objects.all()` вернет все книги в базе данных.

Вы можете переопределить базовый `QuerySet Manager’а`, переопределив метод `Manager.get_queryset()`. `get_queryset()`
должен вернуть `QuerySet` с нужными вам свойствами.

Например, в следующей модели есть два `Manager` - один возвращает все объекты, а другой возвращает только книги Роальда
Даля:

```
# First, define the Manager subclass.
class DahlBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author='Roald Dahl')

# Then hook it into the Book model explicitly.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

    objects = models.Manager() # The default manager.
    dahl_objects = DahlBookManager() # The Dahl-specific manager.
```

В этом примере модели `Book.objects.all()` вернет все книги в базе данных, а `Book.dahl_objects.all()` вернет только те,
которые написаны Роальдом Далем.

Поскольку `get_queryset()` возвращает объект `QuerySet`, вы можете использовать для него `filter()`, `exclude()` и все
другие методы `QuerySet`. Итак, все эти утверждения законны:

```
Book.dahl_objects.all()
Book.dahl_objects.filter(title='Matilda')
Book.dahl_objects.count()
```

В этом примере также отмечен еще один интересный прием: использование нескольких менеджеров в одной модели. Вы можете
прикрепить к модели столько экземпляров `Manager()`, сколько захотите. Это не повторяющийся способ определения общих
«фильтров» для ваших моделей.

Например:

```
class AuthorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role='A')

class EditorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role='E')

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=[('A', _('Author')), ('E', _('Editor'))])
    people = models.Manager()
    authors = AuthorManager()
    editors = EditorManager()
```

Этот пример позволяет вам запрашивать `Person.authors.all()`, `Person.editors.all()` и `Person.people.all()`, что дает
предсказуемые результаты.

__Менеджеры по умолчанию__
`Model._default_manager`
Если вы используете настраиваемые объекты `Manager`, обратите внимание, что первые обнаруженные Django
объекты `Manager` (в том порядке, в котором они определены в модели) имеют особый статус. Django интерпретирует первый
менеджер, определенный в классе, как менеджер по умолчанию, и некоторые части Django (включая `dumpdata`) будут
использовать этот менеджер исключительно для этой модели. В результате рекомендуется быть осторожным при выборе
диспетчера по умолчанию, чтобы избежать ситуации, когда переопределение `get_queryset()` приведет к невозможности
получить объекты, с которыми вы хотите работать.

Вы можете указать собственный менеджер по умолчанию, используя `Meta.default_manager_name`.

Если вы пишете код, который должен обрабатывать неизвестную модель, например, в стороннем приложении, реализующем общее
представление, используйте этот менеджер (или `_base_manager`) вместо того, чтобы предполагать, что модель имеет
менеджер объектов.

## Model Serializers

### Создание модели для работы

Для целей данного руководства мы начнем с создания простой модели `Snippet`, которая будет использоваться для хранения
блоков кода(Сниппетов).

```
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)
```

Так же нам необходимо сделать начальную миграцию для данной модели и синхронизировать базу данных.
`python manage.py makemigrations snippets`
`python manage.py migrate`

### Создание класса сериализатора

Первая вещь, которую нам надо сделать для нашего _API_, это создать способ сериализации и десериализации объектов
модели `Snippet` в такие формы, как, например, _JSON_. Мы можем сделать это описав сериализатор и работать с ним подобно
тому, как мы работаем с _Django_ формами. Создайте модуль `serializers.py` в пакете `snippets`.

```
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
```

Первая часть класса сериализатора определяет поля, которые будут сериализованы/десериализованы. Методы `create()`
и `update()` определяют, как работает создание и обновление объекта модели. Класс сериализатора очень похож на класс
формы в _Django_ и включает такие же проверочные механизмы на различные поля, такие как `requireq`, `max_length`
, `default`. Параметры полей так же могут управлять тем, как сериализатор должен быть отображен в различных
обстоятельствах, таких как рендеринг _HTML_. Параметр `{'base_template': 'textarea.html'}` походит на определение
виджета в поле формы Django. Это полезно для контроля за тем, как браузерная версия _API_ будет отображаться, что мы
пронаблюдаем дальше. Так же мы можем сохранить время, использовав класс `ModelSerializer`, применение которого будет
показано позже, а пока мы оставим описание нашего сериализатора развернутым.

### Работа с Сериализаторами

Прежде чем двигаться дальше, давайте освоимся с классом `Serializer`. Для этого перейдем в консоль _Django_.
`python manage.py shell`
Теперь нам необходимо импортировать несколько пакетов. Так же давайте сделаем пару сниппетов, с которыми будем работать.

```
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Snippet(code='foo = "bar"n')
snippet.save()

snippet = Snippet(code='print "hello, world"n')
snippet.save()
```

Теперь у нас есть несколько объектов `Snippet`, с которыми мы можем поиграть. Давайте посмотрим на сериализацию одного
из объектов.

```
serializer = SnippetSerializer(snippet)
serializer.data

# {'id': 2, 'title': u'', 'code': u'print "hello, world"n', 'linenos': False, 'language': u'python', 'style': u'friendly'}
```

Сейчас мы перевели объект модели во встроенные типы данных _Python_. Для завершения сериализации мы сформируем из этих
данных `JSON`.

```
content = JSONRenderer().render(serializer.data)
content

# '{"id": 2, "title": "", "code": "print "hello, world"n", "linenos": false, "language": "python", "style": "friendly"}'
```

- _Десериализация - подобна сериализации. Сначала мы парсим данные во встроенные типы данных Python._

```
from io import BytesIO

stream = BytesIO(content)
data = JSONParser().parse(stream)
Затем переводим эти данные в полностью сформированный объект.
serializer = SnippetSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print "hello, world"n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()
# <Snippet: Snippet object>;
```

Обратите внимание, насколько похожа работа с _API_ на работу с формами. Эта схожесть должна стать более заметной, когда
мы начнем писать представления, использующие наш сериализатор. Так же мы можем сериализовать запрос(`Queryset`), а не
отдельный объект модели. Для этого необходимо добавить параметр `many=True` в аргументы сериализатора.

```
serializer = SnippetSerializer(Snippet.objects.all(), many=True)
serializer.data

# [OrderedDict([('id', 1), ('title', u''), ('code', u'foo = "bar"n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 2), ('title', u''), ('code', u'print "hello, world"n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 3), ('title', u''), ('code', u'print "hello, world"'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])]
```

### Использование модельных сериализаторов

Наш класс `SnippetSerializer` дублирует множество информации, которую уже содержит модель `Snippet`. Было бы не плохо,
если бы мы могли оставлять наш код кратким. Так же, как _Django_ предоставляет классы Form и ModelForm, DRF
предоставляет классы `Serializer` и `ModelSerializer`. Давайте перепишем наш класс сериализатора, используя
класс `ModelSerializer`. Для этого перейдите в модуль `snippets/serializers.py` и измените код, как описано ниже.

```
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
```

У сериализаторов есть одно интересное свойство - вы можете узнать все поля объекта сериализатора, выведя его
представление. Чтобы попробовать это, откройте консоль _Django_ и выполните следующее:

```
from snippets.serializers import SnippetSerializer
serializer = SnippetSerializer()
print(repr(serializer))
# SnippetSerializer():
#    id = IntegerField(label='ID', read_only=True)
#    title = CharField(allow_blank=True, max_length=100, required=False)
#    code = CharField(style={'base_template': 'textarea.html'})
#    linenos = BooleanField(required=False)
#    language = ChoiceField(choices=[('Clipper', 'FoxPro'), ('Cucumber', 'Gherkin'), ('RobotFramework', 'RobotFramework'), ('abap', 'ABAP'), ('ada', 'Ada')...
#    style = ChoiceField(choices=[('autumn', 'autumn'), ('borland', 'borland'), ('bw', 'bw'), ('colorful', 'colorful')...
```

Важно помнить, что класс `ModelSerializer` не делает ничего магического. Это всего лишь синтаксический сахар для
создания классов сериализаторов: 1. Автоматически определяет набор полей; 2. Простая и стандартная реализация
методов `create()` и `update()`. Создание стандартных _Django_ представлений используя сериализатор Давайте посмотрим,
как мы можем написать несколько представлений _API_, используя наш новый класс `Serializer`. На данный момент мы не
будем использовать возможности, предоставляемые _DRF_, мы просто напишем обычные Django представления. Для этого
откройте `snippets/views.py` и добавьте следующее:

```
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
Корнем нашего API должно быть представление, которое поддерживает вывод всех существующих сниппетов, а так же создание новых.
@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
```

Помните, что, поскольку мы хотим использовать `POST` запрос в данном представлении от клиентов, у которых не
будет `CSRF` токена, необходимо добавить декоратор `csrf_exempt` Это, конечно, не то, что бы вы стали делать в
нормальных условиях, но в текущих условиях, этого будет достаточно. Так же нам нужно представление, которое обрабатывает
отдельный сниппет и позволяет получать, обновлять и удалять сниппет.

```
@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
 ```    

В конце, мы должны привязать данные представления. Создайте `snippets/urls.py` со следующим содержимым:

```
from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
```

Так же мы должны привязать данный диспетчер URL к корневому. Для этого зайдите в `urls.py` и подключите _URL_ диспетчер
нашего приложения:

```
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('snippets.urls')),
]
```

Ничего страшного в том, что есть несколько непродуманных моментов. Например, если мы пришлем неправильно
сформированный `JSON`, или если запрос будет сделан с помощью метода, не поддерживаемого представлением, мы получим
ошибку `500 'Server error'`. Однако, пока нам этого достаточно.

## View Django

...

## APIView

...

## URL Manager

__Чистая, элегантная схема URL:__ важная деталь высококачественного веб-приложения. Django позволяет оформлять URL как
угодно, без каких-либо ограничений со стороны фреймворка. См. «Классные URI не меняются» _ создателя World Wide Web Тима
Бернерса-Ли, где приведены убедительные аргументы в пользу того, почему URL-адреса должны быть чистыми и удобными.

__Быстрый обзор__
Чтобы разработать URL-адреса для приложения, вы создаете модуль Python, неофициально называемый `URLconf` (конфигурация
URL-адреса). Этот модуль представляет собой чистый код Python и является отображением между выражениями пути URL и
функциями Python (вашими представлениями). Это сопоставление может быть сколь угодно коротким или длинным. Оно может
ссылаться на другие сопоставления. И поскольку это чистый код Python, его можно создавать динамически. Django также
предоставляет способ перевода URL-адресов в соответствии с активным языком. Дополнительную информацию смотрите в
документации по интернационализации.

__Как Django обрабатывает запрос__
Когда пользователь запрашивает страницу вашего сайта на Django, система следует этому алгоритму, чтобы определить, какой
код Python выполнить:
Django определяет используемый корневой модуль `URLconf`. Обычно это значение параметра `ROOT_URLCONF`, но если входящий
объект `HttpRequest` имеет атрибут `urlconf` (установленный промежуточным программным обеспечением), его значение будет
использоваться вместо параметра `ROOT_URLCONF`. Django загружает этот модуль Python и ищет переменную urlpatterns. Это
должна быть sequence (последовательность(
экземпляров `django.urls.path()` и/или `django.urls.re_path()`. Django проходит по каждому шаблону URL по порядку и
останавливается на первом, который соответствует запрошенному URL, сопоставляя его с `path_info`. Как только один из
шаблонов URL совпадает, Django импортирует и вызывает заданное представление, которое является функцией Python (или
представление на основе классов). Представлению передаются следующие аргументы:
Экземпляр `HttpRequest`. Если сопоставленный шаблон URL не содержит именованных групп, то совпадения из регулярного
выражения предоставляются как позиционные аргументы. Ключевые аргументы состоят из любых именованных частей, совпадающих
с указанным выражением пути, переопределенных любыми аргументами, указанными в необязательном аргументе `kwargs`
для `django.urls.path()` или `django.urls.re_path()`. Если шаблон URL-адреса не совпадает или если на каком-либо этапе
этого процесса возникает исключение, Django вызывает соответствующее представление обработки ошибок.

__Вот пример URLconf:__

```
from django.urls import path

from . import views

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]
```

__Примечания:__
Чтобы получить значение из URL-адреса, используйте угловые скобки. Захваченные значения могут дополнительно включать тип
преобразователя. Например, используйте `<int:name>` для захвата целочисленного параметра. Если конвертер не включен,
сопоставляется любая строка, за исключением символа `/`. Нет необходимости добавлять косую черту в начале, потому что
она есть в каждом URL. Например, это `articles`, а не `/articles`.

__Примеры запросов:__
Запрос к `/articles/2005/03/` будет соответствовать третьей записи в списке. Django вызовет
функцию `views.month_archive(request, year=2005, month=3)`.
`/articles/2003/` будет соответствовать первому шаблону в списке, а не второму, потому что шаблоны проверяются по
порядку, а первый - первый тест, который нужно пройти. Не стесняйтесь использовать порядок для вставки таких особых
случаев. Здесь Django вызовет функцию `views.special_case_2003(request)`
`/articles/2003` не соответствует ни одному из этих шаблонов, потому что каждый шаблон требует, чтобы URL-адрес
заканчивался косой чертой.
`/articles/2003/03/building-a-django-site/` будет соответствовать окончательному шаблону. Django вызвал бы
функцию `views.article_detail(request, year=2003, month=3, slug="building-a-django-site")`.

__Конвертеры пути__
По умолчанию доступны следующие конвертеры пути:

`str` - соответствует любой непустой строке, за исключением разделителя пути, '/'. Это значение по умолчанию, если
преобразователь не включен в выражение.
`int` - соответствует нулю или любому положительному целому числу. Возвращает int.
`slug` - соответствует любой строке заголовка, состоящей из букв или цифр `__ASCII__`, а также символов дефиса и
подчеркивания. Например, `build-your-1st-django-site`.
`uuid` - соответствует форматированному UUID. Чтобы предотвратить сопоставление нескольких URL-адресов с одной и той же
страницей, необходимо использовать дефисы, а буквы должны быть строчными.
Например, `075194d3-6885-417e-a8a8-6c931e272f00`. Возвращает экземпляр `UUID`.
`path` - соответствует любой непустой строке, включая разделитель пути, `/`. Это позволяет вам сопоставлять полный путь
URL, а не сегмент пути URL, как в случае с `str`.

__Использование регулярных выражений__
Если синтаксиса путей и преобразователей недостаточно для определения шаблонов URL-адресов, вы также можете использовать
регулярные выражения. Для этого используйте `re_path()` вместо `path()`.

В регулярных выражениях Python для именованных групп регулярных выражений используется синтаксис `(?P<name>pattern)`,
где `name` - имя группы, а `pattern` - некоторый шаблон для сопоставления.

__Вот пример URLconf из предыдущего, переписанный с использованием регулярных выражений:__

```
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article_detail),
]
```

__Это примерно то же самое, что и в предыдущем примере, за исключением:__
Точные URL-адреса, которые будут соответствовать, немного более ограничены. Например, год 10000 больше не будет
соответствовать, поскольку целые числа года должны быть ровно четырьмя цифрами. Каждый захваченный аргумент отправляется
в представление в виде строки, независимо от того, какое совпадение обеспечивает регулярное выражение. При переключении
с `path()` на `re_path()` или наоборот, особенно важно знать, что тип аргументов представления может измениться, и
поэтому вы может потребоваться адаптировать ваши отображения.

__Использование безымянных групп регулярных выражений__
Также как и с синтаксисом именованной группы, например `(?P<year>[0-9]{4})`, вы также можете использовать более короткую
безымянную группу, например `([0-9]{4})`. Это использование не особенно рекомендуется, поскольку оно упрощает случайное
внесение ошибок между предполагаемым значением совпадения и аргументами представления. В любом случае рекомендуется
использовать только один стиль в данном регулярном выражении. Когда оба стиля смешаны, любые безымянные группы
игнорируются, и только именованные группы передаются в функцию просмотра.

__Вложенные аргументы__
Регулярные выражения допускают вложенные аргументы, и Django разрешит их и передаст в представление. При реверсировании
Django попытается заполнить все внешние захваченные аргументы, игнорируя все вложенные захваченные аргументы. Рассмотрим
следующие шаблоны URL, которые могут принимать аргумент страницы:

```
from django.urls import re_path

urlpatterns = [
    re_path(r'^blog/(page-(\d+)/)?$', blog_articles),                  # bad
    re_path(r'^comments/(?:page-(?P<page_number>\d+)/)?$', comments),  # good
]
```

Оба шаблона используют вложенные аргументы и разрешаются: например, blog/page-2/ приведет к совпадению с `blog_articles`
с двумя позиционными аргументами: `page-2/` и `2`. . Второй шаблон для `''comments` будет
соответствовать `comments/page-2/` с ключевым аргументом `page_number`, установленным в 2. Внешний аргумент в этом
случае является аргументом без захвата (?:...).

Для представления `blog_articles` необходимо, чтобы внешний захваченный аргумент был изменен на
противоположный, `page-2/` или без аргументов в этом случае, в то время как для комментариев можно обратить либо без
аргументов, либо со значением для `page_number`.

Вложенные захваченные аргументы создают сильную связь между аргументами представления и URL-адресом, как показано на
примере `blog_articles`: представление получает часть URL-адреса `(page-2/)`, а не только значение, которое интересует
представление. Эта связь еще более выражена при реверсировании, так как для переворота представления нам нужно передать
часть URL вместо номера страницы.

Как правило, фиксируйте только те значения, с которыми представление должно работать, и используйте аргументы без
захвата, когда регулярному выражению требуется аргумент, но представление его игнорирует.

__Что ищет URLconf__

`URLconf` выполняет поиск по запрошенному URL как в обычной строке Python. Не включает параметры `GET` или `POST` или
имя домена.

Например, в запросе на `https://www.example.com/myapp/URLconf` будет искать `myapp/`.

В запросе на `https://www.example.com/myapp/?page=3` URLconf будет искать `myapp/`.

URLconf не смотрит на метод запроса. Другими словами, все методы запроса - `POST`, `GET`, `HEAD` и т.д. - будут
перенаправлены на одну и ту же функцию для одного и того же `URL`.

__Включение других URLconfs__

В любой момент ваши `urlpatterns` могут «включать» другие модули `URLconf`. По сути, это «корень» набора нижестоящих
URL-адресов.

__Например, вот выдержка из URLconf для самого Django website. Он включает ряд других URLconfs:__*

```
from django.urls import include, path

urlpatterns = [
    # ... snip ...
    path('community/', include('aggregator.urls')),
    path('contact/', include('contact.urls')),
    # ... snip ...
]
```

Всякий раз, когда Django встречает `include()`, он отрезает любую часть URL-адреса, совпадающую до этого момента, и
отправляет оставшуюся строку во включенный `URLconf` для дальнейшей обработки.

Другая возможность - включить дополнительные шаблоны URL-адресов, используя список экземпляров `path()`.

__Например, рассмотрим этот URLconf:__

```
from django.urls import include, path

from apps.main import views as main_views
from credit import views as credit_views

extra_patterns = [
    path('reports/', credit_views.report),
    path('reports/<int:id>/', credit_views.report),
    path('charge/', credit_views.charge),
]

urlpatterns = [
    path('', main_views.homepage),
    path('help/', include('apps.help.urls')),
    path('credit/', include(extra_patterns)),
]
```

В этом примере URL-адрес `/credit/reports/` будет обрабатываться представлением Django `credit_views.report()`.

Это можно использовать для удаления избыточности из URLconfs, где один префикс шаблона используется многократно.
Например, рассмотрим этот URLconf:

```
from django.urls import path
from . import views

urlpatterns = [
    path('<page_slug>-<page_id>/history/', views.history),
    path('<page_slug>-<page_id>/edit/', views.edit),
    path('<page_slug>-<page_id>/discuss/', views.discuss),
    path('<page_slug>-<page_id>/permissions/', views.permissions),
]
```

__Мы можем улучшить это, указав общий префикс пути только один раз и сгруппировав суффиксы, которые отличаются:__

```
from django.urls import include, path
from . import views

urlpatterns = [
    path('<page_slug>-<page_id>/', include([
        path('history/', views.history),
        path('edit/', views.edit),
        path('discuss/', views.discuss),
        path('permissions/', views.permissions),
    ])),
]
```

__Захваченные параметры__
__Включенный URLconf получает любые захваченные параметры из родительских URLconfs, поэтому следующий пример допустим:__

```
# In settings/urls/main.py
from django.urls import include, path

urlpatterns = [
    path('<username>/blog/', include('foo.urls.blog')),
]

# In foo/urls/blog.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog.index),
    path('archive/', views.blog.archive),
]
```

В приведенном выше примере захваченная переменная username передается во включенный URLconf, как и ожидалось.

__Передача дополнительных параметров функции предствления__
У URLconfs есть ловушка, которая позволяет передавать дополнительные аргументы функциям просмотра в виде словаря Python.

Функция `path()` может принимать необязательный третий аргумент, который должен быть словарем дополнительных ключевых
аргументов для передачи в функцию представление.

__Например:__

```
from django.urls import path
from . import views

urlpatterns = [
    path('blog/<int:year>/', views.year_archive, {'foo': 'bar'}),
]
```

В этом примере для запроса к `/blog/2005/` Django вызовет `views.year_archive(request, year=2005, foo='bar')`.

Этот метод используется в фреймворке синдикации для передачи метаданных и параметров представлениям.

__Разрешение конфликтов__
Возможно иметь шаблон URL, который захватывает именованные ключевые аргументы, а также передает аргументы с такими же
именами в свой словарь дополнительных аргументов. Когда это произойдет, аргументы в словаре будут использоваться вместо
аргументов, записанных в URL-адресе.

__Передача дополнительных параметров в `include()`__
Точно так же вы можете передать дополнительные параметры в `include()`, и каждой строке во включенном URLconf будут
переданы дополнительные параметры.

__Например, эти два набора URLconf функционально идентичны:__

Установите один:

```
# main.py
from django.urls import include, path

urlpatterns = [
    path('blog/', include('inner'), {'blog_id': 3}),
]

# inner.py
from django.urls import path
from mysite import views

urlpatterns = [
    path('archive/', views.archive),
    path('about/', views.about),
]
```

Установите второй:

```
# main.py
from django.urls import include, path
from mysite import views

urlpatterns = [
    path('blog/', include('inner')),
]

# inner.py
from django.urls import path

urlpatterns = [
    path('archive/', views.archive, {'blog_id': 3}),
    path('about/', views.about, {'blog_id': 3}),
]
```

Обратите внимание, что дополнительные параметры будут всегда передаваться каждой строке во включенном URLconf,
независимо от того, действительно ли представление строки принимает эти параметры как действительные. По этой причине
этот метод полезен только в том случае, если вы уверены, что каждое представление во включенном URLconf принимает
дополнительные параметры, которые вы передаете.

__Обратное разрешение URL-адресов__
Распространенной потребностью при работе над проектом Django является возможность получения URL-адресов в их
окончательных формах либо для встраивания в сгенерированный контент (URL-адреса представлений и ресурсов, URL-адреса,
отображаемые пользователю и т.д.), либо для обработки потока навигации на сервере (перенаправления и т.д.)

Настоятельно рекомендуется избегать жесткого кодирования этих URL-адресов (трудоемкая, немасштабируемая и подверженная
ошибкам стратегия). Столь же опасна разработка специальных механизмов для генерации URL-адресов, которые параллельны
структуре, описанной в URLconf, что может привести к созданию URL-адресов, которые со временем устареют.

Другими словами, нужен `DRY` механизм. Среди других преимуществ это позволит эволюционировать дизайн URL без
необходимости просматривать весь исходный код проекта для поиска и замены устаревших URL.

Основная информация, доступная для получения URL-адреса – это идентификация (например, имя) представления, отвечающего
за его обработку. Другая часть информации, которая обязательно должна участвовать в поиске правильного URL, – это типы (
позиционные, ключевые слова) и значения аргументов представления.

Django предоставляет решение, в котором преобразователь URL-адресов является единственным хранилищем дизайна
URL-адресов. Вы загружаете его с помощью своего URLconf, и затем его можно использовать в обоих направлениях:

Начиная с URL-адреса, запрошенного пользователем/браузером, он вызывает правильное представление Django, предоставляя
любые аргументы, которые могут ему понадобиться, с их значениями, извлеченными из URL-адреса. Начиная с идентификации
соответствующего представления Django и значений аргументов, которые будут ему переданы, получите связанный URL. Первый
- это использование, которое мы обсуждали в предыдущих разделах. Второй - это то, что известно как обратное разрешение
URL, обратное сопоставлениеURL *, *обратный поиск URL или просто реверсирование URL.

Django предоставляет инструменты для реверсирования URL-адресов, соответствующие различным уровням, на которых требуются
URL-адреса:

- В шаблонах: использование тега шаблона `url`.
- В коде Python: использование функции reverse().
- В коде более высокого уровня, связанном с обработкой URL-адресов экземпляров модели Django: метод get_absolute_url().

__Примеры:__
Снова рассмотрим эту запись URLconf:

```
from django.urls import path

from . import views

urlpatterns = [
    #...
    path('articles/<int:year>/', views.year_archive, name='news-year-archive'),
    #...
]
```

В соответствии с этой схемой URL для архива, соответствующего году nnnn, - это `/articles/<nnnn>/`.

Вы можете получить их в коде шаблона, используя:

```
<a href="{% url 'news-year-archive' 2012 %}">2012 Archive</a>
{# Or with the year in a template context variable: #}
<ul>
{% for yearvar in year_list %}
<li><a href="{% url 'news-year-archive' yearvar %}">{{ yearvar }} Archive</a></li>
{% endfor %}
</ul>
```

Или в коде Python:

```
from django.http import HttpResponseRedirect
from django.urls import reverse

def redirect_to_year(request):
    # ...
    year = 2006
    # ...
    return HttpResponseRedirect(reverse('news-year-archive', args=(year,)))
```

Если по какой-то причине было решено, что URL-адреса, по которым публикуется контент для ежегодных архивов статей,
должны быть изменены, вам нужно будет изменить только запись в URLconf.

В некоторых сценариях, где представления носят общий характер, между URL-адресами и представлениями может существовать
отношение «многие к одному». В таких случаях имя представления не является достаточно хорошим идентификатором, когда
приходит время реверсирования URL-адресов. Прочтите следующий раздел, чтобы узнать о решении, которое предлагает Django
для этого.

__Именование шаблонов URL__
Чтобы выполнить реверсирование URL, вам необходимо использовать именованные шаблоны URL, как это сделано в примерах
выше. Строка, используемая для имени URL, может содержать любые символы. Вы не ограничены допустимыми именами Python.

При именовании шаблонов URL-адресов выбирайте имена, которые вряд ли будут конфликтовать с выбором имен других
приложений. Если вы называете свой шаблон URL-comment, а другое приложение делает то же самое, URL-адрес, который
находит `reverse()`, зависит от того, какой шаблон последним присутствует в `urlpatterns` вашего проекта.

Добавление префикса к именам URL-адресов, возможно, производных от имени приложения (например, `myapp-comment`
вместо `comment`), снижает вероятность коллизий.

Вы можете сознательно выбрать то же имя URL, что и другое приложение, если хотите переопределить представление.
Например, обычным вариантом использования является переопределение `LoginView`. Некоторые части Django и большинства
сторонних приложений предполагают, что это представление имеет шаблон URL-адреса с именем `login`. Если у вас есть
настраиваемое представление входа в систему и его URL-адрес имеет имя `login`, `reverse()` найдет ваше настраиваемое
представление, если оно находится в `urlpatterns` после `django.contrib.auth.urls` (если он вообще включен).

Вы также можете использовать одно и то же имя для нескольких шаблонов URL, если они отличаются своими аргументами. В
дополнение к имени URL `reverse()` соответствует количеству аргументов и именам ключевых аргументов. Конвертеры пути
также могут вызывать ValueError, чтобы указать на отсутствие совпадения, подробности смотрите в разделе Регистрация
пользовательских конвертеров пути.

__Пространства имен URL__

__Вступление__
Пространства имен URL-адресов позволяют однозначно перевернуть именованные URL, даже если разные приложения используют
одинаковые имена URL. Для сторонних приложений рекомендуется всегда использовать URL-адреса в пространстве имен (как мы
это делали в учебнике). Точно так же он позволяет вам изменять URL-адреса, если развернуто несколько экземпляров
приложения. Другими словами, поскольку несколько экземпляров одного приложения будут совместно использовать именованные
URL-адреса, пространства имен предоставляют способ различать эти именованные URL-адреса.

Приложения Django, которые правильно используют пространство имен URL-адресов, могут быть развернуты более одного раза
для определенного сайта. Например `django.contrib.admin` имеет класс `AdminSite`, который позволяет развертывать более
одного экземпляра admin. В следующем примере мы обсудим идею развертывания приложения для опросов из учебника в двух
разных местах, чтобы мы могли предоставить одни и те же функции двум разным аудиториям (авторам и издателям).

Пространство имен URL состоит из двух частей, каждая из которых является строкой:

__пространство имен приложения__
Оно описывает имя развертываемого приложения. Каждый экземпляр одного приложения будет иметь одно и то же пространство
имен приложения. Например, приложение администратора Django имеет в некоторой степени предсказуемое пространство имен
приложения `admin`.

__пространство имен экземпляра__
Оно определяет конкретный экземпляр приложения. Пространства имен экземпляров должны быть уникальными для всего вашего
проекта. Однако пространство имен экземпляра может быть таким же, как пространство имен приложения. Это используется для
указания экземпляра приложения по умолчанию. Например, экземпляром администратора Django по умолчанию имеет пространство
имен экземпляра `admin`. URL-адреса в пространстве имен указываются с помощью оператора `:`. Например, ссылка на главную
страницу индекса приложения администратора осуществляется с помощью `admin:index`. Это указывает на пространство
имен `admin` и именованный URL `index`.

Пространства имен также могут быть вложенными. Именованный URL-адрес `sports:polls:index` будет искать шаблон с
именем `index` в пространстве имен `polls`, который сам определен в пространстве имен верхнего уровня `sports`.

__Реверсирование пространств имён URL__
Получив URL-адрес с пространством имен (например, `polls:index`) для разрешения, Django разбивает полное имя на части, а
затем пытается выполнить следующий поиск:

Сначала Django ищет соответствующий `application namespace` (в этом примере `polls`). Это даст список экземпляров этого
приложения.

Если определено текущее приложение, Django находит и возвращает преобразователь URL-адресов для этого экземпляра.
Текущее приложение можно указать с помощью аргумента `current_app` функции `reverse()`.

Тег шаблона `url` использует пространство имен текущего разрешенного представления в качестве текущего приложения
в `RequestContext`. Вы можете изменить это значение по умолчанию, установив для текущего приложения
атрибут `request.current_app`.

Если текущего приложения нет, Django ищет экземпляр приложения по умолчанию. Экземпляр приложения по умолчанию - это
экземпляр, у которого есть `instance namespace`, совпадающий с `application namespace` (в этом примере экземпляр `polls`
называется 'polls').

Если экземпляра приложения по умолчанию нет, Django выберет последний развернутый экземпляр приложения, каким бы ни было
его имя экземпляра.

Если предоставленное пространство имен не соответствует `application namespace` на шаге 1, Django попытается выполнить
прямой поиск пространства имен как `instance namespace`.

Если есть вложенные пространства имен, эти шаги повторяются для каждой части пространства имен, пока не будет найдено
только имя представления. Затем имя представления будет преобразовано в URL-адрес в найденном пространстве имен.

__Пример__
Чтобы продемонстрировать эту стратегию разрешения проблем в действии, рассмотрим пример двух экземпляров
приложения `polls` из учебника: один под названием `author-polls`, а другой - publisher-polls'. Предположим, мы улучшили
это приложение, чтобы оно учитывало пространство имен экземпляра при создании и отображении опросов.
*__urls.py__*

```
from django.urls import include, path

urlpatterns = [
    path('author-polls/', include('polls.urls', namespace='author-polls')),
    path('publisher-polls/', include('polls.urls', namespace='publisher-polls')),
]
```    

*__polls/urls.py__*

```
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    ...
]
```

__Используя эту настройку, возможны следующие поиски:__

Если один из экземпляров является текущим - скажем, если бы мы отображали страницу сведений в экземпляре `author-polls`

- `polls: index` преобразуется в индексную страницу `author-polls`; то есть оба следующих результата приведут
  к `/author-polls/`.

__В методе представления на основе классов:__

```reverse('polls:index', current_app=self.request.resolver_match.namespace)```
__и в шаблоне:__

```{% url 'polls:index' %}```
Если текущего экземпляра нет - скажем, если мы отображали страницу где-то еще на сайте, - `polls:index` будет
преобразовываться в последний зарегистрированный экземпляр `polls`. Поскольку нет экземпляра по умолчанию (пространство
имен экземпляров `polls`), будет использоваться последний зарегистрированный экземпляр `polls`. Это
будет `publisher-polls`, поскольку он объявлен последним в `urlpatterns`.

`author-polls:index` всегда будет преобразовываться в индексную страницу экземпляра `author-polls` (и аналогично
для `publisher-polls`).

Если бы также существовал экземпляр по умолчанию, то есть экземпляр с именем `polls`, единственное изменение из
приведенного выше было бы в случае, если нет текущего экземпляра (второй элемент в списке выше). В этом
случае `polls:index` будет разрешаться в индексную страницу экземпляра по умолчанию вместо экземпляра, объявленного
последним в `urlpatterns`.

__Пространства имен URL и включенные `URLconfs`__
Пространства имен приложений включенных URLconfs можно указать двумя способами.

Во-первых, вы можете установить атрибут `app_name` во включенном модуле URLconf на том же уровне, что и
атрибут `urlpatterns`. Вы должны передать фактический модуль или строковую ссылку на модуль в `include()`, а не сам
список `urlpatterns`.

*__polls/urls.py__*

```
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    ...
]
```

*__urls.py__*

```
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
]
```

URL-адреса, определенные в `polls.urls`, будут иметь пространство имен приложения `polls`.

Во-вторых, вы можете включить объект, содержащий данные встроенного пространства имен. Если вы `include()` список
экземпляров `path()` или `re_path()`, URL-адреса, содержащиеся в этом объекте, будут добавлены в глобальное пространство
имен . Однако вы также можете `include()` кортеж из 2, содержащий:

``(<list of path()/re_path() instances>, <application namespace>)``

__Например:__

```
from django.urls import include, path

from . import views

polls_patterns = ([
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
], 'polls')

urlpatterns = [
    path('polls/', include(polls_patterns)),
]
```

Это будет включать назначенные шаблоны URL-адресов в заданное пространство имен приложения.

Пространство имен экземпляра можно указать с помощью аргумента `namespace` для `include()`. Если пространство имен
экземпляра не указано, по умолчанию будет использоваться пространство имен приложения включенного URLconf. Это означает,
что он также будет экземпляром по умолчанию для этого пространства имен.

## Routers

__Маршрутизаторы__

```
Роутинг ресурсов позволяет быстро объявлять все общие маршруты для заданного контроллера ресурса. Вместо объявления отдельных маршрутов... ресурсный маршрут объявляет их одной строчкой кода.
    —Документация Ruby on Rails
```

Некоторые веб фреймворки, как Rails, автоматически реализуют механизм логической свзяи URL'ов приложения с входящими
запросами. `REST framework` добавляет поддержку автоматического роутинга для Django, тем самым предоставляя пользователю
простой и надежный способ написания логики представлении для набора URL. Использование Ниже приводится пример простого
URL conf с использованием `SimpleRouter`.

```
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', AccountViewSet)
urlpatterns = router.urls
```

Метод `register()` должен включать два обязательных аргумента:
`prefix` - префикс URL, использующийся с данным набором роутеров.
`viewset` - класс `viewset`.

__Опционально вы можете указать дополнительный аргумент:__
`base_name` - основа для использования с URL именами. Елси аргумент не указан, то базовое имя будет автоматически
сгенерировано на основе атрибута queryset из viewset, при наличии такого. Обратите внимание, что если `viewset` не
включает атрибут `queryset`, то вы должны использовать base_name при регистрации `viewset`. Пример выше генерирует
следующие URL паттерны:

|URL pattern|Name|
|-----------|----|
|^users/$| `user-list`|
|^users/{pk}/$|`user-detail`|
|^accounts/$|`account-list`|
|^accounts/{pk}/$|`account-detail`|

Примечание: аргумент `base_name` используется для того, чтобы указать исходную часть паттерна имени представления. В
примере выше это часть `user` или `account`. Как правило вам не требуется указывать аргументы для `base_name`, но при
наличии `viewset`, в котором вы кастомно определили метод `get_queryset`, `viewset` может не иметь списка
атрибутов `.queryset`. Если вы попробуете зарегистрировать этот `viewset`, то увидите ошибку, наподобие этой.
``'base_name' argument not specified, and could not automatically determine the name from the viewset, as it does not have a '.queryset' attribute.``
Это значит, что вам необходимо однозначно указать аргумент base_name при регистрации viewset, так как он не может
автоматически определяться исходя из имени модели. Использование `include` с маршрутизаторами Атрибут `.urls` экземпляра
роутера всего навсего является стандартом списка URL паттернов. Существуют разные способы включения этих URL'ов.
Например, вы можете добавить `router.urls` к списку существующих представлений...

```
router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    url(r'^forgot-password/$', ForgotPasswordFormView.as_view()),
]

urlpatterns += router.urls
```

Помимо этого вы можете использовать функцию include Django, например...

```
urlpatterns = [
    url(r'^forgot-password/$', ForgotPasswordFormView.as_view()),
    url(r'^', include(router.urls)),
]
```

Пространства имен могут быть URL паттернами роутера

```
urlpatterns = [
    url(r'^forgot-password/$', ForgotPasswordFormView.as_view()),
    url(r'^api/', include(router.urls, namespace='api')),
]
```

При использовании пространства имен с гиперссылочными сериализаторами, вам также нужно удостовериться, что любой
параметр `view_name` сериализаторов корректно отражает пространство имен. В примере выше вам потребовалось бы включить
параметр `view_name='api:user-detail` для полей сериализатора, которые связаны гиперссылкой с отдельными представлениями
пользователя. Дополнительные ссылки и действия Любые методы `viewset`, используемые с декораторами `@detail_route`
или `@list_route` также будут маршрутизированы. Например, при использовании данного метода на классе `UserViewSet:`

```
from myapp.permissions import IsAdminOrIsSelf
from rest_framework.decorators import detail_route

class UserViewSet(ModelViewSet):
    ...

    @detail_route(methods=['post'], permission_classes=[IsAdminOrIsSelf])
    def set_password(self, request, pk=None):
        ...
```

Дополнительно будет сгенерирован следующий URL паттерн:

|URL pattern|Name|
|-----------|----|
|^users/{pk}/set_password/$|`user-set-password`|

Если вы не хотите использовать стандартную генерацию URL для ваших кастомных действий, то используйте
параметр `url_path` для настройки. Например, если вы хотите изменить URL для вашего кастомного действия
на `^users/{pk}/change-password/$`, то можете написать следующее:

```
from myapp.permissions import IsAdminOrIsSelf
from rest_framework.decorators import detail_route

class UserViewSet(ModelViewSet):
    ...

    @detail_route(methods=['post'], permission_classes=[IsAdminOrIsSelf], url_path='change-password')
    def set_password(self, request, pk=None):
        ...
```

Этот пример сгенерирует следующий URL паттерн:

|URL pattern|Name|
|-----------|----|
|^users/{pk}/change-password/$|`user-change-password`|

Если вы не хотите использовать стандартные имена для ваших кастомных действий, то можете использовать
параметр `url_name` для настройки. Например, если вы хотите изменить имя вашего кастомного действия
на `user-change-password`, то можете написать следующее:

```
from myapp.permissions import IsAdminOrIsSelf
from rest_framework.decorators import detail_route

class UserViewSet(ModelViewSet):
    ...

    @detail_route(methods=['post'], permission_classes=[IsAdminOrIsSelf], url_name='change-password')
    def set_password(self, request, pk=None):
        ...
```

Этот пример сгенерирует следующий URL паттерн:

|URL pattern|Name|
|-----------|----|
|^users/{pk}/set_password/$|`user-change-password`|

Вы также можете использовать параметр `url_path` и `url_name` вместе, чтобы дополнительно контролировать генерирование
URL для кастомных представлений. Для дополнительно информации смотри документацию viewset о создании .

__Руководство API__

`SimpleRouter`
Этот роутер включает маршруты для стандартного набора действий `list`, `create`, `retrieve`, `update`, `partial_update`
и `destroy`. `Viewset` также может выделить дополнительные методы для маршрутизации, использя декораторы `@detail_route`
или `@list_route`

|URL Style|HTTP Method|Action|URL Name|
|---------|-----------|------|--------|
|{prefix}/|GET|list|{basename}-list|
|POST|create|||
|{prefix}/{lookup}/|GET, или как указано в аргументах `методов`|метод декоратор `@list_route`|{basename}-{methodname}|
|{prefix}/{lookup}/{methodname}/|GET|retrieve|{basename}-detail|
|PUT|update|||
|PATCH|partial_update|||
|DELETE|destroy|||
|{prefix}/{lookup}/{methodname}/|GET, или как указано в аргументах `методов`|метод декоратор `@detail_route`|{basename}-{methodname}|

Как и в случае с `SimpleRouter`, закрывающие слеши путей URL можно удалить, установив значение `False` в
настройке `trailing_slash` при инициализации роутера.
``router = DefaultRouter(trailing_slash=False)``

__Кастомные роутеры__
Вам редко понадобится применять кастомный роутер, но он может быть полезен, если у вас есть особые требования к
структуре URL вашего API. Это позволит вам инкапсулировать структуру URL для повтороного использования, т.е. вам не
придется отдельно писать URL паттерны для каждого нового представления. Самый простой способ применения кастомного
роутера это образовать подласс от одного из существующих классов роутера. Атрибут `.routes` используется для
шаблонизирования URL паттернов, которые будут отображаться для каждого `viewset`. Атрибут `.routes` это список, который
содержит именованные кортежи (`namedtuple`) `Route`.

__Аргументы именованных кортежей Route:__
`url`: Строка, которая представляет URL для маршрутизации. Может включать следующие форматирующие строки:
`{prefix}` - префикс URL, который будет использоваться с набором путей.
`{lookup}` - поле поиска, которое используется для сопоставления с единичным экземпляром.
`{trailing_slash}` - либо '/' или пустая строка, в зависимости от аргумента `trailing_slash`.
`mapping`: отображение имен методов HTTP для методов представления
`name`: URL name, используемое в reverse вызовах. Может включать следующую форматирующую строку:
`{basename}` - основа, которая используется с создающимися URL именами.
`initkwargs`: Словарь любого дополнительного аргумена, который должен передаваться при инициализации представления.
Заметьте, что аргумент `suffix` зарезервирован для определения типа `viewset` и используется при создании имени
представления и навигационных цепочек. Кастомизация динамических путей Вы также можете кастомизировать маршрутизацию
декораторов `@list_route` и `@detail_route`. Чтобы маршрутизировать их внесите именованные кортежи
`DynamicListRoute` и/или `DynamicDetailRoute` в списке `.routes list..`
Аргументы `DynamicListRoute` и `DynamicDetailRoute`:
`url`: Строка, которая представляет URL для маршрутизации. Может включать те же форматирующие строки, как и `Route` и
дополнительно принимает форматирующие строки `{methodname}` и `{methodnamehyphen}`.
`name`: Имя URL, используемое в reverse вызовах. Может включать следующие форматирующие строки: `{basename}`
, `{methodname}` и `{methodnamehyphen}`.
`initkwargs`: Словарь любого дополнительного аргумена, который должен передаваться при инициализации представления.

__Пример:__
Слеюущий пример будет маршрутизировать только действия `list` и `retrieve` и не использует закрывающие слеши.

```
from rest_framework.routers import Route, DynamicDetailRoute, SimpleRouter

class CustomReadOnlyRouter(SimpleRouter):
    """
    A router for read-only APIs, which doesn't use trailing slashes.
    """
    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            initkwargs={'suffix': 'Detail'}
        ),
        DynamicDetailRoute(
            url=r'^{prefix}/{lookup}/{methodnamehyphen}$',
            name='{basename}-{methodnamehyphen}',
            initkwargs={}
        )
    ]
```

Давайте посмотрим на пути, которые наш `CustomReadOnlyRouter` сгенерирует для простого `viewset`.
*__views.py__*

```
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    @detail_route()
    def group_names(self, request, pk=None):
        """
        Returns a list of all the group names that the given
        user belongs to.
        """
        user = self.get_object()
        groups = user.groups.all()
        return Response([group.name for group in groups])
```

*__urls.py__*

```
router = CustomReadOnlyRouter()
router.register('users', UserViewSet)
urlpatterns = router.urls
```

Будет сгенерирован следующий маппинг...

|URL|HTTP Method|Action|URL Name|
|---|-----------|------|--------|
|/users|GET|list|user-list|
|/users/{username}|GET|retrieve|user-detail|
|/users/{username}/group-names|GET|group_names|user-group-names|

Для другого примера настроек атрибута `.routes` см код источника класса `SimpleRouter`.

__Продвинутые кастомные роутеры__
Если вы хотите обеспечить полностью настраивомое поведение, то можете переписать `BaseRouter` и метод `get_urls(self)`.
Метод должен инспетировать зарегистрированные `viewsets` и вернуть список URL паттернов. К зарегистрированным кортежам
базовых имен, префиксов и `viewset` можно получить доступ через атрибут `self.registry`. Также вы можете переписать
метод `get_default_base_name(self, viewset)` или же всегда явно прописывать аргумент `base_name` при
регистрации `viewsets` в роутере.
