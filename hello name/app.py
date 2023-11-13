from flask import Flask, render_template,request

app = Flask(__name__)


@app.route("/",methods=["GET","POST"])

def index():
    name = request.args.get('name','world')
    # if "name" in request.args:
    #     name = request.args["name"]
    # else:
    #     name = 'world'
    # return render_template('index.html',pagetitle='Homepage', name = name)
    if request.method == "GET" :
        return render_template('index.html')
    elif request.method == "POST":
        return render_template('greet.html',name=request.form.get("name","world"))


# @app.route('/greet',methods=["POST"])

# def greet():
#     return render_template('greet.html',name=request.args.get('name','word'))





if __name__ == "__main__":

    app.run(debug=True,port=9000)