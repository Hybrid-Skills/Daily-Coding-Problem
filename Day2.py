def div_method(arr):
    product = 1
    for i in arr:
        product *= i
    answer = []
    for j in arr:
        answer.append(product//j)
    return answer


def multiply_method(arr):
    answer = []
    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if j == i:
                pass
            else:
                product *= arr[j]
        answer.append(product)
    return answer


question = list(map(int, input('Put your list here:').split(',')))
print(div_method(question))
print(multiply_method(question))
