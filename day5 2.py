def salarycalculation(grade,salary):
    if(salary>10000):
        if(grade=='a'):
            salary=salary+(salary/5)
            print(salary)
        elif(grade=='b'):
            salary=salary+(salary/10)
            print(salary)
    else:
        if(grade=='a'):
            salary=salary+(salary/7)
            print(salary)
        elif(grade=='b'):
            salary=salary+(salary/12)
            print(salary)
grade=input("enter the grade of your employee"+"like'a'or'b'")
salary=int(input("enter your employee salary"))
salarycalculation(grade,salary)
            
