from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = "ST1994" 

class User:
    directory = {}
    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name
        User.directory[username] = self #Directorio común donde estan los usuarios indexados

User ("jhondoe", "123456", "Jhon Doe")
User ("janedoe", "123456", "Jane Doe")

@app.route("/")
def home():
    if "username" in session:
        u = session ["username"]
        user = User.directory[u]
        return render_template("saludo.html", nombre = user.name)
    else:
        return redirect("/login")         
    


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method ==  "GET":
        return render_template ("login.html")
    else: 
        username = request.form["username"]
        password = request.form ["password"]
        if username in User.directory and password == User.directory[username].password:
            session["username"] = username
            return redirect("/")
        else:
            return render_template("login.html", error="Usuario o Contraseña incorrectas")




@app.route("/logout", methods=["POST"])
def cerrar_sesion(self):
        # Eliminar información de sesión
        self.username = None
        self.token = None  
        if "username" in session:
            u = session ["username"]
            return render_template("login.html", nombre = user.name)
        else:
            return redirect("/login")
 
def logout():
    self.username = None#Destruir información de sesión
    self.token = None #Redirigir a /login


   
   

if __name__ =="__main__": #Responsable de levantar el servidor local que pone en funcionamiento la aplicación
    app.run(debug=True)