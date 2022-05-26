import datetime


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


def end_time(ride):
    delta = datetime.timedelta(0, ride["duration"])
    time = ride["startTime"]
    start = datetime.datetime(
        int(time[:4]),
        int(time[5:7]),
        int(time[8:10]),
        int(time[11:13]),
        int(time[14:16]),
        int(time[17:19]),
    )
    end = start + delta
    return str(end) + str(time[19:])
