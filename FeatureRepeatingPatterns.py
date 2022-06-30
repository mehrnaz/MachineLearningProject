import CreateTimeSeries as ts
from detecta import detect_cusum
from OpenDataFunc import get_data_for_domain
import statistics


def get_feature_repeating_patterns(time_series_local: list, epsilon):
    changes = ts.create_changepoint_list(time_series_local, epsilon)
    ta, times_start, times_end, amp = detect_cusum(changes, 0.3, 0.08, ending=True, show=False)
    num_changes = len(times_start)
    num_requests = list()
    lens_of_changes = list()
    for i in range(num_changes):
        counter = 0
        lens_of_changes.append(times_end[i] - times_start[i])
        for a in range(times_start[i], times_end[i] + 1):
            counter += time_series_local[a]
        num_requests.append(counter)
    if len(num_requests) > 1:
        return num_changes, sum(num_requests) / len(num_requests), statistics.stdev(lens_of_changes)
    elif len(num_requests) == 1:
        return num_changes, sum(num_requests) / len(num_requests), 0
    else:
        return num_changes, 0, 0



if __name__ == "__main__":
    data = get_data_for_domain('duolingo.com')

    r = ts.get_local_time_series(data, 3600)
    print(r)
    print(len(r))
    print(sum(r))
    changes = ts.create_changepoint_list(r, 8)

    print(get_feature_repeating_patterns(r, 8))
