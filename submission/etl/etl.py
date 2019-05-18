"""
This python script can be used to extract data from the train.csv
to create the required csv files for each dimension.

Author: Bruce How (22242664) & Haolin Wu (21706137)
"""

import csv

# Global variables used to store already seen rows, prevents duplicates
seen_breed = []
seen_color = []
seen_rescuer = []
seen_location = []
seen_age = []

def breed_data(file, row):
    breed1, breed2 = row[3], row[4]

    # Check to see if we have already seen the breed
    if [breed1, breed2] in seen_breed:
        return # Already exists, don't add duplicates

    seen_breed.append([breed1, breed2])

    breed_purity = "Mixed"
    if breed2 == "0":
        breed_purity = "Pure"
        breed2 = "" # NULL color

    data = ["", breed1, breed2, breed_purity]
    file.writerow(data)

def color_data(file, row):
    color1, color2, color3 = row[6], row[7], row[8]

    if [color1, color2, color3] in seen_color:
        return

    seen_color.append([color1, color2, color3])

    color_purity = "Mixed"
    if color2 == "0":
        color_purity = "Pure"
        color2 = ""
        color3 = ""
    elif color3 == "0":
        color3 = ""

    data = ["", color1, color2, color3, color_purity]
    file.writerow(data)

def location_data(file, row):
    location = row[17]

    if location in seen_location:
        return

    seen_location.append(location)
    data = ["", location]
    file.writerow(data)

def age_data(file, row):
    age = row[2]
    if age in seen_age:
        return

    seen_age.append(age)
    data = ["", age]
    file.writerow(data)

# Used for Sterilized, Dewormed, Vaccinated
def generic_data(file):
    file.writerow(["", "Yes"])
    file.writerow(["", "No"])
    file.writerow(["", "Not Sure"])

def rescuer_data(file, row):
    rescuer = row[18]
    if rescuer in seen_rescuer:
        return
    seen_rescuer.append(rescuer)
    data = ["", rescuer]
    file.writerow(data)

def fact_data(file, row):
    alt_id = row[21]
    type = row[0]
    gender = row[5]
    maturity_size = row[9]
    fur_length = row[10]
    vaccinated = row[11]
    dewormed = row[12]
    sterilized = row[13]
    health = row[14]

    # No Specified
    if maturity_size == "0":
        maturity_size = ""
    if fur_length == "0":
        fur_length = ""
    if health == "0":
        health = ""

    # Measures
    video_amt = row[19]
    photo_amt = int(float(row[22])) # PhotoAmt is of type float in train.csv
    fee = row[16]
    adoptionspeed = row[23]

    # Foreign Keys
    breed = ""
    for i in range(0, len(seen_breed)):
        if seen_breed[i] == [row[3], row[4]]:
            breed = i+1 # Foreign key is index + 1
            break

    color = ""
    for i in range(0, len(seen_color)):
        if seen_color[i] == [row[6], row[7], row[8]]:
            color = i+1
            break

    rescuer = ""
    for i in range(0, len(seen_rescuer)):
        if seen_rescuer[i] == row[18]:
            rescuer = i+1
            break

    location = ""
    for i in range(0, len(seen_location)):
        if seen_location[i] == row[17]:
            location = i+1
            break

    age = ""
    for i in range(0, len(seen_age)):
        if seen_age[i] == row[2]:
            age = i+1
            break

    # Fact data row, "" replaced with auto-increment
    data = ["", alt_id, breed, color, type, gender, age, location, maturity_size,
            fur_length, vaccinated, dewormed, sterilized, health,
            rescuer, video_amt, photo_amt, fee, adoptionspeed]
    file.writerow(data)

def main():
    # Input/Source file
    train = open("data/train.csv", "r", encoding='ISO-8859-1')
    color_labels_f = open("data/color_labels.csv", "r")
    breed_labels_f = open("data/breed_labels.csv", "r")
    state_labels_f = open("data/state_labels.csv", "r")

    # Output files
    breed = open("csv/DimBreed.csv", "w")
    breed_labels = open("csv/DimBreedLabels.csv", "w")
    color = open("csv/DimColor.csv", "w")
    color_labels = open("csv/DimColorLabels.csv", "w")
    location = open("csv/DimLocation.csv", "w")
    state = open("csv/DimState.csv", "w")
    gender = open("csv/DimGender.csv", "w")
    pet_type = open("csv/DimType.csv", "w")
    age = open("csv/DimAge.csv", "w")
    maturity_size = open("csv/DimMaturitySize.csv", "w")
    fur_length = open("csv/DimFurLength.csv", "w")
    vaccinated = open("csv/DimVaccinated.csv", "w")
    dewormed = open("csv/DimDewormed.csv", "w")
    sterilized = open("csv/DimSterilized.csv", "w")
    health = open("csv/DimHealth.csv", "w")
    rescuer = open("csv/DimRescuer.csv", "w")
    adoption_speed = open("csv/DimAdoptionSpeed.csv", "w")
    fact = open("csv/FactPetAdoptionRate.csv", "w")

    # Reader
    read_train = csv.reader(train)
    read_breed_labels = csv.reader(breed_labels_f)
    read_color_labels = csv.reader(color_labels_f)
    read_state_labels = csv.reader(state_labels_f)

    # Writers
    write_breed = csv.writer(breed)
    write_breed_labels = csv.writer(breed_labels)
    write_color = csv.writer(color)
    write_color_labels = csv.writer(color_labels)
    write_location = csv.writer(location)
    write_state_labels = csv.writer(state)
    write_gender = csv.writer(gender)
    write_pet_type = csv.writer(pet_type)
    write_age = csv.writer(age)
    write_maturity_size = csv.writer(maturity_size)
    write_fur_length = csv.writer(fur_length)
    write_vaccinated = csv.writer(vaccinated)
    write_dewormed = csv.writer(dewormed)
    write_sterilized = csv.writer(sterilized)
    write_health = csv.writer(health)
    write_rescuer = csv.writer(rescuer)
    write_adoption_speed = csv.writer(adoption_speed)
    write_fact = csv.writer(fact)

    # Custom headers (Based on the Snowflake Schema)
    header = next(read_train)
    write_breed.writerow(["BreedID", "PrimaryBreed", "SecondaryBreed", "BreedPurity"])
    write_color.writerow(["ColorID", "PrimaryColor", "SecondaryColor", "TertiaryColor", "ColorPurity"])
    write_location.writerow(["LocationID", "Location"])
    write_gender.writerow(["GenderID", "Gender"])
    write_pet_type.writerow(["TypeID", "Type"])
    write_age.writerow(["AgeID", "Age"])
    write_maturity_size.writerow(["MaturitySizeID", "MaturitySize"])
    write_fur_length.writerow(["FurLengthID", "FurLength"])
    write_vaccinated.writerow(["VaccinatedID", "Vaccinated"])
    write_dewormed.writerow(["DewormedID", "Dewormed"])
    write_sterilized.writerow(["SterilizedID", "Sterilized"])
    write_health.writerow(["HealthID", "Health"])
    write_adoption_speed.writerow(["AdoptionSpeedID", "AdoptionSpeed", "ListingDuration"])
    write_rescuer.writerow(["RescuerID", "Rescuer"])

    write_fact.writerow(["PetID", "PetAltID", "BreedID", "ColorID", "TypeID", "GenderID",
                        "AgeID", "LocationID", "MaturitySizeID", "FurLengthID", "VaccinatedID",
                        "DewormedID", "SterilizedID", "HealthID", "RescuerID", "VideoAmt",
                        "PhotoAmt", "Fee", "AdoptionSpeed"])

    # Extraction of data from color_labels.csv
    print("Extracting data from color_labels.csv")
    write_color_labels.writerow(next(read_color_labels))
    for row in read_color_labels:
        write_color_labels.writerow(["", row[1]])

    # Extraction of data from breed_labels.csv
    print("Extracting data from breed_labels.csv")
    header = next(read_breed_labels) # Skip the header - dont incl type
    write_breed_labels.writerow(["BreedLabelID", "BreedName"])
    for row in read_breed_labels:
        write_breed_labels.writerow(["", row[2]])

    # Extraction of data from state_labels.csv
    print("Extracting data from state_labels.csv")
    header = next(read_state_labels)
    write_state_labels.writerow(["StateID", "State"])
    for row in read_state_labels:
        write_state_labels.writerow([row[0], row[1]])

    # Breed, Color, Location, Age, Rescuer & Fact dimensions
    print("Extracting data from train.csv")
    for row in read_train:
        breed_data(write_breed, row)
        color_data(write_color, row)
        location_data(write_location, row)
        age_data(write_age, row)
        rescuer_data(write_rescuer, row)
        fact_data(write_fact, row)

    # Health
    write_health.writerow(["", "Healthy"])
    write_health.writerow(["", "Minor Injury"])
    write_health.writerow(["", "Serious Injury"])

    # Furlength
    write_fur_length.writerow(["", "Short"])
    write_fur_length.writerow(["", "Medium"])
    write_fur_length.writerow(["", "Long"])

    # MaturitySize
    write_maturity_size.writerow(["", "Small"])
    write_maturity_size.writerow(["", "Medium"])
    write_maturity_size.writerow(["", "Large"])
    write_maturity_size.writerow(["", "Extra Large"])

    # Gender
    write_gender.writerow(["", "Male"])
    write_gender.writerow(["", "Female"])
    write_gender.writerow(["", "Mixed"])

    # Type
    write_pet_type.writerow(["", "Dog"])
    write_pet_type.writerow(["", "Cat"])

    # Sterilized, Dewormed, Vaccinated
    generic_data(write_sterilized)
    generic_data(write_dewormed)
    generic_data(write_vaccinated)

    # Adoption speed
    write_adoption_speed.writerow(["", "Instant", 0])
    write_adoption_speed.writerow(["", "Fast", 7])
    write_adoption_speed.writerow(["", "Average", 30])
    write_adoption_speed.writerow(["", "Slow", 90])

if __name__ == '__main__':
    main()
