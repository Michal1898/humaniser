import csv
import json
from random import choice, randrange
from datetime import timedelta, date

FEMALE=True
MALE=False
START_DATE=date(1930,1,1)
END_DATE=date(2016,1,1)

with open("names_cr/krestni_muzi.csv", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    data = list(reader)

first_names=[]
for record in data[:250]:
    first_names.append(record[1])

with open("names_cr/prijmeni_muzi_1.csv", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    data = list(reader)

surnames=[]
for record in data[:250]:
    surnames.append(record[1])

addresses=[]
for adr_index in range(1,8):
    address_path="addresses_cr/adr_"+str(adr_index)+".csv"
    with open(address_path, encoding="windows-1250", newline="") as f:
        reader = csv.reader(f)
        data = list(reader)

        for record in data[1:]:
            addresses.append(record)

    customer_db=[]
for a in range (0,100):
    person={}
    person["firstname"] = choice(first_names)
    person["surname"] = choice(surnames)
    person["gender"] = MALE
    time_between_dates = END_DATE-START_DATE
    days_between_dates = time_between_dates.days
    random_number_of_days = randrange(days_between_dates)
    random_date = START_DATE + timedelta(days=random_number_of_days)
    person["birthdate"]=random_date.strftime("%Y-%m-%d")
    person_address = choice(addresses)
    person_address = person_address[0]
    person_address=person_address.split(";" , -1)

    person["city"] = person_address[0]
    person["street"] = person_address[1]
    person["house_no"] = person_address[2]
    person["plz"] = person_address[3]

    customer_db.append(person)

with open("names_cr/krestni_zeny.csv", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    data = list(reader)

first_names=[]
for record in data[:250]:
    first_names.append(record[1])

with open("names_cr/prijmeni_zeny_1.csv", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    data = list(reader)

surnames=[]
for record in data[:250]:
    surnames.append(record[1])

for a in range (0,100):
    person={}
    person["firstname"] = choice(first_names)
    person["surname"] = choice(surnames)
    person["gender"] = FEMALE
    time_between_dates = END_DATE-START_DATE
    days_between_dates = time_between_dates.days
    random_number_of_days = randrange(days_between_dates)
    random_date = START_DATE + timedelta(days=random_number_of_days)
    person["birthdate"]=random_date.strftime("%Y-%m-%d")

    person_address = choice(addresses)
    person_address = person_address[0]
    person_address=person_address.split(";" , -1)

    person["city"] = person_address[0]
    person["street"] = person_address[1]
    person["house_no"] = person_address[2]
    person["plz"] = person_address[3]

    customer_db.append(person)

print(customer_db)

with open("output/customer_db.json", 'w') as out_file:
    json.dump(customer_db, out_file, indent=2)