# this snippet is for if excercise

print("Please Enter your height")

height = input()

print("Please Enter your weight")

weight = input()

print("your BMI is {}".format(float(weight) / (float(height) * float(height))))

BMI = float(weight) / (float(height) * float(height))

if BMI >= 30:
    print("My Friend you are obese")
elif 25 < BMI < 30:
    print("My Friend you are Overweight")
elif 18.5 < BMI < 25:
    print("My Friend you are Overweight")
else:
    print("You are underweight")

# next exercise

India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York", "Chicago", "Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]

city1 = input()

city2 = input()

if city1 in India and city2 in India:
    print("Both cities are in India")
elif city1 in USA and city2 in USA:
    print("Both cities are in USA")
elif city1 in UK and city2 in UK:
    print("Both cities are in UK")
else:
    print("They belong to different countries")