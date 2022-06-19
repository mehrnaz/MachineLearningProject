import pandas as pd
import json
import os
from OpenDataFunc import get_data_for_domain
from FeatureSetDNSAnswer import get_feature_set_DNS_answer
from FeatureSetName import get_feature_set_domain_name
from GetAllRawDataFunc import get_all_data
from FeatureSetTTL import get_feature_set_TTL


def get_row(name, data_list, blacklisted):
    dnsAnswerSet = get_feature_set_DNS_answer(data_list) + list((0, 0))
    domainNameSet = get_feature_set_domain_name(name)
    ttlSet = get_feature_set_TTL(data_list) # list((0, 0, 0, 0, 0))
    timeSet = list((0, 0, 0, 0))
    return list((name,)) + timeSet + dnsAnswerSet + ttlSet + domainNameSet + list((blacklisted,))


df = pd.DataFrame(columns=["name", "shortLife", "dailySimilarity", "repeatingPatterns",
                           "accessRatio", "NumberOfDistinctIps", "NumOfDistCountries",
                           "NumberOfDomainsThatShareIP", "ReverseDNSQuery", "AverageTTL",
                           "StdDevOfTTL", "NumOfDistTTL", "NumOfTTLChange", "PercOfSpecTTl",
                           "PercOfNumChars", "PercOfLengthOfLMS", "Blacklisted"])

counter = 0
with open(os.path.join(".", "domains_subset.json"), 'rb') as f:
    labels = json.load(f)
    data = get_all_data()
    for item in data:
        if counter % 20 == 0:
            print(counter)
        counter += 1
        row = get_row(item, data[item], item in labels['blacklisted'])
        df.loc[len(df.index)] = row


df.to_csv("data_csv.csv")
df.info()
print(df.info())
print(df.mean())

print(df.loc[df['Blacklisted'] == 0].mean())
print(df.loc[df['Blacklisted'] == 1].mean())
