# BakeCake
Custom cake shop  
[See the website in action](https://mrdave.pythonanywhere.com/)

## How to install

Python should already be installed. This project is tested on Python 3.10 and 3.11. You may use other versions as you will, but YMMV.

Clone the repo / download code

Using virtual environment [virtualenv/venv](https://docs.python.org/3/library/venv.html) is recommended for project isolation.

Install requirements:
```commandline
pip install -r requirements.txt
```

Migrate database
```commandline
python manage.py migrate
```

Start a dev server
```commandline
python manage.py runserver
```

### env variables

To configure those settings, create a `.env` file in the root folder of the project and put in there the following:

- `SECRET_KEY` - A secret key for a particular Django installation. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value.
- `DEBUG` - A boolean that turns on/off debug mode. If your app raises an exception when DEBUG is True, Django will display a detailed traceback, including a lot of metadata about your environment, such as all the currently defined Django settings (from settings.py).
- `ALLOWED_HOSTS` - A list of strings representing the host/domain names that this Django site can serve. This is a security measure to prevent HTTP Host header attacks, which are possible even under many seemingly-safe web server configurations. [See details at Django docs.](https://docs.djangoproject.com/en/5.0/ref/settings/#allowed-hosts)
- `CSRF_TRUSTED_ORIGINS` - A list of trusted origins for unsafe requests [See details at Django docs.](https://docs.djangoproject.com/en/5.0/ref/settings/#csrf-trusted-origins)

## How to use

Open webpage in your browser. If using dev server it will be available at `localhost:8000`.

Use Django Admin site to add or edit features (such as cake toppings). Access it by navigationg to `localhost:8000/admin`. 

Create a superuser account:
```commandline
python manage.py createsuperuser
```

## Project goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
