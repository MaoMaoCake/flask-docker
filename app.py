from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://postgres:postgres@postgres:5432/name"

class Item(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '{0}, age {1}'.format(self.name,self.age)

@app.route('/')
def root():
    # this should get a list of all the info on the app
    data = Item.query.all()
    return render_template("index.html",data=data)

@app.route('/data', methods=["POST","DELETE"])
def data():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form.get("age")
        print(name,age)
        db.session.add(Item(name=name, age=age))
        db.session.commit()
        return redirect('/')

if __name__ == '__main__':
    app.run()
