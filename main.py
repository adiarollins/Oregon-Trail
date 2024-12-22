import random
MILES_LEFT = 2000
FOOD = 500
HEALTH = 5
MONTHS = [3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12]
MONTHS_WITH_31_DAYS = [3 , 5 , 6 , 7 , 8 , 10 , 12 ]
CURRENT_MONTH = 3
CURRENT_DAY = 1
PLAYING = True

#name: add_day
#purpose: update the date
#inputs: x = minumum days needed , y = maximum number of days
#returns: none
def add_day(x,y):
  global MILES_LEFT, FOOD, HEALTH, MONTHS, MONTHS_WITH_31_DAYS, CURRENT_MONTH, CURRENT_DAY
  daysAdded = random.randint(x,y)
  CURRENT_DAY = daysAdded + CURRENT_DAY
  if CURRENT_DAY > 30:
    for i in range (1,len(MONTHS_WITH_31_DAYS)):
      if CURRENT_MONTH == MONTHS_WITH_31_DAYS[i]: 
        if CURRENT_DAY > 31:
          CURRENT_MONTH = CURRENT_MONTH + 1
          CURRENT_DAY = CURRENT_DAY - 31
    if CURRENT_DAY > 30: 
      CURRENT_MONTH = CURRENT_MONTH + 1
      CURRENT_DAY = CURRENT_DAY - 30
#name: travel
#purpose: moves you randomly between 30-60 miles and takes 3-7 days (random).
#inputs: none
#returns: none
def travel():
  global MILES_LEFT, FOOD, HEALTH, MONTHS, MONTHS_WITH_31_DAYS, CURRENT_MONTH, CURRENT_DAY
  add_day(3,7)
  FOOD = FOOD - 5
  MILES_LEFT = MILES_LEFT - random.randint(30,60)
  if MILES_LEFT <= 0:
    MILES_LEFT = 0

#name: hunt
#purpose: adds 100 lbs of food and takes 2-5 days (random)
#inputs: none
#returns: none
def hunt():
  global MILES_LEFT, FOOD, HEALTH, MONTHS, MONTHS_WITH_31_DAYS, CURRENT_MONTH, CURRENT_DAY
  add_day(2,5)
  FOOD = FOOD + 95

#name: rest
#purpose: increases health 1 level (up to 5 maximum) and takes 2-5 days (random).
#inputs: none
#returns: none
def rest():
  global MILES_LEFT, FOOD, HEALTH, MONTHS, MONTHS_WITH_31_DAYS, CURRENT_MONTH, CURRENT_DAY
  add_day(2,5)
  FOOD = FOOD - 5
  if HEALTH == 5:
    print ('You are at max health.')
  else:
    HEALTH = HEALTH + 1         
#name: status
#purpose: Print your status 
#inputs: none
#returns: none
def status():
  global MILES_LEFT, FOOD, HEALTH, MONTHS, MONTHS_WITH_31_DAYS, CURRENT_MONTH, CURRENT_DAY
  print('Day: ' + str(CURRENT_MONTH) + '/' + str(CURRENT_DAY))
  print('Miles Left: ' + str(MILES_LEFT))
  print('Food (lbs): ' + str(FOOD))
  print('Health: ' + str(HEALTH))

#name: help
#purpose: lists all the commands.
#inputs: none
#returns: none
def help_():
  print ("Each turn you can take one of 3 actions:")
  print ('')
  print ('  travel - moves you randomly between 30-60 miles and takes 3-7 days (random).')
  print ('  rest   - increases health 1 level (up to 5 maximum) and takes 2-5 days (random).')
  print ('  hunt   - adds 100 lbs of food and takes 2-5 days (random).')
  print ('')
  print ('When prompted for an action, you can also enter one of these commands without using up your turn:')
  print ('  status - lists food, health, distance traveled, and day.')
  print ('  help   - lists all the commands.')
  print ('  quit   - will end the game.')
  print ('')
  print ('You can also use these shortcuts for commands:')
  print ("  't', 'r', 'h', 's', '?', 'q'")

#name: quit
#purpose: End the game
#inputs: none
#returns: none
def quit():
  global PLAYING
  PLAYING = False

#name: select_action
#purpose: to anaylze the action the user choose
#inputs: none
#returns: none
def select_action():
  global ACTION
  if ACTION == 't' or ACTION == 'travel' :
    travel()
  elif ACTION == 'r' or ACTION == 'rest' :
    rest()
  elif ACTION == 'h' or ACTION == 'hunt' :
    hunt()
  elif ACTION == 's' or ACTION == 'status' :
    status()
  elif ACTION == '?' or ACTION == 'help' :
    help_()
  elif ACTION == 'q' or ACTION == 'quit' :
    quit()

def health():
  global HEALTH, CURRENT_DAY, CURRENT_MONTH
  a = 0
  b = random.randint(0,5)
  c = CURRENT_MONTH
  d = random.randint(0,5)
  if CURRENT_MONTH != c:
    a = 0 
  if b == 1 and a >= 2 or CURRENT_DAY >= 23 and a <= 2:
    if d == 0:
      print ('You stubbed your toe.')
    if d == 1:
      print ('You fell running from a bear.')
    if d == 2:
      print ('You got sick.')
    if d == 3:
      print ('You sprained your ankle.')
    if d == 4:
      print ('You hurt your wrist.')
    if d == 5:
      print ('Your back is in pain.')
    HEALTH = HEALTH - 1
    a = a + 1


#Welcome Print
print ('Welcome to the Oregon Trail!')
print ('  The year is 1850 and Americans are headed out West to populate the frontier. Your goal is to travel by wagon train from Independence, MO to Oregon (2000 miles). You start on March 1st, and your goal is to reach Oregon by December 31st. The trail is arduous. Each day costs you food and health. You can hunt and rest, but you have to get there before winter!')
print ('')
print ("Each turn you can take one of 3 actions:")
print ('')
print ('  travel (t) - moves you randomly between 30-60miles and takes 3-7 days (random).')
print ('  rest (r) - increases health 1 level (up to 5maximum) and takes 2-5 days (random).')
print ('  hunt (h) - adds 100 lbs of food and takes 2-5days (random).')
print ('')
print ('When prompted for an action, you can also enterone of these commands without using up your turn:')
print ('  status (s) - lists food, health, distancetraveled, and day.')
print ('  help (?) - lists all the commands.')
print ('  quit (q) - will end the game.')
print ('')
print ('You can also use these shortcuts for commands:')
print ("  't', 'r', 'h', 's', '?', 'q'")


#Game

while PLAYING:
  ACTION = input('What would you like to do today? ')
  select_action()
  health()
  status()
  if HEALTH == 0:
    print ('Unfortunately you ran out of Health and died Thanks for playing!')
    PLAYING = False
  if FOOD == 0:
    print ('Unfortunately you ran out of Food and Starved to death. Thanks for playing!')
    PLAYING = False
  if MILES_LEFT <= 0:
    print ('CONGRATULATIONS! You made it to Oregon in one piece! Thanks for Playing!')
    PLAYING = False
  if CURRENT_MONTH == 12 and CURRENT_DAY >= 31 or CURRENT_MONTH == 13:
    print ("Unfortunately you didn't make it to Oregon on time. Thanks for playing!")
    PLAYING = False
