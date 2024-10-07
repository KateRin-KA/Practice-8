first=int(input("Ввелите число 1"))
second=int(input("Ввелите число 2"))
third=int(input("Ввелите число 3"))
if first==second and first==third:
    print(3)
if first == second or first == third or second==third:
    print(2)
if first != second and first != third and second != third:
    print(0)
