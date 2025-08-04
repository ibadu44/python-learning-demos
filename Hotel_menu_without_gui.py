totalprice=0
user_decision=1
while user_decision ==1:
        food_menu={
            'Appetizer':{"Spring Rolls": '60', "Garlic Bread": '350', "Mozzarella Sticks": '620'},

            "Desserts": {"Chocolate Lava Cake": '700', "Cheesecake": '650'},
            
            'Main Course':{'Small Pizza':'250','Medium Pizza':'500','Large Pizza':'750','Small Pasta':'450','Medium Pasta':'550','Large Pasta':'650','Zinger Burger':'350','Salad':'450'},
            
            "Drinks":{"Coca-Cola": '200', "Fresh Orange Juice": '350', "Coffee": '370'}}

        print('User Access Granted')
        print('''Hi Welcome to our Restaurant IBAD'S Restaurant
        What would you like to order ?
        
        ''')
        print('-------------- Our Restaurant Menu --------------')
        for category, items in food_menu.items():
            print(f"\n--- {category} ---") 
            for item, price in items.items():
                print(f"{item} :{price:}")
        print()
        category=input('Please Enter the category you would like to have : ')
        food=input('\nPlease Enter the Food name you would like to have : ')
        print()
        more_item=int(input('\nWould You Like to order anything else ?\nIF yes Please Press 1 and if you are done press 0 : '))
        totalprice=totalprice+int(food_menu[category][food])
        user_decision=more_item
print('\nYour Total Bill is {} Thank You for shopping with us Come again !'.format(totalprice))