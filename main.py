import flask
from flask import Flask, render_template,request
import sqlite3
conn = sqlite3.connect("studentmanagement.db",check_same_thread=False)

listOfTables=conn.execute("SELECT name from sqlite_master WHERE type='table' AND name='STUDENT' ").fetchall()



if listOfTables!=[]:
    print("Table Already Exists ! ")
else:
    conn.execute(''' CREATE TABLE STUDENT(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT,ADNO INTEGER,ROLLNUMBER INTEGER,BRANCH TEXT,SEMESTER TEXT,
    DOB TEXT,USERNAME TEXT,PASSWORD TEXT); ''')


cursor = conn.cursor()




ap = Flask(__name__)


@ap.route("/")
def hom():
    return render_template("login.html")


@ap.route("/search")
def sea():
    return render_template("search.html")


@ap.route("/delete")
def delete():
    return render_template("delete.html")


@ap.route("/register", methods = ["GET", "POST"])
def regis():
    if request.method=="POST":
        getName=request.form["name"]
        getAdmno=request.form["admno"]
        getRoll0no=request.form["Rollno"]
        getBranch= request.form["br"]
        getSemester= request.form["sem"]
        getDOB=request.form["dob"]
        getUsername= request.form["username"]
        getPass = request.form["pass"]
        print(getName)
        print(getAdmno)
        print(getRoll0no)
        print(getBranch)
        print(getSemester)
        print(getDOB)
        print(getUsername)
        print(getPass)
        try:
            conn.execute("INSERT INTO STUDENT (name,ADNO,ROLLNUMBER,BRANCH,SEMESTER,DOB,USERNAME,PASSWORD) VALUES ('"+getName+"',"+getAdmno+","+getRoll0no+",'"+getBranch+"',"+getSemester+",'"+getDOB+"','"+getUsername+"','"+getPass+"')")
            print("Successfully inserted")
        except Exception as e:
            print(e)

    return render_template("register.html")


if __name__ == "__main__":
    ap.run()