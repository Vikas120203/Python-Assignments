user_rating = float(input("enter rating(0 to 5):")) ## Movie Ratings
if user_rating >= 4.5 and user_rating <= 5: 
    print("blockbuster") 
elif user_rating>=3.5 and user_rating<4.5:
    print("hit")
elif user_rating>=3.0 and user_rating<3.5:
    print("Good")
elif user_rating>=2.5 and user_rating<3.0:
    print("avg")
elif user_rating > 5.0:
    print("invalid")
else:
    print("flop")
