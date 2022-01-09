# django-polls

App allows visitors to vote on custom web polls. You can create questions, choices and choose a specific publish date for each poll.


## General Info
* Developed with Python 3.8.10
* Django v4.0
* DB Adapter SQLite: does not require additional services

## Recommendation
To avoid any compatibilites issues, you can use ```virtualenv``` to run the project and install dependencies. Read more on https://docs.python.org/3.8/library/venv.html

## Quick start

1. Clone the project and navigate to directory with ```cd django-polls```

2. Install dependencies running ```pip install -r requirements.txt```

3. Run ```python manage.py migrate``` to create the polls models.

4. Run ```python manage.py createsuperuser``` to create a admin superuser.

5. Start the development server running ```python manage.py runserver``` and visit http://127.0.0.1:8000/admin/polls/question/add/ to create a poll.

6. Visit http://127.0.0.1:8000/polls/ to vote.
