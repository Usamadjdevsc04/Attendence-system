import csv
from datetime import datetime
import pandas as pd


class Human:
    all = []

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Human.all.append(self)


class employee(Human):
    def __init__(self, designation: str, joiningdate, department: str, employeeno: int, phonenumber: int):
        self.designation = designation
        self.joiningdate = joiningdate
        self.department = department
        self.employeeno = employeeno
        self.phonenumber = phonenumber
        employee.all.append(self)


class assets(Human):

    def __init__(self, name, age, designation, joiningdate, department, employeeno, phonenumber, assets):
        self.name = name
        self.age = age
        self.designation = designation
        self.joiningdate = joiningdate
        self.department = department
        self.employeeno = employeeno
        self.phonenumber = phonenumber
        self.assets = assets
        assets.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open('syncclouds.csv', 'a', newline="") as csvfile:
            fieldnames = ["name", "age", "designation", "joiningdate", "department", "employeeno", "phonenumber",
                          "assets"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writer.writeheader()
            while True:
                name = input("Enter the employee name : ")
                age = input("Enter age  :")
                designation = input("Enter the designation: ")
                joiningdate = input("Enter the joining date: ")
                department = input("Enter the department  : ")
                employeeno = input("Enter the employee no : ")
                phonenumber = input("Enter the phone number  : ")
                assets = input("Enter the assets  : ")
                with open("syncclouds.csv") as f:
                    reader = csv.reader(f)
                    header = reader
                if header == "":
                    writer.writeheader()
                writer.writerow(
                    {"assets": assets, "name": name, "age": age, "designation": designation, "joiningdate": joiningdate,
                     "department": department, "employeeno": employeeno, "phonenumber": phonenumber})
                want = input("Do you want more employees Y/N")
                if want == "n":
                    break


assets.instantiate_from_csv()

with open('syncclouds.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)


class attendance(employee):
    def __init__(self, employeeno, date, day, timein, timeout, breakin, breakout):
        self.employeeno = employeeno
        self.date = date
        self.day = day
        self.timein = timein
        self.timeout = timeout
        self.breakin = breakin
        self.breakout = breakout
        attendance.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open('attendance.csv', 'a', newline="") as csvfile:
            fieldnames = ["employeeno", "timein", "timeout", "breakin", "breakout"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            while True:
                employeeno = input("enter employeeno")
                timein = input("enter the time of entering the office : ")
                timeout = input("enter the time of leaving the office : ")
                breakin = input("enter the time for entering the office after break : ")
                breakout = input("enter the time of leaving the office for break : ")
                with open("attendance.csv") as f:
                    reader = csv.reader(f)
                    header = (reader)
                if header == "":
                    writer.writeheader()
                writer.writerow(
                    {"employeeno": employeeno, "timein": timein, "timeout": timeout, "breakin": breakin,
                     "breakout": breakout})
                break

            timein = print("entry time : ", timein)
            timeout = print("time to exit: ", timeout)
            breakout = print("time to exit from break: ", breakout)
            breakin = print("time to leave for break:", breakin)


attendance.instantiate_from_csv()

data = pd.read_csv("syncclouds.csv", index_col="employeeno")
first = data.loc["02"]
print(first)