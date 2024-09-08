import string
import random


GREEN = "\033[32m"
RESET = "\033[0m"  

if __name__ == '__main__':
    s1 = string.ascii_lowercase  
    s2 = string.ascii_uppercase  
    s3 = string.digits           
    s4 = string.punctuation      
    
    while True:
        try:
            plen = int(input("Enter the length of the password: "))
            break
        except ValueError:
            print("Oops! That's not a valid number. Please try again...")

    
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    
    password = "".join(random.sample(s, plen))

    
    print(f"Your password is: {GREEN}{password}{RESET}")
