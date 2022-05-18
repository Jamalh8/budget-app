from budget import Budget

food = Budget(500)
clothing= Budget(200)
entertainment = Budget(100)

print(f'Current food balance is {food}')
print(f'Current clothing balance is {clothing}')
print(f'Current entertainment balance is {entertainment}')
print(food.deposit(100))
print(clothing.withdraw(100))