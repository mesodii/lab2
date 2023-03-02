pas = input('Введите пароль')

is_numeric = False
is_lower = False
is_upper = False
is_spec = False

for f in pas:
    if f.isnumeric():
        is_numeric = True
    if f.islower():
        is_lower = True
    if f.isupper():
        is_isupper = True

if len(pas) > 6 and is_numeric and is_lower and is_isupper:
    print("Надежный пароль")
else:
    print('Пароль ненадежный')


