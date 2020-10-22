from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='zea'
app.config['MYSQL_PASSWORD']='1234'
app.config['MYSQL_DB']='crudapplication'


mysql = MySQL(app)
app.secret_key = "flash message"


from app import routes