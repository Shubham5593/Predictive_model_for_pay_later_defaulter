import pickle 
import json 
import numpy as np
import os

class CreditCardDefaultPrediction():
    def __init__(self,limit_bal,sex,education,marriage,age,pay_1,pay_2,pay_3,pay_4,pay_5,pay_6,
                 bill_amt1,bill_amt2,bill_amt3,bill_amt4,bill_amt5,bill_amt6,pay_amt1,
                 pay_amt2,pay_amt3,pay_amt4,pay_amt5,pay_amt6):
                 
                 self.limit_bal=limit_bal
                 self.sex=sex
                 self.education=education
                 self.marriage=marriage
                 self.age=age
                 self.pay_1 = pay_1
                 self.pay_2 = pay_2
                 self.pay_3 = pay_3
                 self.pay_4 = pay_4
                 self.pay_5 = pay_5
                 self.pay_6 = pay_6
                 self.bill_amt1 = bill_amt1
                 self.bill_amt2 = bill_amt2
                 self.bill_amt3 = bill_amt3
                 self.bill_amt4 = bill_amt4
                 self.bill_amt5 = bill_amt5
                 self.bill_amt6 = bill_amt6
                 self.pay_amt1 = pay_amt1
                 self.pay_amt2 = pay_amt2
                 self.pay_amt3 = pay_amt3
                 self.pay_amt4 = pay_amt4
                 self.pay_amt5 = pay_amt5
                 self.pay_amt6 = pay_amt6

    def load_model(self):
        with open("xgb_model.pkl","rb") as f:
            self.model = pickle.load(f)

        with open("columns_data.json","r") as f:
            self.columns_data = json.load(f)

    def get_predict(self):

        self.load_model()

        test_array = np.zeros(len(self.columns_data["columns"]))

        test_array[0] = self.limit_bal
        test_array[1] = self.columns_data["SEX"][self.sex]
        test_array[2] = self.columns_data["EDUCATION"][self.education]
        test_array[3] = self.columns_data["MARRIAGE"][self.marriage]

        test_array[4] = self.age

        test_array[5] = self.columns_data["PAY"][self.pay_1]
        test_array[6] = self.columns_data["PAY"][self.pay_2]
        test_array[7] = self.columns_data["PAY"][self.pay_3]
        test_array[8] = self.columns_data["PAY"][self.pay_4]
        test_array[9] = self.columns_data["PAY"][self.pay_5]
        test_array[10] = self.columns_data["PAY"][self.pay_6]

        test_array[11] = self.bill_amt1
        test_array[12] = self.bill_amt2
        test_array[13] = self.bill_amt3
        test_array[14] = self.bill_amt4
        test_array[15] = self.bill_amt5
        test_array[16] = self.bill_amt6

        test_array[17] = self.pay_amt1
        test_array[18] = self.pay_amt1
        test_array[19] = self.pay_amt1
        test_array[20] = self.pay_amt1
        test_array[21] = self.pay_amt1
        test_array[22] = self.pay_amt1

        predict_defaulters = self.model.predict([test_array],validate_features=False)

        return predict_defaulters[0]


# obj = CreditCardDefaultPrediction(100177.948900,"male","University Graduate","single",26,
#             "Use of revolving credit", "Use of revolving credit", "Use of revolving credit",
#             "Use of revolving credit", "Use of revolving credit","payment delay for one month",
#              53268.433585,39104.790676,40026.678964,40557.147511,43552.090485,41398.759145,
#              1960.580259,1953.925334,1509.004214,3687.650346,53.562619,1705.569801)
             
# print(obj.get_predict())

