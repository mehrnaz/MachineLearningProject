from OpenDataFunc import get_data_for_domain

import collections
from collections import Counter

def get_TTL_counter(data):
    
    """
    get_TTL_counter : the count of all TTL 
    param data : list of data for one domain
    return a counter of all the TTL for a given domain 
    """
    TTL_counter = Counter()
    for d in data:
        c = d['ttl_counts']
        TTL_counter += c

    return(TTL_counter)

def convert_TTL_to_list(count) : 
    
    """
    Convert a counter to a list 
    count : the counter we want to convert 
    return a list with all the element of the count 
    """
    count = dict(count)
    list = []
    for element in count : 
        for i in range(count[element]) :
            list.append(element)
    
    return list

# just for testing
if __name__ == "__main__":
    data = get_data_for_domain('fbx.in')
    for i in data:
        print(i)

    print(get_TTL_counter(data))
    print(convert_TTL_to_list(get_TTL_counter(data)))

    import FeatureTTLChanges as fc

    print(fc.number_of_TTL_changes(data))