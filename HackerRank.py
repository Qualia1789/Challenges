global_list = []
numbers = []
numbers2 = []
names = []
list = []
raw_input_string = '''5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39'''
raw_input_list = raw_input_string.split('\n')

def raw_input():
    return raw_input_list.pop(0)


for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    numbers.append(score)
    list = [name,score]
    global_list.append(list)

print(numbers) #works up to here

def takeSecond(score):
    return score[1]

global_list.sort(key=takeSecond) #works up to here


y = min(numbers)
print(y) #works up to here
i = 0
while i < len(global_list): 
    x = global_list[i]
    print(x)
    if x[1] == y:
        global_list.remove(x)
    else:
        i = i + 1

print(global_list)
    

for beta in global_list: 
    numbers2.append(beta[1])

z = min(numbers2)
def alphabetically(name):
    return name[0]
global_list.sort(key=alphabetically)
print(global_list)
for alpha in global_list:
    if alpha[1] == z:
        print(alpha[0])
    

            

