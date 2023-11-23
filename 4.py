try:
    num1 = int(input("number 1 ?"))
    num2 = int(input("number 2 ?"))
    
except ValueError:
    print("You should enter numerical value")
finally:
    print('sum : ',num1 + num2)