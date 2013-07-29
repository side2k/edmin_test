Развертывание:

* клонируем репозиторий:
<pre>
git clone https://github.com/side2k/edmin_test.git edmin_test
</pre>
* заходим в клонированный каталог, разворачиваем там virtualenv и устанавливаем зависимости:
<pre>
cd edmin_test
virtualenv .
source bin/activate
pip install -r requirements.txt
</pre>
* создаем рабочую копию локальных настроек:
<pre>
cp edmin_test/settings/local_settings.tpl edmin_test/settings/local_settings.py
</pre>
* редактируем файл local_settings.py и прописываем туда реквизиты БД, например, так:
<pre>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'edmin_test',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
</pre>
в приведенном примере будет использоваться база mysql с наименованием edmin_test на локальном сервере, и вход туда будет осуществляться под пользователем root без пароля
* если база еще не создана, то создаем её
* создаем необходимые таблицы:
<pre>
./manage.py syncdb --noinput
</pre>
* запускаем локальный тестовый сервер:
<pre>
./manage.py runserver
</pre>
* открываем браузером http://localhost:8000
