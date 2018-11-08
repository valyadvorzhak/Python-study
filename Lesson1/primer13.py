#Если перед открывающей кавычкой стоит символ 'r' (в любом регистре), то механизм экранирования отключается.

text = 'Текст' 

S = r'C:\newt.txt'
print(S)


#в первом случае пишется "сырой путь", но вконце ставится экранирующий слешь. квадратные скобки следом [:-1] вырезают из полученной строки весь текст кроме последнего символа. таким образом получается строка, завершающаяся слешем, и при этом не нарушающая никаких ограничений.


P = r'\n\n\\'[:-1]
print(P)

#во втором случае с помощью знака "+" конкатенируется (объединяется) сырая строка с несырой, в которой символ "\" экранируется первым слешем
E = r'\n\n' + '\\'
print(E)


#в третьем случае НЕ используется метод сырой строки. поэтому нужно экранировать все нестандартные знаки (к которым относится как перенос каретки, так и сам символ слеша)
Z = '\\n\\n'
print(Z)




#Строки в тройных апострофах или кавычках

c = '''это очень большая
... строка, многострочный
... блок текста'''
print(c)

f='это очень большая\nстрока, многострочный\nблок текста'
print(f)



