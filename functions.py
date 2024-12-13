def find_winner(name1, name2, value1, value2):

    if value1 > 21 and value2 > 21:
        print("Both players are over 21. It's a draw!")
    elif value1 > 21:
        print(f"{name2} won!")  
    elif value2 > 21:
        print(f"{name1} won!")  
    elif value1 == value2:
        print("Draw")  
    elif value1 > value2:
        print(f"{name1} won!")  
    else:
        print(f"{name2} won!")  