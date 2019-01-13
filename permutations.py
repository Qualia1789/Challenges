from itertools import permutations 

global_list = []
final_list = []

raw_input_string = '''HACK 2'''
raw_input_list = raw_input_string.split('\n')

def raw_input():
    return raw_input_list.pop(0)
    
def permutation(string, n):
    global_list = list(permutations(string, int(n)))
    global_list.sort()
    for i in global_list: 
        final_list.append("".join(list(i)))
    
    print("\n".join(final_list))
    
    


if __name__ == '__main__':
    new_input = raw_input()
    string, n = new_input.split()
    permutation(string,n)