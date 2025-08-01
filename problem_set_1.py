

text = input("enter your text: ")
print (text.lower())              #indoor voice
print (text.replace(" ","..."))   #Playback Speed

m = float(input("enter your kg: ")) #Einstein
c = 300000000
e = m * c ** 2
print (e)

name = input ("نام و نام خانوادگی :").title()
age = int(input("سن خود را وارد کنید: "))
term = input ("نام دوره خود را وارد کنید: ")
score1, score2, score3 = map(float, input("نمره سه درس را جدا جدا وارد کنید: ").split())
average = (score1 + score2 + score3) / 3

print (f"نام و نام خانوادگی: {name}")
print (f"سن: {age}")
print (f"نام دوره: {term}")
print (f"نمرات: {score1, score2, score3}")
print (f"میانگین نمرات: {average}")

if average >= 60 :
    print ("پاس")
else:
    print("رد")