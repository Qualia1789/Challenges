from itertools import combinations

global_list = []
final_list = []
number_list = []
answer = []

raw_input_string = '''HACK 2'''
raw_input_list = raw_input_string.split('\n')

def raw_input():
    return raw_input_list.pop(0)



    
def combine(string, n):
    m = int(n) + 1
    number_list = list(range(1,m))
    word_input = sorted(list(string))
    for x in number_list: 
        global_list.append(list(combinations(word_input, x)))
        print(global_list)
    final_list = [j for i in global_list for j in i] # this adds two sublists together
    for t in final_list: 
        answer.append("".join(list(t)))
    return "\n".join(answer)
    
        

    
    


if __name__ == '__main__':
    new_input = raw_input()
    string, n = new_input.split()

    print(combine(string,n))

    