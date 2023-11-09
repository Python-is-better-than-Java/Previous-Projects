from PIL import Image
from numpy import asarray
import numpy
 
 
# load the image and convert into
# numpy array
img = Image.open('Map.jpg')
numpydata = asarray(img)
data = []
 
# data
#print(numpydata)

for i in range(0, len(numpydata)):
    row = []
    for j in range(0, len(numpydata[i])):
        if numpydata[i][j][0] == 255:
            row.append(1)
        else:
            row.append(0)
    data.append(row)
#print(len(data))
new_data = []
for i in range(0,len(data) - 1):
    new_row = []
    if ((data[i] != data[i + 1]) and (0 in data[i])):
        i1 = 0
        #print(len(data[i]))
        i2 = len(data[i]) - 1
        while (data[i][i1] == 1):
            #print(i1)
            i1 += 1
        while (data[i][i2] == 1):
            i2 -= 1
        for j in range(i1, i2 + 1):
            new_row.append(data[i][j])
        new_data.append(new_row)
print(len(new_data[0]))
# for i in range(0,len(data)):
#      for j in data[i]:
#           if j == 1:
#                data[i].remove(j)
#           else:
#                break

dat_file = open("list.txt", "w")
dat_file.write("[")
for i in new_data:
    dat_file.write("[")
    for j in i:
        dat_file.write(str(j) + ",")
    dat_file.write("],")
dat_file.write("]")
dat_file.close()
#print(len(data[0]))
#file = open('dash.txt')