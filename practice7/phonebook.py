import csv
from psycopg2.extras import execute_batch
from connect import get_connection, create_table


def insert_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO contacts (first_name, phone) VALUES (%s, %s)",
            (name, phone)
        )
        conn.commit()
        print("Contact added successfully!")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    finally:
        cur.close()
        conn.close()


def import_csv():
    conn = get_connection()
    cur = conn.cursor()

    try:
        with open("contacts.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            data = [
                (row["first_name"], row["phone"])
                for row in reader
            ]

        execute_batch(
            cur,
            """
            INSERT INTO contacts (first_name, phone)
            VALUES (%s, %s)
            ON CONFLICT (phone) DO NOTHING
            """,
            data
        )

        conn.commit()
        print("CSV imported successfully!")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    finally:
        cur.close()
        conn.close()


def update_contact():
    phone = input("Enter current phone number: ")
    name = input("Enter new name (leave empty to skip): ")
    new_phone = input("Enter new phone (leave empty to skip): ")

    if not name and not new_phone:
        print("Nothing to update.")
        return

    conn = get_connection()
    cur = conn.cursor()

    try:
        if name and new_phone:
            cur.execute(
                "UPDATE contacts SET first_name = %s, phone = %s WHERE phone = %s",
                (name, new_phone, phone)
            )
        elif name:
            cur.execute(
                "UPDATE contacts SET first_name = %s WHERE phone = %s",
                (name, phone)
            )
        else:
            cur.execute(
                "UPDATE contacts SET phone = %s WHERE phone = %s",
                (new_phone, phone)
            )

        conn.commit()

        if cur.rowcount:
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    finally:
        cur.close()
        conn.close()


def search_contacts():
    print("1. Search by name")
    print("2. Search by phone prefix")

    choice = input("Choose search type: ")
    value = input("Enter search value: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        cur.execute(
            "SELECT * FROM contacts WHERE first_name ILIKE %s ORDER BY id",
            (f"%{value}%",)
        )
    elif choice == "2":
        cur.execute(
            "SELECT * FROM contacts WHERE phone LIKE %s ORDER BY id",
            (f"{value}%",)
        )
    else:
        print("Invalid choice.")
        cur.close()
        conn.close()
        return

    results = cur.fetchall()

    for contact in results:
        print(contact)

    if not results:
        print("No contacts found.")

    cur.close()
    conn.close()


def show_contacts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts ORDER BY id")
    results = cur.fetchall()

    for contact in results:
        print(contact)

    if not results:
        print("PhoneBook is empty.")

    cur.close()
    conn.close()


def delete_contact():
    print("1. Delete by name")
    print("2. Delete by phone")

    choice = input("Choose deletion type: ")
    value = input("Enter value: ")

    conn = get_connection()
    cur = conn.cursor()

    try:
        if choice == "1":
            cur.execute(
                "DELETE FROM contacts WHERE first_name = %s",
                (value,)
            )
        elif choice == "2":
            cur.execute(
                "DELETE FROM contacts WHERE phone = %s",
                (value,)
            )
        else:
            print("Invalid choice.")
            return

        conn.commit()

        if cur.rowcount:
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    finally:
        cur.close()
        conn.close()


def main():
    create_table()

    while True:
        print("\n===== PHONEBOOK =====")
        print("1. Add contact")
        print("2. Import from CSV")
        print("3. Update contact")
        print("4. Search contacts")
        print("5. Delete contact")
        print("6. Show all contacts")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            insert_contact()
        elif choice == "2":
            import_csv()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            search_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            show_contacts()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()