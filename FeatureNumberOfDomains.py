from OpenDataFunc import get_data_for_domain
from FeatureSetDNSAnswer import get_unique_domains_set


def get_feature_number_of_ips(data):
    """
    Gets the feature: Number of distinct IP addresses
    :param data:list of data for one domain
    :return:Then umber of distinct IP addresses resolved by this url
    """
    return len(get_unique_domains_set(data))


# just for testing
if __name__ == "__main__":
    data = get_data_for_domain('zwbaxgy.ws')
    for i in data:
        print(i)

    print(get_feature_number_of_ips(data))

