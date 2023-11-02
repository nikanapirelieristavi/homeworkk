
# შექმენით ფუნქცია რომელსაც გადაეცემა 3 პარამეტრი(სამკუთხედის გვერდები) 
# და დაპრინტავს "ასეთი სამკუთხედი იარსებებს", 
# ან დაპრინტავს "ასეთი სამკუთხედი ვერ იარსებებს" )

def triangle ():
    first = print(int(input("the first side: ")))
    second = print(int(input("the second side: ")))
    third = print(int(input("the third side: ")))
    print(first)
    print(second)
    print(third)

    if first or second or third <= 0:
        print("this triangle is invalid!")
    else:
        print("success!")

triangle()
    
