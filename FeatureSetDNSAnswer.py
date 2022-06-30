import FeatureNumberOfCountries as nc
from FeatureNumberOfDomains import get_feature_number_of_ips
from FeatureReverseDNS import get_feature_reverse_DNS
# get_feature_number_of_countries(data)


def get_feature_set_DNS_answer(data):
    reverseFatures = get_feature_reverse_DNS(data)
    return list((get_feature_number_of_ips(data), nc.get_feature_number_of_countries_using_geolocDb(data), 0, reverseFatures[0], reverseFatures[1], reverseFatures[2]))
    # nc.get_feature_number_of_countries_using_geolocDb(data)

def get_reduced_set_DNS(data):
    return list((get_feature_number_of_ips(data), 0,0,0,0,0))
