def calculate_bmi(weight, height):
    height = height / 100  # convert cm to meters
    bmi = weight / (height * height)

    if bmi < 18.5:
        category = "Catergory: Underweight"
    elif 18.5 <= bmi < 25:
        category = "Catergory: Normal Weight"
    elif 25 <= bmi < 30:
        category = "Catergory: Overweight"
    else:
        category = "Catergory: Obesity"

    return bmi, category
