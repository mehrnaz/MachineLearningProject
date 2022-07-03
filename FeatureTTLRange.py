from PreliminaryFunctionTTLFeatures import get_TTL_counter


def percentage_usage_of_specific_TTL_ranges(count):
    """
    gets how often are which ttl ranges used
    :param count:
    :return:
    """
    sum_TTL = sum(count.values())

    count = dict(count)
    range_TTL = {"0;1": 0, "1;10": 0, "10;100": 0, "100;300": 0, "300;900": 0, "900;inf": 0}

    for element in count:
        if (element >= 0) and (element < 1):
            range_TTL["0;1"] = count[element] * 100 / sum_TTL
        elif (element >= 1) and (element < 10):
            range_TTL["1;10"] = count[element] * 100 / sum_TTL
        elif (element >= 10) and (element < 100):
            range_TTL["10;100"] = count[element] * 100 / sum_TTL
        elif (element >= 100) and (element < 300):
            range_TTL["100;300"] = count[element] * 100 / sum_TTL
        elif (element >= 300) and (element < 900):
            range_TTL["300;900"] = count[element] * 100 / sum_TTL
        elif (element >= 900):
            range_TTL["900;inf"] = count[element] * 100 / sum_TTL

    return range_TTL["0;1"], range_TTL["1;10"], range_TTL["10;100"], range_TTL["100;300"], range_TTL["300;900"], range_TTL["900;inf"]
