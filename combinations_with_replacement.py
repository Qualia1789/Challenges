from itertools import combinations_with_replacement

raw_input_string = '''HACK 2'''
raw_input_list = raw_input_string.split('\n')

def raw_input():
    return raw_input_list.pop(0)
    
def combination(string, n):
    global_list = []
    final_list = []
    input_list = []
    input_list = list(string)
    input_list.sort()
    global_list = list(combinations_with_replacement(input_list, int(n)))
    print(global_list)
    for i in global_list: 
        final_list.append("".join(list(i)))
        
    return final_list
    


if __name__ == '__main__':
    new_input = raw_input()
    string, n = new_input.split()
    print(combination(string,n))