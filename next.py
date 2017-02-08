import random
print("Бiй")
print("Куди нанесеш цлар?")
where = ["голова", "тулуб", "лапи"]
голова = int(random.randint(5, 10))
тулуб = int(random.randint(3, 7))
лапи = int(random.randint(1, 4))
for part in where:
    print(part)
part = input()
if part == "голова":
    print("Ти завдав" + str(голова))
for part in where:
    print(part)
part = input()
if part == "тулуб":
    print("Ти завдав" + str(тулуб))
pldmg = (str(голова) or str(тулуб) or str(лапи) + str(лапи) or str(голова) or str(тулуб))
print(pldmg)
