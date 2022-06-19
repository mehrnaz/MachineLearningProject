from PreliminaryFunctionTTLFeatures import get_TTL_counter
from PreliminaryFunctionTTLFeatures import convert_TTL_to_list


def average_TTL(list) :
    
    """
    Compute the average value of the TTL
    list : the list of all the TTL values 
    return the average value of TTL for a given domain 
    """
    average = sum(list)/len(list)
    return average 

