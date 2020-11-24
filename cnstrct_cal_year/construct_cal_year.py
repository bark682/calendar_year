def construct_cal_year(year):
    import leap_year as lp

    is_leap = lp.leap_year(year)
    return is_leap

print(construct_cal_year(1900))