import json, operator

def process_json_file(file):
    '''
It will remove duplicates and return sorted list, middle
element as root of binary tree.
    '''
    data_list = []
    #open json file here
    with open('{0}'.format(file), 'r') as data_dict:
        data = json.load(data_dict)

    # remove duplicate items
    data_list = [dict(t) for t in set([tuple(d.items()) for d in data])]

    #sort the list
    sorted_list = sorted(data_list, key=operator.itemgetter('score'))

    # now find the middle element
    middle = (len(data_list) + 1) // 2
    root = data_list[middle]
    #remove the item from data_list
    data_list.remove(root)
    root = root['score']
    return data_list, root

if __name__=='__main__':
    process_json_file(file)
