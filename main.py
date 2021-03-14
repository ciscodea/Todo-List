from flask import (
    request,
    session,
    make_response,
    redirect,
    render_template,
    url_for,
    flash
)
from app.firestore_service import get_users, get_todos, set_todo, delete_todo,update_todo
import unittest
from app import create_app
from app.forms import LoginForm, TodoForm, DeletTodoForm, UpdateTodoForm
from flask_login import login_required, current_user


app = create_app()


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    response = make_response(redirect('/home'))

    return response

@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    user_ip = session.get('user_ip')
    username = current_user.id

    todo_form = TodoForm()
    delete_form = DeletTodoForm()
    update_form = UpdateTodoForm()

    context = {
        'user_ip': user_ip,
        'todos': get_todos(user_id=username),
        'username': username,
        'todo_form':todo_form,
        'delete_form': delete_form,
        'update_form': update_form,
    }

    if todo_form.validate_on_submit():
        set_todo(user_id=username, description=todo_form.description.data)
        flash('Tu tarea se creo con éxito')

        return redirect(url_for('home'))
    return render_template('home.html', **context)


@app.route('/todos/delete/<todo_id>', methods=['POST', 'GET'])
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id=user_id, todo_id=todo_id)

    return redirect(url_for('home'))


@app.route('/todos/update/<todo_id>/<int:done>', methods=['POST', 'GET'])
def update(todo_id, done):
    user_id = current_user.id
    update_todo(user_id=user_id, todo_id=todo_id, done=done)
    
    return redirect(url_for('home'))