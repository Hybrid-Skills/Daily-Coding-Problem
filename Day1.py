def check_number(list,k):
    for i in list:
        list = list[1:]
        if (k - i) in list:
            return True
    else:
        return False


input_list = list(map(int, input('Give the array : \n').split(sep=',')))
k = int(input('Check sum of : '))

if check_number(input_list, k):
    print('yes')
else:
    print('no')
