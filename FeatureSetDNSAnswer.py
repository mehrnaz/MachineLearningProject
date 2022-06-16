
def get_unique_domains_set(data):
    """
    Returns all distinct ips for this domain
    :param data:
    :return:
    """
    ips = set()
    for d in data:
        for i in d['ips']:
            ips.add(i)
    return(ips)