# ActivityPeriod-models
Design and implementation of a Django application with User and ActivityPeriod models and write
a custom management command to populate the database with some dummy data , and design an API to serve that data in the json format.

<br>

# Django App deployed at : 
http://dishvyas.pythonanywhere.com/



# Setup and Installation
##  Setup Virtual environment Pyhton3


- clone Repositry
    <pre><code> git clone https://github.com/dishvyas/User-PeriodActivity-Model-using-Django.git</pre></code>


- install virtualenv if not installed
    <pre><code> pip install virtualenv </pre></code> 

- Create virtual environment for Python 3 and activate
    <pre><code>virtualenv venv -p python3 </pre></code> 
    <pre><code>source venv/bin/activate</pre></code>

- Install all the packages
    <pre><code>pip install -r requirements.txt</pre></code>
   

- Migrate
    <pre><code>python manage.py migrate</code></pre>
    
- Custom management command 
    <pre><code>python manage.py create_dummy_users number</code></pre>   
 
- Run Server
    <pre><code>python manage.py runserver</code></pre>

