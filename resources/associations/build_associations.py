"""
This python script can be used to create the data use for
association rule minig in Weka.

Author: Bruce How (22242664) & Haolin Wu (21706137)
"""

import csv

speeds = ["Instant", "Fast", "Average", "Slow", "Not Adopted"]
states = {}

def get_color_purity(row):
    color2 = row[7]
    if color2 == 0:
        return "Pure"
    return "Mixed"

def get_breed_purity(row):
    breed2 = row[4]
    if breed2 == 0:
        return "Pure"
    return "Mixed"

def get_state_name(row):
    postcode = row[17]
    return states[postcode]

def get_adoption_speed(row):
    return speeds[int(row[23])]


def main():
    # Input and output files
    train = open("data/train.csv", "r", encoding='ISO-8859-1')
    state = open("data/state_labels.csv", "r")
    output = open("csv/associations.csv", "w")

    read_train = csv.reader(train)
    read_state = csv.reader(state)
    write_output = csv.writer(output)

    # Write headings
    write_output.writerow(["Type", "Age", "BreedPurity", "Gender", "ColorPurity",
                            "MaturitySize", "FurLength", "Vaccinated", "Dewormed",
                            "Sterilized", "Health", "Quantity", "Fee", "State",
                            "VideoAmt", "PhotoAmt", "AdoptionSpeed"])


    # Populate state dict
    print("Extracting data from state_labels.csv")
    next(read_state)
    for row in read_state:
        states[row[0]] = row[1]

    # Extraction of data from source
    print("Extracting data from train.csv")
    next(read_train) # Skip the header
    for row in read_train:
        type = row[0]
        age = row[2]
        breed_purity = get_breed_purity(row)
        gender = row[5]
        color_purity = get_color_purity(row)
        maturity_size = row[9]
        fur_length = row[10]
        vaccinated = row[11]
        dewormed = row[12]
        sterilized = row[13]
        health = row[14]
        quantity = row[15]
        fee = row[16]
        state = get_state_name(row)
        video_amt = row[19]
        photo_amt = int(float(row[22])) # PhotoAmt is of type float in train.csv
        adoption_speed = get_adoption_speed(row)

        write_output.writerow([type, age, breed_purity, gender, color_purity, maturity_size, fur_length, vaccinated, dewormed, sterilized, health,
        quantity, fee, state, video_amt, photo_amt, adoption_speed])

if __name__ == '__main__':
    main()
