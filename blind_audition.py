logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
participant = {}
while True:
  name = input("Enter your name: ")
  price = input("Enter the bid price: $")
  participant[name] = price
  ans = input("Anymore users who want to bid?\nType 'Yes' or 'No'.\n").lower()
  if ans == 'yes':
    continue
  else:
    break

highest_bid = -1
for name in participant:
  bid = int(participant[name])
  if bid > highest_bid:
    highest_bid = bid
  winner = name

print(f"The winner is {winner}!")
