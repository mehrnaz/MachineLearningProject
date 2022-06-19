from PreliminaryFunctionTTLFeatures import get_TTL_counter
from PreliminaryFunctionTTLFeatures import convert_TTL_to_list

import statistics 

def standart_deviation_of_TTL(list) : 
    
    """
    Compute the standart deviation of the TTL
    list : the list of all the TTL values
    return the standart deviation of TTL for a given domain 
    """

    if len(list) > 1:
        standart_deviation = statistics.stdev(list)
    else:
        return 0
    return standart_deviation
