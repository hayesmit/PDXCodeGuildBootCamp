again = "yes"
while again != "no":
    madLib = [input("pick a season. >> "), input("now pick an animal. >> "),
              input("someone you enjoy spending time with> >> "), input("add an adjective. >> "),
              input("give me an activity. >> ")]

    print("I am really looking forward to " + madLib[0] + ". Taking my " + madLib[1] + " on hikes with " + madLib[2] +
          " is aways nice, and sunny days are also " + madLib[3] + ". Until then I will enjoy the advantages that "
          "winter has to offer, such as " + madLib[4] + " and spending time indoors without feeling like I have waisted the day.")
    again = input("would you like to play again? yes or no? >> ")
