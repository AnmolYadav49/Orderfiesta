python -m venv venv
.\venv\Scripts\python.exe -m pip install django pillow
.\venv\Scripts\django-admin.exe startproject orderista_core .
.\venv\Scripts\python.exe manage.py startapp accounts
.\venv\Scripts\python.exe manage.py startapp canteen
.\venv\Scripts\python.exe manage.py startapp orders
.\venv\Scripts\python.exe manage.py startapp ai_services
