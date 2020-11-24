
def get_year():
    
    while True:
        yr = input("Plese Enter Year: ")
        if int(yr)>=1800 and int(yr)<=2099:
            break
        else:
            print("Invalid Entry!")
            continue
    
    return yr
