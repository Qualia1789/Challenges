from itertools import product

cartesian_list = []
joined_list = []
raw_input_string = '''1 2
 3 4'''
raw_input_list = raw_input_string.split('\n')

def raw_input():
    return raw_input_list.pop(0)

if __name__ == '__main__':
    A = map(int,raw_input().split())
    B = map(int,raw_input().split())

joined_list = [A,B]

cartesian_list = list(product(*joined_list))
for i in cartesian_list: 
    print(i),