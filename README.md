# SQLite Jadvaldan malumotlarni o`chirish va schotchikni reset qilish
``` 
delete from api_report;    
delete from sqlite_sequence where name='api_report';
```

# EHTIYOT BO'LISH KERAK! Postgresql Jadvaldan malumotlarni o`chirish va schotchikni reset qilish! 

``` 
TRUNCATE public.api_report RESTART IDENTITY;
```

----------------------------------------------
# Loyihani Ubuntu server 20.04 ga o'rnatish
## 1-qadam. Ubuntu omborlaridan barcha bog'liqlik paketlarni o'rnatish
``` 
sudo apt update
sudo apt install python3-venv libpq-dev postgresql postgresql-contrib curl
```
## 2-qadam. PostgreSQL maʼlumotlar bazasini o'rnatish va foydalanuvchi yaratish
``` 
sudo -u postgres psql
CREATE DATABASE ipolisdb;
CREATE USER ipolisuser WITH PASSWORD 'nc778119';

ALTER ROLE ipolisuser SET client_encoding TO 'utf8';
ALTER ROLE ipolisuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE ipolisuser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE ipolisdb TO ipolisuser;
```

## 3-qadam. Github dan loyihani ko'chirib olish va virtualmuhit yaratish
``` 
git clone https://github.com/dohcgle/ipolis.git
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
```

## 4-qadam. requirements.txt o'rnatish va loyihani sozlash
``` 
pip install -r requirements.txt
sudo nano ipolis/settings.py
```
### Postgresql bazasini sozlash
``` 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ipolisdb',
        'USER': 'ipolisuser',
        'PASSWORD': 'nc778119',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

``` 
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py collectstatic
```

# pgAdmin4 o'rnatish
```
sudo curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add
sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
sudo apt install pgadmin4-web
```

### Apache server portni o'zgartirish
``` 
sudo nano /etc/apache2/ports.conf
listen 80 > 8081
sudo systemctl restart apache2
sudo service apache2 restart
```

## pgAdmin4 web serverni sozlash
``` 
sudo /usr/pgadmin4/bin/setup-web.sh
email: utn1002@gmail.com
pass: nc778119
```

# Postgresql bazasiga dostup berish.

``` 
sudo nano /etc/postgresql/12/main/pg_hba.conf
```
### Quyidagini qo'shish kk:
``` 
host     all            all             0.0.0.0/0               md5
```
----------------------------------------------------------------------------
``` 
sudo nano /etc/postgresql/12/main/postgresql.conf  
```
### Quyidagini qo'shish kk:
``` 
listen_addresses = '*'
```

### Docker containerga kirish:
``` 
sudo docker exec -it <container_id> /bin/sh
```


### Create user Payme
```
python manage.py create_paycom_user 
```# ipolis
