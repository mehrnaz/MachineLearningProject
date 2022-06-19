def number_of_TTL_changes(data):
    
    """
    Compute the average TTL changes 
    param data : list of data for one domain
    return : the average TTL changes for a given domain 
    """
    
    list_TTL_changes = []
    for d in data :
        list_TTL_changes.append(d['ttl_changes'])
        
    average_TTL_changes = sum(list_TTL_changes) / len(list_TTL_changes)
    
    return average_TTL_changes