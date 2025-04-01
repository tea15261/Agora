from flask import render_template, Blueprint, request, redirect, url_for, session, flash
from app.db import db, User

bp = Blueprint('main', __name__)
bp.secret_key = "2338724829301376494238947647623886783284y9"

@bp.route('/')
def index():
    if "username" in session:
        return redirect(url_for('main.dashboard'))
    return render_template('index.html')

@bp.route('/faq')
def faq():
    return render_template('faq.html')

@bp.route('/contact')
def contact():
    return render_template('contact.html')

@bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', username=session.get('username'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session["username"] = user.name  # Store username in session
            flash("Login successful!", "success")
            print("User logged in:", user.name)
            return redirect(url_for('main.dashboard'))  # Redirect to dashboard

        flash("Invalid email or password", "danger")
        print("Invalid login attempt for email:", email)
        return redirect(url_for('main.login'))  # Reload login page

    return render_template('login.html')

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if user already exists
        if User.query.filter_by(email=email).first():
            flash("Email already registered!", "warning")
            print("Email already registered:", email)
            return redirect(url_for('main.signup'))
        
        if User.query.filter_by(name=name).first():
            flash("Name already registered!", "warning")
            print("Name already registered:", name)
            return redirect(url_for('main.signup'))

        # Create new user
        new_user = User(name=name, email=email)
        new_user.set_password(password)  # Hash password before storing

        db.session.add(new_user)
        db.session.commit()

        flash("Signup successful! Please login.", "success")
        print("Signup successful for user:", name)
        return redirect(url_for('main.login'))

    return render_template('signup.html')

@bp.route('/logout')
def logout():
    session.pop("username", None)
    flash("Logged out successfully.", "info")
    print("User logged out")
    return redirect(url_for('main.index'))