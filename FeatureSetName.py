from FeaturePercentageOfLMS import get_feature_percentage_LMS
from FeaturePercentageOfNumericalChars import get_feature_percentage_numerical_chars
import enchant


def get_feature_set_domain_name(name: str):
    """
    Returns the domain name feature set
    :param name: name of the domain
    :return: two values -> perc of numerical chars, perc of longest LMS
    """
    d = enchant.Dict("en_US")
    return list((get_feature_percentage_numerical_chars(name), get_feature_percentage_LMS(name, d)))