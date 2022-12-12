from flask import Flask,render_template,request,jsonify
import numpy as np
import config
from utils import CreditCardDefaultPrediction
from flask_mysqldb import MySQL


app = Flask(__name__)

############################## MYSQL CONFIGURATION STEP####################
# app.config["MYSQL_HOST"] = "localhost"
# app.config["MYSQL_USER"] = "root"
# app.config["MYSQL_PASSWORD"] = "Shubham0306"
# app.config["MYSQL_DB"] = "db_default_credit_card_prediction"
# mysql = MySQL(app)


@app.route("/")

def home():
    return render_template("index.html")

@app.route("/predict_defaulters",methods = ["GET","POST"])

def get_predict():
    data = request.form 

    limit_bal = data["limit_bal"]
    sex = data["sex"]
    education = data["education"]
    marriage = data["marriage"]
    age = eval(data["age"])
    pay_1 = data["pay_1"]
    pay_2 = data["pay_2"]
    pay_3 = data["pay_3"]
    pay_4 = data["pay_4"]
    pay_5 = data["pay_5"]
    pay_6 = data["pay_6"]
    bill_amt1 = eval(data["bill_amt1"])
    bill_amt2 = eval(data["bill_amt2"])
    bill_amt3 = eval(data["bill_amt3"])
    bill_amt4 = eval(data["bill_amt4"])
    bill_amt5 = eval(data["bill_amt5"])
    bill_amt6 = eval(data["bill_amt6"])
    pay_amt1 = eval(data["pay_amt1"])
    pay_amt2 = eval(data["pay_amt2"])
    pay_amt3 = eval(data["pay_amt3"])
    pay_amt4 = eval(data["pay_amt4"])
    pay_amt5 = eval(data["pay_amt5"])
    pay_amt6 = eval(data["pay_amt6"])

    obj = CreditCardDefaultPrediction(limit_bal,sex,education,marriage,age,pay_1,pay_2,pay_3,pay_4,pay_5,pay_6,
                                     bill_amt1,bill_amt2,bill_amt3,bill_amt4,bill_amt5,bill_amt6,
                                     pay_amt1,pay_amt2,pay_amt3,pay_amt4,pay_amt5,pay_amt6)

    r = obj.get_predict()

#### Adding Values Into Database ####

    # cursor = mysql.connection.cursor()
    # querry = "CREATE TABLE IF NOT EXISTS defaulter_prediction(limit_bal varchar(255),sex varchar(255),education varchar(255),marriage varchar(255),age varchar(255),
    #                                                          pay_1 varchar(255),pay_2 varchar(255),pay_3 varchar(255),pay_4 varchar(255),pay_5 varchar(255),pay_6 varchar(255),
    #                                                          bill_amt1 varchar(255),bill_amt2 varchar(255),bill_amt3 varchar(255),bill_amt4 varchar(255),bill_amt5 varchar(255),bill_amt6 varchar(255),
    #                                                          pay_amt1 varchar(255),pay_amt2 varchar(255),pay_amt3 varchar(255),pay_amt4 varchar(255),pay_amt5 varchar(255),pay_amt6 varchar(255),default varchar(5))"
    # cursor.execute(querry)
    # cursor.execute("INSERT INTO defaulter_prediction(limit_bal,sex,education,marriage,age,pay_1,pay_2,pay_3,pay_4,pay_5,pay_6,bill_amt1,bill_amt2,bill_amt3,bill_amt4,bill_amt5,bill_amt6,pay_amt1,pay_amt2,pay_amt3,pay_amt4,pay_amt5,pay_amt6,default) VALUES 
    #                                                 (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
    #                                                 (limit_bal,sex,education,marriage,age,pay_1,pay_2,pay_3,pay_4,pay_5,pay_6,bill_amt1,bill_amt2,bill_amt3,bill_amt4,bill_amt5,bill_amt6,pay_amt1,pay_amt2,pay_amt3,pay_amt4,pay_amt5,pay_amt6,r))
    
    # mysql.connection.commit()
    # cursor.close()

    if r == 1:
        result = "Customer will not pay next month bill (defaulter)"
    else :
        result = "Customer will pay their bill duly (No defaulter)"

    return render_template("index1.html",r=result)

# jsonify({"Result":f"Prediction is {result}"}) >> For API check

if __name__ == "__main__":
    app.run()