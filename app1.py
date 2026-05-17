from flask import Flask, render_template ,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:/FLASK26/ToDo/todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class ToDo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(500),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    status=db.Column(db.String(500),default="Pending")
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/',methods=["GET","POST"])
def home_page():
    if request.method=="POST":
        title=request.form['title']
        desc=request.form['desc']
        todo=ToDo(title=title,desc=desc,status='pending')
        db.session.add(todo)
        db.session.commit()
    alltodo=ToDo.query.all()
    return render_template("index.html",alltodo=alltodo)
    
@app.route('/update')

@app.route('/delete/<int:sno>')
def delete(sno):
    deltodo=ToDo.query.filter_by(sno=sno).first()
    db.session.delete(deltodo)
    db.session.commit()
    return redirect('/')

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=8000)
  
