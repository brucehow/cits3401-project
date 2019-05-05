"""
This python script can be used to extract data from the train.csv
to create the required csv files for each dimension.

Author: Bruce How (22242664) & Haolin Wu (21706137)
"""

import csv

def breed_data(file, row):
    breed1, breed2 = row[3], row[4]
    data = ["", breed1, breed2]
    file.writerow(data)

def color_data(file, row):
    color1, color2, color3 = row[6], row[7], row[8]
    data = ["", color1, color2, color3]
    file.writerow(data)

def location_data(file, row):
    location = row[17]
    data = ["", location]
    file.writerow(data)

def gender_data(file, row):
    gender = row[5]
    data = ["", gender]
    file.writerow(data)

def type_data(file, row):
    type = row[0]
    data = ["", type]
    file.writerow(data)

def generic_data(file):
    file.writerow(["", "Yes"])
    file.writerow(["", "No"])
    file.writerow(["", "Not Sure"])

def rescuer_data(file, row):
    rescuer = row[18]
    data = ["", rescuer]
    file.writerow(data)

def main():
    # Input/Source file
    train = open("data/train.csv", "r", encoding='ISO-8859-1')

    # Output files
    breed = open("csv/DimBreed.csv", "w")
    color = open("csv/DimColor.csv", "w")
    location = open("csv/DimLocation.csv", "w")
    gender = open("csv/DimGender.csv", "w")
    type = open("csv/DimType.csv", "w")
    age = open("csv/DimAge.csv", "w")
    maturity_size = open("csv/DimMaturitySize.csv", "w")
    fur_length = open("csv/DimFurLength.csv", "w")
    vaccinated = open("csv/DimVaccinated.csv", "w")
    dewormed = open("csv/DimDewormed.csv", "w")
    sterilized = open("csv/DimSterilized.csv", "w")
    health = open("csv/DimHealth.csv", "w")
    rescuer = open("csv/DimRescuer.csv", "w")
    fact = open("csv/FactPetAdoptionRate.csv", "w")

    # Reader/Writers
    read_train = csv.reader(train)
    write_breed = csv.writer(breed)
    write_color = csv.writer(color)
    write_location = csv.writer(location)
    write_gender = csv.writer(gender)
    write_type = csv.writer(type)
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
    write_breed.writerow(["BreedID", "PrimaryBreed", "SecondaryBreed"])
    write_color.writerow(["ColorID", "PrimaryColor", "SecondaryColor", "TertiaryColor"])
    write_location.writerow(["LocationID", "Location"])
    write_gender.writerow(["GenderID", "Gender"])
    write_type.writerow(["TypeID", "Type"])
    write_rescuer.writerow(["RescuerID", "Rescuer"])
    write_health.writerow(["HealthID", "Health"])


    # Iterate through each row from train.csv
    for row in read_train:
        breed_data(write_breed, row)
        color_data(write_color, row)
        location_data(write_location, row)
        gender_data(write_gender, row)
        type_data(write_type, row)
        rescuer_data(write_rescuer, row)

    # Health
    write_health.writerow(["", "Healthy"])
    write_health.writerow(["", "Minor Injury"])
    write_health.writerow(["", "Serious Injury"])

    # Sterilized, Dewormed, Vaccinated
    generic_data(write_sterilized)
    generic_data(write_dewormed)
    generic_data(write_vaccinated)

    # TODO Iterate through each row from color_labels.csv

if __name__ == '__main__':
    main()
