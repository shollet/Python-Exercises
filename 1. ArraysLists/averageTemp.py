# Arrays/Lists

def challenge():
    # prompt
    temperatures = []
    days = int(input("How many day's temperature: "))

    # loop

    for day in range(1, days+1):
        temperature = float(input("Day " + str(day) + "'s high temp: "))
        temperatures.append(temperature)

    # average and above

    average = round(sum(temperatures) / len(temperatures), 2)
    above = 0
    for temp in temperatures:
        if temp > average:
            above += 1

    # print

    print('Average =', average)
    print(str(above) + " day(s) above average")


challenge()