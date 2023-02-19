def if_child(list, age):
    for i in range(len(list)):
        if age < list[i]["age"]:
            list["child"] = True
        else:
            list["child"] = False

def elder(list):
    max_age = 0
    max_key = 0
    for i in range(len(list)):
        if list[i]["age"] > max_age:
            max_age = list[i]["age"]
            max_key = i
            print(i)
    return list["name"], list["surname"]

def get_count_occupation(list, occupation):
    count = 0
    for i in range(len(list)):
        if occupation == list[i]["occupation"]:
            count += 1
    return count

def adding_resident(list, resident):#набросок! нет решения!
    list.append(resident)
    return

def count_religion(list, religion):
    count = 0
    for i in range(len(list)):
        if religion == list[i]["religion"]:
            count += 1
    return count




