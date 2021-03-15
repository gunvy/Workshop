"""จงเขียนโปรแกรมเพื่อทำการคำนวณเกรดโดยมีเงื่อนไขดังนี้
คะแนน 80 - 100 ได้ A
คะแนน 75 - 79 ได้ B+
คะแนน 70 - 74 ได้ B
คะแนน 65 - 69 ได้ C+
คะแนน 60 - 64 ได้ C
คะแนน 55 - 59 ได้ D+
คะแนน 50 - 54 ได้ D
คะแนน 0 - 49 ได้ F
และให้แสดงผลตามตัวอย่างด้านล่าง
Enter your score: 49101
grade:  F """


def grade():
    Enter_score = input("Enter your score : ")
    if int(Enter_score) >= 80 and int(Enter_score) <= 100:
        print("grade is A ")
    elif int(Enter_score) >= 75 and int(Enter_score) <= 79:
        print("grade is B ")
    elif int(Enter_score) >= 65 and int(Enter_score) <= 69:
        print("grade is C+ ")
    elif int(Enter_score) >= 60 and int(Enter_score) <= 64:
        print("grade is C ")
    elif int(Enter_score) >= 55 and int(Enter_score) <= 59:
        print("grade is D ")
    elif int(Enter_score) >= 50 and int(Enter_score) <= 54:
        print("grade is D+ ")
    elif int(Enter_score) >= 0 and int(Enter_score) <= 49:
        print("grade is F ")
    else:
        print("score Eror !!!, Input score agian")
        grade()


grade()
