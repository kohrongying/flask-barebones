# Flask Barebones
Just a template for flask, login and registration funcionality included. Best used with Linux OS.
- Bootstrap 4 CDN used
- Blueprints, alembic migration incorporated
- Does not include testing

### Install all required things
- pip: `sudo apt-get install python-pip`
- virtual environment `sudo pip install virtualenv`
- autoenv `pip install autoenv`

### Clone this repo and cd inside 
```
virtualenv venv
cd .. 
echo "source `which activate.sh`" >> ~/.bashrc
cd project_name
```
### Get all required packages
```
pip install -r requirements.txt
```

### Create database
- install postgres `sudo apt-get install postgresql postgresql-contrib`
- if there's issue with psycopg2: `sudo apt install libpg-dev python3-dev`
- create user and database 
```
sudo -i -u postgres
createuser --interative
createdb rongying

psql 
rongying#/ create database flaskbarebones;
# CREATE DATABASE
rongying#/ \c flaskbarebones
\q
```
After that, export database URL to os. Export config settings too.
```
export APP_SETTINGS='config.DevelopmentConfig'
export DATABASE_URL='postgresql:///flaskbarebones'
```

### Alembic Migration
- init will create migrations folder
- migrate after models in models.py are created, this will create a migrations file
- upgrade will apply changes to your db 

```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```
To check on relations created
```
psql
\c flaskbarebones
\dt
\d user
select * from user;
\q 
```

### Run Flask
At root of project folder
```
python run.py
```

### Credits
These great tutorials: [here](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) and [here](https://realpython.com/blog/python/flask-by-example-part-1-project-setup/)