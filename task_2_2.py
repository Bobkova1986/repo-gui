words_list=['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
message = []

for item in words_list:
    if item.replace("+", "").replace("-", "").isdigit():
        if item.isdigit():
            message.append(f'"{int(item):02}"')
        else:
            message.append(f'"{item[0]}{int(item[1:]):02}"')
    else:
        message.append(item)

print(' '.join(message))
