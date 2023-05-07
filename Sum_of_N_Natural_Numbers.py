'''  Write a Function Which Returns the Sum of First N naturals Numbers '''

def Sum_N_Natural(n):
    return n*(n+1)//2

number = int(input("Enter the Number : "))
print("The sum of  first N natural Numbers is : ",Sum_N_Natural(number))

''' This above  function takes constant time because no work is done N times  
    Only multiplication and division are done which are constant operations'''