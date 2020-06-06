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
- <code>blank=True</code> means that it's required on frontend.
- <code>null="False"</code> means that can't be null on database.
- Views are receiving as a first parameter request, and we can see the request including the user by print it <code>print(request.user)</code>

# Parts

- <code>settings.py</code> you add all de new apps
- <code>urls.py</code> it's the router and you have to add here all your new routes.
- Templates helps to split the work with html and make it simple. Yo need to add the root of your folder with templates to <code>settings.py</code>
- Use render to show html, allows you to use templates.

# Html

- Use a dictionary with render is tha way of pass variable to the html and use those with <code>{{var}}</code>
- To loop a list you can use <code>{% for item in my_list %} li {{ item }} li {% endfor %}</code>
- <code>{{ forloop.counter }}</code> allow you to watch the iteration number
- Also is possible to use conditions whit <code>{% if condition %}code{% endif %}</code> or {% else %}
- Built-in filter are a awesome tool to transform variables: <link>https://docs.djangoproject.com/en/3.0/ref/templates/builtins/</link>
- <code>|safe</code> filter render the html code.

# Shell
- Console: <code>python manage.py shell</code>

