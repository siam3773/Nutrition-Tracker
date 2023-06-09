import requests
import json
import mysql.connector

listOfFoods = ['4025', '4053', '8120', '9016', '9037', '9040', '9148', '9150', '9159', '9176', '9200', '9226', '9236', '9266', '9442', '10123', '11168', '11206', '11216', '11252', '11282', '11297', '11422', '11979', '12104', '14136', '14400', '15164', '16069', '17224', '18064', '19081', '20444', '1009054', '1017063', '10020444', '10211821']

db = mysql.connector.connect(

    host="PsyDuck3773.mysql.pythonanywhere-services.com",
    user="PsyDuck3773",
    password="siam0001",
    database="PsyDuck3773$Nutrition_Tracker"

)
listOfNutrients=[]
for id in listOfFoods:
    u = f"https://api.spoonacular.com/food/ingredients/{id}/information?apiKey=43585d37781e4241b34151b42eaa6cfd&includeNutrition=true&amount=100&unit=%22gm%22"
    response = requests.get(url=u)

    data = response.json()

    i = 0
    product = {}

    product["name"] = data["name"]
    for k in data["nutrition"]["nutrients"]:
        product[data["nutrition"]["nutrients"][i]["name"]] = float(data["nutrition"]["nutrients"][i]["amount"])

        i += 1

    query = "CREATE TABLE IF NOT EXISTS FoodsNew (Id INT PRIMARY KEY DEFAULT 0, name VARCHAR(200) DEFAULT '0', Choline FLOAT DEFAULT 0, Magnesium FLOAT DEFAULT 0, Vitamin_B1 FLOAT DEFAULT 0, Vitamin_B6 FLOAT DEFAULT 0, Calories FLOAT DEFAULT 0, Poly_Unsaturated_Fat FLOAT DEFAULT 0, Sodium FLOAT DEFAULT 0, Potassium FLOAT DEFAULT 0, Protein FLOAT DEFAULT 0, Vitamin_K FLOAT DEFAULT 0, Folate FLOAT DEFAULT 0, Fiber FLOAT DEFAULT 0, Zinc FLOAT DEFAULT 0, Vitamin_B2 FLOAT DEFAULT 0, Copper FLOAT DEFAULT 0, Vitamin_E FLOAT DEFAULT 0, Vitamin_D FLOAT DEFAULT 0, Phosphorus FLOAT DEFAULT 0, Saturated_Fat FLOAT DEFAULT 0, Vitamin_A FLOAT DEFAULT 0, Folic_Acid FLOAT DEFAULT 0, Lycopene FLOAT DEFAULT 0, Cholesterol FLOAT DEFAULT 0, Caffeine FLOAT DEFAULT 0, Vitamin_C FLOAT DEFAULT 0, Vitamin_B3 FLOAT DEFAULT 0, Carbohydrates FLOAT DEFAULT 0, Selenium FLOAT DEFAULT 0, Iron FLOAT DEFAULT 0, Vitamin_B5 FLOAT DEFAULT 0, Sugar FLOAT DEFAULT 0, Net_Carbohydrates FLOAT DEFAULT 0, Mono_Unsaturated_Fat FLOAT DEFAULT 0, Alcohol FLOAT DEFAULT 0, Vitamin_B12 FLOAT DEFAULT 0, Fat FLOAT DEFAULT 0, Manganese FLOAT DEFAULT 0)"


    mycursor = db.cursor()


    mycursor.execute(query)
    db.commit()
    print("ok1")
    print(id)
    query = "insert into FoodsNew(Id, name, Choline, Magnesium, Vitamin_B1, Vitamin_B6, Calories, Poly_Unsaturated_Fat, Sodium, Potassium,Protein, Vitamin_K, Folate, Fiber, Zinc, Vitamin_B2, Copper, Vitamin_E, Vitamin_D, Phosphorus, Saturated_Fat, Vitamin_A, Folic_Acid, Lycopene, Cholesterol, Caffeine, Vitamin_C, Vitamin_B3, Carbohydrates, Selenium, Iron, Vitamin_B5, Sugar, Net_Carbohydrates, Mono_Unsaturated_Fat, Alcohol, Vitamin_B12, Fat, Manganese) values({}, '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {},{},{})".format(
        id, product["name"], product["Choline"], product["Magnesium"], product["Vitamin B1"], product["Vitamin B6"],
        product["Calories"], product["Poly Unsaturated Fat"], product["Sodium"], product["Potassium"],
        product["Protein"], product["Vitamin K"], product["Folate"], product["Fiber"], product["Zinc"],
        product["Vitamin B2"], product["Copper"], product["Vitamin E"], product["Vitamin D"], product["Phosphorus"],
        product["Saturated Fat"], product["Vitamin A"], product["Folic Acid"], product["Lycopene"],
        product["Cholesterol"], product["Caffeine"], product["Vitamin C"], product["Vitamin B3"],
        product["Carbohydrates"], product["Selenium"], product["Iron"], product["Vitamin B5"], product["Sugar"],
        product["Net Carbohydrates"], product["Mono Unsaturated Fat"], product["Alcohol"], product["Vitamin B12"],
        product["Fat"], product["Manganese"])

    print(query)
    product.clear()
    mycursor.execute(query)
    db.commit()
