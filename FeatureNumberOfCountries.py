from OpenDataFunc import get_data_for_domain
from FeatureSetDNSAnswer import get_unique_domains_set
from urllib.request import urlopen
import json


def get_feature_number_of_countries(data: list):
    """
    Gets the feature: Number of distinct IP addresses
    :param data:list of data for one domain
    :return:Then umber of distinct IP addresses resolved by this url
    """
    dist_ips = get_unique_domains_set(data)
    dist_countries = set()
    for ip in dist_ips:
        url = 'http://ipinfo.io/{}/json'.format(ip)
        response = urlopen(url)
        resp = json.load(response)
        dist_countries.add(resp['country'])
    return len(dist_countries)


# just for testing
if __name__ == "__main__":
    data = get_data_for_domain('duolingo.com')
    for i in data:
        print(i)

    print(get_feature_number_of_countries(data))

