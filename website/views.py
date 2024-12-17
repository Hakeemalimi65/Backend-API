from flask import Blueprint, request, url_for, redirect, render_template
from .models import Contact
from . import db

views = Blueprint("views",__name__)


@views.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

@views.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
        db.session.add(new_contact)
        db.session.commit()
        return redirect(url_for('views.index'))
    return render_template('create.html')

@views.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    contact = Contact.query.get_or_404(id)
    if request.method == 'POST':
        contact.first_name = request.form['first_name']
        contact.last_name = request.form['last_name']
        contact.email = request.form['email']
        db.session.commit()
        return redirect(url_for('views.index'))
    return render_template('update.html', contact=contact)

@views.route('/delete/<int:id>')
def delete(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('views.index'))
