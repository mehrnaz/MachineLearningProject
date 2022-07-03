import os
import pickle
import string
import json
from random import sample

def get_all_data():
    """
    This function returns all data as a dictionary with a list of dictionaries.
    """
    res = dict()
    for a in range(1, 32):
        for i in ['0'] + list(string.ascii_lowercase):
            # Open the data files one by one, should work on any system, expects the data to be in a folder 202101
            with open(os.path.join(".", "202101", "202101{:02d}_{}.data".format(a, i)), 'rb') as f:
                data = pickle.load(f)

            for item in data:
                if item not in res.keys():
                    res[item] = list()
                data[item]['date'] = "202101{:02d}".format(a)
                res[item].append(data[item])
    return res


def get_selection_with_less_legit(nleg, data, exclude_low_numbers):
    """
    Gets data but ignores some legitimate domains
    :param nleg: Number of legitimate domains to keep
    :param data:
    :param exclude_low_numbers: Exclude legitimate domains that have just one datapoint
    :return:
    """
    res = dict()
    legits = list()
    with open(os.path.join(".", "domains_subset.json"), 'rb') as f:
        labels = json.load(f)
        for item in data:
            if item in labels["legitimate"]:
                if exclude_low_numbers and len(data[item]) <= 1:
                    continue
                legits.append(item)
        if len(legits) < nleg:
            print("Sent more legit than can be get")
            nleg = len(legits)
        sa = sample(legits, nleg)
        for item in data:
            if item in sa:
                res[item] = data[item]
            elif item in labels["blacklisted"]:
                res[item] = data[item]
    return res

if __name__ == "__main__":
    data = get_all_data()
    selected = get_selection_with_less_legit(500, data, True)
    print(len(data), " ", len(selected))
