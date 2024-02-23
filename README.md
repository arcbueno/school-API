# school-API
REST API made with Django REST 

<h3>Creating a Django REST API</h3> 

1. Create a virtualenv with
    ```bash
    virtualenv myenv
    ```

2. Activate the virtualenv with
    ```bash
    myenv\Scripts\Activate
    ```

3. Install all needed libraries that you can see in the requirements.txt

4. Create a setup project with
    ```bash
    django-admin startapp setup
    ```

5. Create a new django-rest project with
    ```bash
    python manage.py startapp myproject
    ```

6. Add the rest_framework and myproject in the INSTALLED_APPS list in the setup/settings.py file


<h3>Creating models</h3>

1. Create your entities in the myproject/models.py file

2. Make migrations with the command
    
    ```bash
    python manage.py makemigrations
    ```
3. And commit the migrations with
    
    ```bash
    python manage.py migrate
    ```

<h3>Creating models</h3>

1. Create your entities in the myproject/models.py file

2. Make migrations with the command
    
    ```bash
    python manage.py makemigrations
    ```
3. And commit the migrations with
    
    ```bash
    python manage.py migrate
    ```

<h3> Other settings</h3>

- To create a new superuser (will have access on the /admin page), run

    ```bash
    python manage.py createsuperuser
    ```

- To run, execute the command

    ```bash
    python manage.py runserver
    ```