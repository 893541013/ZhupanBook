grade = [{"a":98},{"b":89},{"c":59},{"d":56}]

hege,buhege=[],[]

for i in grade:
    for k in i:
        if i[k] >= 60:
            hege.append(k)
        else:
            buhege.append(k)
print("合格的:{}"   "不合格的：{}".format(hege,buhege))

    