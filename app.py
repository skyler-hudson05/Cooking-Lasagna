# Variables
EXPECTED_BAKED_TIME = 40
layers = int(input("How many layers of lasagna do you want to make? "))


# Preparing the lasagna
def PreparationTimeMinutes(layers):
  prepTimeMin = layers * 2
  return print("It took you ", prepTimeMin, " minutes to prepare")

PreparationTimeMinutes(layers)


# How much time is left in oven
timeInOven = int(input("How long has the lasagna been in the oven? "))
def RemainingMinutesInOven(timeInOven):
  timeLeftInOven = 40 - timeInOven
  return print("You have", timeLeftInOven, " minutes left")

RemainingMinutesInOven(timeInOven)


# Total minutes spent making lasagna
def TotalMinutesMakingMeal(layers, timeInOven):
  totalTimeInMinutes = layers + timeInOven
  return print("You've spent ", totalTimeInMinutes, " minutes on this meal so far")

TotalMinutesMakingMeal(layers, timeInOven)
