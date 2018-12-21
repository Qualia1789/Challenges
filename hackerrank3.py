def test1(s):
    list1 = list(s)
    true_list1 = []
    for x in list1: 
        str(x)
        true_list1.append(x.isalnum()) 
    if any(i == True for i in true_list1):
        return True
    else: 
        return False

def test2(s):
    list2 = list(s)
    true_list2 = []
    for x in list2:
        str(x)
        true_list2.append(x.isalpha())
    if any(i == True for i in true_list2):
        return True
    else: 
        return False

def test3(s):
    list3 = list(s)
    true_list3 = [] 
    for x in list3: 
       str(x) 
       true_list3.append(x.isdigit())
    if any(i == True for i in true_list3):
        return True
    else: 
        return False

def test4(s):
    list4 = list(s) 
    true_list4 = []
    for x in list4: 
       str(x) 
       true_list4.append(x.islower())
    if any(i == True for i in true_list4):
        return True
    else: 
        return False
         
        

def test5(s):
    list5 = list(s)
    true_list5 = []
    for x in list5:
        str(x)
        true_list5.append(x.isupper())
    if any(i == True for i in true_list5):
        return True
    else: 
        return False


 

     
if __name__ == '__main__':
    s = '123'

print(test1(s))
print(test2(s))
print(test3(s))
print(test4(s))
print(test5(s))

