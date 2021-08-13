# объединить 2 списка в словарь
keys = [1, 2, 3]
values = ['inna', 'boris', 'gleb']
create_dict = dict(zip(keys, values))
print(create_dict)

new_dict = {1: 'tom', 2: 'bob', 'name': 'stas'}
return_key_values = {k: v for k, v in new_dict.items() if k in keys}
print(return_key_values)

s = 'hello'
print('o' in s)
print(s.endswith('o'))
print(s.startswith('o'))
print(s.find('o'))

print(f'{10:>10}')