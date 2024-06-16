# 初始化字典 tel
tel = {'jack': 4098, 'sape': 4139}

# 添加一个新条目 'guido'
tel['guido'] = 4127
print(tel)  # 字典 tel 的当前内容

# 键为 'jack' 的值
print(tel['jack'])

# 删除键为 'sape' 的条目
del tel['sape']

# 添加一个新条目 'irv'
tel['irv'] = 4127
print(tel)  # 更新后的字典 tel

# 字典 tel 的键列表
print(list(tel))

# 字典 tel 的排序键列表
print(sorted(tel))

# 检查 'guido' 是否在字典 tel 中
print('guido' in tel)

# 检查 'jack' 是否不在字典 tel 中
print('jack' not in tel)
