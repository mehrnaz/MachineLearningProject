from OpenDataFunc import get_data_for_domain
from urllib.request import urlopen
from urllib.error import HTTPError
import json


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


def get_feature_number_of_countries_using_ipinfo(data: list):
    """
    Gets the feature: Number of distinct IP addresses
    :param data:list of data for one domain
    :return:Then umber of distinct IP addresses resolved by this url
    """
    dist_ips = get_unique_domains_set(data)
    dist_countries = set()
    for ip in dist_ips:
        url = 'http://ipinfo.io/{}/json'.format(ip)
        try:
            response = urlopen(url)
        except HTTPError:
            print("Error")
            return -1
        resp = json.load(response)
        dist_countries.add(resp['country'])
    return len(dist_countries)


def get_feature_number_of_countries_using_geolocDb(data: list):
    """
    Gets the feature: Number of distinct IP addresses
    :param data:list of data for one domain
    :return:Then umber of distinct IP addresses resolved by this url
    """
    dist_ips = get_unique_domains_set(data)
    dist_countries = set()
    for ip in dist_ips:
        url = 'https://geolocation-db.com/json/{}&position=true'.format(ip)
        try:
            response = urlopen(url)
        except HTTPError:
            print("Error")
            continue
        except Exception as exc:
            print(exc)
            continue
        resp = json.load(response)
        dist_countries.add(resp['country_name'])
    return len(dist_countries)

# just for testing
if __name__ == "__main__":
    data = get_data_for_domain('duolingo.com')
    for i in data:
        print(i)

    print(get_feature_number_of_countries_using_geolocDb(data))

