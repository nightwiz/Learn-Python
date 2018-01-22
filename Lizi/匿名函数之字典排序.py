nums = [11, 12345, 22, 32, 18, 78902, 11223344]
nums.sort()
print(nums)

infors = [{"name": "laowang", "age": 10}, {"name": "xiaoming", "age": 9}, {"name": "banzhang", "age": 20}]

# infors.sort() # 报错，字典内有不同类型的数据无法做比较

infors.sort(key=lambda x: x['name'])    # 根据name排序
infors.sort(key=lambda x: x['age'])     # 根据age排序

print(infors)
