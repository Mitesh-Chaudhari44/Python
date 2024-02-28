Total = 0
Marks = []
print("Enter Marks Of 5 Courses :")
for i in range(5):
    n = int(input())
    Marks.append(n)
for i in range(5):
    if Marks[i] >= 40:
        a = "pass"
    else:
        a = "fail"
        break
for i in range(5):
    Total = Total + Marks[i]   
Percentage = (Total/500)*100
print(Percentage)
if a == "pass":
    if Percentage >= 75:
        print("Disticnstion")
    elif Percentage >= 60 and Percentage < 75:
        print("First Division")  
    elif Percentage >= 50 and Percentage < 60:
        print("Second Division")
    elif Percentage >= 40 and Percentage < 50:
        print("Third Division")
else:
    print("Fail") 