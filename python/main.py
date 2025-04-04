
class Calculator:
    def add(self, a , b):
        return a + b
    
    def sub(self , a , b):
        return a - b

    def mult(self,a , b):
        return a * b
    
    def divide(self, a , b):
        try:
            
            if(b != 0):
                c = a / b
                return c
            else:
                print("You can't divide the number by zero !")
        except ValueError:
            print("Please Enter a right digit")

b1 = Calculator()

while True:
    try:
        x = float(input("Enter the first value: "))
        y = input("Enter the operator :")

        z = float(input("Enter the seconnd value :"))
        if(y == "+" ):
            result = b1.add(x,z)
        
        elif(y == "-"):
            result = b1.sub(x,z)
        
        elif(y == "*"):
            result =  b1.mult(x,z) 
              

        elif(y == "/"):
            result = b1.divide(x,z)


        print(f"result is {result}")    
       
    except ValueError:
        print("please Enter a valid number !!")
    check = input("Do you want to use calc (y/n) :")
    if(check == "n"):
        break
    
