def main():
    time = input('what time is it right now? ')
    mealTime = convert(time)

    if 7 <= mealTime <= 8: 
        print("breakfast time")
    elif 12 <= mealTime <= 13: 
        print("launch time")
    elif 18 <= mealTime <= 19: 
        print("dinner time")


def convert(time):
    hours, minutes = time.split(':')
    timeFormatted = float(int(hours) + int(minutes) / 60)
    return timeFormatted;

main()

###########################################################################
# SOLUTION FOE THE EXTRA CHALLENGE

def main():
    time = input('what time is it right now? ')
    mealTime = convert(time)

    if 7 <= mealTime <= 8: 
        print("breakfast time")
    elif 12 <= mealTime <= 13: 
        print("launch time")
    elif 18 <= mealTime <= 19: 
        print("dinner time")


def convert(time):
    timeAmount, timing = time.split(' ')
    hours, minutes = timeAmount.split(':')
    timeFormatted = float(int(hours) + int(minutes) / 60)
    if timing == 'p.m.':
        timeFormatted = timeFormatted + 12

    return timeFormatted;

main()