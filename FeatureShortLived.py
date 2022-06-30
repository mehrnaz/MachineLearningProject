import CreateTimeSeries as ts
from detecta import detect_cusum
from OpenDataFunc import get_data_for_domain


def get_feature_short_lived(time_series_global: list, epsilon):
    changes = ts.create_changepoint_list(time_series_global, epsilon)
    ta, times_start, times_end, amp = detect_cusum(changes, 0.3, 0.08, ending=True, show=False)
    num_changes = len(times_start)
    num_requests = list()
    for i in range(num_changes):
        counter = 0
        for a in range(times_start[i], times_end[i] + 1):
            counter += time_series_global[a]
        num_requests.append(counter)
    if num_changes > 0:
        return num_changes, sum(num_requests) / len(num_requests)
    else:
        return 0, 0


if __name__ == "__main__":
    data = get_data_for_domain('app-measurement.com')
    r = ts.get_global_time_series(data, 3600)
    print(r)
    print(len(r))
    print(sum(r))

    print(get_feature_short_lived(r, 8))
