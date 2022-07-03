import pandas as pd
import json
import os
from FeatureSetDNSAnswer import get_feature_set_DNS_answer
from FeatureSetDNSAnswer import get_reduced_set_DNS
from FeatureSetName import get_feature_set_domain_name
from GetAllRawDataFunc import get_all_data
from FeatureSetTTL import get_feature_set_TTL
from FeatureSetTimeBased import get_feature_set_time_based
from GetAllRawDataFunc import get_selection_with_less_legit

"""A script for getting DNS answer feature set. To speed thing up it can be set to get less data."""


def get_row(name, data_list, blacklisted):
    dnsAnswerSet = get_feature_set_DNS_answer(data_list)
    return list((name,)) + dnsAnswerSet + list((blacklisted,))


df = pd.DataFrame(columns=["name", "NumberOfDistinctIps", "NumOfDistCountries",
                           "NumberOfDomainsThatShareIP", "ReverseDNSQueryARecrods", "ReverseDNSQueryNSrecords",
                           "ReverseDNSErrors", "Blacklisted"])

counter = 0
with open(os.path.join(".", "domains_subset.json"), 'rb') as f:
    labels = json.load(f)
    data = get_all_data()
    data = get_selection_with_less_legit(2000, data, True)
    for item in data:
        if counter % 20 == 0:
            print(counter)
        counter += 1
        row = get_row(item, data[item], item in labels['blacklisted'])
        df.loc[len(df.index)] = row


df.to_csv("data_csv_onlyDNS2000.csv")
df.info()
print(df.info())

