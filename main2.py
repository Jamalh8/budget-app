from budget import Budget


def updated_food():
    file1= open ('f_budg.txt','r')
    new_food= int(file1.read())
    file1.close()
    return new_food

def updated_clothes():
    file2= open ('c_budg.txt', 'r')
    new_clothes= int(file2.read())
    file2.close()
    return new_clothes

def updated_ent():
    file3= open ('e_budg.txt', 'r')
    new_ent= int(file3.read())
    file3.close()
    return new_ent

food = Budget(updated_food)
print(updated_food())

clothes = Budget(updated_clothes)
print(updated_clothes())

entertainment = Budget(updated_ent)
print(updated_ent())

# # running = True

# while running:
#     control= input('1:edit burdget')
#     if control ==1:

