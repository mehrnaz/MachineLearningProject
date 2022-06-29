import CreateTimeSeries as ts
from OpenDataFunc import get_data_for_domain
import numpy as np


def preprocess_timeseries(T: list):
    m = np.mean(T)
    st = np.std(T)
    res = list()
    for i in T:
        res.append((i - m) / st)
    return np.asarray(res)


def get_feature_daily_similarity(dailySeries: list):
    processed = list()
    for i in dailySeries:
        processed.append(preprocess_timeseries(i))
    distances = list()
    for i in range(len(dailySeries)):
        for j in range(i + 1, len(dailySeries)):
            distances.append(np.linalg.norm(processed[i] - processed[j]))
    return sum(distances) / len(distances)  # there seems to be a mistake in the article


if __name__ == "__main__":
    data = get_data_for_domain('duolingo.com')
    for i in data:
        print(i)

    r = ts.get_global_time_series(data, 3600)
    daily = ts.get_daily_series(r, 3600)
    print(daily)

    print(get_feature_daily_similarity(daily))