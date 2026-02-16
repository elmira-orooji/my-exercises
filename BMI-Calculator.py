
def get_user_input():
    height = float(input("Enter your height (m) : "))
    weight = float(input("Enter your weight (kg) : "))
    return height,weight



def bmi_calculation(height,weight):
    bmi = weight // (height * 2)
    return bmi
    

def get_bmi_result(bmi):

    print("your bmi is :",bmi)

    if(bmi <= 18.5 and bmi <= 24.9):
        print("Normal")
    
    elif(bmi <= 25 and bmi >= 29.9):
        print("Overweight")
    
    elif(bmi <= 30 and bmi >= 24.9):
        print("Obese")
    
    elif(bmi < 18.5):
        print("Underweight")

    else:
        print("Extremely obese")


def main():
   
   height,weight = get_user_input()
   bmi = bmi_calculation(height,weight)
   get_bmi_result(bmi)

if __name__ == "__main__":
    main()