EXPECTED_BAKE_TIME = 40


def bake_time_remaining(minutes):
    """
Complete the bake_time_remaining() function that takes the actual minutes the lasagna has been in the oven as an argument and returns how many minutes the lasagna still needs to bake based on the EXPECTED_BAKE_TIME constant

"""
    return EXPECTED_BAKE_TIME - minutes


def preparation_time_in_minutes(number_of_layers):

    """
Calculate preparation time in minutes 

number_of_layers (int): number of layers 
return: 
int: number_of_layers multiplied by 2

"""
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
       elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
      int: The total time elapsed (in minutes) preparing and baking.

   This function takes two integers representing the number of lasagna 
   the total elapsed minutes spent cooking (preparing + baking)
"""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time



 