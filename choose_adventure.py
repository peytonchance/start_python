import random
first_name = input("What is your first name?")

print("Hello " + first_name + "! I'm the matchmaker and I want to find you somebody to love.")

pref = input("Do you like boys or girls?")

if pref.lower() in ['boys', 'boy']:
    print("Cool, I know just the guy.")
    dinner = input("This is Kevin. He's perfect for you...I think. Just one question remains: where do you want to go for dinner? Chipotle or Med Deli?")
    if dinner.lower() in ['chipotle', 'chip', 'c', 'mexican', 'burrito']:
        print("Kevin LOVES Chipote. Enjoy your happily ever after!")
    elif dinner.lower() in ['med deli', 'med', 'mediterranean deli', 'deli', 'meddeli']:
        print("Kevin is banned from Med Deli for life...YIKES! You found out his secret. It will never work.")
    else:
        print("That wasn't an option...sorry!")

elif pref.lower() in ['girls', 'girl']:
    print("Awesome, I know just the girl.")
    dinner = input("This is Carla. She's perfect for you...I think. Just one question remains: what movie do you want to see? The Post or Coco?")
    if dinner.lower() in ['the post', 'post', 'the']:
        print("Carla thinks the New York Times deserves more credit for the Pentagon Papers...YIKES! This date could get messy.")
    elif dinner.lower() in ['coco', 'co co']:
        print("Carla LOVES Coco because it is the best cartoon musical movie of our generation. I can hear wedding bells ringing!")
    else:
        print("That wasn't an option...sorry!")
else:
    print("You're right, gender is a social construct. I'll pick from the whole list!")
    choice = random.randint(0, 1)
    if choice == 0:
        dinner = input("This is Kevin. He's perfect for you...I think. Just one question remains: where do you want to go for dinner? Chipotle or Med Deli?")
        if dinner.lower() in ['chipotle', 'chip', 'c', 'mexican', 'burrito']:
            print("Kevin LOVES Chipote. Enjoy your happily ever after!")
        elif dinner.lower() in ['med deli', 'med', 'mediterranean deli', 'deli', 'meddeli']:
            print("Kevin is banned from Med Deli for life...YIKES! You found out his secret. It will never work.")
    else:
        dinner = input("This is Carla. She's perfect for you...I think. Just one question remains: what movie do you want to see? The Post or Coco?")
        if dinner.lower() in ['the post', 'post', 'the']:
            print("Carla thinks the New York Times deserves more credit for the Pentagon Papers...YIKES! This date could get messy. I'll go ahead and cancel it.")
        elif dinner.lower() in ['coco', 'co co']:
            print("Carla LOVES Coco because it is the best cartoon musical movie of our generation. I can hear wedding bells ringing!")
        else:
            print("That wasn't an option...sorry!")
