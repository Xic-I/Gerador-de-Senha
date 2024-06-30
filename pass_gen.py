import string
import random

def random_pass(service_name, words):
        rand_word = ''.join(random.choices(words))
        for i in range(27):
            rand_word+=random.choice(words)
        with open("passwords.txt", "a") as file:
            file.write(f"{service_name}: {rand_word}\n")
            file.close
        print(f"{service_name}: {rand_word}")

if __name__ == '__main__':
    words_and_numbers = string.ascii_letters + string.digits
    plataforma = input("Plataforma: ")
    especials = input("Caracteres especiais?\n[Y / N] ")
    if especials.lower() == 'y':
        words_and_numbers = string.ascii_letters + string.digits + string.punctuation
        random_pass(plataforma, words_and_numbers)
    else:
         random_pass(plataforma, words_and_numbers)