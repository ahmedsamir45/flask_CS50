from flask import Flask, render_template,request
import sqlite3 
import os 

currentdirectory = os.path.dirname(os.path.abspath(__file__))

db = sqlite3.connect(currentdirectory+'\APPLICATION.db',check_same_thread=False)

cr = db.cursor()



app = Flask(__name__)


REGISTRANTS ={}

SPORTS = ['Basketball','Soccer','Ultimate Frisbee']


@app.route("/")

def index():
    return render_template('index.html',sports=SPORTS)
   

@app.route('/register', methods=['POST'])

def register():
    

    
    name = request.form.get('name')
    sport = request.form.get('sport')
    if not name or sport not in SPORTS:
        return render_template('failure.html')
        
    my_tuple=(name,sport)
    cr.execute(f"insert into registrants (name,sport) values(?,?);",my_tuple)
    db.commit()
    return render_template('success.html')

        
        
   
   


@app.route('/registrants')
def registrants():
    return render_template('registrants.html',registrants=REGISTRANTS )







if __name__ == "__main__":

    app.run(debug=True,port=9000)

