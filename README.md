Для того, чтобы бот начал работать на сервере, необходимо проделать следующие действия:
1. Создать виртуальное окружение python
2. Установить зависимости, предварительно активировав окружение, командой pip install -r requirements.txt
3. В файле django_admin/django_admin/settings.py раскомментировать переменную STATIC_ROOT и закомментировать переменную STATICFILES_DIRS, переменной DEBUG задать значение False
4. Выполнить в терминале команду python manage.py collectstatic
5. В корневом каталоге проекта создать файл .htaccess и вписать в него следующее:
Options +ExecCGI
AddDefaultCharset utf-8
AddHandler wsgi-script .py

RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f

RewriteRule ^(.*)$ путь/до_скрипта/wsgi.py$1 [QSA,L]

6. В терминале активировать команду, предварительно активировав виртуальное окружение Python 
nohup python путь/до_скрипта/app.py
7. Для остановки бота следует активировать следующие команды:
ps aux | grep путь/до_скрипта/app.py
Скопировать pid процесса данного скрипта и активировать команду kill <pid>
