hakjum = 0
score = ''
total = 0
total_hakjum = 0
score_dict = {"A+" : 4.5,"A0": 4.0,"B+": 3.5 ,"B0" : 3.0,"C+": 2.5,"C0": 2.0,"D+":1.5,"D0": 1.0,"F": 0,"P" : -1}

for i in range(20):
    _,hakjum, score = input().split()
    if score == "P":
        continue
    total_hakjum += float(hakjum)

    total += float(hakjum) * score_dict[score]

print(total/total_hakjum)