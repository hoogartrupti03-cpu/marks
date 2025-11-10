
def calc_grade(m1, m2, m3, m4, m5):
    avg = (m1 + m2 + m3 + m4 + m5) / 5

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print("Average Marks =", avg)
    print("Grade =", grade)
     m1 = float(input("Enter marks of subject 1: "))
     m2 = float(input("Enter marks of subject 2: "))
     m3 = float(input("Enter marks of subject 3: "))
     m4 = float(input("Enter marks of subject 4: "))
     m5 = float(input("Enter marks of subject 5: "))

calc_grade(m1, m2, m3, m4, m5)
