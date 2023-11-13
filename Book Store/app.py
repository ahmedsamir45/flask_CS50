from flask import Flask, render_template,request,session,redirect
from flask_session import Session 
import sqlite3 
import os 




app = Flask(__name__)




currentdirectory = os.path.dirname(os.path.abspath(__file__))

db = sqlite3.connect(currentdirectory+'\store.db',check_same_thread=False)


cr = db.cursor()



app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)





@app.route("/")

def index():
    books1 = db.execute('SELECT * FROM books')
    books2=books1.fetchall()
    return render_template('books.html',books=books2)



@app.route( "/cart", methods=["GET","POST"])

def cart():

    # Ensure cart exists

    if "cart" not in session:
        session["cart"]=[]

    # POST

    if request.method == "POST":
        id = int(request.form.get('id'))
        if id:
            session['cart'].append(id)
        return redirect('/cart')

    x=[]
    for value in  session['cart']:
        x.append(value)
    mytuple = tuple(x)
    print(mytuple)
    
    books = cr.execute(f"SELECT * FROM books WHERE id in {mytuple}")
    books3=books.fetchall()
    return render_template("cart.html",books=books3 )



if __name__ == "__main__":

    app.run(debug=True,port=9000)
    