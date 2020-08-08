import random

user_input = int(input("How long should the password be?\n"))

char_list = []
for i in range(user_input):
    # generate a random char based on ASCII code
    random_char = chr((random.randint(48, 191)))

    if random_char == ' ':
        random_char = chr((random.randint(48, 191)))

    char_list.append(random_char)

random.shuffle(char_list)
print("Generated password is: ", ''.join(char_list))
