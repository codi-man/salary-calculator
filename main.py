#This function will calculate the amount of salary of each employee by multiplying the number of hours with hourly rate.
#This function can also be used to those things that requires the same programming

#Enter the amount of employees
employees = int(input("Enter number of employee(s): "))

#Create a main function
def main():
    hours = [0]*employees

    for index in range(employees):
        print('Enter the hours worked by employee #', index + 1, ': ', sep='', end='')
        hours[index] = float(input())

    #Enter the amount of money the employees are paid hourly
    pay_rate = float(input('Enter the hourly pay rate: '))

    #Multiply the number of hours with hourly rate to get the salary's amount
    for index in range(employees):
        gross_pay = hours[index]*pay_rate
        print('Gross pay for employee ', index + 1, ': $', format(gross_pay, ',.2f'), sep='')

#Call the main function
main()