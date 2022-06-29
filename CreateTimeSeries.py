from OpenDataFunc import get_data_for_domain

# 9455600 timestamp for 01/01/2021 00:00:00 - the start of global time series
def subtract_start(a):
    res = a - 9455600
    if a < 0:
        print("Timestamp weirdly lower than zero")
    return res


def get_global_time_series(data: list, timestep: int):
    """
    Creates a global time series, from 01/01/2021 00:00:00 to 31/01/2021 24:00:00
    :param data: A list of data dictionaries for the domain
    :param timestep: Time interval
    :return: List of ints that represent the number of requests for every time interval
    """
    timestamps = list()
    for i in data:
        timestamps.append(sorted(map(subtract_start, i['timestamp'])))
    timeCounter = timestep
    res = list()
    currentList = None
    currentIndex = 0
    indexOfCurrentList = 0
    if len(timestamps) > 0:
        currentList = timestamps[0]
    while timeCounter <= (31 * 24 * 60 * 60):
        if currentList is None:
            res.append(0)
            timeCounter += timestep
            continue
        counterOfTimestamps = 0
        while True:
            if currentIndex >= len(currentList):
                indexOfCurrentList += 1
                if indexOfCurrentList >= len(timestamps):
                    currentList = None
                    break
                else:
                    currentList = timestamps[indexOfCurrentList]
                    currentIndex = 0
            if currentList[currentIndex] < timeCounter:
                counterOfTimestamps += 1
                currentIndex += 1
            else:
                break
        res.append(counterOfTimestamps)
        timeCounter += timestep
    return res


def get_global_time_series_nicer(data: list, timestep: int):
    """
    Creates a global time series, from 01/01/2021 00:00:00 to 31/01/2021 24:00:00
    :param data: A list of data dictionaries for the domain
    :param timestep: Time interval
    :return: List of ints that represent the number of requests for every time interval
    """
    timestamps = list()
    for i in data:
        timestamps += sorted(map(subtract_start, i['timestamp']))
    timeCounter = timestep
    res = list()
    currentIndex = 0
    while timeCounter <= (31 * 24 * 60 * 60):
        counterOfTimestamps = 0
        while True:
            if currentIndex >= len(timestamps):
                    break
            if timestamps[currentIndex] < timeCounter:
                counterOfTimestamps += 1
                currentIndex += 1
            else:
                break
        res.append(counterOfTimestamps)
        timeCounter += timestep
    return res



def get_local_time_series(data: list, timestep: int):
    """
    Returns a local time series, from the first time the doamin was requested to the last
    :param data: A list of data dictionaries for the domain
    :param timestep: Time interval
    :return:  List of ints that represent the number of requests for every time interval
    """
    timestamps = list()
    for i in data:
        timestamps.append(sorted(map(subtract_start, i['timestamp'])))
    timeCounter = timestep
    res = list()
    currentList = None
    currentIndex = 0
    indexOfCurrentList = 0
    if len(timestamps) > 0:
        currentList = timestamps[0]
        timeCounter = currentList[0] + timestep
    while True:
        if currentList is None:
            break
        counterOfTimestamps = 0
        while True:
            if currentIndex >= len(currentList):
                indexOfCurrentList += 1
                if indexOfCurrentList >= len(timestamps):
                    currentList = None
                    break
                else:
                    currentList = timestamps[indexOfCurrentList]
                    currentIndex = 0
            if currentList[currentIndex] <= timeCounter:
                counterOfTimestamps += 1
                currentIndex += 1
            else:
                break
        res.append(counterOfTimestamps)
        timeCounter += timestep
    return res


def get_local_time_series_nicer(data: list, timestep: int):
    """
    Returns a local time series, from the first time the doamin was requested to the last
    :param data: A list of data dictionaries for the domain
    :param timestep: Time interval
    :return:  List of ints that represent the number of requests for every time interval
    """
    timestamps = list()
    for i in data:
        timestamps += sorted(map(subtract_start, i['timestamp']))
    timeCounter = timestep
    res = list()
    currentIndex = 0
    if len(timestamps) > 0:
        timeCounter = timestamps[0] + timestep
    while True:
        if currentIndex >= len(timestamps):
            break
        counterOfTimestamps = 0
        while True:
            if currentIndex >= len(timestamps):
                break
            if timestamps[currentIndex] <= timeCounter:
                counterOfTimestamps += 1
                currentIndex += 1
            else:
                break
        res.append(counterOfTimestamps)
        timeCounter += timestep
    return res


def create_changepoint_list(timeseries: list, epsilon: int):
    """
    Creates a change point list as in section 3.1.1 of the paper
    :param timeseries: List of numbers of requests for the domain for every time interval
    :param epsilon: the window for the change
    :return:
    """
    res = list()
    for t in range(len(timeseries)):
        pt_minus = 0
        pt_plus = 0
        numVals = epsilon
        counter = 0
        for i in range(1, epsilon + 1):
            if t - i < 0:
                numVals = i - 1
                break
            counter += timeseries[t - i]
        if numVals != 0:
            pt_minus = counter / numVals
        numVals = epsilon
        counter = 0
        for i in range(1, epsilon + 1):
            if t + i >= len(timeseries):
                numVals = i - 1
                break
            counter += timeseries[t + i]
        if numVals != 0:
            pt_plus = counter / numVals
        dt = abs(pt_minus - pt_plus)
        res.append(dt)
    return res


def get_daily_series(timeseries: list, timestep: int):
    """
    Gives you the timeseries for every day (31 days)
    :param timeseries:
    :param timestep: The timestep used for this timeseries, must divide the number of seconds in a day
    :return: list of lists, every list is a timeseries here
    """
    numberOfEntriesPerDay = int((60*60*24) / timestep)
    res = list()
    if (60*24*60) % timestep != 0:
        print("Select a timestep that can divide the day exactly.")
        return
    for i in range(31):
        res.append(timeseries[i * numberOfEntriesPerDay : ((i + 1) * numberOfEntriesPerDay) - 1])
    return res


if __name__ == "__main__":
    data = get_data_for_domain('duolingo.com')
    for i in data:
        print(i)

    r = get_local_time_series(data, 3600)
    print(r)
    print(len(r))
    print(sum(r))
    nicer = get_local_time_series_nicer(data, 3600)
    print(nicer)
    print(len(nicer))
    print(sum(nicer))
    print(r == nicer)
    dt = create_changepoint_list(r, 8)
    print(dt)
    print(len(dt))
    print(sum(dt))

