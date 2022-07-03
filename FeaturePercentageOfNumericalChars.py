

def get_feature_percentage_numerical_chars(name: str):
    """
    Feature -> the percentage of chars in the name of the domain that are numerical
    :param name: name of the domain
    :return: one number, floating point -> percentage
    """
    numbers = sum(c.isdigit() for c in name)
    return numbers / len(name)

if __name__ == "__main__":
    print(get_feature_percentage_numerical_chars('123abc.com'))