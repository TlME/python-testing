
print("Let's see how long you have lived in days, minutes and seconds.")
isThisSomeKindofJokeToYou = input("What is your name? ")
print("Now enter your age")
doesItLookLikeImJoking = int(input("Age: "))
days = doesItLookLikeImJoking * 365
minutes = days * 60 * 24
seconds = minutes * 60
print(isThisSomeKindofJokeToYou, "has been alive for", days, "days,", minutes,
      "minutes and", seconds, "seconds! Very wow!")
