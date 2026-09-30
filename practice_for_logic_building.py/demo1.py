# Take the input of income , food , rent , travel , recharge , entertainment . calculate total expenses and saving

income = float(input("enter the income "))
rent = float(input("enter the room rent "))
food = float(input("enter the total food expenece"))
travel = float(input("enter the travel cost"))
recharge = float(input("enter the recharge amount"))
enterainment = float(input("enter the enterainment cost"))

total_expenses = rent+food+travel+recharge+enterainment
saving = income-total_expenses

if saving<0:
    print("bhai salary aane se pehle expenses aa gaye")
elif saving==0:
    print("balance zen mode")
elif saving>5000:
    print("future ceo detected")


# let the student enter food item prices repeatedly. enter 0 to stop . do not add the 0 to the total.

total_food_item_cost =0
while True:
    price = float(input("enter the food_item price"))
    if price==0:
        print("total cost of food item ", total_food_item_cost)
        break
    total_food_item_cost=total_food_item_cost+price




