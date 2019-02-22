from myclass import Mobile_phone
from linked_class import Stack

phone_1 = Mobile_phone()
phone_2 = Mobile_phone("red", "Apple", 64, 1)
phone_3 = Mobile_phone("black", "Samsung", 32, 2)
phone_4 = Mobile_phone("white", "Meizu", 64, 2)

my_stack = Stack()
my_stack.push(phone_1)
my_stack.push(phone_2)
my_stack.push(phone_3)
my_stack.push(phone_4)

print(my_stack.length())
my_stack.pop().read_parameters()


print(my_stack.length())
my_stack.peek().read_parameters()
print(my_stack.length())
my_stack.pop().read_parameters()



