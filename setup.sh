#!/usr/bin/env sh

# Copy Wallet profiles
cp /wallet/* /usr/lib/oracle/21/client64/lib/network/admin/

export DBNAME='djangodbtest501_high'
export DBUSER='admin'
export DBPASSWORD='Maghiara2019'


# Run migrations and collectstatic
cd /django-rest
/django-rest/env/bin/python manage.py migrate
/django-rest/env/bin/python manage.py collectstatic --noinput
/django-rest/env/bin/python manage.py runserver 0.0.0.0:8000

echo "DONE! :)"