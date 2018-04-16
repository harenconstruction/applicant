# Updating Production #

1. Back up the files and database.
2. Stop the service.
3. git pull on the production branch.
4. Run the db migration - (env) python manage.py migrate
5. (env) python manage.py collectstatic
6. Start the service.
