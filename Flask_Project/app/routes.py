from flask import render_template, url_for, flash, request, redirect
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User
from flask_login import login_user, current_user, logout_user

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(fullname=form.fullname.data, email=form.email.data, tel=form.tel.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Log in successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('register'))


@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html', title='Dashboard')



@app.route("/assess")
def assess():
    return render_template('assessment.html', title='Self Assessment Test')

@app.route("/selftest",methods=["GET","POST"])
def selftest():
    comp = []
    resp = request.form.getlist('meet')
    for i in resp:
        comp.append(int(i))
    result = sum(comp)
    if result >= 50:
        return render_template("highrisk.html")
    elif result < 50:
        return render_template("lowrisk.html")	

@app.route("/medicalhistory")
def medhistory():
    return render_template('medhistory.html',title='Medical history')
@app.route("/meddata",methods=["GET","POST"])
def meddata():
    name = request.form["name"]
    age = request.form["age"]
    email = request.form["email"]
    phone = request.form["phone"]
    blood = request.form["blood"]
    gender = request.form["gender"]
    comor = request.form["diab"]
    specs = request.form["specs"]
    age = int(age)
    phone = int(phone)
    with sql.connect("medhistory.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO history(name,age,email,phone,blood,gender,comor,specs) VALUES(?,?,?,?,?,?,?,?)",
                    (name,age,email,phone,blood,gender,comor,specs))
        con.commit()
    flash('Details recorded successfully','success')
    return render_template("dashboard.html")
    con.close()

