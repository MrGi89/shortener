# URL shortener application

**USAGE:**

App is available for free on: https://jmrshortener.herokuapp.com/. App provides possibility to shorten passed url. 

**PREREQUIREMENTS:**

* python 3
* git
* pip

**INSTALATION:**

Clone and install repository:
```
git clone https://github.com/MrGi89/shortener.git
```

Install required depencies:
```
cd ./shortener
pip install -r requirements.txt
```

Create environment file:
```
touch .env
```

Add variables:
```
SECRET_KEY="Your secret key!"
DEBUG=True
```

Make migrations and run server:
```
./manage.py migrate && ./manage.py runserver
```