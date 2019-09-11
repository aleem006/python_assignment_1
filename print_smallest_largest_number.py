number_list = []
number = int(input('Enter Numbers of Elements  :'))

for i in range(1, number + 1):
    element=int(input("Enter elements: "))
    number_list.append(element)

print(number_list)
number_list.sort()

print("Largest Number is : ", number_list[number-1])
print("Smallest  Number is : ", number_list[0])