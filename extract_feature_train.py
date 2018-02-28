from collections import OrderedDict


def convert_color(color):
    if color == 'r':
        return '2'
    if color == 'b':
        return '1'
    if color == 'g':
        return '0'


with open('training.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
sort_dict = OrderedDict()
for line in content:
    elements = line.split(' ')
    number = int(elements[0])
    sort_dict[number] = {}
    sort_dict[number]['color'] = elements[1]
    sort_dict[number]['value'] = elements[2]
    # sort_dict[number] = elements[2]
reversed_sorted = OrderedDict(sorted(sort_dict.items(), reverse=True))
keys = reversed_sorted.keys()
key_len = len(keys)
number_before = 4
extract_number_element_before = key_len - number_before - 100
data = open('training.csv','w')
for i in range(0,extract_number_element_before):
    text = convert_color(reversed_sorted[keys[i]]['color'])
    for j in range(i+1,i+number_before):
        text = text + ',' + str(reversed_sorted[keys[j]]['value'])
    count = 0
    for k in range(2,5):
        if reversed_sorted[keys[i+1]]['color'] != reversed_sorted[keys[i+5]]['color'] and reversed_sorted[keys[i+1]]['color'] != reversed_sorted[keys[i+6]]['color']:
            break;
        if reversed_sorted[keys[i+1]]['color'] == reversed_sorted[keys[i+k]]['color']:
            count+=1
        else:
             break;
    if count == 3:
    # if reversed_sorted[keys[i+1]]['color'] == reversed_sorted[keys[i+2]]['color'] and reversed_sorted[keys[i+1]]['color'] != reversed_sorted[keys[i+3]]['color'] and reversed_sorted[keys[i+1]]['color'] != reversed_sorted[keys[i+4]]['color'] and reversed_sorted[keys[i+1]]['color'] != 'g':
        text = text + ',1'
    else:
        text = text + ',0'
    # count = 0
    # for j in range(i+1,key_len):
    #     count += 1
    #     if reversed_sorted[keys[j]]['color'] == 'g':
    #         break
    # text = text + ',' + str(count)
    # r = 0
    # b = 0
    # g = 0
    # for j in range(i+1,i+101):
    #     if reversed_sorted[keys[j]]['color'] == 'r':
    #         r += 1
    #     else:
    #         if reversed_sorted[keys[j]]['color'] == 'b':
    #             b += 1
    #         else:
    #             g += 1
    # text += ','+str(r)+','+str(g)+','+str(b)
    # # for j in range(i+1,i+number_before):
    #     text = text + ',' + convert_color(reversed_sorted[keys[j]]['color'])
    # count = 0
    # for j in range(i,key_len):
    #     if reversed_sorted[keys[j]]['color'] != reversed_sorted[keys[i]]['color']:
    #         break;
    #     count += 1
    # text = text + ',' + str(count)+'\n'
    text = text + '\n'
    data.write(text)
data.close()
