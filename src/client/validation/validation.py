from client.exception.exceptions import WrongInput

def validate_profile(foodie_type, spice_level, preffered_type, tooth_type):
    
    if foodie_type not in ["Vegetarian", "Non Vegetarian", "Eggetarian"]:
        raise WrongInput("Input should be among Vegetarian/ Non Vegetarian/ Eggetarian")
    if spice_level not in ["High", "Medium", "Low"]:
        raise WrongInput("Spice level should be among [High/ Medium/ Low]")
    if preffered_type not in ["North Indian", "South Indian", "Other"]:
        raise WrongInput("Preffered food should be among [North Indian/ South Indian/ Other]")
    if tooth_type not in ["Yes","No"]:
        raise WrongInput("Sweed tooth should be one of among [Yes/ No]")
    