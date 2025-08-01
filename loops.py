movies = ["pianist" , "god father" , "matrix" , "seller" , "barbie" , "shining"]
scores = [9.5 , 9 , 8.7 , 7.2 , 6 , 8]
for index in range(6):
    print(movies[index] ,":" , scores[index])
max_scores = scores[-1]
max_index = -1
for i in range(6):
    if scores[i] > max_scores:
        max_scores = scores [i]
        max_index = i
        print (movies[max_index] , ":" , max_scores)

mail = "computeronic@gmail.com"
word = mail.split("@")
for i in word:
    print(i.capitalize())




