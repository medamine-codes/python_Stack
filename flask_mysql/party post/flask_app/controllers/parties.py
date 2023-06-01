from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.party import Party
from flask_app.models.user import User
@app.route('/parties/new')
def new_party():
    if not 'user_id' in session:
        return redirect('/')
    return render_template("new_party.html")
@app.route('/parties/create',methods=['POST'])
def create_party():
    if not 'user_id' in session:
        return redirect('/')
    # print(request.form)
    if(Party.validate(request.form)): 
        data={
            **request.form,
            'user_id':session['user_id']
        }
        print(data)
        Party.create_party(data)
        return redirect('/dashboard')
    return redirect('/parties/new')
@app.route('/parties/<int:id>')
def one_party(id):
    if not 'user_id' in session:
        return redirect('/')
    party = Party.get_by_id({'id':id})
    return render_template("one_party.html",party=party)
@app.route('/parties/<int:id>/edit')
def edit_party(id):
    if not 'user_id' in session:
        return redirect('/')
    party_to_edit = Party.get_by_id({'id':id})
    return render_template('edit_party.html', party=party_to_edit)
@app.route('/parties/<int:id>/update', methods=['POST'])
def update_party(id):
    if not 'user_id' in session:
        return redirect('/')
    if(Party.validate(request.form)):
        Party.update_party(request.form)
        print(request.form)
        return redirect('/dashboard')
    return redirect(f'/parties/{id}/edit')
@app.route('/parties/<int:id>/destroy')
def destroy_party(id):
    if not 'user_id' in session:
        return redirect('/')
    Party.cancel_party({'id':id})
    return redirect('/dashboard')