"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
from app import app, db, filefolder
from flask import render_template, request, redirect, url_for, flash,session, abort, send_from_directory
from forms import LoginForm
from models import UserProfile
from werkzeug.utils import secure_filename
import os
import datetime


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route('/profile', methods=[ "GET" ,"POST"])
def profile ():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        lastname = form.lastname.data
        gender = form.gender.data
        email = form.email.data
        location = form.location.data
        now = datetime.datetime.now()
        firstname = form.firstname.data
        file = form.upload.data
        filename = secure_filename(file.filename)
        biography = form.biography.data
        user = UserProfile(first_name=firstname, last_name=lastname, gender=gender, email=email, location=location, biography=biography, photo_name=filename, date_created=now)
        db.session.add(user)
        db.session.commit()
        file.save(os.path.join(filefolder, filename))
        flash('Successfully added.', 'success')
        return redirect(url_for('profiles')) 
    return render_template("profile.html", form=form)
    
  
@app.route("/profiles")
def profiles():
    users = UserProfile.query.all()
    return render_template('profiles.html', users=users)


@app.route("/profiles/<filename>")
def myprofile(filename):
    user = UserProfile.query.filter_by(id=filename).first()
    return render_template('myprofile.html', user=user)
    
    
@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
    




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
