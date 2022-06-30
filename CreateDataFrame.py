import pandas as pd
import json
import os
from OpenDataFunc import get_data_for_domain
from FeatureSetDNSAnswer import get_feature_set_DNS_answer
from FeatureSetDNSAnswer import get_reduced_set_DNS
from FeatureSetName import get_feature_set_domain_name
from GetAllRawDataFunc import get_all_data
from FeatureSetTTL import get_feature_set_TTL
from FeatureSetTimeBased import get_feature_set_time_based


def get_row(name, data_list, blacklisted):
    dnsAnswerSet = get_reduced_set_DNS(data_list) #get_feature_set_DNS_answer(data_list)
    domainNameSet = get_feature_set_domain_name(name)
    ttlSet = get_feature_set_TTL(data_list) # list((0, 0, 0, 0, 0))
    timeSet = get_feature_set_time_based(data_list, 3600, 8, 5, 15)
    return list((name,)) + timeSet + dnsAnswerSet + ttlSet + domainNameSet + list((blacklisted,))


df = pd.DataFrame(columns=["name", "shortLife_nchanges", "shortLife_avgReq", "dailySimilarity",
                           "repeatingPatterns_nChanges", "repeatingPatterns_avgReq", "repeatingPatterns_stdChangeLen",
                           "accessRatio_idle", "accessRatio_active", "NumberOfDistinctIps", "NumOfDistCountries",
                           "NumberOfDomainsThatShareIP", "ReverseDNSQueryARecrods", "ReverseDNSQueryNSrecords",
                           "ReverseDNSErrors", "AverageTTL",
                           "StdDevOfTTL", "NumOfDistTTL", "NumOfTTLChange", "SpecTTL01", "SpecTTL110", "SpecTTL10100",
                           "SpecTTL100300", "SpecTTL300900", "SpecTTL900inf",
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


df.to_csv("data_csv_all_reduced.csv")
df.info()
print(df.info())
print(df.mean())

print(df.loc[df['Blacklisted'] == 0].mean())
print(df.loc[df['Blacklisted'] == 1].mean())
