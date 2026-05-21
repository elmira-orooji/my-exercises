
def get_user_input():
    height = float(input("Enter your height (m) : "))
    weight = float(input("Enter your weight (kg) : "))
    return height,weight



def bmi_calculation(height,weight):
    bmi = weight // (height * 2)
    return bmi
    

def get_bmi_result(bmi):

    print("your bmi is :",bmi)

    if( 18.5 <= bmi < 25):
        print("Normal")
    
    elif( 25 <=  bmi < 30):
        print("Overweight")
    
    elif( 30 <= bmi < 35):
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