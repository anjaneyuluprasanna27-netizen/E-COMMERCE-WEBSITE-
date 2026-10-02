# E-COMMERCE-WEBSITE-
An e-commerce website is a digital store on the internet where people can buy and sell physical goods, digital products, or service
Wax & Groove separated files

Source: uploaded Wax & Groove documentation.

IMPORTANT:
- The source document is documentation/snippets, not a complete Django project.
- Django is not installed in the current runtime, so a live Django server cannot be started here.
- The source references cart_update, cart_remove and cart_state in urls.py but does not provide their function implementations. Those routes are therefore commented in the separated urls.py rather than inventing code.
- The JavaScript references CSRF_TOKEN, ENDPOINTS.add, ENDPOINTS.checkout, renderCart and showToast; those definitions are also not included in the source document.

To run a completed Django project locally:
1. Install Django and a MySQL driver.
2. Create waxgroove_db in MySQL using schema.sql or Django migrations.
3. Put the DATABASES settings into waxgroove/settings.py and set your MySQL password.
4. Configure INSTALLED_APPS, TEMPLATES, STATIC files, middleware, root URLs, and manage.py.
5. Run: python manage.py makemigrations
6. Run: python manage.py migrate
7. Run: python manage.py runserver

Separated source files:
store/models.py
store/views.py
store/urls.py
store/templates/store/index.html
store/static/store/style.css
store/static/store/app.js
waxgroove/settings_snippet.py
schema.sql
