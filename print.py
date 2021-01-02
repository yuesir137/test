
def twoSum(nums, target: int):
    hashmap = {}  # 建立字典
    for i, num in enumerate(nums):
        hashmap[num] = i  # 储存列表中每个值的位置
    print(hashmap)
    for i, num in enumerate(nums):
        j = hashmap.get(target-num)  # 获取差值在列表中的位置
        if j is not None and i!=j:  # 判断差值在不在列表中，并且保证是不同的两数
            return [i, j]
nums=[2,7,23,34]
target=9
print(twoSum(nums,target))
map={2:1,7:2}
print(map.get(7))


'''函数内修改列表的值
List=["a","b"]
def change(List):
    temp=[]
    while List:
        l=List.pop()
        l=l+"c"
        temp.append(l)
    while temp:
        List.append(temp.pop())
change(List)
print(List)'''
