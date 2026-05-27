from fastapi import FastAPI
import mysql.connector



conn_obj = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Divya@801",
    database="API_CRUD"
)

cursor_obj = conn_obj.cursor(dictionary=True)

# CREATE TABLE
create_table_query = """
CREATE TABLE IF NOT EXISTS expenses(

    expense_id INT PRIMARY KEY AUTO_INCREMENT,

    title VARCHAR(100),

    amount INT,

    category VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
"""

cursor_obj.execute(create_table_query)
conn_obj.commit()

app = FastAPI()



@app.get("/")
def home():
    return {"msg": "Expense Tracker API Running"}



@app.post("/add_expense")
def add_expense(new_data: dict):

    title = new_data["t"]
    amount = new_data["a"]
    category = new_data["c"]

    query = """
    INSERT INTO expenses(title, amount, category)
    VALUES(%s,%s,%s)
    """

    values = (title, amount, category)

    cursor_obj.execute(query, values)

    conn_obj.commit()

    return {"msg": "Expense Added Successfully"}


@app.get("/view_expenses")
def view_expenses():

    query = "SELECT * FROM expenses"

    cursor_obj.execute(query)

    data = cursor_obj.fetchall()

    return data

@app.delete("/delete_expense/{expense_id}")
def delete_expense(expense_id: int):
    query="delete from expenses where expense_id=%s"
    cursor_obj.execute(query,(expense_id,))
    conn_obj.commit()
    return{"msg":"Expense Deleted Sucessfully"}

@app.put("/update_expense/{expense_id}")
def update_expense(expense_id: int, new_data: dict):

    title = new_data["t"]
    amount = new_data["a"]
    category = new_data["c"]

    query = """
    UPDATE expenses
    SET title=%s,
        amount=%s,
        category=%s
    WHERE expense_id=%s
    """

    values = (title, amount, category, expense_id)

    cursor_obj.execute(query, values)

    conn_obj.commit()

    return {"msg": "Expense Updated Successfully"}

@app.get("/search_expense?{category}")
def search_expense(category: str):
    query = """
    SELECT * FROM expenses
    WHERE category=%s
    """
    cursor_obj.execute(query,(category,))
    data=cursor_obj.fetchall()
    return data
@app.get("/sort_expense/{sort_type}")
def sort_expense(sort_type: str):

    if sort_type == "high":
        query = "SELECT * FROM expenses ORDER BY amount DESC"

    elif sort_type == "low":
        query = "SELECT * FROM expenses ORDER BY amount ASC"

    else:
        query = "SELECT * FROM expenses"

    cursor_obj.execute(query)

    data = cursor_obj.fetchall()

    return data
