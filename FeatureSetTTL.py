from FeatureAverageTTL import average_TTL
from FeatureDistinctTTL import number_of_distinct_TTL_values
from FeatureStandartDeviationTTL import standart_deviation_of_TTL
from FeatureTTLChanges import number_of_TTL_changes
from FeatureTTLRange import percentage_usage_of_specific_TTL_ranges
import PreliminaryFunctionTTLFeatures as pr


def get_feature_set_TTL(data):
    """
    Returns all the TTL based features
    :param data:
    :return: averageTTL, stdofTTL, dstTTLvalues, numOfChanges, usageOfRanges
    """
    counter = pr.get_TTL_counter(data)
    li = pr.convert_TTL_to_list(counter)
    return list((average_TTL(li), standart_deviation_of_TTL(li), number_of_distinct_TTL_values(counter),
                 number_of_TTL_changes(data))) + list(percentage_usage_of_specific_TTL_ranges(counter))

