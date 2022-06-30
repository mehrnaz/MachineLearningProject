from GetAllRawDataFunc import get_all_data



def get_feature_access_ratio(data: list, idle_treshold, active_treshold):
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