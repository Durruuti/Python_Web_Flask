from flask import Blueprint, render_template, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html", boolean=True)

@auth.route("/logout")
def logout():
    return "<h1>Cerrar sesión</h1>"

@auth.route("/sign-up", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("El correo tiene que ser mayor que 3 caracteres", category="error")
        elif len(firstName) < 2:
            flash("El nombre tiene que ser mayor que 1 caracteres", category="error")
        elif password1 != password2:
            flash("La contraseña no coincide", category="error")
        elif len(password1) < 7:
            flash("La contraseña mínimo tiene que tener 7 caracteres", category="error")
        else:
            new_user = User(email=email, firstName=firstName, password=)
            flash("¡Cuenta creada!", category="success")
            # añadir usuario a base de datos
    return render_template("sign-up.html")
