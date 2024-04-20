#Python packages are imported at the top of a script
import os

#list all available Python packages
#print(help('modules'))

#common built-in Python data types
strng = 'Hello, World!'
int_num = 1
float_num = 5.0
boolean = True
byte = b'\x00'

#common built-in data structures
data_list = [strng, int_num, float_num, boolean, byte]
data_dictionary = {'String':strng, 'Integer':int_num, 'Flaot':float_num, 'Boolean':boolean, 'Bytes':byte}
data_tuple = (strng, int_num, float_num, boolean, byte)
data_set = {strng, int_num, float_num, boolean, byte}

#the print function outputs information into our terminal
print(f'The data_list is a {type(data_list)}')

#the elements of a list can be iterated over with a for loop
for element in data_list:
    print(f'{element} is a {type(element)}')