def paycheck(currentmonth, currentday):
    if currentmonth == 1:
        if currentday <= 15:
            current_semimonthly_period = 1
        else:
            current_semimonthly_period = 2
        return current_semimonthly_period

    elif currentmonth == 2:
        if currentday <= 15:
            current_semimonthly_period = 3
        else:
            current_semimonthly_period = 4
        return current_semimonthly_period

    elif currentmonth == 3:
        if currentday <= 15:
            current_semimonthly_period = 5
        else:
            current_semimonthly_period = 6
        return current_semimonthly_period

    elif currentmonth == 4:
        if currentday <= 15:
            current_semimonthly_period = 7
        else:
            current_semimonthly_period = 8
        return current_semimonthly_period

    elif currentmonth == 5:
        if currentday <= 15:
            current_semimonthly_period = 9
        else:
            current_semimonthly_period = 10
        return current_semimonthly_period

    elif currentmonth == 6:
        if currentday <= 15:
            current_semimonthly_period = 11
        else:
            current_semimonthly_period = 12
        return current_semimonthly_period

    elif currentmonth == 7:
        if currentday <= 15:
            current_semimonthly_period = 13
        else:
            current_semimonthly_period = 14
        return current_semimonthly_period

    elif currentmonth == 8:
        if currentday <= 15:
            current_semimonthly_period = 15
        else:
            current_semimonthly_period = 16
        return current_semimonthly_period

    elif currentmonth == 9:
        if currentday <= 15:
            current_semimonthly_period = 17
        else:
            current_semimonthly_period = 18
        return current_semimonthly_period

    elif currentmonth == 10:
        if currentday <= 15:
            current_semimonthly_period = 19
        else:
            current_semimonthly_period = 20
        return current_semimonthly_period

    elif currentmonth == 11:
        if currentday <= 15:
            current_semimonthly_period = 21
        else:
            current_semimonthly_period = 22
        return current_semimonthly_period

    elif currentmonth == 12:
        if currentday <= 15:
            current_semimonthly_period = 23
        else:
            current_semimonthly_period = 24
        return current_semimonthly_period
