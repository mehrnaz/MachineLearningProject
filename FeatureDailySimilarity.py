import CreateTimeSeries as ts
from OpenDataFunc import get_data_for_domain
import numpy as np


def preprocess_timeseries(T: list):
    """
    Preprocessing the timeseries as described in the paper (for every point subratct mean and divide by std. deviation
    :param T: timeseries as cerated by CreateTimeSeries scripts
    :return: Numpy array of the reduced timeseries
    """
    m = np.mean(T)
    st = np.std(T)
    res = list()
    for i in T:
        if st == 0:
            p = 0
        else:
            p = (i - m) / st
        res.append(p)
    return np.asarray(res)


def get_feature_daily_similarity(dailySeries: list):
    """
    Feature daily similarity -> avg euclidean distance between daily timeseries
    :param dailySeries: time series cut into dais as created by functions in CreateTimeSeries
    :return: One value -> the avg of euclidean distances between daily series
    """
    if len(dailySeries) <= 1:
        return 0
    processed = list()
    for i in dailySeries:
        processed.append(preprocess_timeseries(i))
    distances = list()
    for i in range(len(dailySeries)):
        for j in range(i + 1, len(dailySeries)):
            distances.append(np.linalg.norm(processed[i] - processed[j]))
    return sum(distances) / len(distances)  # there seems to be a mistake in the article


if __name__ == "__main__":
    data = get_data_for_domain('app-measurement.com')
    for i in data:
        print(i)

    r = ts.get_global_time_series(data, 3600)
    daily = ts.get_daily_series(r, 3600)
    print(daily)

    print(get_feature_daily_similarity(daily))