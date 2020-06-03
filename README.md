# Link
https://www.youtube.com/watch?v=F5mRW0jo-U4

# Setting up

- Create a virtual environment with <code>python3 -m venv .env</code>
- Set up the environment whit <code>source .env/bin/activate</code>
- Install django whit <code>pip install django==2.0.7</code>
- <code>python manage.py migrate</code> will fix the migrations problems.
- Change your setting on settings.py .
- <code>python manage.py runserver</code> will run the server on local.
- There is a couple of apps already installed, mainly for authentication and security.
- To create a a admin user <code>python manage.py createsuperuser</code>

# Beginning

- Create a new app whit <code>python manage.py startapp</code> .
- Add your app to settings.py
- Make the migration for this app with <code>python manage.py makemigrations</code>
- Migrate the new app with <code>python manage.py migrate</code>
- Go to admin.py and add <code>from .models import Name
  admin.site.register(name)</code>
- And now you can run the server and go to <code>/admin/name</code> to see your work.


# Tips
- With <code>python manage.py shell</code> you can use the shell mode to do everything.
- Adding new objects with <code>name.objects.create(atribute="")</code>
- Show all objects with <code>Product.objects.all()
</code>