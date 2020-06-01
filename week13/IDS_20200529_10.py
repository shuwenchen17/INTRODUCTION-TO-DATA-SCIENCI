def get_bmi(height, weight):
    """
    Calculate BMI based on height and weight
    """
    height = height/100
    bmi = weight/height**2   
    return bmi
print(get_bmi(145, 45))    