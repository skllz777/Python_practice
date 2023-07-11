def open_or_senior(data):
    status = []
    for d in data:
        for b in d:
            if b > 7 and b > 55:
                status.append("Senior")
            else:
                status.append("Open")
    return status

