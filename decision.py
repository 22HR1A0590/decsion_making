# decsion_making
'''1)Get two integers x and y from the user and write a program to relate 2 integers as equal to, less than or greater than.
Input format:
Input consist of 2 integers
The first input corresponds to  the first number.(a)
The second input corresponds to the second number.(b)
Output format:
If the first number is equal to the second number, print "x and y are equal". Otherwise, print "x greater than y" or "x less than y"
Sample Input:
6
8
Sample Output:
6 less than 8'''

Ans:
x = int(input())
y = int(input())
if x == y:
    print(f"{x} and {y} are equal")
elif x > y:
    print(f"{x} greater than {y}")
else:
    print(f"{x} less than {y}")

'''2)Write a program to check whether the given character is vowel or consonant.
Input format:
The input consist of a character
Output format:
The output consists of a below-given string
“Vowel” / “Consonant” / “Not an alphabet”
Sample Input:
e
Sample Output:
Vowel'''

Ans:
a=input()
if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u'):
    print('Vowel')
elif(a>'a' and 'a'<a):
    print("Consonant")
else:
    print("Not an alphabet")

''' 3)The newly appointed Vice-Chancellor of Anna University wanted to create an automated grading system for the students to check their grade. When a student enters a mark, the grading system displays the corresponding grade.
Write a program to solve the given problem.
  Marks scored  
  Grade 
100
S
90 - 99
A
80 - 89
B
70 - 79
C
60 - 69
D
50 - 59
E
<50
F
Input format:
The input consists of one integer which corresponds to the marks scored by the student
Output format:
If a student marks greater than 100, print "Invalid Input". Otherwise, print the grade.
Sample Input:
78
Sample Output:C'''

Ans:
def determine_grade(marks):
    if marks > 100:
        return "Invalid Input"
    elif marks == 100:
        return "S"
    elif 90 <= marks <= 99:
        return "A"
    elif 80 <= marks <= 89:
        return "B"
    elif 70 <= marks <= 79:
        return "C"
    elif 60 <= marks <= 69:
        return "D"
    elif 50 <= marks <= 59:
        return "E"
    else:  # marks < 50
        return "F"
marks = int(input())
grade = determine_grade(marks)
print(grade)

'''4) A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00'''
 
 Ans:
def calculate_profit_or_loss(cost, selling_price_per_banana):
    total_cost = cost
    total_selling_price = selling_price_per_banana * 12
    profit_or_loss = total_selling_price - total_cost
    return profit_or_loss
cost = float(input())
selling_price_per_banana = float(input())
result = calculate_profit_or_loss(cost, selling_price_per_banana)

'''5)Write a program to determine the fee amount to be collected from a student. 
Refer the table below for fee details.
  Student Type  
  Student Type denoted as  
  Fee Details  
Merit Seat Day Scholar
MSDS
Tuition fee + Bus fee
Merit Seat Hosteller
MSH
Tuition fee + Hostel fee
Management Seat Day Scholar
MGSDS
150% of Tuition fee + Bus fee
Management Seat Hosteller
MGSH
150% of Tuition fee + Hostel fee
Input format:
The first input corresponds to the student type
The second input corresponds to the tuition fee
The third input corresponds to the bus fee or hostel fees
Output format:
Print the total fee amount of the corresponding student with 2 decimal places.
Refer below sample output for formatting
Sample Input:
MSH
40000
50000
Sample Output:
90000.00'''

Ans:

def calculate_fee(student_type, tuition_fee, additional_fee):
    if student_type == "MSDS":
        # Merit Seat Day Scholar
        total_fee = tuition_fee + additional_fee
    elif student_type == "MSH":
        # Merit Seat Hosteller
        total_fee = tuition_fee + additional_fee
    elif student_type == "MGSDS":
        # Management Seat Day Scholar
        total_fee = (1.5 * tuition_fee) + additional_fee
    elif student_type == "MGSH":
        # Management Seat Hosteller
        total_fee = (1.5 * tuition_fee) + additional_fee
    else:
        return None  # Invalid student type

    return total_fee
student_type = input().strip()
tuition_fee = float(input())
additional_fee = float(input())
total_fee = calculate_fee(student_type, tuition_fee, additional_fee)

'''6)Ask a user for their birth year encoded as two digits (like "62") and for the current year, also encoded as two digits (like "99"). Write a program to find the users current age in years.
Input format:
Input consists of 2 integers
The first integer corresponds to the last 2 digits of the birth year
The second integer corresponds to the last 2 digits of the current year
Output format:
Print the user's current age
Refer below sample output for formatting.
Sample Input:
62
00
Sample Output:
38'''

Ans:
def calculate_age(birth_year, current_year):
    if current_year >= birth_year:
        age = current_year - birth_year
    else:
        age = (100 + current_year) - birth_year
    return age
birth_year = int(input())
current_year = int(input())
full_birth_year = 1900 + birth_year if birth_year >= 50 else 2000 + birth_year
full_current_year = 2000 + current_year
age = calculate_age(full_birth_year, full_current_year)
print(age)

'''7)There are 3 labs in the CSE department(L1, L2, and L3) with a seating capacity of x, y, and z respectively. Find the lab which has minimal seating capacity.  
Input format:
Input consists of 3 integers
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
Output format:
Print the minimal seating lab capacity
Refer the Sample output for formatting
Sample Input:
30
40
20
Sample Output:
L3'''

Ans :
L1=int(input())
L2=int(input())
L3=int(input())
if((L1<L2) and (L1<L3)):
    print("L1")
elif(L2<L3 and L2<L1):
    print("L2")
else:
    print("L3")

'''8)There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z respectively. One of the 3 labs has been allocated for ACE training. Out of the available labs, find the lab which has minimal seating capacity.
Input format:
Input consists of 3 integers and a string
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the lab which is allocated for ACE training
Output format:
Print the minimal seating capacity lab amongst the available labs.
Refer the Sample output for formatting
Sample Input:
30
40
20
L3
Sample Output:
L1'''

Ans:
def find_min_capacity_lab(capacities, allocated_lab):
    if allocated_lab in capacities:
        del capacities[allocated_lab]
    min_lab = min(capacities, key=capacities.get)
    return min_lab
a = int(input())  
b = int(input())  
c = int(input())  
allocated_lab = input().strip()  # Lab allocated for ACE training
capacities = {
    "L1": a,
    "L2": b,
    "L3": c
}
result_lab = find_min_capacity_lab(capacities, allocated_lab)
print(result_lab)

'''9)There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z. A single lab needs to be allocated to a class of 'n' students. How many of the 3 labs can accommodate 'n' students?
Input format:
Input consists of 4 integers
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the number of students(x)
Output format:
Print the number of labs which can accommodate the 'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
2 '''

Ans:
def count_accommodating_labs(capacities, students):
    count = 0
    for capacity in capacities:
        if capacity >= students:
            count += 1
    return count


a = int(input("Enter seating capacity of L1: "))  
b = int(input("Enter seating capacity of L2: "))  
c = int(input("Enter seating capacity of L3: "))  
students = int(input("Enter the number of students: ")) 
capacities = [a, b, c]
result_count = count_accommodating_labs(capacities, students)
print(result_count)

'''10) There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
L1

Ans:
def find_suitable_lab(capacities, students):
    suitable_labs = {}
    for lab, capacity in capacities.items():
        if capacity >= students:
            suitable_labs[lab] = capacity  
        if suitable_labs:
        max_lab = max(suitable_labs, key=suitable_labs.get)
        return max_lab
    else:
        return None 
x = int(input("Enter seating capacity of L1: "))  
y = int(input("Enter seating capacity of L2: ")) 
z = int(input("Enter seating capacity of L3: "))  
n = int(input("Enter the number of students: "))  
capacities = {
    "L1": x,
    "L2": y,
    "L3": z
}
result_lab = find_suitable_lab(capacities, n)
if result_lab:
    print(result_lab)
else:
    print("No suitable lab available")






















