class multiplefunctions():
    def Subfields():
        SubfieldsInAI=["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for i in SubFieldsInAI:
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
        marks=[98,87,95,95,93]
        total_marks=sum(marks)
        total_sub=len(marks)
        percentage=(total_marks/(total_sub *100))*100
        for i in range(len(marks)):
            print(f"Subject{i+1}={marks[i]}")
        print(f"Total: {total_marks}")
        print(f"Percentage: {percentage}")
  

    def AreaOfTriangle():
        height=int(input("Height : "))
        breadth=int(input("Breadth : "))
        area=(height*breadth)/2
        print("Area formula : (Height*Breadth)/2")
        print("Area of Triangle :",area)
    
    def PerimeterOfTriangle():
        height1=int(input("Height1 : "))
        height2=int(input("Height2 : "))
        breadth1=int(input("Breadth : "))
        perimeter=height1+height2+breadth1
        print("Perimeter formula: Heigth1+Height2+Breadth")
        print("Perimeter of Triangle:",perimeter)
