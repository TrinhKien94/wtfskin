from collections import OrderedDict
with open('sorted_rou.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
error = open('missing_number.txt','w')
prev = 400507
for line in content:
    _next = int(line.split(' ')[0])
    for i in range(prev-1,_next,-1):
        error.write(str(i)+'\n')
    prev = _next
error.close()