#City Infrastructure Management System

class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner
        
        def change_owner(self, new_owner):
              print(f'Transfering title from {self.owner} to {new_owner}!')
              self.owner = new_owner

        def get_info(self):
            print(f'This is a {self.type} vehicle. Registration number: {self.registration_number}. Current owner: {self.owner}')

mustang = Vehicle(10101010, '2 door', 'James Dean')

print()
mustang.get_info()
print('\nWe sold the pony?!?\n')
mustang.change_owner('Donald Duck')
print()
print('Were selling it again...\n')
mustang.change_owner('Isaias Palma')
print()
mustang.get_info()
print()

              
