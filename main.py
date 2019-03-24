
###helping user set his/her thermostat at the best temperature for him/her
###setting to moderate temperature that can help the user maintain good performance
###transforming user's room into a productive study space

#Start room temperature
roomtemp = 90;

#current time
import datetime
from pytz import timezone
now = datetime.datetime.now()
print ("Local current time :", now.strftime("%a, %b %d, %Y  %I:%M:%S %p"))
hour = now.hour

#greeting
if hour < 12:
    greeting = "Good morning"
elif hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good night"

print("{}!".format(greeting))

#function for converting fahrenheit to celsuic
def idealtemp(F):
    idealtemp_C = round(((F-32)*(5/9)),1)
    return idealtemp_C

print("\nWeclome to Room Temperature Controller—StudySmart! Are you ready to pep up your productivity with StudySmart? Let's do it!")

print("Please select the goal of your day: Learning or Relaxing")
Mode_of_Temp = input ()


#learning condition
learning_upper= "Learning"
learning_lower= "learning"
#Relaxing condition
relaxing_upper="Relaxing"
relaxing_lower="relaxing"
#Reading condition
reading_upper= "Reading"
reading_lower= "reading"
#Mathematics condition
mathematics_upper= "Mathematics"
mathematics_lower= "mathematics"
#Memorization condition
memorization_upper= "Memorization"
memorization_lower= "memorization"
#Adult condition
adult_upper= "Adult"
adult_lower= "adult"
#Minor condition
minor_upper= "Minor"
minor_lower= "minor"
#Girl condition
female_upper= "Female"
female_lower= "female"
#Boy condition
male_upper= "Male"
male_lower= "male"

while Mode_of_Temp != learning_upper and Mode_of_Temp != learning_lower and Mode_of_Temp != relaxing_lower and Mode_of_Temp != relaxing_upper:
    print ("Please reselect (check spelling): Learning or Relaxing")
    Mode_of_Temp = input ()

if (Mode_of_Temp == learning_upper or Mode_of_Temp == learning_lower):
    print ("Good Choice!")
    Mode_of_learning = input("Now please select Learning mode: Reading, Mathematics or Memorization\n")

    #check spelling for mode_of_learning
    while Mode_of_learning != reading_upper and Mode_of_learning != reading_lower and Mode_of_learning != mathematics_lower and Mode_of_learning != mathematics_upper and Mode_of_learning != memorization_lower and Mode_of_learning != memorization_upper:
        print ("Please reselect (check spelling): Reading or Mathematics or Memorization")
        Mode_of_learning = input ()
    print("You had select " + Mode_of_learning+".")
        
    #reading
    if Mode_of_learning == reading_upper or Mode_of_learning == reading_lower:
        roomtemp = 55.4
        print("StudySmart has automatically set your room to Reading-mode, "+ str(roomtemp)+ " Fahrenheit, " + str(idealtemp(roomtemp)) + " Celsuic.")

    #math
    if Mode_of_learning == mathematics_upper or Mode_of_learning == mathematics_lower:
        Mode_of_mathematics = input("What is your gender identity? Male or Female\n")
        
        #check Mode_of_mathematics spelling
        while Mode_of_mathematics != male_lower and Mode_of_mathematics != male_upper and Mode_of_mathematics != female_lower and Mode_of_mathematics != female_upper:
            print ("Please reselect (check spelling): Male or Female")
            Mode_of_mathematics = input ()
        print("You had select " + Mode_of_mathematics+".")
        
        if Mode_of_mathematics == female_upper or Mode_of_mathematics == female_lower:
            roomtemp = 62.0
            print("\nStudySmart has automatically set your room to "+ str(roomtemp)+ " Fahrenheit, " + str(idealtemp(roomtemp)) + " Celsuic.")
        
        if Mode_of_mathematics == male_upper or Mode_of_mathematics == male_lower:
            roomtemp = 58.0
            print("\nStudySmart has automatically set your room to "+ str(roomtemp)+ " Fahrenheit, " + str(idealtemp(roomtemp)) + " Celsuic.")
       
        
    #memorization
    if Mode_of_learning == memorization_upper or Mode_of_learning == memorization_lower:
        roomtemp = 72.0
        print("StudySmart has automatically set your room to Memorization-mode, "+ str(roomtemp)+ " Fahrenheit, " + str(idealtemp(roomtemp)) + " Celsuic.")
        
        
#relaxing
if (Mode_of_Temp == relaxing_upper or Mode_of_Temp == relaxing_lower):
    print ('\nIf you work hard, you deserve a little free time.') 
    Mode_of_relaxing = input("Now please select relaxing mode: Adult or Minor\n")
    
    while Mode_of_relaxing != adult_lower and Mode_of_relaxing != adult_upper and Mode_of_relaxing != minor_lower and Mode_of_relaxing != minor_upper:
        print ("Please reselect (check spelling): Adult or Minor")
        Mode_of_relaxing = input ()
       
    
    if Mode_of_relaxing == adult_upper or Mode_of_relaxing == adult_lower:
        roomtemp = 63.0
        print("\nStudySmart has automatically set your room to Adult-relaxing-mode, "+ str(roomtemp)+ " Fahrenheit, " + str(idealtemp(roomtemp)) + " Celsuic.")
        
    if Mode_of_relaxing == minor_upper or Mode_of_relaxing == minor_lower:
        roomtemp = 67.0
        print("\nStudySmart has automatically set your room to Minor-relaxing-mode, "+ str(roomtemp)+ " Fahrenheit, " + str(idealtemp(roomtemp)) + " Celsuic.")
        
print("According to research, this room temperature can help you maintain good performance for this specific task. \n\nAlright now, lets get some work done together!")





