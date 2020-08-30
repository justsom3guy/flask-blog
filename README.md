# Flask Blog

Flask project with MongoDB (Atlas) as the database and using Multiple Flask modules like

* [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/)

* [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)

* [Flask-Login](https://flask-login.readthedocs.io/en/latest/)

* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)

* [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/)

* [Flask-Mongoengine](http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/)

* [Flask-mail](https://pythonhosted.org/Flask-Mail/)

The project is hosted on [Heroku](https://project-flask-blog.herokuapp.com/).

---

## Setup

### Terminal

``` bash
python3 -m venv env
pip install -r requirements.txt
touch .env .flaskenv
```

### In .env

``` env
HOST="{mongo-host-uri}"
```

### In .flaskenv

``` flaskenv
FLASK_APP=main.py
FLASK_ENV=development
SECRET_KEY="{super secret key}"
JWT_SECRET_KEY = '{super secret key 2}'
JWT_TOKEN_LOCATION = 'cookies'
JWT_COOKIE_CSRF_PROTECT = True
```

### For secret keys

``` python
>>> import secrets
>>> secrets.token_hex(16) #for python-terminal else print the output.
```

---

## Todo

* [x] Connect to mongo-DB

* [x] Implement flask-login

* [ ] Front-end of the pages

* [ ] Implement flask-mail

* [ ] Create production model

* [ ] Testing
