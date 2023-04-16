from calendar import day_abbr
import sys
counterError = 0

def endProgram():
    print("\nThank you for using the Unit Converter, have a great day. XD")
    sys.exit()

def convertDistance(unit, valueGiven):
    valueGiven = float(valueGiven) #ensures float for formating
    km = m = cm = mm = mi = yd = ft = inch = 0 #inch is used since "in" is a keyword

    #Implemented for future precision
    def metToImp():   #Metric To Imperial
        nonlocal km, mi
        mi = km / 1.609347218694
    def impToMet():   #Imperial to Metric
        nonlocal mi, km
        km = mi * 1.609347218694

    #establishing km and mi, pow is used to ensure the correct amount of 0's is typed
    if unit == "km":
        km = valueGiven
        metToImp()
    elif unit == "m":
        m = valueGiven
        km =  m / pow(10,3)
        metToImp()
    elif unit == "cm":
        cm = valueGiven
        km = cm / pow(10,5)
        metToImp()
    elif unit == "mm":
        m = valueGiven
        km = mm / pow(10,6)
        metToImp()
    elif unit == "mi":
        mi = valueGiven
        impToMet()
    elif unit == "yd":
        yd = valueGiven
        mi = yd / 1760
        impToMet()
    elif unit == "ft":
        ft = valueGiven
        mi = ft / 5280
        impToMet()
    elif unit == "inch":
        inch = valueGiven
        mi = inch / 63360
    else:
        print("Error: Invalid unit selected. Please ensure that you select a supported unit.")
        return
    
    
    m = km * pow(10,3)
    cm = km * pow(10,5)
    mm = km * pow(10,6)
    yd = mi * 1760
    ft = mi * 5280
    inch = mi * 63360

    if unit == "km":
        unit = "Kilometers (km)"
    elif unit == "m":
        unit = "Meters (m)"
    elif unit == "cm":
        unit = "Centimeters (cm)"
    elif unit == "mm":
        unit = "Millimeters (mm)"
    elif unit == "mi":
        unit = "Miles (mi)"
    elif unit == "yd":
        unit = "Yards (yd)"
    elif unit == "ft":
        unit = "Feet (ft)"
    elif unit == "inch":
        unit = "Inches (inch)"
    
    print(f"\n{valueGiven} {unit} is converted as:\n")
    print("Kilometers:\t\t{0:.4f} km".format(km))
    print("Meters:\t\t\t{0:.4f} m".format(m))
    print("Centimeters:\t\t{0:.4f} cm".format(cm))
    print("Millimeters:\t\t{0:.4f} mm".format(mm))
    print("Miles:\t\t\t{0:.4f} mi".format(mi))
    print("Yards:\t\t\t{0:.4f} yd".format(yd))
    print("Feet:\t\t\t{0:.4f} ft".format(ft))
    print("Inch:\t\t\t{0:.4f} inch".format(inch))

    selectCategory()

def selectDistance():
    unit, valueReceived = "", 0
    print("\n\nPlease select a unit to convert from by typing the listed unit.\n")
    unit = input("Kilometer | Meter | Centimetre | Millimetre | Mile | Yard | Foot | Inch\t\t|| Quit\n").capitalize()
    if unit == "Quit":
        endProgram()
    valueReceived = input("Please enter the value\t\t|| Quit\n").capitalize()
    if unit == "Quit":
        endProgram()
    
    if   unit == "Kilometer":
        convertDistance("km", valueReceived)
    elif unit == "Meter":
        convertDistance("m", valueReceived)
    elif unit == "Centimetre":
        convertDistance("cm", valueReceived)
    elif unit == "Millimetre":
        convertDistance("mm", valueReceived)
    elif unit == "Mile":
        convertDistance("mi", valueReceived)
    elif unit == "Yard":
        convertDistance("yd", valueReceived)
    elif unit == "Foot":
        convertDistance("ft", valueReceived)
    elif unit == "Inch":
        convertDistance("inch", valueReceived)
    else:
        print("A proper unit was not selected, please try again.")
        selectDistance()

def convertMass(unit, valueGiven):
    valueGiven = float(valueGiven)
    t = kg = g = mg = lbs = st = oz = 0
    
    #ensures forward precision
    def metToImp():   #Metric To Imperial
        nonlocal t, lbs
        lbs = t * 2204.62
    def impToMet():   #Imperial to Metric
        nonlocal lbs, t
        t = lbs / 2204.62

    #establishing t and lb, pow is used to ensure the correct amount of 0's is typed
    if unit == "t":
        t = valueGiven
        metToImp()
    elif unit == "kg":
        kg = valueGiven
        t =  kg / pow(10,3)
        metToImp()
    elif unit == "g":
        g = valueGiven
        t =  mg / pow(10,6)
        metToImp()
    elif unit == "mg":
        mg = valueGiven
        t =  mg / pow(10,9)
        metToImp()
    elif unit == "lbs":
        lbs = valueGiven
        impToMet()
    elif unit == "st":
        st = valueGiven
        lbs =  st * 14
        impToMet()
    elif unit == "oz":
        oz = valueGiven
        lbs =  oz / 16
        metToImp()
    else:
        print("Error: Invalid unit selected. Please ensure that you select a supported unit.")
        return
    
    kg = t * pow(10,3)
    g  = t * pow(10,6)
    mg = t * pow(10,9)
    st = lbs / 14
    oz = lbs * 16

    if unit == "t":
        unit = "Tonnes (t)"
    elif unit == "kg":
        unit = "Kilograms (kg)"
    elif unit == "g":
        unit = "Grams (g)"
    elif unit == "mg":
        unit = "Milligrams (mg)"
    elif unit == "lbs":
        unit = "Pounds (lbs)"
    elif unit == "st":
        unit = "Stone (st)"
    elif unit == "oz":
        unit = "Ounces (oz)"
    
    print(f"{valueGiven} {unit} is converted as:\n")
    print("Tonnes:\t\t{0:.4f} t".format(t))
    print("Kilograms:\t{0:.4f} kg".format(kg))
    print("Grams:\t\t{0:.4f} g".format(g))
    print("Milligrams:\t{0:.4f} mg".format(mg))
    print("Stone:\t\t{0:.4f} st".format(st))
    print("Pounds:\t\t{0:.4f} lbs".format(lbs))
    print("Ounces:\t\t{0:.4f} oz".format(oz))

    selectCategory()

def selectMass():
    unit, valueReceived = "", 0
    print("\n\nPlease select a unit to convert from by typing the listed unit.\n")
    unit = input ("Ton | Kilogram | Gram | Milligram | Stone | Pounds | Ounce\t\t|| Quit\n").capitalize()
    if unit == "Quit":
        endProgram()
    valueReceived = input("Please enter the value\t\t|| Quit\n").capitalize()
    if unit == "Quit":
        endProgram()

    if   unit == "Ton":
        convertMass("t", valueReceived)
    elif unit == "Kilogram":
        convertMass("kg", valueReceived)
    elif unit == "Gram":
        convertMass("g", valueReceived)
    elif unit == "Milligram":
        convertMass("mg", valueReceived)
    elif unit == "Stone":
        convertMass("st", valueReceived)
    elif unit == "Pounds":
        convertMass("lbs", valueReceived)
    elif unit == "Ounce":
        convertMass("oz", valueReceived)
    else:
        print("A proper unit was not selected, please try again.")
        selectMass()

def convertTemperature(unit, valueGiven):
    valueGiven = float(valueGiven)
    c = f = k = r = 0
    if unit == 'c':
        c = valueGiven
    elif unit == 'f':
        f = valueGiven
        c = (f - 32) /1.8
    elif unit == 'k':
        k = valueGiven
        c = k - 273.15
    elif unit == 'r':
        r = valueGiven
        c = (r - 491.67) /1.8
    else:
        print("Error: Invalid unit selected. Please ensure that you select a supported unit.")
        return
    
    k = c + 273.15
    f = (c * 1.8) +32
    r = (c + 273.15) *1.8

    if unit == 'c':
        unit = "Degrees Celcius ('C)"
    elif unit == 'k':
        unit = "Kelvin (K)"
    elif unit == 'f':
        unit = "Degrees Farenheit ('F)"
    elif unit == 'r':
        unit = "Degrees Rankine ('R)"
    
    print(f"{valueGiven} {unit} is converted as:\n")
    print("Degrees Celcius:\t{0:.2f} 'C".format(c))
    print("Kelvin:\t\t\t{0:.2f} K".format(k))
    print("Degrees Farenheit:\t{0:.2f} 'F".format(f))
    print("Degrees Rankine:\t{0:.2f} 'R".format(r))

    selectCategory()

def selectTemperature():
    unit, valueReceived = "", 0
    print("\n\nPlease select a unit to convert from by typing the listed unit.\n")
    unit = input("Celcius | Kelvin | Farenheit | Rankine\t\t|| Quit\n").capitalize()
    if unit == "Quit":
        endProgram()
    valueReceived = input("Please enter the value\t\t|| Quit\n").capitalize()
    if unit == "Quit":
        endProgram()
    
    if   unit == "Celcius":
        convertTemperature('c', valueReceived)
    elif unit == "Kelvin":
        convertTemperature('k', valueReceived)
    elif unit == "Farenheit":
        convertTemperature('f', valueReceived)
    elif unit == "Rankine":
        convertTemperature('r', valueReceived)
    else:
        print("A proper unit was not selected, please try again.")
        selectTemperature()

def convertTime(unit, valueGiven):
    valueGiven = float(valueGiven)
    day = hr = min = sec = 0
    if unit == "day":
        day = valueGiven
    elif unit == "hr":
        hr = valueGiven
        day = hr / 24
    elif unit == "min":
        min = valueGiven
        day =  min / 1440
    elif unit == "sec":
        sec = valueGiven
        day = sec / 86400
    else:
        print("Error: Invalid unit selected. Please ensure that you select a supported unit.")
        return
    
    hr  = day *24
    min = day * 1440
    sec = day * 86400

    if unit == "day":
        unit = "Days"
    if unit == "hr":
        unit = "Hours"
    if unit == "min":
        unit = "Minutes"
    if unit == "sec":
        unit = "Seconds"
    
    print(f"{valueGiven} {unit} is converted as:\n")
    print("Days:\t\t{0:.1f}".format(day))
    print("Hours:\t\t{0:.1f}".format(hr))
    print("Minutes:\t{0:.1f}".format(min))
    print("Seconds:\t{0:.1f}".format(sec))

    selectCategory()

def selectTime():
    unit, valueReceived = "", 0
    print("\n\nPlease select a unit to convert from by typing the listed unit.\n")
    unit = input("Day | Hour | Minute | Second\t\t|| Quit\n").capitalize().capitalize()
    if unit == "Quit":
        endProgram()
    valueReceived = input("Please enter the value\t\t|| Quit\n").capitalize().capitalize()
    if unit == "Quit":
        endProgram()
    
    if   unit == "Day":
        convertTime("day", valueReceived)
    elif unit == "Hour":
        convertTime("hr", valueReceived)
    elif unit == "Minute":
        convertTime("min", valueReceived)
    elif unit == "Second":
        convertTime("sec", valueReceived)
    else:
        print("A proper unit was not selected, please try again.")
        selectTime()

def selectCategory():
    selection = ""
    print("\n\nPlease select a catagory by typing the listed word.")
    selection = input("Distance | Mass | Temperature | Time\t\t|| Quit\n").capitalize()
    if   selection == "Distance":
        selectDistance()
    elif selection == "Mass":
        selectMass()
    elif selection == "Temperature":
        selectTemperature()
    elif selection == "Time":
        selectTime()
    elif selection == "Quit":
        endProgram()
    else:
        print("It seems you selected an unsupported catagory, please try again")
        selectCategory()


#startOfProgram
print("\nThis program is created for the purposes of converting Units of Meassurement")
print("Enter \"Quit\" at any time to terminate the program manually.")
print("In order to protect the user, the program will terminate if invalid input is detected three (3) times, consecutively.")
print("Please note that this program is case  sensitive.")
selectCategory()
