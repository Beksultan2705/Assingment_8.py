import sqlite3

class Employee:
    def __init__(self, id=None, name='', position='', salary=0.0, hire_date=''):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.hire_date = hire_date

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Имя: {self.name}\n"
            f"Должность: {self.position}\n"
            f"Зарплата: {self.salary}\n"
            f"Дата найма: {self.hire_date}\n"
        )

class EmployeeDAO:
    def __init__(self, db_name="Employee_DB.sqlite"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()
        self.add_employees()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            position TEXT,
            salary REAL,
            hire_date TEXT
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def add_employees(self):
        cursor = self.conn.execute("SELECT COUNT(*) FROM employee")
        if cursor.fetchone()[0] == 0:
            self.insert(Employee(name="Артем", position="TeamLead", salary=125000, hire_date="2022-01-29"))
            self.insert(Employee(name="Микаил", position="Programmer", salary=80000, hire_date="2024-03-10"))

    def insert(self, employee: Employee):
        query = "INSERT INTO employee (name, position, salary, hire_date) VALUES (?, ?, ?, ?)"
        self.conn.execute(query, (employee.name, employee.position, employee.salary, employee.hire_date))
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT * FROM employee")
        return [Employee(*row) for row in cursor.fetchall()]

    def get_by_id(self, id):
        cursor = self.conn.execute("SELECT * FROM employee WHERE id = ?", (id,))
        row = cursor.fetchone()
        return Employee(*row) if row else None

    def update(self, employee: Employee):
        query = """
        UPDATE employee
        SET name = ?, position = ?, salary = ?, hire_date = ?
        WHERE id = ?
        """
        self.conn.execute(query, (employee.name, employee.position, employee.salary, employee.hire_date, employee.id))
        self.conn.commit()

    def delete(self, id):
        self.conn.execute("DELETE FROM employee WHERE id = ?", (id,))
        self.conn.commit()
