## Installation 

Creating a virtual environment

``` 
$ python3 -m venv env 
$ source env/bin/activate
``` 
clone the repo to local machine

```
$ git clone https://github.com/Maheshoo7/activityPeriodApi.git

$ cd activityPeriodApi/
```
Install the required packages

```
$ pip install -r requirements.txt
```

I have used postgresql, so you might have to setup postgresql or you can change it to default database in settings.py

Migrate the database

```
$ python manage.py makemigrations
$ python manage.py migrate
```
Runserver

```
$ python manage.py runserver
```
open the link http://127.0.0.1:8000/user/ to see the result

To add data copy the below Json data and paste in the input area, or can also be added using Postman

```
{
    "real_name": "The Red Album",
    "tz": "Asia/Dubai",
    "activity_periods" : [
        {"start_time": "2020-06-21T13:30:42.744148Z", "end_time": "2020-06-21T13:30:42.744191Z"},
        {"start_time": "2020-06-21T13:30:42.754148Z", "end_time": "2020-06-21T13:30:42.774191Z"},
        {"start_time": "2020-06-21T13:30:42.764148Z", "end_time": "2020-06-21T13:30:42.784191Z"}
    ]
}
```
