time_hour = int(input("Enter the hour of the day (1-24): "))  
mood = input("How are you feeling? (sleepy, thirsty, etc.): ")

if time_hour > 0 and time_hour <= 24:
    print('Suggesting a drink option...')
    
    if mood == 'sleepy' and time_hour < 10:
        print('coffee')
    elif mood == 'thirsty' or time_hour < 2:
        print('lemonade')
    else:
        print('water')
