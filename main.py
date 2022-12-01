import sys
import math
import os


def distance(arr1, arr2):
    d = 0
    for index in range(0,len(arr1)):
        d += math.pow((float(arr1[index]) - float(arr2[index])), 2)
    d = math.sqrt(d)
    return d


if len(sys.argv) < 4:
    file_name = sys.argv[2]
    k = int(sys.argv[1])
    iter = 200
else:
    iter = int(sys.argv[2])
    file_name = sys.argv[3]
    k = int(sys.argv[1])

epsi = 0.001
data = []
min_index = 0
min_d = sys.float_info.max
current_d = 0
members_count = []
count = 0
temp_clusters = []

with open(f"test_data/tests/{file_name}") as file:
    N = len(file.readlines())
    file.seek(0)

if k >= N or k < 1:
    print("Invalid number of clusters!")
    sys.exit()

if iter < 1 or iter >= 1000:
    print("Invalid maximum iteration!")
    sys.exit()

with open(f"test_data/tests/{file_name}") as file:
    for i in range(0, k):
        members_count.append(1)
        line = file.readline()
        current_values = line.split(",")
        current_values[-1] = current_values[-1].replace(os.linesep, "")
        current_values[-1] = current_values[-1].replace("\n", "")
        data.append(current_values)
        temp_clusters.append(current_values)
    file.seek(0)
line_count = 0
small_change = True

while count < iter:
    for i in range(0, k):
        temp_clusters[i] = data[i].copy()
    with open(f"test_data/tests/{file_name}") as file:
        line_count=0
        for line in file:
            min_index = 0
            min_d = sys.float_info.max
            current_values = line.split(",")
            current_values[-1] = current_values[-1].replace(os.linesep, "")
            current_values[-1] = current_values[-1].replace("\n", "")
            for index in range(0, k):
                current_d = distance(data[index], current_values)
                if current_d < min_d:
                    min_index = index
                    min_d = current_d
            members_count[min_index] += 1
            for i in range(0, len(data[min_index])):
                data[min_index][i] = (float(data[min_index][i]) * float((members_count[min_index]-1)) + float(current_values[i])) / members_count[min_index]
        file.seek(0)
    small_change = True

    for j in range(0, k):
        if distance(temp_clusters[j], data[j]) >= epsi:
            small_change = False
    if small_change:
        break
    count+=1
    if count >= iter:
        break
for j in range(0, len(data)):
    for i in range(0, len(data[0])):
        data[j][i] = round(data[j][i],4)

print(data)