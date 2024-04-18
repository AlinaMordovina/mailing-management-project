coursework_6 Django

Веб-приложение сервиса управления рассылками, администрирования и получения статистики.

Технологии:
- python 3.12
- PostgreSQL
- Redis

Используемые библиотеки:
- psycopg2-binary 2.9.9
- pillow 10.2.0
- ipython 8.21.0
- pytils 0.4.1
- redis 5.0.3
- python-dotenv 1.0.1
- django-apscheduler 0.6.2


Инструкция для развертывания проекта:
1. Клонировать проект

https://github.com/AlinaMordovina/mailing-management-project.git

2. Создать виртуальное окружения

Находясь в директории проекта запустить в терминале команды:

python -m venv venv

source venv/bin/activate

3. Установить зависимости

Все зависимости указаны в файле requirements.txt

Для установки всех зависимостей из файла необходимо запустить в терминале команду:

pip install -r requirements.txt

4. Cоздать базу данных

Для создания базы данных необходимо запустить в терминале команду:

CREATE DATABASE DATABASE_NAME

5. Применить миграции 

Для создания и применения миграций необходимо запустить в терминале команды:

python3 manage.py makemigrations
python3 manage.py migrate

6. Заполнить файл .env по образцу env.sample
7. Для создания суперпользователя необходимо применить команду "python manage.py csu"
8. Для запуска проекта использовать команду "python manage.py runserver", либо через конфигурационные настройки PyCharm.







Автор проекта: Мордовина Алина