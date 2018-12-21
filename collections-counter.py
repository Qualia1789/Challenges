# Enter your code here. Read input from STDIN. Print output to STDOUT
list = []
global_list=[]
earnings = []
sorted_list = []
raw_input_string = '''10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50'''
raw_input_list = raw_input_string.split('\n')

def raw_input():
    return raw_input_list.pop(0)




if __name__ == '__main__':
    n = int(raw_input())
    size_list = map(int,raw_input().split())
    print(size_list)
    customers = int(raw_input())
    for i in range(0,customers): 
        size, price = map(int,raw_input().split())
        list = [size, price]
        global_list.append(list)
        global_list.sort(key = lambda x: (x[0]), reverse = True)
    print(global_list)

for i in global_list: 
    for x in size_list: 
        if i[0] == x:
            earnings.append(i[1])
            
            
        
print(global_list)
print(size_list)
print(earnings)
revenue = sum(earnings)
print(revenue)

