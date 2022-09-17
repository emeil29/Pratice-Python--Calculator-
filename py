def add(n1, n2):
    return n1+n2
def subtract(n1, n2):
    return n1-n2    
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2

operation ={
    "+" : add,
    "-" :subtract,
    "*" : multiply,
    "/" :divide
}
num1 = int(input('What is your first number '))
num2 = int(input('What is your next number '))


for key in operation:
   print(key)
operation_key = input("Pick up an operation from the list above \n")
calc = operation[operation_key]
answer= calc(num1, num2)
print(answer)
