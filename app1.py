from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:/FLASK26/todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class ToDo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    ToDo=db.Column(db.String(500),nullable=False)
    description=db.Column(db.String(500),nullable=False)
    status=db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.ToDo}"

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route('/Products')
def products():
    return 'this is products page'

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=8000)
