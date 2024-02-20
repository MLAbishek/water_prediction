import pickle
import os


month_dict = {
    "April": 0,
    "August": 1,
    "December": 2,
    "February": 3,
    "January": 4,
    "July": 5,
    "June": 6,
    "March": 7,
    "May": 8,
    "November": 9,
    "October": 10,
    "September": 11,
}
color_of_water = {
    "Colorless": 0,
    "Faint Yellow": 1,
    "Light Yellow": 2,
    "Near Colorless": 3,
    "Yellow": 4,
}
water_body = {
    "Aquifer": 0,
    "Ground": 1,
    "Lake": 2,
    "Reservoir": 3,
    "River": 4,
    "Spring": 5,
    "Stream": 6,
    "Well": 7,
}


def predict(dataset):
    """send the values in 2d array"""
    """encode the values before sending them"""
    with open("D:\\programming\\coding\\water\\model.pickle", "rb") as f:
        classifier = pickle.load(f)
    ans = classifier.predict(dataset)
    if ans == 1:
        return "drinkable water"
    else:
        return "not drinkable"


"""Gets values from the user."""
# create a pipeline from frontend
ph = float(input("Enter ph:"))
iron = float(input("Enter iron value:"))
nitrate = float(input("Enter nitrate value:"))
chloride = float(input("Enter chloride value:"))
lead = float(input("Enter lead value:"))  # exponents input
zinc = float(input("Enter zinc value:"))
color = input("Enter color of water")  # categorical input
color = color_of_water[color]
turbidity = float(input("Enter turbidity value:"))
fluoride = float(input("Enter fluoride value:"))
copper = float(input("Enter copper value:"))
odor = float(input("Enter odor value:"))
sulphate = float(input("Enter sulphate value:"))
conductivity = float(input("Enter conductivity value:"))
chlorine = float(input("Enter chloride value:"))
manganese = float(input("Enter manganese value:"))
total_dissolved_solids = float(input("Enter total_dissolved_salts value:"))
source = input("Enter source of water:")  # categorical input
source = water_body[source]
water_temperature = float(input("Enter temp of water value:"))
air_temperature = float(input("Enter temp of air value:"))
month = input("Enter month:")  # categorical input
month = month_dict[month]
date = int(input("Enter date:"))  # int
time_of_the_day = int(input("Enter time:"))  # 24 hr format,int,hours only
question = [
    [
        ph,
        iron,
        nitrate,
        chloride,
        lead,
        zinc,
        color,
        turbidity,
        fluoride,
        copper,
        odor,
        sulphate,
        conductivity,
        chlorine,
        manganese,
        total_dissolved_solids,
        source,
        water_temperature,
        air_temperature,
        month,
        date,
        time_of_the_day,
    ]
]
print(predict(question))
