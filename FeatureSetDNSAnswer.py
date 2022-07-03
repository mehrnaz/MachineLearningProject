import FeatureNumberOfCountries as nc
from FeatureNumberOfDomains import get_feature_number_of_ips
from FeatureReverseDNS import get_feature_reverse_DNS
# get_feature_number_of_countries(data)


def get_feature_set_DNS_answer(data):
    """
    The only really problematic feature set as extracting those features takes really long time and also getting
    information about the number of domains that share an address is difficult if not nearly impossible
    :param data:
    :return: six values -> number of ips, number of countries, 0 (missing feature) and three for reverse DNS
    """
    reverseFatures = get_feature_reverse_DNS(data)
    return list((get_feature_number_of_ips(data), nc.get_feature_number_of_countries_using_geolocDb(data), 0, reverseFatures[0], reverseFatures[1], reverseFatures[2]))
    # nc.get_feature_number_of_countries_using_geolocDb(data)

def get_reduced_set_DNS(data):
    """Only returns the one feature that does not require querying internet"""
    return list((get_feature_number_of_ips(data), 0,0,0,0,0))
