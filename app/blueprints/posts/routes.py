'''
from flask import request, flash, redirect, url_for, render_template
from flask_login import current_user
from . import posts
from .forms import CatchForm
from app.models import Post
from app import db

@posts.route('/catch', methods=['GET','POST'])
def catch():
    form = CatchForm()
    if request.method == 'POST' and form.validate_on_submit():

        #This data is coming from the post form in models
        post_data = {
            'img_url': form.img_url.data,
            'name': form.title.data,
            'ability': form.ability.data,
            'base_exp': form.base_exp.data,
            'user_id': current_user.id
        }

        #Create Post Instance
        new_post = Post()

    

        # Set post_data to our Post Attributes
        new_post.from_dict(post_data)

        #Save to Database
        db.session.add(new_post)
        db.session.commit()

        flash('Successfully Caught Pokemon', 'Success')
        return redirect(url_for('main.home'))
    else:
        return render_template('catch.html', form=form)
    
'''

        
