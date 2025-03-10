def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;
    def zero_fuel(distance_to_pump, mpg, fuel_left):
    # Calculate maximum distance the car can travel
    max_distance = mpg * fuel_left
    
    # Return True if the car can reach the pump, False otherwise
    return max_distance >= distance_to_pump
