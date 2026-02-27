from datetime import datetime, timedelta

def parse(s):

    date = s[:10]

    h = int(s[-5:-3])
    m = int(s[-2:])

    if "-" in s:
        h = -h
        m = -m

    dt = datetime.strptime(date,"%Y-%m-%d")

    return dt - timedelta(hours=h, minutes=m)


t1 = parse(input())
t2 = parse(input())

diff = abs(t1 - t2)

days = diff.total_seconds() // 86400

print(int(days))