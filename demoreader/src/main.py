from art import MENU,resources

item_data = []
is_resource_finished = False
is_money_less = False
do_want_exit = False
current_choosing_option = ''
'''we are going to create a method that will add all the item in the dictionary into
the empyt list called item_data'''
def convertData():
  for item in MENU:
    item_data.append(item)


'''to work with the coins or the money we are creating this method
which will take some user input and calculate it'''
def calculateCoint():
  # to store the total dolar we are going to create a variable called total
  total = 0
  total += int(input("how many quarters?:"))*0.25
  total += int(input("how many dimes?:"))*0.10
  total += int(input("how many nickles?:"))*0.05
  total += int(input("how many pennies?:"))*0.01
  print(f"the money i have put {total}")
  return total
# TODO 2: we also need to update our logic like when something is orders the MENU
# should also be changed or updated

'''now i am going to create another mehtod that will show the resources and also going to
show the money that you have paid to get the drink or food'''
def showResources(user_choosing_food):
    # nwo i am going to check the current choosing is empty or not ..
    if current_choosing_option == '':
        for item in resources:
            print(item , ":" , resources[item],"kg")
        # now i am going to check if the user option is matchin with the item_data variable
        if user_choosing_food in item_data:
            print(f"Money: {MENU[user_choosing_food]['cost']}" )
        else:
            print(f"Money: {0}$" )
    else:
        # TODO 1 : we need to change this logic and think of a better on..
        if current_choosing_option == "espresso":
            print(f"Water{MENU[current_choosing_option]['ingredients']['water']}")
            print(f"Coffe: {MENU[current_choosing_option]['ingredients']['coffee']}")
        else:
            print(f"Water:{MENU[current_choosing_option]['ingredients']['water']}")
            print(f"Milk:{MENU[current_choosing_option]['ingredients']['milk']}")
            print(f"Coffee:{MENU[current_choosing_option]['ingredients']['coffee']}")
        print(f"Money: {MENU[current_choosing_option]['cost']}" )


'''now i am going to creat another that will check the resource 
which user have orderd before doing anything'''
def checkingResource(user_choosing_food):
    # print(MENU[user_choosing_food]['ingredients']['milk'])
    total = 0
    if user_choosing_food == "espresso":
        if MENU[user_choosing_food]['ingredients']['water']<= resources['water'] and MENU[user_choosing_food]['ingredients']['coffee']<= resources['coffee']:
            is_resource_finished = False
        else:
            is_resource_finished = True
    else:
        if MENU[user_choosing_food]['ingredients']['water']<= resources['water'] and MENU[user_choosing_food]['ingredients']['milk']<= resources["milk"] and MENU[user_choosing_food]['ingredients']['coffee']<= resources['coffee']:
            is_resource_finished = False
        else:
            is_resource_finished = True
    return is_resource_finished


'''now we need to check if the money is suffecient with the inserted money
that user inserted inside the machine for ordering the food'''
def checkingValidationMoney(money):
    if MENU[user_choosing_food]['cost'] == money:
        is_money_less = False
    elif MENU[user_choosing_food]['cost'] < money:
        changed_money = money - MENU[user_choosing_food]['cost']
        print(f"Here is {changed_money}$")
        is_money_less = False
    elif MENU[user_choosing_food]['cost']> money:
        is_money_less = True
    return is_money_less



'''now i am going to create another method that will create the 
thing that users orders by checking everything is okay like the 
resource isn't empty or money isn't valid'''
def making_the_food(is_resource_finished,is_money_less):
    if (not is_resource_finished) and (not is_money_less):
        checkingDrink(current_choosing_option)
        print(f"Here is your {user_choosing_food}. Enjoy!")
    else:
        print("The resource or money isn't suuffecient")

'''to printing the document we are going to create a method that will do this'''
def desplayDetail(user_choosing_food,is_resource_finished):
    # print(is_resource_finished)
    is_resource_finished = checkingResource(user_choosing_food)
    if not is_resource_finished:
        # calculateCoint()
        total = calculateCoint()
        is_money_less =  checkingValidationMoney(total)
        if not is_money_less:
            making_the_food(is_resource_finished, is_money_less)
        else:
            print("Soory that's not enough money")
    else:
        resource = ''
        if resources['water'] < MENU[current_choosing_option]['ingredients']['water']:
            resource = 'water'
        elif resources['milk']< MENU[current_choosing_option]['ingredients']['milk']:
            resource = 'milk'
        else:
            resource = 'coffee'
        print(f"Sorry  there is not enough {resource}")

'''now i am going to create another function that will update the resource after the 
user buying some drink'''
def checkingDrink(option):
    sub1 =0
    sub2 = 0
    sub3 = 0
    if option == "espresso":
        sub1 = MENU[option]['ingredients']['water'] - resources['water']
        sub2 = MENU[option]['ingredients']['coffee'] - resources['coffee']
        resources['water'] = sub1
        resources['coffee'] = sub2
    else:
        sub1 = MENU[option]['ingredients']['water'] - resources['water']
        sub2 = MENU[option]['ingredients']['coffee'] - resources['coffee']
        sub3 = MENU[option]['ingredients']['milk'] - resources['milk']
        resources['water'] = sub1
        resources['milk'] = sub3
        resources['coffee']  = sub2

while not do_want_exit:
    user_choosing_food = input("What would you like?  (espresso/latte/cappuccino):").lower()
    convertData()
    if user_choosing_food == "report":
        showResources(user_choosing_food)
    elif user_choosing_food == str(item_data[0]):
        current_choosing_option = user_choosing_food
        desplayDetail(user_choosing_food, is_resource_finished)
    elif user_choosing_food == item_data[1]:
        current_choosing_option = user_choosing_food
        desplayDetail(user_choosing_food,is_resource_finished)
    elif user_choosing_food == (item_data[2]):
        current_choosing_option = user_choosing_food
        desplayDetail(user_choosing_food, is_resource_finished)
    elif user_choosing_food == "exit":
        do_want_exit = True
    # print(resources)

