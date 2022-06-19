from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('El Email debe ser mayor a 3 carácteres.', category='error')
        elif len(firstName) < 2:
            flash('El nombre debe ser mayor a 1 carácter.', category='error')
        elif password1 != password2:
            flash('Las contraseñas deben ser iguales.', category='error')
        elif len(password1) < 7:
            flash('La contraseña debe tener al menos 7 carácteres.', category='error')
        else:
            # Add user to Database
            flash('Cuenta creada con éxito!.', category='success')
    
    return render_template("sign_up.html")

