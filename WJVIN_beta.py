#Jeep WJ VIN Decoder
#Jeep WJ's were produced between 1999 and 2004
vin = input("Please enter your Jeep WJ's VIN\n")
vin = vin.upper()
if (len(vin) == 17):
    print("You entered " + vin)
else:
    print("You entered " + vin + ", which is not a full 17 character VIN number")

#vailidate WJ
if (vin[4] == ("2" or "X" or "W" or "8")):
    line = "Grand Cherokee"
else:
    line = "\"not a WJ\""

#parse make
if (vin[1] == "J"):
    make = "Jeep"
else:
    print("This doesn't look like it's a Jeep!")

#parse side airbags option
if (vin[2] == "8"):
    side_airbags = "WITH side airbags"
else:
    side_airbags = "without side airbags"

#parse 2 or 4 wheel drive (depends on year)
if (vin[9] == ("X" or "Y") and (vin[4] == "2")):
    drive = "2WD"
elif (vin[9] == ("1" or "2" or "3" or "4") and (vin[4] == "X")):
    drive = "2WD"
else:
    drive = "4WD"

#parse trim level (depends on year)
if (vin[9] == "X"):
    if (vin[5] == "5"):
        trim = "Laredo"
    else:
        trim = "Limited"
else:
    if (vin[5] == "3"):
        trim = "Sport"
    elif (vin[5] == "4"):
          trim = "Laredo"
    elif (vin[5] == "5"):
          trim = "Limited"
    elif (vin[5] == "6"):
          trim = "Overland"
    else:
        print("export model info not available")

#parse engine
if (vin[7] == "S"):
    engine = "4.0 Liter Inline 6"
elif (vin[7] == "N"):
    engine = "4.7 Liter V8"
elif (vin[7] == "J"):
    engine = "4.7 Liter V8 High Output!"
else:
    engine = "an unknown engine"

#parse year
if (vin[9] == "X"):
    year = "1999"
elif (vin[9] == "Y"):
    year = "2000"
elif (vin[9] == "1"):
    year = "2001"
elif (vin[9] == "2"):
    year = "2002"
elif (vin[9] == "3"):
    year = "2003"
elif (vin[9] == "4"):
    year = "2004"
else:
    print("This is not a WJ Jeep.")
    
#Output
print("Looks like a " + year + " " + drive + " " + make + " " + line + " " + trim + " " + "powered by a " + engine + " " + side_airbags)
