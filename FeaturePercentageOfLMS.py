import enchant


def get_feature_percentage_LMS(name: str, d):
    """
    Fetaure percentage of longest meaningful substring in the domain name -> cuts the domain into substrings and tests
     then against an english dictionary, then picks the longest. Ignores substrings of length 1
    :param name: the name of the domain
    :param d: dictionary to use
    :return: One value, floating point number -> percentage
    """
    substrings = [name[i: j] for i in range(len(name))
                  for j in range(i + 1, len(name) + 1)]
    longest = 0
    for i in substrings:
        if 1 < len(i) == sum(c.isalpha() for c in i):
            if d.check(i):
                if len(i) > longest:
                    longest = len(i)

    return longest / len(name)


if __name__ == "__main__":
    print(get_feature_percentage_LMS('123abc.com'))

