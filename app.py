from  flask import Flask,render_template,redirect,request
from database import*
from dump import*
from nam import*
from emm import*
app = Flask(__name__)
db =dbo()
@app.route('/')
def fun():

    return render_template('index.html')
@app.route("/login")
def login():
    return render_template('login.html')
@app.route('/signup')
def signup():
    return render_template('register.html')
@app.route("/store",methods=['post'])
def get():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    res=db.insert(name,email,password)
    if res:
        return render_template('login.html',message="Regstration successfull kindly login")
    else:
        return render_template('register.html',message="Register with another email")
@app.route('/logcheck',methods=['post'])
def check():
    email = request.form.get("email")
    password = request.form.get("password")
    res=ser(email,password)
    name=serr(email)
    if res:
        emai(email, name)
        return render_template("index2.html")

    else:
        return render_template("login.html",message="kindly enter correct details")
@app.route('/adven',methods=['post'])
def adv():
    ad = request.form.get("adv")
    print(ad)
    if(ad=="Adventure"):
        return  render_template("adventure.html")
    elif(ad=="Hill station"):
        return render_template("hill_station.html")
    elif(ad=="Beaches"):
        return render_template("beaches.html")
    elif(ad=="Cultural and History"):
        return render_template("cultural.html")
    elif (ad=="Forts"):
        return render_template("forts.html")
    elif (ad=="Museum"):
        return render_template("museum.html")
    elif(ad=="Theme parks"):
        return render_template("theme_parks.html")

app.run(debug=True)
