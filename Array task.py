exp = [2200,2350,2600,2130,2190]
count = 0
print(exp[1]-exp[0])
print(exp[0]+exp[1]+exp[2])
for value in exp:
    if value == 2000:
        count +=1
if count == 0:
    print("No month")
else:
    print(count)

exp.append(1980)
print(exp)
exp[3] -= 200
print(exp)
