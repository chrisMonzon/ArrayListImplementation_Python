#Author       : Christopher Monzon
#Date         : 10/21/17
#Organization : The Coder School-San Mateo
#Mentor       : Phyo Htut
###################################################################
print "Press [p] to play hangman!"
play = input()
clear = '\n' * 100

while play == "p":
  wList = [] #list of correct letters
  TheCommentsAreHere=0
  playerListDefult = ['','','','','','','','','','','','','','',
                      '','','','','','','','','','','','','','',
                      '','','','','','','','','','','','','','','']
  playerList = []
  uListDefault = ['_','_','_','_','_','_','_','_','_','_','_','_',
                  '_','_','_','_','_','_','_','_','_','_','_','_',
                  '_','_','_','_','_','_','_','_','_','_','_','_',
                  '_','_','_','_','_','_','_','_','_','_','_','_',
                  '_','_','_','_','_','_','_','_','_'] 
             #underscore list
  uList = []
  cList = [] #list of incorrect letters
  turns = 5
  
  print ("Type the word the player needs to identify.")
  word2 = input()                   #giving the answer
  print clear
  #breaking the string to char
  for i in range(0, len(word2)):
    wList.append(word2[i])         #appends the letter to the list of letters that have to be guessed
    uList.append(uListDefault[i]) 
    playerList.append(playerListDefult[i])
    
  print uList                      #prints the list of underscores
  
  while turns > 0:
    print("You have " + str(turns) + " turns left. Guess a letter:")
    guess = input()                 #checking if the input is char
    while len(guess) != 1:          #makes the user guess again if their guess isn't 1 char long
      print "Your answer must be 1 character long."
      guess = input()
    
    flag = False
    index = 0
    for w in wList:
      if w == guess:                #if your guess is right, don't cehck if it is wrong
        flag = True                 #found a match
        playerList[index] = w       # making the wList the playerList's index
        uList[index] = w
      index += 1             
        
    if flag == False:
      #check if the wrong guess is already in the cList,
      #if it is already in the cList, print error message
      #else, reduce the turn and append the wrong guess into the cList
      if len(cList) == 0:
        turns -= 1
        cList.append(guess)
      else:
        doublePen = False           # assuming you are not double penalzing
        for s in cList:             # still going to check the error list to make sure
          if s == guess:            # if you happen to see the letter in the cList
            doublePen = True        # you are getting double penalized

        if doublePen == True:
          print("'" + guess + "' has already been guessed before")
        else:
          turns -= 1                #Subtracting the turns if the guess is wrong
          cList.append(guess)
          
    gameOver = True
    for i in range(0, len(wList)):  #if the wLIst's characers are not the same as the answer's characters,
      if wList[i] != playerList[i]: #gameOver
        gameOver = False
    #print playerList
    print uList
    print "The list of wrong characters include: ", cList, "\n"   #prints the list of wrong characters so the user
    if gameOver:                                                  #knows what letters he already guessed
      break                                                       #break when turns=0 and all guesses are wrong
    if turns == 4:
      print "_____________"
      print "|            |"
      print "|            O"
      print "|            "
      print "|__"
    
    if turns == 3:
      print "_____________"
      print "|            |"
      print "|            O"
      print "|            |"
      print "|__"
    if turns == 2:
      print "_____________"
      print "|            |"
      print "|            O"
      print "|            |"
      print "|__          ^"
    if turns == 1:
      print "_____________"
      print "|            |"
      print "|           _O"
      print "|            |"
      print "|__          ^"
    
  if gameOver == True:
    print "Congratulations! You have correctly guessed the word and not all of the guy's limbs have been.. hung?\n"
    
  if turns <= 0:
    print "Word: ",word2
    print "Sorry, better luck next time. RIP RIP RIP RIP"
    print "_____________"
    print "|            |"
    print "|           _O_"
    print "|            |"
    print "|__          ^"
  #when the game is over, ask the question again to see
  #if the player wants to play more
  print("Would you like to play again?")
  play = input()
  