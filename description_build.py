def get_count (list, type):
    count = 0
    for i in range(len(list)):
        if type == list[i]["type"]:
            count += 1
    return count

def get_old_buildings (list, need_year):
    count = 0
    for i in range(len(list)):
        if need_year >= list[i]["year"]:
            count += 1
    return count
