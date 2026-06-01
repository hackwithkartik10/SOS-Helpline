import pyfiglet
emer=pyfiglet.figlet_format("H E L P L I N E")
print(emer)
print("Find Emergency Phone Numbers ")
print("--- Created by <> Kartik Panchal ---")
n=input("Enter Service Name : ").lower()
if n == "police":
    print("100")
elif n == "emergency":
    print("112")
elif n == "ambulance":
    print("108")
elif n == "fire":
    print("101")
elif n == "women helpline":
    print("1091")
elif n == "cyber":
    print("1930")
elif n == "railwayrolice":
    print("182")
else:
    print("Helpline Not Found")