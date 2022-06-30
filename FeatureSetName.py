from FeaturePercentageOfLMS import get_feature_percentage_LMS
from FeaturePercentageOfNumericalChars import get_feature_percentage_numerical_chars
import enchant


def get_feature_set_domain_name(name: str):
    d = enchant.Dict("en_US")
    return list((get_feature_percentage_numerical_chars(name), get_feature_percentage_LMS(name, d)))