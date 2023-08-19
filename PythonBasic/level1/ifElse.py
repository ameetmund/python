# score = int(input("Enter score: "))

# if score < 40:
#     print("Please try again")
# else:
#     print("Great score")

rating = int(input("Enter user rating between 1 & 5 only: "))

if rating == 1:
    print("Very Bad")

elif rating == 2:
    print("Need to improve")

elif rating == 3:
    print("Thanks")

elif rating == 4:
    print("Very Good")

elif rating == 5:
    print("Excellent")

else:
    print("Rating entered not between 1-5. Please enter right one")