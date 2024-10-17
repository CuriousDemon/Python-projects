# Declare Menu
menu = {
    "Egg Roll" : 35,
    "Egg Chowmin" : 40,
    "Chicken Chowmin" : 50,
    "Alu Biriyani" : 60,
    "Chicken Biriyani" : 100,
}

total = 0

item_list = {}

def display_menu(menu_item):
    print("*"*10)
    for item,price in menu_item.items():
        print(item," = ",price)
    print("*"*10)

def display_order_item(item_lis,menu_item):
    print("*"*10)
    print("Order items ")
    for item,no in item_lis.items():
        print(f"{item} X {no} = {menu_item[item]*no}")
    print("*"*10)


def main_function():
    #Delclare order dictionary
    # ordered = {}   
    while(True):
        global total
        #display menu
        display_menu(menu)
        print("For exit : (-1)")
        try:
            item = input("Enter item name : (for exit type -1)")
            num = int(input("How many you want to order ? : (for exit type -1)"))
        except:
            print("Please enter valid input !!")
            continue
        if (item == '-1' and num == -1):
            break
        if item in menu:
            total += menu[item]*num
            if(item not in item_list):
                item_list[item] = num
            else:
                item_list[item] += num
        else:
            print("Please enter valid item !!")
            continue
        try:
            choice = input("Do you want to order again : (y/n) ")
        except:
            print("Please enter valid input !!")
            continue
        if (choice == 'y'):
            continue
        if(choice == 'n'):
            display_order_item(item_list,menu)
            print("Total payble amount is = ",total)
            break

if(__name__ == "__main__"):
    main_function()
        



