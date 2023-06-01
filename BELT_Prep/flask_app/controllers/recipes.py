from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User
@app.route('/recipes/new')
def new_party():
    if not 'user_id' in session:
        return redirect('/')
    return render_template("new_recipe.html")
@app.route('/recipes/create',methods=['POST'])
def create_recipe():
    if not 'user_id' in session:
        return redirect('/')
    # print(request.form)
    if(Recipe.validate(request.form)): 
        data={
            **request.form,
            'user_id':session['user_id']
        }
        print(data)
        Recipe.create_recipe(data)
        return redirect('/recipes')
    return redirect('/recipes/new')
@app.route('/recipes/<int:id>')
def one_recipe(id):
    if not 'user_id' in session:
        return redirect('/')
    recipe = Recipe.get_by_id({'id':id})
    return render_template("one_recipe.html",recipe=recipe)
@app.route('/recipes/<int:id>/edit')
def edit_recipe(id):
    if not 'user_id' in session:
        return redirect('/')
    recipe_to_edit = Recipe.get_by_id({'id':id})
    return render_template('edit_recipe.html', recipe=recipe_to_edit)
@app.route('/recipes/<int:id>/update', methods=['POST'])
def update_recipe(id):
    if not 'user_id' in session:
        return redirect('/')
    if(Recipe.validate(request.form)):
        Recipe.update_recipe(request.form)
        print(request.form)
        return redirect('/recipes')
    return redirect(f'/recipes/{id}/edit')
@app.route('/recipes/<int:id>/destroy')
def destroy_recipe(id):
    if not 'user_id' in session:
        return redirect('/')
    Recipe.cancel_recipe({'id': id})
    return redirect('/recipes')