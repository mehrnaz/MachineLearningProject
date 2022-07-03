from OpenDataFunc import get_data_for_domain
import socket
import dns.resolver

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


def get_feature_reverse_DNS(data: list):
    """
    Feature for reverse DNS query -> this was difficult to understand so an attempt was made to extract some information
    :param data:
    :return: three values, average number of A records returned for a single ip address, average number of NS records
    for a single ip address, and average number of errors during calculations as it may show whether this domain works
    (that is probably not a very good indicator of anything but still)
    """
    ips = get_unique_domains_set(data)
    NSs = set()
    aRecords = set()
    errors = 0
    herrorsCOunter = 0
    for i in ips:
        try:
            rev = socket.gethostbyaddr(i)
            result = dns.resolver.resolve(rev[0], 'A')
            for ipval in result:
                aRecords.add(ipval)
            result = dns.resolver.resolve(rev[0], 'NS')
            for ns in result:
                NSs.add(ns)
        except socket.herror as he:
            herrorsCOunter += 1
            errors +=1
        except dns.resolver.NXDOMAIN:
            errors += 1
        except dns.resolver.NoAnswer as noas:
            errors += 1
        except Exception as e:
            print(e)
            errors += 1
    if herrorsCOunter == len(ips):
        herrorsCOunter -= 1
    return len(aRecords) / (len(ips) - herrorsCOunter), len(NSs) / len(ips), errors / len(ips)







# just for testing
if __name__ == "__main__":
    data = get_data_for_domain('4shared.com')
    for i in data:
        print(i)
    print(get_feature_reverse_DNS(data))