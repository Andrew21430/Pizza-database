import sqlite3


from flask import Flask, render_template, request


DATABASE = "Database.db"


app = Flask(__name__)








''' FUNCTIONS '''


''' Printing '''


def print_pizza():
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor() 
        # sql statement
        sql = "SELECT * FROM Pizza;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #print format
        print(f"{'id'} {'pizza':<40}")
        for pizza in results:
            #printing out the data
            print(f"{pizza[0]} {pizza[1]:<40}")
        db.close()


def print_base():
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        #sql statement
        sql = "SELECT * FROM Base;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #print format
        print(f"{'id'} {'base':<40}")
        for base in results:
            #printing out the data
            print(f"{base[0]} {base[1]:<40}")
        db.close()


def print_topping():
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        #sql statement
        sql = "SELECT * FROM Topping;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #print format
        print(f"{'id'} {'Topping':<40}")
        for topping in results:
            #printing out the data
            print(f"{topping[0]} {topping[1]:<40}")
        db.close()


'''Multi Table Printing'''


def  print_pizzabase():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT Pizza.id, Pizza.name, Pizza.description, Base.base FROM Pizza INNER JOIN Base ON Pizza.base_id = Base.id"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"{'id':<5} {'Pizza':<20} {'description':<100} {'base':<30}")
    for pizzabase in results:
        print(f"{pizzabase[0]:<5} {pizzabase[1]:<20} {pizzabase[2]:<100} {pizzabase[3]:<30}")


def print_pizzatopping():
    db= sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT Pizza.name, Topping.topping FROM Pizza INNER JOIN Pizza_Topping ON Pizza.id = Pizza_Topping.pizza_id INNER JOIN Topping ON Topping.id = Pizza_Topping.topping_id"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"{'Pizza':<20} {'Topping':<20}")
    for pizzatopping in results:
        print(f"{pizzatopping[0]:<20} {pizzatopping[1]:<20}")


def print_all():
    db= sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT Pizza.name, Topping.topping, Base.base FROM Pizza INNER JOIN Pizza_Topping ON Pizza.id = Pizza_Topping.pizza_id INNER JOIN Topping ON Topping.id = Pizza_Topping.topping_id INNER JOIN Base on Base.id = Pizza.base_id"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"{'Pizza':<20} {'Topping':<20} {'base':<20}")
    for all in results:
        print(f"{all[0]:<20} {all[1]:<20} {all[2]:<20}")


def printing():
    print = int(input("What would you like to print?\n (1) Pizza's \n (2) Base's \n (3) Toppngs\n (4) Pizza Bases \n (5) Pizza Toppings \n (6) All\n"))
    if print == 1:
        print_pizza()
    if print == 2:
        print_base()
    if print == 3:
        print_topping()
    if print == 4:
        print_pizzabase()
    if print == 5:
        print_pizzatopping()
    if print ==6:
        print_all()


def interface():
    function = int(input("What would you like to do? \n (1) Printing\n"))
    if function == 1:
        printing()

@app.route('/')

def homepage():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/pizza/<int:id>')
def pizza(id):
    db=sqlite3.connect(DATABASE)
    cursor= db.cursor()
    cursor.execute('SELECT * FROM Pizza WHERE pizza_id =?',(id,))
    pizza = cursor.fetchone()
    return render_template('pizza.html',pizza=pizza)

@app.route('/toppings')
def topping():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql='SELECT Pizza.name, Pizza.photo, Topping.topping FROM Pizza INNER JOIN Pizza_Topping ON Pizza.pizza_id = Pizza_Topping.pizza_id INNER JOIN Topping ON Topping.topping_id = Pizza_Topping.topping_id'
    cursor.execute(sql)
    results=cursor.fetchall()
    return render_template('toppings.html',results=results)


@app.route('/printtest')
def print():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor() 
    # sql statement
    sql = "SELECT * FROM Pizza;"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('printtest.html',results=results)
    
if __name__ == "__main__":
    app.run(debug=True)
interface()