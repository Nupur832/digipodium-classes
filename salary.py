name = input("Enter name of employee: ")
days = int(input("Enter no of days present: "))
wages = int(input("enter wages per days:"))
sal = wages * days
if sal > 100000:
    HRA = sal*9.1
    DA = sal*3.5
    finalsalary = sal+HRA+DA
    print("\nsal:%1f \nHRA:%1f \nDA:%1f \nfinalsalary:%1f" %(sal,HRA,DA,finalsalary))
elif sal > 80000:
    HRA = sal*9
    DA = sal*3.2
    finalsalary = sal+HRA+DA
    print("\nsal:%1f \nHRA:%1f \nDA:%1f \nfinalsalary:%1f" %(sal,HRA,DA,finalsalary))
elif sal > 60000:
    HRA = sal*9
    DA = sal*2.8
    finalsalary = sal+HRA+DA
    print("\nsal:%1f \nHRA:%1f \nDA:%1f \nfinalsalary:%1f" %(sal,HRA,DA,finalsalary))
elif sal > 50000:
    HRA = sal*8
    DA = sal*2.5
    finalsalary = sal+HRA+DA
    print("\nsal:%1f \nHRA:%1f \nDA:%1f \nfinalsalary:%1f" %(sal,HRA,DA,finalsalary))
elif sal > 40000:
    HRA = sal*7.7
    DA = sal*2.5
    finalsalary = sal+HRA+DA
    print("\nsal:%1f \nHRA:%1f \nDA:%1f \nfinalsalary:%1f" %(sal,HRA,DA,finalsalary))
elif sal > 30000:
    HRA = sal*8
    DA = sal*2.2
    finalsalary = sal+HRA+DA
    print("\nsal:%1f \nHRA:%1f \nDA:%1f \nfinalsalary:%1f" %(sal,HRA,DA,finalsalary))
elif sal > 20000:
    HRA = sal*7
    DA = sal*2.2
    finalsalary = sal+HRA+DA
    print("\nsal:%1f \nHRA:%1f \nDA:%1f \nfinalsalary:%1f" %(sal,HRA,DA,finalsalary))
elif sal > 10000:
    HRA = sal*6
    DA = sal*2.2
    finalsalary = sal+HRA+DA
    print("\nsal:%1f \nHRA:%1f \nDA:%1f \nfinalsalary:%1f" %(sal,HRA,DA,finalsalary))





