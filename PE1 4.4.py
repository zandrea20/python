def BMI_calc(weight_lb, height_in):
    
    weight_kg = weight_lb * 0.453592
    height_m = height_in * 0.0254
    
    bmi = weight_kg  / (height_m * height_m )
    print(f"Your BMI is:{bmi:.2f}")

    if bmi < 18.5:
        weightclass= "Underweight"
    elif 18.5 <= bmi < 24.9:
        weightclass = "Normal weight"
    elif 25 <= bmi < 29.9:
        weightclass = "Overweight"
    else:  
        weightclass = "Obese"
    
    print(f"You are in the {weightclass} weightclass.")

input_weight=float(input("Please enter your weight in Lbs:"))
input_height=float(input("Pleases enter your height in inches:"))
BMI_calc(input_weight, input_height)