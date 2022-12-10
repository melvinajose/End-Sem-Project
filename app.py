from flask import Flask, render_template, request, session, redirect, url_for, jsonify;
from flask_mysqldb import MySQL;
import yaml;
from werkzeug.security import generate_password_hash, check_password_hash;

app = Flask(__name__)

app.secret_key = 'voyage'

db = yaml.full_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'v.o.y.a.g.e.tms@gmail.com'
app.config['MAIL_PASSWORD'] = 'Voyage@123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mysql = MySQL(app)

@app.route('/')
def index1():
    return render_template('main.html')
    
@app.route('/index', methods=['GET','POST'])
def index():
    msg = ''
    if "name" in session:
        name = session["name"]
        initial = name
        return render_template('main1.html', initial = initial)
    else:
        return redirect(url_for('login'))
    if request.method == 'POST':
        contactUs = request.form 
        name = contactUs['name']
        email = contactUs['email']
        message = contactUs['message']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contactUs(name, email, message) VALUES(%s, %s, %s)", (name, email, message))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))
    return render_template('index.html')
    
@app.route('/signup.html', methods=['GET','POST'])
def signup():
    msg=''
    if request.method == 'POST':
        userDetails = request.form 
        name = userDetails['name']
        email = userDetails['email']
        phno = userDetails['phno']
        psswd = userDetails['psswd']
        psswd_hash = generate_password_hash(psswd)
        pswdconfirm = userDetails['pswdconfirm']
        cur = mysql.connection.cursor()
        if psswd == pswdconfirm:
            cur.execute("INSERT INTO users(name, email, phno, psswd, passwd) VALUES(%s, %s, %s, %s, %s)", (name, email, phno, psswd_hash, psswd))
            mysql.connection.commit()
            cur.close()
            msg = 'Signup successful!!'
            return redirect(url_for('login'))
        else:
            msg = 'Incorrect Password!!'
    return render_template('signup.html', msg = msg)

@app.route('/login1.html', methods=['GET','POST'])
def login1():
    msg=''
    if request.method == 'POST':
        userDetails = request.form 
        name = userDetails['name']
        psswd = userDetails['psswd']
        cur = mysql.connection.cursor()
        cur.execute('SELECT psswd FROM users WHERE name = %s', (name, ))
        password = cur.fetchone()
        psswd_hash = check_password_hash(password, psswd)
        print(psswd_hash)
        if psswd_hash == True:
            session['loggedin'] = True
            session['name'] = name
            return redirect(url_for('main1'))
        else:
            msg = 'Invalid Credentials!!'
    return render_template('login1.html', msg = msg)

@app.route('/login.html', methods=['GET','POST'])
def login():
    msg=''
    if request.method == 'POST':
        userDetails = request.form 
        name = userDetails['name']
        psswd = userDetails['psswd']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE name = %s AND passwd = %s', (name, psswd))
        account = cur.fetchone()
        if account:
            session['loggedin'] = True
            session['name'] = name
            return redirect(url_for('main1'))
        else:
            msg = 'Invalid Credentials!!'
    return render_template('login.html', msg = msg)


@app.route('/main1.html')
def main1():
    msg = ''
    if "name" in session:
        name = session["name"]
        initial = name
        return render_template('main1.html', initial = initial)
    else:
        return redirect(url_for('login'))

@app.route('/booking2.html', methods=['GET','POST'])
def booking2():
    if request.method == 'POST':
        bookingDetails = request.form 
        from_city = bookingDetails['from_city']
        to_city = bookingDetails['to_city']
        d_date = bookingDetails['d_date']
        a_date = bookingDetails['a_date']
        adult_no = bookingDetails['adult_no']
        child_no = bookingDetails['child_no']
        session['to_city'] = to_city
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO bookings(name, from_city, to_city, d_date, a_date, adult_no, child_no) VALUES(%s, %s, %s, %s, %s, %s, %s)", (str(session.get('name')), from_city, to_city, d_date, a_date, adult_no, child_no))
        mysql.connection.commit()
        cur.close()
        return render_template('confirm.html')
    return render_template('booking2.html')

@app.route('/confirm.html' )
def confirm():
    return render_template('confirm.html')

@app.route('/confirm1.html')
def confirm1():
   msg = Message('Booking Confirmation', sender = 'v.o.y.a.g.e.tms@gmail.com', recipients = [''])
   msg.body = "Your booking has been confirmed by Voyage!! Have a great holiday time!!!"
   mail.send(msg)
   return "Sent"
   return redirect(url_for('index'))
   return render_template('confirm1.html')

@app.route('/yatch.html')
def yatch():
    return render_template('yatch.html')

@app.route('/forgotpass.html')
def forgotpass():
    return render_template('forgotpass.html')

@app.route('/tourplace.html')
def tourplace():
    return render_template('tourplace.html')

@app.route('/hiking.html')
def hiking():
    return render_template('hiking.html')

@app.route('/california.html')
def california():
    return render_template('california.html')

@app.route('/losangeles.html')
def losangeles():
    return render_template('losangeles.html')

@app.route('/newjersey.html')
def newjersey():
    return render_template('newjersey.html')

@app.route('/newyork.html')
def newyork():
    return render_template('newyork.html')

@app.route('/sanfrancisco.html')
def sanfrancisco():
    return render_template('sanfrancisco.html')

@app.route('/stories-booking1.html')
def storiesbooking1():
    return render_template('stories-booking1.html')

@app.route('/stories-booking.html')
def storiesbooking():
    return render_template('stories-booking.html')

@app.route('/stories-hotel.html')
def storieshotel():
    return render_template('stories-hotel.html')

@app.route('/stories-stay.html')
def storiesstay():
    return render_template('stories-stay.html')

@app.route('/virginia.html')
def virginia():
    return render_template('virginia.html')

@app.route("/logout")
def logout():
    session.pop("name", None)
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True)

