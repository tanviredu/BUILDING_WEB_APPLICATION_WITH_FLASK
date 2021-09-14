#import
from flask import Flask,render_template,abort,jsonify,request,redirect,url_for
from flask.wrappers import Request
from model import db,save_db
app = Flask(__name__)


@app.route("/")
def welcome():
    ''' Returning the card list in the welcome page'''
    #return render_template("welcome.html",message="Flask is the easiest framework")
    return render_template("welcome.html",cards=db)
@app.route("/card/<int:index>")
def card_view(index):
    try:
        max_index = len(db)-1 ## find the length of the json object
        card = db[index]
        return render_template("card.html",card=card,index=index,max_index=max_index)
    except IndexError:
        abort(404)




##api
@app.route("/api/card/")
def api_card_list():
    return jsonify(db)    ## you must pass a dict not a list

@app.route("/add_card",methods=["GET","POST"])
def add_card():
    if request.method == "POST":
        ## getting post value
        question = request.form["question"]
        answer = request.form["answer"]
        card = {"question":question,"answer":answer}
        db.append(card)
        save_db() ## make the change permanent
        ## we redirect the user to the card that
        ## user made 
        ## so card_view and send it the 
        ## last index since it is the 
        ## last item of the list
        return redirect(url_for('card_view',index=len(db)-1))

    else:
        return render_template("add_card.html")

@app.route("/remove_card/<int:index>",methods=["GET","POST"])
def remove_card(index):
    try:
        if request.method == "POST":
            del db[index]
            save_db()
            return redirect(url_for("welcome"))
        else:
            return render_template("remove_card.html",card=db[index])
    except IndexError:
        abort(404)



@app.route("/api/card/<int:index>")
def api_card_detail(index):
    try:
        return db[index]
    except:
        abort(404)



## run application with this command
#1)set FLASK_APP=app.py
#2)set FLASK_ENV=development
#3)flask run

