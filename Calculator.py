def calc():
    while True:
        print("\n---Calculator---\n")
        print("Select Operation:  ")
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication ")
        print("4. Division")
        print("5. Exit")

        choice=int(input("\nChoice: "))
        if choice==5:
            print("Exiting the Calculator...")
            break

        n1=int(input("Enter first num: "))
        n2=int(input("Enter second num: "))
    
        if choice==1:
            add(n1,n2)
        elif choice==2:
            sub(n1,n2)
        elif choice==3:
            mul(n1,n2)
        elif choice==4:
            div(n1,n2)
        else :
            print("Please Enter valid input (Any number from the list above)......")

def add(n1,n2):
    ra=n1 + n2
    print("\nThe addition is : ",ra)
    print("Click to continue.....")
    input()

def sub(n1, n2):
    rs=n1 - n2
    print("\nThe Substraction is : ",rs)
    print("Click to continue.....")
    input()

def mul(n1,n2):
    rm=n1 * n2
    print("\nThe Multiplication is : ",rm)
    print("Click to continue.....")
    input()

def div(n1,n2):
    rd=n1 / n2
    print("\nThe Division is : ",rd)
    print("Click to continue.....")
    input()

calc()