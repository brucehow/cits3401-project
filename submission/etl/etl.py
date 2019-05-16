"""
This python script can be used to extract data from the train.csv
to create the required csv files for each dimension.

Author: Bruce How (22242664) & Haolin Wu (21706137)
"""

import csv

# Global variables used to store already seen rows
seen_breed = []
seen_color = []
seen_rescuer = []
seen_location = []
rowIndex = 0

def breed_data(file, row):
    breed1, breed2 = row[3], row[4]

    # Check to see if we have already seen the breed
    if [breed1, breed2] in seen_breed:
        return # Already exists, don't add duplicates

    seen_breed.append([breed1, breed2])

    breed_purity = "Mixed"
    if breed2 == "0":
        breed_purity = "Pure"

    data = ["", breed1, breed2, breed_purity]
    file.writerow(data)

def color_data(file, row):
    color1, color2, color3 = row[6], row[7], row[8]

    if [color1, color2, color3] in seen_color:
        return

    seen_color.append([color1, color2, color3])

    color_purity = "Mixed"
    if color2 == "0" or color3 == "0":
        color_purity = "Pure"

    data = ["", color1, color2, color3, color_purity]
    file.writerow(data)

def location_data(file, row):
    location = row[17]

    if location in seen_location:
        return

    seen_location.append(location)
    data = ["", location]
    file.writerow(data)

def gender_data(file, row):
    gender = row[5]
    data = ["", gender]
    file.writerow(data)

def pet_type_data(file, row):
    pet_type = row[0]
    data = ["", pet_type]
    file.writerow(data)

def age_data(file, row):
    age = row[2]
    data = ["", age]
    file.writerow(data)

def maturity_size_data(file, row):
    maturity_size = row[9]
    data = ["", maturity_size]
    file.writerow(data)

def fur_length_data(file, row):
    fur_length = row[10]
    data = ["", fur_length]
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

    # Measures
    video_amt = row[19]
    photo_amt = row[22]
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

    # Pet age
    global rowIndex
    rowIndex += 1 # Each row represents an individual pet's age

    # Fact data row, "" replaced with auto-increment
    data = ["", alt_id, breed, color, type, gender, rowIndex, location, maturity_size,
            fur_length, vaccinated, dewormed, sterilized, health,
            rescuer, video_amt, photo_amt, fee, adoptionspeed]
    file.writerow(data)

def main():
    # Input/Source file
    train = open("data/train.csv", "r", encoding='ISO-8859-1')
    color_labels_f = open("data/color_labels.csv", "r")
    breed_labels_f = open("data/breed_labels.csv", "r")

    # Output files
    breed = open("csv/DimBreed.csv", "w")
    breed_labels = open("csv/DimBreedLabels.csv", "w")
    color = open("csv/DimColor.csv", "w")
    color_labels = open("csv/DimColorLabels.csv", "w")
    location = open("csv/DimLocation.csv", "w")
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
    fact = open("csv/FactPetAdoptionRate.csv", "w")

    # Reader
    read_train = csv.reader(train)
    read_breed_labels = csv.reader(breed_labels_f)
    read_color_labels = csv.reader(color_labels_f)

    # Writers
    write_breed = csv.writer(breed)
    write_breed_labels = csv.writer(breed_labels)
    write_color = csv.writer(color)
    write_color_labels = csv.writer(color_labels)
    write_location = csv.writer(location)
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
    write_rescuer.writerow(["RescuerID", "Rescuer"])

    write_fact.writerow(["PetID", "PetAltID", "BreedID", "ColorID", "TypeID", "GenderID",
                        "AgeID", "LocationID", "MaturitySizeID", "FurLengthID", "VaccinatedID",
                        "DewormedID", "SterilizedID", "HealthID", "RescuerID", "VideoAmt",
                        "PhotoAmt", "Fee", "AdoptionSpeed"])

    # Populate csv files, iterate through each row from train.csv
    for row in read_train:
        breed_data(write_breed, row)
        color_data(write_color, row)
        location_data(write_location, row)
        gender_data(write_gender, row)
        pet_type_data(write_pet_type, row)
        age_data(write_age, row)
        maturity_size_data(write_maturity_size, row)
        fur_length_data(write_fur_length, row)
        rescuer_data(write_rescuer, row)
        fact_data(write_fact, row)

    # Health
    write_health.writerow(["", "Healthy"])
    write_health.writerow(["", "Minor Injury"])
    write_health.writerow(["", "Serious Injury"])

    # Sterilized, Dewormed, Vaccinated
    generic_data(write_sterilized)
    generic_data(write_dewormed)
    generic_data(write_vaccinated)

    # Iterate through each row from color_labels.csv
    write_color_labels.writerow(next(read_color_labels))
    for row in read_color_labels:
        write_color_labels.writerow(["", row[1]])

    # Iterate through each row from breed_labels.csv
    header = next(read_breed_labels) # Skip the header - dont incl type
    write_breed_labels.writerow(["BreedLabelID", "BreedName"])
    for row in read_breed_labels:
        write_breed_labels.writerow(["", row[2]])


if __name__ == '__main__':
    main()
