from flask import render_template, redirect, request, url_for, flash
from app import app, mysql

@app.route('/')
def Index():

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()
    return render_template('home.html', students = data)



@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        flash("Data Added Successfully!")
        idnum = request.form['idnum']
        name = request.form['name']
        email = request.form['email']
        yrlvl = request.form['yrlvl']
        course = request.form['course']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (idnum, name, email, yrlvl, course) VALUES (%s,%s,%s,%s,%s)", (idnum, name, email, yrlvl, course))
        mysql.connection.commit()
        return redirect(url_for('Index'))


@app.route('/update/<id>', methods = ['POST'])
def update(id):
    if request.method == 'POST':
        idnum = request.form['idnum']
        name = request.form['name']
        email = request.form['email']
        yrlvl = request.form['yrlvl']
        course = request.form['course']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE students SET idnum=%s, name=%s, email=%s, yrlvl=%s, course=%s WHERE id = %s", (idnum, name, email, yrlvl, course, id))
        mysql.connection.commit()
        flash("Data Updated Successfully!")
        return redirect(url_for('Index'))

    else:
        return render_template('edit.html')

@app.route('/delete/<id>', methods = ['POST','GET'])
def delete(id):
    flash("Data Deleted Successfully!")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id = %s", [id])
    mysql.connection.commit()
    return redirect(url_for('Index'))

