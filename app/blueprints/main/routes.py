from flask import request, render_template
import requests
from app.blueprints.auth.forms import PokeForm
from . import main
from werkzeug.security import check_password_hash
from flask_login import login_required

@main.route("/")
@main.route('/home')
def home():
     return render_template('home.html')

#@main.route('/home/<username>')
#def home(username):
    #return f'Hello {username}, welcome back!'

@main.route('/poke', methods=['GET', 'POST'])
@login_required
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
            return render_template('pokemon.html', form=form, my_pokedata=my_pokedata)
        else:
                'That Pokemon does not exist.'
    return render_template('pokemon.html', form=form)



