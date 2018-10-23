
import pandas as pd
arr = []
with open("file.LOG", "r") as f:
    data = f.readlines()
    for line in data:
        words = line.split()
        arr.append(words)


dates = []
nextToOut = []
userNames = []
length = len(arr)
for line in range(length):
    if 'OUT:' in arr[line]:
        dates.append(arr[line][0])
        nextToOut.append(arr[line][(arr[line].index('OUT:')) + 1])
        userNames.append(arr[line][-1])

df = pd.DataFrame({
    "Hour": dates,
    "Feature": nextToOut,
    "UserName": userNames,

})
print (df)

# print (len(dates))
# print (len(nextToOut))
# print (len(userNames))
