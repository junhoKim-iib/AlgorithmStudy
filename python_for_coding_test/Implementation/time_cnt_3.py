N = int(input())


hours, mins, secs = 0, 0, 0
time_now = str(hours) + str(mins) + str(secs)
cnt = 0

while hours <= N:

    secs += 1

    if secs > 59:
        secs -= 60
        mins += 1

    if mins > 59:
        mins -= 60
        hours += 1

    time_now = str(hours) + str(mins) + str(secs)
    
    if '3' in time_now:
        cnt += 1

print(cnt)