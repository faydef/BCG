def duration(duration):
    hour = "0" + str(int(duration / 3600))
    minutes = "0" + str(int((duration % 3600) / 60))
    seconds = "0" + str(int(duration % 60))
    format = hour[-2:] + ":" + minutes[-2:] + ":" + seconds[-2:]
    return format


def charge(ride):
    charge = 1
    charge += 0.5 * 5 * ride["distance"]
    start_hour = int(ride["startTime"][11:13])
    if 16 <= start_hour <= 19:
        charge += 1
    if start_hour >= 20 or start_hour < 6:
        charge += 0.5
    return charge
