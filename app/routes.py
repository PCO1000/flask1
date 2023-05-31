from flask import request, render_template, redirect, url_for, flash
import requests
from app import app
from app.forms import PokeForm, LoginForm, SignUpForm


@app.route("/")
@app.route('/home')
def home():
     return render_template('home.html')

REGISTERED_USERS = {
    'hosan@gmail.com': {
        'name': 'Hosan',
        'password': 'pokemaster'
    }
}

@app.route('/login', methods = ['GET', 'POST'])
def login():
     form = LoginForm()
     if request.method == 'POST' and form.validate_on_submit():
          email = form.email.data.lower()
          password = form.password.data
          if email in REGISTERED_USERS and password == REGISTERED_USERS[email]['password']:
               flash(f'Welcome back{REGISTERED_USERS[email]["name"]}!', 'success')
               return redirect(url_for('home'))
          else:
               error = 'Invalid email or Password'
               return render_template('login.html', form=form, error=error)
          #return '<h1>Logged In</h1>'
     else:
          print('Not Validated')
          return render_template('login.html', form=form)
     
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.first_name.data + ' ' + form.last_name.data
        email = form.email.data.lower()
        password = form.password.data
        REGISTERED_USERS[email] = {
             'name': name,
             'password': password
        }
        print(REGISTERED_USERS)
        return 'Thank you for Signing Up!'
    else:
        return render_template('signup.html', form=form)



#@app.route('/home/<username>')
#def home(username):
    #return f'Hello {username}, welcome back!'

@app.route('/poke', methods=['GET', 'POST'])
def poke():
    form = PokeForm()
    if request.method =='POST' and form.validate_on_submit():
        pok_name = form.pokemon_name.data
        #pok_name = request.form.get('pok_name')
      
        url = f'https://pokeapi.co/api/v2/pokemon/{pok_name}'
        response = requests.get(url)
        if response.status_code == 200:
            poke_data = response.json()
            my_pokedata = {
                'pk_name': poke_data['forms'][0]['name'], 
                'pk_ability': poke_data['abilities'][0]['ability']['name'],
                'pk_base_exp': poke_data['base_experience'],
                'pk_sprite_url': poke_data['sprites']['front_shiny']
            }
            return my_pokedata
        else:
                'That Pokemon does not exist.'
    return render_template('pokemon.html', form=form)