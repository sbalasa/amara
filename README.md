# Amara
Simple Django app demonstrating Ajax


### An AJAX form which creates a record with the following fields:
- Customer Name
- Email Address (must be a valid email address format)
- Subscription Type (with the options: Free, Plus, Pro)
- Displaying the records entered on each submission (it updates without needing to refresh the page).
- Storing the records persistently using a Django model.

### Setup the environment
- `pip3 install -r requirements.txt`

### To Run
- `python3 manage.py makemigrations`
- `python3 manage.py migrate`
- `python3 manage.py runserver 0.0.0.0:8000 --nostatic`
