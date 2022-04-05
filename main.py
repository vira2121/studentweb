from flask import Flask, render_template,request

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
        print(getBranch)
        print(getRoll0no)
        print(getSemester)
        print(getDOB)
        print(getUsername)
        print(getPass)
    return render_template("register.html")


if __name__ == "__main__":
    ap.run()