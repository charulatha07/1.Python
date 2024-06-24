class multiplefunctions():
    def Subfields():
        SubfieldsInAI=["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for i in SubfieldsInAI:
            print(i)
        
    def OddEven():
        num=int(input("Enter a number: "))
        if(num%2!=0):
            print(num, "is odd Number")
            message = num, "is odd Number"
        else:
            print(num, "is Even Number")
            message = num,"is Even Number"
            return message
     
    def EligibleForM():
        Gender=input("Your Gender : ")
        Age=int(input("Your Age : "))
        if(Gender == "Male" and Age>21):
            message=print("ELIGIBLE")
        elif(Gender=="Female" and Age>18):
            message=print("ELIGIBLE")
        else:
            message=print("NOT ELIGIBLE")
        return message
    
    def percentage():
        Subject1=int(input("Subject1="))
        Subject2=int(input("Subject2="))
        Subject3=int(input("Subject3="))
        Subject4=int(input("Subject4="))
        Subject5=int(input("Subject5="))
        total_marks=Subject1+Subject2+Subject3+Subject4+Subject5
        total_sub=5
        percentage=(total_marks/(total_sub *100))*100
        print(f"Total: {total_marks}")
        print(f"Percentage: {percentage}")
    
    def Triangle():
        height=int(input("Height : "))
        breadth=int(input("Breadth : "))
        area=(height*breadth)/2
        print("Area formula : (Height*Breadth)/2")
        print("Area of Triangle :",area)
        height1=int(input("Height1 : "))
        height2=int(input("Height2 : "))
        breadth1=int(input("Breadth : "))
        perimeter=height1+height2+breadth1
        print("Perimeter formula: Heigth1+Height2+Breadth")
        print("Perimeter of Triangle:",perimeter)
   