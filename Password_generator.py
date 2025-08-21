import random    # this import random values
import string

def passw_generator(length: int = 10):
   alphabet = string.ascii_letters + string.digits + string.punctuation

   # ''.join(...) = concatenates the randomly chosen characters
   password = ''.join(random.choice(alphabet) for i in range(length)) 
   return password

y = int(input("enter length of the password: "))

x = passw_generator(y)
print("generated password: ", x) 
 