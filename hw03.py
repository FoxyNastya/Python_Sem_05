'''Проверка палиндрома. Напишите функцию, которая проверяет, является 
ли строка палиндромом (то есть чистается одинаково) справа налево и слева нараво) 
с использованием рекурсии'''



def palindrom(string):
    reversed_string = ''.join(reversed(string))
    if string == reversed_string:
        return 'yes'
    else:
       return 'no'
    
slovo = str.lower(input("Напечатайте любое слово: "))
print(palindrom(slovo))