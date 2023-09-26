# How to run

To run this example, simply paste the following commands on your terminal and
then open a browser on "localhost:8000".

(You'll need Poetry for this)

```
git clone git@github.com:Arlaxia/htmx-playground.git
cd htmx-playground/

poetry install
poetry run python manage.py migrate
poetry run python manage.py runserver
```

# To update styles with Tailwind

Open another tab on your terminal and run the following command:

```
tailwindcss -i ./static/main.css -o ./static/styles.css --minify --watch
```

If this doesn't work, you may need to run in poetry's:

```
poetry env info --path
source /{{ path }}/bin/activate
tailwindcss -i ./static/main.css -o ./static/styles.css --minify --watch
```


Or install Tailwind globally:

```
npm install -g tailwindcss
```