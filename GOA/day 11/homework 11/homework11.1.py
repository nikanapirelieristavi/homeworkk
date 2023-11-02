#შექმენით ფუნქცია რომელსაც გადაეცემა სამი სახელი (სამი პარამეტრი) და დაპრინტავს ამ სახელებისგან სიას ( join ან split) გაიხსენეთ
def restaurant_bill(name,bill,place):
    print(f"Hello {name}")   # f stringi romeligac funqciebis videoshi vswavle 
    print(f"your bill is {bill} and complete your payment at {place}")
restaurant_bill("nika", 100, "chipotle")
# ori varianti gavakete arvici romelia swori

def greet_all(people):
    for person in people:
        print("Hello " + person)
friends = ["nika, rati, luka"]
greet_all(friends)
