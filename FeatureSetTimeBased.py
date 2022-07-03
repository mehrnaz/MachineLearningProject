import CreateTimeSeries as ts
from FeatureRepeatingPatterns import get_feature_repeating_patterns
from FeatureDailySimilarity import get_feature_daily_similarity
from FeatureShortLived import get_feature_short_lived
from FeatureAccessRatio import get_feature_access_ratio


def get_feature_set_time_based(data, timestep, epsilon, idle_treshold, active_treshold):
    """
    Time based feature set
    :param data:
    :param timestep:
    :param epsilon:
    :param idle_treshold:
    :param active_treshold:
    :return: eight values shortLived1,2 - daily - repeatingPattern1,2,3 - accessRatio1,2
    """
    local_series = ts.get_local_time_series_nicer(data, timestep)
    global_series = ts.get_global_time_series_nicer(data, timestep)

    repeating = get_feature_repeating_patterns(local_series, epsilon)
    short_lived = get_feature_short_lived(global_series, epsilon)
    access = get_feature_access_ratio(data, idle_treshold, active_treshold)
    daily = get_feature_daily_similarity(ts.get_daily_series(global_series, timestep))

    return list((short_lived[0], short_lived[1], daily, repeating[0], repeating[1], repeating[2], access[0], access[1]))
