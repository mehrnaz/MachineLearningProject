from GetAllRawDataFunc import get_all_data



def get_feature_access_ratio(data: list, idle_treshold, active_treshold):
    """
    Access ratio feature -> determines whether a domain is active or idle.
    :param data: the list of data for the domain
    :param idle_treshold:  if the number of days when this domain is queried is less or equal to this it is idle
    :param active_treshold: if the number of days when this domain is queried is greater or equal to this it is active
    :return: returns two boolean values, first denotes if the domain is idle and the second if it is active
    """
    idle = False
    active = False
    if len(data) <= idle_treshold:
        idle = True
    if len(data) >= active_treshold:
        active = True
    return idle, active



if __name__ == "__main__":
    data = get_all_data()
    numbersOfPoints = list()
    for item in data:
        numbersOfPoints.append(len(data[item]))

    print(sum(numbersOfPoints)/ len(numbersOfPoints))
    for i in range(1,32):
        print(i, ": ", numbersOfPoints.count(i))