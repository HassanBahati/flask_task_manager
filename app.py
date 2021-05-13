#imports 
from flask import Flask , render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

#configurations 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# model for the content 
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200),nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
#function returning a string everytime a new entry is created
    def __repr__(self):
        return '<Task %r>' %self.id

# route 
@app.route('/', methods=['POST', 'GET'])
def index():
    # if the request is a post, submit form else return form 
    if request.method == 'POST':
        #logic for adding a task
        task_content = request.form['content']
        #todo object (model for contennt task)
        new_task = Todo(content=task_content)

        #logic for adding new todo to db
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue saving data to db'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)  