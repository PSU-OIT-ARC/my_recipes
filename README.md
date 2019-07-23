# My Recipes

Demo application showing use of Django as backend and Vue/Nuxt.js as frontend.

Reference: https://scotch.io/tutorials/building-a-universal-application-with-nuxtjs-and-django

The Django backend is located in the `api/` directory.

The Vue/Nuxt frontend is located in the `client/` directory.

## Quick Start

### Create a Python Virtual Environment

Install the packages in `requirements.txt`

```sh
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Run the Django migrations

```sh
cd api
python manage.py migrate
```

### Run the app

1.  Start the Django app
    ```sh
    cd api
    python manage.py runserver
    ```

2.  Start the Vue app

    In a new Terminal:
    ```sh
    cd client
    npm run dev
    ```

3.  Open the app in a browser: `http://localhost:3000`