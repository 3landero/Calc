from art import logo

def add (n1, n2):
  return n1 + n2

def subs(n1,n2):
  return n1 - n2

def mult(n1,n2):
  return n1 * n2

def div(n1 ,n2):
  return n1 / n2

operations ={
  "+": add,
  "-": subs,
  "*": mult,
  "/": div,
}

print(logo)

print("Welcome to the calculator!")

answer = 0
eternal_loop = False

while eternal_loop == False:  

  if answer !=0:
    first_number= answer
  else:
    first_number= int(input("What´s the first number?\n"))

  
  for op in operations:
    print(op)

  ops = input("Pick an operation from the line above\n")
  second_number= int(input("What´s the next number?\n"))

  calculation_function = operations[ops]
  answer = calculation_function(first_number,second_number)

  print(f"{first_number} {ops} {second_number} = {answer}")

  cont = input(f"Type Y to continue with {answer} or N to start a new calculation\n").upper()

  if cont == "Y":
    answer = answer
  elif cont == "N":
    answer = 0