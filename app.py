from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/home/<username>')
def home(username):
    return f'Hello {username}, welcome back!'

@app.route('/poke', methods=['GET', 'POST'])
def poke():
    if request.method =='POST':
        pok_name = request.form.get('pok_name')
      
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
    return render_template('forms.html')