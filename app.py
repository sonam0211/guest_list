from flask import Flask, redirect, url_for, request , render_template
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from sqlalchemy.sql import exists
from sqlalchemy import or_    
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///experi8.sqlite3'

db = SQLAlchemy(app)

class experi8(db.Model):
   id = db.Column('guest_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   last  = db.Column(db.String(50))
   place = db.Column(db.String(200)) 
   phone = db.Column(db.Integer) 

   def __init__(self, name, last , place , phone):
      self.name = name
      self.last = last
      self.place = place
      self.phone = phone
      


@app.route('/')
def success():
   return render_template('e6home.html')

@app.route('/guest')
def guest():
   return render_template('e6guest.html')   


@app.route('/addrec', methods = ['GET', 'POST'])
def addrec():
   if request.method == 'POST':
     if  db.session.query(experi8).filter_by(phone = request.form['phone']).first():
         exists = True
         return 'You Already Have This Guest In Your List'
     else:
         exists = False
         
         if request.form['name'] and request.form['last'] and request.form['place'] and request.form['phone']:
          experis8 = experi8(request.form['name'], request.form['last'],
            request.form['place'], request.form['phone'])

         
      
       
         
          db.session.add(experis8)
          db.session.commit()
     return render_template('e6more.html')    
       



@app.route('/see')
def see():
   return render_template('e6see.html' ,experi8 = experi8.query.all())


if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)  