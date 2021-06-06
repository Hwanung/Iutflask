import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh je suis pas homosexuel'

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/<int:post_Id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        Id = request.form['Id']
        SepalLengthCm = request.form['SepalLengthCm']
        SepalWidthCm = request.form['SepalWidthCm']
        PetalLengthCm = request.form['PetalLengthCm']
        PetalWidthCm = request.form['PetalWidthCm']
        Species = request.form['Species']

        if not Id:
            flash('id req')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (id, SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species) VALUES (?, ?,?,?,?,?)',
                         (Id, SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(Id):
    post = get_post(Id)

    if request.method == 'POST':
        Id = request.form['Id']
        SepalLengthCm = request.form['SepalLengthCm']
        SepalWidthCm = request.form['SepalWidthCm']
        PetalLengthCm = request.form['PetalLengthCm']
        PetalWidthCm = request.form['PetalWidthCm']
        Species = request.form['Species']

        if not Id:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET SepalLengthCm  = ?, SepalWidthCm = ?,PetalLengthCm = ?,PetalWidthCm = ?,Species = ?    '
                         ' WHERE Id = ?',
                         (Id, SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(Id):
    post = get_post(Id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE Id = ?', (Id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))