raw_input_string = '''abracadabra
5 k'''
raw_input_list = raw_input_string.split('\n')

def raw_input():
    return raw_input_list.pop(0)
    
def mutate_string(string, position, character):
    l = list(string)
    l[int(position)] = character
    str = ''.join(l)
    return str


if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)