# MySite-v2
Re-implementation of my Toners and Laptops Site.

1. clone
2. run virtualenv env
3. run source env/bin/activate
4. run pip install -r requirements.txt
5. run python3 manage.py migrate
5. run python3 manage.py createsuperuser or
    > python3 manage.py ldap_sync_users
    >python3 manage.py ldap_promote <username>
6. run python3 manage.py runserver.
