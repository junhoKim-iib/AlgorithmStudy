N = int(input())


hour, min, sec = 0, 0, 0
time = str(hour) + str(min) + str(sec)
cnt = 0

while hour <= N:

    sec += 1

    if sec > 59:
        sec -= 60
        min += 1

    if min > 59:
        min -= 60
        hour += 1

    time = str(hour) + str(min) + str(sec)
    
    if '3' in time:
        cnt += 1

print(cnt)