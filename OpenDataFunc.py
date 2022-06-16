import os
import pickle
import string


def get_data_for_domain(domain_name: str, interesting_features=('ttl_changes', 'ips', 'ttl_counts', 'timestamp')):
    """
    This function returns all data for a given domain name. Can request only some features.
    :param domain_name:The name of the domain to get data for
    :param interesting_features:The list of features I want in the result. Default is all
    :return: list of dictionaries with the data for this domain
    """
    res = list()
    first_char = domain_name[0].lower()
    if first_char not in list(string.ascii_lowercase):
        first_char = 0
    for a in range(1, 32):
        with open(os.path.join(".", "202101", "202101{:02d}_{}.data".format(a, first_char)), 'rb') as f:
            data = pickle.load(f)

        for item in data:
            if item == domain_name:
                # returns only the features in interesting_features and date
                intr_dict = {}
                for feature in interesting_features:
                    intr_dict[feature] = data[item][feature]
                intr_dict['date'] = "202101{:02d}".format(a)
                res.append(intr_dict)
    return res
