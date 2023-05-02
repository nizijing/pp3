
def test1():
    '''使用列表推导'''
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    vector = [ele for row in matrix for ele in row]
    print(vector) # [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test2():
    '''使用 * '''
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    (arr1, *middle_arr, arr2) = arr
    print(arr1, middle_arr, arr2) # 1 [2, 3, 4, 5, 6, 7, 8] 9


test1()
test2()
