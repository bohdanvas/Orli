import time
import random

print("Я чую кроки...")
time.sleep(1.5)
print("Хто це?")
time.sleep(1)
print("Не ховайся, вийди та назви себе")
gamer = input()
print("Витаю тебе " + gamer + " у Востбет, звидки ти прибув до нас?  ")
place = ["Бордо?", "Достан?", "Капара?"]
for town in place:
    print(town)
town = input()
if town == "Бордо":
    print("Hiкого ще не зустрiчав з Бордо, однак чув, що це мiсто безстрашних людей. Ти ж один з таких?")
elif town == "Достан":
    print("О, так-так, це чудове мiсто Достан, батькiвшина вiдважних людей. Ти ж один з таких?")
elif town == "Капара":
    print("Багато часу минуло вiдколи я востаннє був в Капарi, у мiстi смiливих людей. Ти ж один з таких?")
else:
    print("Згинь з очей моїх незнайомцю.")
    input()
    quit()
answer = ("так", "ТАК","Так", "нi", "Нi", "НI")
answer = input()
if answer == "так"or "ТАК" or "Так":
    print("Тодi ти та людина, на яку я так довго чекав.")
    time.sleep(2)
    print("Ти вiдправишся на бiй з злим драконом - Гyдо.")
elif answer == "Нi" or "НI" or "нi":
    print("Твоя воля, я помилявся, ти не той про кого мовили мудриці.")
    input()
    quit()
time.sleep(1.2)
print("Обернись на право.")
time.sleep(1.5)
print (" Перед собою ти бачиш три скринi, в кожнiй знаходиться рiч, \
яка знадобиться тобi в твоїй подорожi.")
time.sleep(1)
print("Однак, ти можеш вiдкрити тiльки одну з них. Яку ти обереш?")
time.sleep(1.2)
thing = ["першу", "другу", "третю"]
for Lol in thing:
    print(Lol)
Lol = input()
if Lol == "першу":
    print("Отже, у подорож ти вiзьмеш лук")
elif Lol == "другу":
    print("Тобi дiстається меч")
elif Lol == "третю":
    print("Спис - це саме те що тобi треба")
print("Ти вирушив у подорож")
time.sleep(1)
print("Ти йшов не день i не два, уже збився з лiку.")
time.sleep(1.3)
print("I от перед тобою висока стiна, кiнця-краю якої не видно.")
time.sleep(1.3)
print("Якщо ти смiливий ти ввiйдеш в тунель який веде крiзь стiну.")
ch1 = str(input("Ризикнеш? [т/н]"))
if ch1 in ["Так", "так", "та", "ТАК", "т"]:
    print("Я не помилився в тобi")
else:
    print("Ти обрав невiрний шлях. Ти зустрiв Халка, який розчавив тебе")
    input()
    quit()
print("В тунелi ти натрапив на злого Гоблiна, у тебе немає виходу - ти повинен здолати його")
time.sleep(1.5)
print("Бiй")
pldmg1 = int(random.randint(3, 10))
gobdmg1 = int(random.randint(1, 7))
print ("ти нанiс", pldmg1)
print ("Гоблiн завдав тобi", gobdmg1)
pldmg3 = int(random.randint(3, 10))
gobdmg3 = int(random.randint(1, 7))
print ("ти нанiс", pldmg3)
print ("Гоблiн завдав тобi", gobdmg3)
pldmg2 = int(random.randint(3, 10))
gobdmg2 = int(random.randint(1, 7))
print ("ти нанiс", pldmg2)
print ("Гоблiн завдав тобi", gobdmg2)
pldmg = pldmg1 + pldmg2 + pldmg3
gobdmg = gobdmg1 + gobdmg2 + gobdmg3
if pldmg > gobdmg:
    print("Тобi повезло - ти перемiг!")
elif pldmg < gobdmg:
    print("Тебе перемогли. Ти найшов свою смерть в найтемнiшому мiсцi планети")
print("Ось ще один")
print("Далі буде")
