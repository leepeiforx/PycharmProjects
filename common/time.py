import datetime


def strtodatetime(datestr, format):
    return datetime.datetime.strptime(datestr, format)


def datediff(beginDate, endDate):
    format = "%Y-%m-%d"
    beginDate = str(beginDate)
    endDate = str(endDate)
    bd = strtodatetime(beginDate, format)
    ed = strtodatetime(endDate, format)
    if bd > ed:
        bd, ed = ed, bd
    oneday = datetime.timedelta(days=1)
    count = 0
    while bd != ed:
        ed = ed - oneday
        count += 1
    return count
