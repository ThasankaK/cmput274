# 1) xs = "Today is a\n" + "good day to learn python"
# print(xs)

# xs = "Today " + "is a \n" + "good day to learn python"
# print(xs)

# xs = "Today is a" + "\n" + "good day to learn python";
# print(xs)

# xs = "Today is a" + "\ngood day to learn python";
# print(xs)
# 2) num1 = input("Enter an integer number: ")
# num2 = input("Enter an integer number: ")
# print(max(num1,num2))
# 5) tempC = input('Enter Temperature in Celsius: ')
# numC = int(tempC)
# tempF = (numC * (9/5)) + 32
# print("{:.1f} degrees Celsius is {} Fahrenheit".format(numC,tempF))

# 5a) tempF = input('Enter Temperature in Fahrenheit: ')
# numF = int(tempF)
# tempC = (numF - 32) * (5/9)
# print("{:.1f} degrees Fahrenheit is {} Celsius".format(numF,tempC))

# 5b) money_cad = int(input('Enter Amount in CAD: '))
# money_usd = money_cad * 0.76
# print("I have {:.2f} CAD which is {} USD".format(money_cad,money_usd))

# 5c) initial = input('What is the initial amount in your account?($) ')
# total = int(initial)*(1+0.025)**5
# print('You will have saved',str(total),'after 5 years')

"""
6) tempC = input('Enter Temperature in Celsius: ')
    numC = int(tempC);
    tempF = (numC * (9/5)) + 32
    print(str(numC) + " degrees in Celsuis " + str(tempC) + " Fahrenheit");
""" 
"""
8) Assignment1 = int(input("Enter Grade for Morning Problems: "));
Assignment2 = int(input("Enter Grade for Weekly Exercises: "));
Assignment3 = int(input("Enter Grade for Assignments: "));
Assignment4 = int(input("Enter Grade for Quizzes: "));
Assignment5 = int(input("Enter Grade for Midterm: "));
Assignment6 = int(input("Enter Grade for Final Exam: ")); 
MorningProblem = Assignment1 * 0.05;
WeeklyExercises = Assignment2 * 0.05;
Assignments = Assignment3 * 0.10;
Quizzes = Assignment4 * 0.20;
Midterm = Assignment5 * 0.25;
FinalExam = Assignment6 * 0.35;
FinalGrade = MorningProblem + WeeklyExercises + Assignments + Quizzes + Midterm + FinalExam;
print(format(FinalGrade, '.2f'))
""" 
