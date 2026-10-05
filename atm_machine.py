# Thank you for using my program
import time

bal = 99
in_put = 99

print("ATM starting.", end="")
time.sleep(0.5)

print("\rATM starting..", end="")
time.sleep(0.5)

print("\rATM starting...", end="")
time.sleep(0.5)

print("\rATM starting.   ")

while True:
     
    in_put = float(input("What would you like to to do sir(0 to quit 1 to see controls):"))

    if in_put == 1:
        print("Press 2 to Deposit money")
        print("Press 3 to Withdraw money")
        print("press 4 to check balance")
    
    if in_put == 2:
        
        in_put = float(input("How much money do you like do deposit:"))
        bal = bal + in_put
        print(f"Your new bal is${bal:+,.2f}")
        float(input("What would you like to to do sir(0 to quit 1 to see controls):"))

    if in_put == 3:

        in_put = float(input("How much money do you like do withdraw:"))
        bal = bal - in_put
        print(f"Your new bal is${bal:+,.2f}")
        float(input("What would you like to to do sir(0 to quit 1 to see controls):"))

    if in_put == 4:
        print(f"Your bal is${bal:+,.2f}")
        float(input("What would you like to to do sir(0 to quit 1 to see controls):"))

    if in_put == 0:
        break
print("goodbye")

# have a nice day
    
