def converter(value, units, to):
    allowed_units = ('C', 'F', 'K')
    if type(units) is not str or type(to) is not str:
        raise TypeError("units must be instances of str")

    u = units.upper()
    t = to.upper()

    #Wrong units exception
    if u not in allowed_units or t not in allowed_units:
        raise ValueError(f"units are invalid. Allowed units {allowed_units}")
    #Absolute zero exception
    if u == 'K' and value < 0 or u == 'C' and value < -273.15 or u == 'F' and value < -459.67:
        raise ValueError("absolute zero is 0K, value too low")

    if u == t:
        #print(f"{value} {u} is equal to {value} {t}")
        return value
    elif u == 'F':
        ans = round(((value - 32) * 5 / 9), 2)
        if t == 'K':
            ans += 273.15
            #print(f"{value} F is equal to {ans} K")
        else:
            #print(f"{value} F is equal to {ans} C")
            pass
    elif u == 'C' and t == 'F':
        ans = round((value * 9 / 5 + 32), 2)
        #print(f"{value} C is equal to {ans} F")
    elif u == 'C' and t == 'K':
        ans = round((value + 273.15), 2)
        #print(f"{value} C is equal to {ans} K")
    elif u == 'K':
        ans = round((value - 273.15), 2)
        if t == 'F':
            ans = round((ans * 9 / 5 + 32), 2)
            #print(f"{value} K is equal to {ans} F")
        else:
            #print(f"{value} K is equal to {ans} C")
            pass

    return ans