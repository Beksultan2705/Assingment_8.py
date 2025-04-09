from Employee_DB import Employee, EmployeeDAO

def main():
    db = EmployeeDAO()

    while True:
        print("\nМеню:")
        print("1. Показать всех")
        print("2. Добавить")
        print("3. Найти по ID")
        print("4. Обновить")
        print("5. Удалить")
        print("6. Выход")

        cmd = input("Выбери действие: ")

        if cmd == "1":
            employees = db.get_all()
            if employees:
                for emp in employees:
                    print("\n" + str(emp))
            else:
                print("Список сотрудников пуст.")

        elif cmd == "2":
            name = input("Имя: ")
            pos = input("Должность: ")
            sal = input("Зарплата: ")
            date = input("Дата найма (YYYY-MM-DD): ")
            try:
                sal = float(sal)
                db.insert(Employee(name=name, position=pos, salary=sal, hire_date=date))
                print("Сотрудник добавлен.")
            except ValueError:
                print("Ошибка: Зарплата должна быть числом.")

        elif cmd == "3":
            id = input("ID: ")
            try:
                id = int(id)
                emp = db.get_by_id(id)
                print("\n" + str(emp) if emp else "Сотрудник не найден.")
            except ValueError:
                print("Ошибка: ID должен быть целым числом.")

        elif cmd == "4":
            id = input("ID: ")
            try:
                id = int(id)
                emp = db.get_by_id(id)
                if not emp:
                    print("Сотрудник не найден.")
                    continue
                emp.name = input(f"Имя ({emp.name}): ") or emp.name
                emp.position = input(f"Должность ({emp.position}): ") or emp.position
                salary = input(f"Зарплата ({emp.salary}): ")
                emp.salary = float(salary) if salary else emp.salary
                emp.hire_date = input(f"Дата найма ({emp.hire_date}): ") or emp.hire_date
                db.update(emp)
                print("Данные сотрудника обновлены.")
            except ValueError:
                print("Ошибка: Неверный формат ввода.")

        elif cmd == "5":
            id = input("ID: ")
            try:
                id = int(id)
                emp = db.get_by_id(id)
                if emp:
                    db.delete(id)
                    print("Сотрудник удалён.")
                else:
                    print("Сотрудник не найден.")
            except ValueError:
                print("Ошибка: ID должен быть целым числом.")

        elif cmd == "6":
            print("Выход из программы.")
            break

        else:
            print("Ошибка ввода. Пожалуйста, выберите действие из меню.")

if __name__ == "__main__":
    main()
