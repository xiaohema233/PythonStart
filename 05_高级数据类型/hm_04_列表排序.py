name_list = ["zhangsan", "lisi", "wangwu", "wangxiaoer"]
num_list = [6, 8, 4, 1, 10]
print(name_list)
print(num_list)

# 升序
name_list.sort()
num_list.sort()
print("------升序----------")
print(name_list)
print(num_list)

# 降序
name_list.sort(reverse=True)
num_list.sort(reverse=True)
print("------降序----------")
print(name_list)
print(num_list)

# 逆序（反转）
name_list.reverse()
num_list.reverse()
print("------逆序（反转）----------")
print(name_list)
print(num_list)
