logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


print(logo)
def add(n1, n2):
  return n1 + n2

def substration(n1, n2):
  return n1 - n2

def mulitplication(n1, n2):
  return n1 * n2

def division(n1, n2):
  return n1 / n2

num_1 = float(input("Enter the number: "))
operator = input("+\n-\n*\n/\nSelect an operator: ")
num_2 = float(input('Enter the second number: '))

operation ={
  '+': add,
  '-': substration,
  '*': mulitplication,
  '/': division
 }
calculation = operation[operator]
ans1 = calculation(num_1, num_2)
print(f"{num_1} {operator} {num_2} = {ans1}")

while True:
  proceed = input(f'Type "y" to continue calculating with {ans1}, or type "n" to start a new calculation: ')
  if proceed == 'y':
    num_3 = float(input('Enter the subsequent number: '))
    operator = input("+\n-\n*\n/\nSelect an operator: ")
    calculation = operation[operator]
    ans2 = calculation(ans1, num_3)

    print(f"{ans1} {operator} {num_3} = {ans2}")

    ans1 = ans2

  else:
    break