# Owl's Django App

[Django Docs](https://docs.djangoproject.com/en/5.0/)
[Project template](https://docs.djangoproject.com/en/5.0/intro/tutorial01/#creating-a-project)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/midnight-animals/owl-django-app
```
2. Prepare python virtual environment
```bash
cd owl-django-app/demoapp
sudo apt update
sudo apt install python3-venv
python3 -m venv env
```

3. Activate virtual environment
```bash
source env/bin/activate
```
You can deactive the virtual environment by
```bash
deactivate
```
4. Install the required dependency

```bash
pip install -r requirements.txt
```
5. Run Development server
```bash
# https://docs.djangoproject.com/en/5.0/intro/tutorial01/#the-development-server
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your web browser to access the app.
