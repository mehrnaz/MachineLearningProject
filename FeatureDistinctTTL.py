from PreliminaryFunctionTTLFeatures import get_TTL_counter

def number_of_distinct_TTL_values(count) :
    
    """
    Compute the number of distinct TTL for a domain 
    count : the counter of TTL for a domain
    return the number of distinct TTL values for a given domain
    """
    count = set(count)
    return len(count)