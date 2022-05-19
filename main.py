from budget import Budget

def update_f():
    with open ('f_budg.txt', 'w') as file1:
        file1.write(str(food.balance))

def update_c():
    with open ('c_budg.txt', 'w') as file2:
        file2.write(str(clothing.balance))

def update_e():
    with open ('e_budg.txt', 'w') as file3:
        file3.write(str(entertainment.balance))
 
food = Budget(500)
update_f()

clothing= Budget(200)
update_c()

entertainment = Budget(100)
update_e()


print(f'Current food balance is {food}')
print(f'Current clothing balance is {clothing}')
print(f'Current entertainment balance is {entertainment}')

print('\n')
print(food.withdraw(100))
update_f()

print(clothing.withdraw(100))
update_c()

print(entertainment.withdraw(50))
update_e()

print('\n')
print(f'Current food balance is {food}')
print(f'Current clothing balance is {clothing}')
print(f'Current entertainment balance is {entertainment}')

# print(food.withdraw(entertainment.deposit(100)))

