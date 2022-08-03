
print("welcome to a fun quiz :)" )

player = input("do you want to play the game? ")
if player.lower() != "yes":
    quit()
score = 0
print ("ok lets play :)")
score = 0

response = input("hour many hours are in a day")
if response.lower() == "24":
    print ("correct")
    score += 1
else:
    print ("this is not correct")


response = input("what is the capital of the uk")
if response.lower() == "london":
    print ("correct")
    score += 1
else:
    print ("this is not correct")


response = input ("how many days are there in a year")
if response.lower() == "365":
    print ("correct")
    score += 1
else:
    print("this is not correct")


response = input("what is the capital of amarica" )
if response.lower() == "washington":
    print ("correct")
    score += 1
else:
    print ("this is not correct ")


response = input("how many meters in a km?" )
if response.lower() == "1000":
    print ("correct")
    score += 1
else:
    print ("this is not correct ")


response = input("what is the meaning to life?" )
if response.lower() == "42":
    print ("correct")
    score += 1
else:
    print ("this is not correct ")


response = input("what does larp stand for?" )
if response.lower() == "live action role play":
    print ("correct")
    score += 1
else:
    print ("this is not correct ")



response = input("what is the nickname of the ultra marines from warhammer 40" )
if response.lower() == "smurfs":
    print ("correct")
    score += 1
else:
    print ("this is not correct ")

response = input("what does the leters OU stand for and for which university?" )
if response.lower() == "open university":
    print ("correct")
    score += 1
else:
    print ("this is not correct ")


response = input("what is the main battle tank of the uk?" )
if response.lower() == "challenger two":
    print ("correct")
    score += 1
else:
    print ("this is not correct ")


print ("your score is " + str(score) + "out of a score of 10 ")