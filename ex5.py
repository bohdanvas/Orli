name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = "Brown"

print("Let's talk about %s." % name)
print("He's %d inches tal./" % height)
print("He's %d pounds heavy." % weight)
print("He's got %s eyes and %s hair." % (eyes, hair))
print("Actually that's not too heavy")
print("His teeth are usually %s depending on the coffee." % teeth)

print("If I add %d, %d and %d I get %d." % (age, height, weight, age + height + weight))

inches_per_centimeters = 2.54
pounds_per_kilo = 0.45359237

print("He's %d centimeters tall." % (height * inches_per_centimeters))
print("He's %d kilos heavy." % (weight * pounds_per_kilo))
