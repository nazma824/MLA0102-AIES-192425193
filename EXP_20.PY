# Person DOB Knowledge Base

# Knowledge Base: DOB -> Person Details
person_db = {
    "15-08-1998": {
        "Name": "Arun",
        "Age": 28,
        "Gender": "Male",
        "Address": "Chennai",
        "Phone": "9876543210",
        "Occupation": "Engineer"
    },

    "22-03-2000": {
        "Name": "Priya",
        "Age": 26,
        "Gender": "Female",
        "Address": "Bangalore",
        "Phone": "9876501234",
        "Occupation": "Doctor"
    },

    "10-12-1995": {
        "Name": "Karthik",
        "Age": 30,
        "Gender": "Male",
        "Address": "Coimbatore",
        "Phone": "9876512345",
        "Occupation": "Teacher"
    },

    "05-07-2002": {
        "Name": "Divya",
        "Age": 24,
        "Gender": "Female",
        "Address": "Madurai",
        "Phone": "9876523456",
        "Occupation": "Designer"
    }
}


# Logical reasoning/query function
def find_person_by_dob(dob):
    if dob in person_db:
        details = person_db[dob]

        print("Person Details")
        print("------------------------")
        print("Name       :", details["Name"])
        print("DOB        :", dob)
        print("Age        :", details["Age"])
        print("Gender     :", details["Gender"])
        print("Address    :", details["Address"])
        print("Phone      :", details["Phone"])
        print("Occupation :", details["Occupation"])
    else:
        print("Person not found")


# Query
dob = input("Enter Date of Birth (DD-MM-YYYY): ")
find_person_by_dob(dob)
