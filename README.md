# gdrive_to_commons
Google drive to commons

# Steps:
1. Create virtual env (based on python 3.7.1). 
2. `pip install -r requirements.txt`. 
2. Install pre-commit using https://pre-commit.com/
3. Run `pre-commit install`.
4. `python manage.py migrate` 
5. `python manage.py collectstatic`. 
3. `python manage.py runserver` (or run it from pycharm).
