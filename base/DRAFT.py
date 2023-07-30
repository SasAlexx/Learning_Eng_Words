dic = {
    'hello': 'привіт',
    'hello1': 'привіт',
    'asd': 'asdasd',
    'asdasdsa': 'qweqwe',
}

new_dic = {key: dic[key] for key in dic if key not in ['hello', 'hello1']}

print(new_dic)