import random
import array

max_len=8
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z' 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
           '*', '(', ')', '<']
final = digits + letters + symbols
rand_digit = random.choice(digits)
rand_letter = random.choice(letters)
rand_symbol = random.choice(symbols)
temp_pass = rand_digit + rand_letter + rand_symbol

for x in range(max_len - 4):
    temp_pass = temp_pass + random.choice(final)
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
password = ""
for x in temp_pass_list:
        password = password + x

print("The password is:")
print(password)