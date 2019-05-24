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
    color3 = row[8]
    if color2 == "0" and color3 == "0":
        return "Pure"
    return "Mixed"

def get_type(row):
    pet_type = row[0]
    if pet_type == "2":
        return "Cat"
    return "Dog"

def get_age(row):
    age = row[2]
    if int(age) <= 2:
        return "0to2Months"
    elif int(age) > 2 and int(age) < 6:
        return "2to5Months"
    else:
        return "5orMoreMonths"

def get_fee(row):
    fee = row[16]
    if fee == "0":
        return "Free"
    else:
        return "NotFree"

def get_quantity(row):
    quantity = row[15]
    if quantity == "1":
        return "Single"
    else:
        return "Multiple"

def get_video_amt(row):
    video_amt = row[19]
    if video_amt == "0":
        return "None"
    else:
        return "VideosUploaded"

def get_photo_amt(row):
    photo_amt = int(float(row[22]))
    if photo_amt == 0 or photo_amt == 1:
        return "OneOrLess"
    elif photo_amt == 2:
        return "Two"
    elif photo_amt == 3:
        return "Three"
    elif photo_amt == 4:
        return "Four"
    elif photo_amt == 5:
        return "Five"
    else:
        return "5orMore"

def get_gender(row):
    gender = row[5]
    if gender == "1":
        return "Male"
    elif gender == "2":
        return "Female"
    else:
        return "Mixed"

def get_breed_purity(row):
    breed2 = row[4]
    if breed2 == "0":
        return "Pure"
    return "Mixed"

def get_maturity_size(row):
    maturity_size = row[9]
    if maturity_size == "1":
        return "Small"
    elif maturity_size == "2":
        return "Medium"
    elif maturity_size == "3":
        return "Large"
    elif maturity_size == "4":
        return "Extra Large"
    else:
        return "Not Specified"

def get_vaccinated(row):
    vaccinated = row[11]
    if vaccinated == "1":
        return "Yes"
    elif vaccinated == "2":
        return "No"
    else:
        return "Not Sure"

def get_dewormed(row):
    dewormed = row[12]
    if dewormed == "1":
        return "Yes"
    elif dewormed == "2":
        return "No"
    else:
        return "Not Sure"

def get_sterilized(row):
    sterilized = row[13]
    if sterilized == "1":
        return "Yes"
    elif sterilized == "2":
        return "No"
    else:
        return "Not Sure"

def get_fur_length(row):
    fur_length = row[10]
    if fur_length == "1":
        return "Short"
    elif fur_length == "2":
        return "Medium"
    elif fur_length == "3":
        return "Long"
    else:
        return "Not Specified"

def get_health(row):
    health = row[14]
    if health == "1":
        return "Healthy"
    elif health == "2":
        return "Minor Injury"
    elif health == "3":
        return "Serious Injury"
    else:
        return "Not Specified"

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
        type = get_type(row)
        age = get_age(row)
        breed_purity = get_breed_purity(row)
        gender = get_gender(row)
        color_purity = get_color_purity(row)
        maturity_size = get_maturity_size(row)
        fur_length = get_fur_length(row)
        vaccinated = get_vaccinated(row)
        dewormed = get_dewormed(row)
        sterilized = get_sterilized(row)
        health = get_health(row)
        quantity = get_quantity(row)
        fee = get_fee(row)
        state = get_state_name(row)
        video_amt = get_video_amt(row)
        photo_amt = get_photo_amt(row) # PhotoAmt is of type float in train.csv
        adoption_speed = get_adoption_speed(row)

        write_output.writerow([type, age, breed_purity, gender, color_purity, maturity_size, fur_length, vaccinated, dewormed, sterilized, health,
        quantity, fee, state, video_amt, photo_amt, adoption_speed])

if __name__ == '__main__':
    main()
