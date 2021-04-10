# https: // www.codewars.com/kata/56170e844da7c6f647000063/train/python

def people_with_age_drink(age):
    if age < 14:
        return 'drink toddy'
    if 14 <= age < 18:
        return 'drink coke'
    if 18 <= age < 21:
        return 'drink beer'
    if age >= 21:
        return 'drink whisky'


# https: // www.codewars.com/kata/5417423f9e2e6c2f040002ae/train/python
def digitize(n):
    n_str = str(n)
    result_list = []
    for i in range(len(n_str)):
        result_list.append(int(n_str[i]))
    return result_list


print(digitize(235))
