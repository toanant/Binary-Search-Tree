from bst import Node
from clean import process_json_file


def get_results(file):
    '''
    Pass file name to get result of both Problems.
    '''
    data,root =process_json_file('{0}'.format(file))

    root = Node(root)
    for value in data:
        root.insert(value['score'])

    height = root.maxDepth(root)
    unique_value = len(data) + 1 # Since Middle element is removed as root Node.

    print "Height of Standard Binary Tree is : {0}".format(height)
    print 'Unique dict values are : {0}'.format(unique_value)

if __name__=='__main__':
    get_results(file)
