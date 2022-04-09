grade = [{"a":98},{"b":89},{"c":59},{"d":56}]


hege = []
buhege = []


if grade[0]["a"] > 59:
    hege.append("a")
else:
    buhege.append("a")
if grade[1]["b"] > 59:
    hege.append("b")
else:
    buhege.append("b")
if grade[2]["c"] > 59:
    hege.append("c")
else:
    buhege.append("c")
if grade[3]["d"] > 59:
    hege.append("d")
else:
    buhege.append("d")
    print(hege,buhege)
