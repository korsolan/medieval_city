def get_next_event(data, list_event):
    for i in range(len(list_event)):
        if data < list_event[i]["date"]:
            pass
    return list_event["name"]
#как привести к нормальной дате


