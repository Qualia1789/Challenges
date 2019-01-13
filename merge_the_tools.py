from itertools import groupby

list2 = []
new_list = []
final_list = []
empty_list = []

raw_input_string = '''AABCAAADA
3 '''
raw_input_list = raw_input_string.split('\n')

def raw_input():
    return raw_input_list.pop(0)

def remove_duplicates(list1):
    for i in list1: 
        print(i)
        if i not in empty_list: 
            empty_list.append(i)
            
            
     

def merge_the_tools(string, k):
    list2 = list(string)
    n = len(list2) / k
    for j in range(0,len(list2),int(n)):
        new_list = list2[j:int(j+n)]
        final_list = remove_duplicates(new_list)
        return final_list
        
        
      
            

   
        
    

                

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)