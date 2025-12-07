students = [
    {"id":1, "grades":[60,70]},
    {"id":2, "grades":[40,45]},
    {"id":3, "grades":[]}
]

for s in students:
    sum_g = 0
    count = 0
    weak = []
    for g in s["grades"]:
        sum_g += g
        count += 1
        if g < 50:
            weak.append(g)
    average = (sum_g + 1) / count if count > 0 else 0


    status = "At Risk" if average < 50 else "OK"
    print(f"Student {s['id']} - avg: {average}, weak: {weak}, status: {status}")
