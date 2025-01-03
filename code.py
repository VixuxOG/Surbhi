import mysql.connector as sql

# Database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'railwaydata'
}

try:
    conn = sql.connect(**db_config)
    if conn.is_connected():
        print('Successfully connected to the database.')
        c1 = conn.cursor()
        while True:
            print("\nRAILWAY RESERVATION MANAGEMENT")
            print("###############################\n")
            print("1. Add new Passenger Detail")
            print("2. Add new Train Detail")
            print("3. Add new PNR Record")
            print("4. Reservation of Ticket")
            print("5. Exit")

            try:
                ch = int(input("Enter your choice: "))

                if ch == 1:
                   print("\nPassenger Details Form")
                   name = input("Enter your full name: ")
                   age = int(input("Enter your age: "))
                   gender = input("Enter your gender: ")
                   total = int(input("Enter total number of people: "))
                   date = input("Enter your date (yyyy-mm-dd): ")

                   query = "INSERT INTO passenger (name, age, gender, total, date) VALUES (%s, %s, %s, %s, %s)"
                   values = (name, age, gender, total, date)

                   c1.execute(query, values)
                   conn.commit()
                   print("Passenger details added successfully.")
                elif ch == 2:
                    print("\nTrain Details Form")
                    train_name = input("Enter train name: ")
                    boogie_type = input("Enter boogie type: ")

                    query = "INSERT INTO train (train_name, boogie_type) VALUES (%s, %s)"
                    values = (train_name, boogie_type)

                    c1.execute(query, values)
                    conn.commit()
                    print("Train details added successfully.")

                elif ch == 3:
                    print("\nAdd PNR Record")
                    pnr_no = input("Enter pnr_no: ")
                    passenger_id = input("Enter passenger_id: ")
                    train_id = input("Enter train_id: ")
                    available_seats = int(input("Enter number of seats available: "))

                    query = "INSERT INTO reservation (pnr_no, passenger_id, train_id, available_seats) VALUES (%s, %s, %s, %s)"
                    values = (pnr_no, passenger_id, train_id, available_seats)

                    c1.execute(query, values)
                    conn.commit()
                    print("PNR number added successfully.")

                elif ch == 4:
                    print("\nReservation of Ticket")
                    passenger_id = int(input("Enter your Passenger ID: "))
                    train_id = int(input("Enter Train id: "))
                    seats = int(input("Enter number of seats: "))

                    # Get the current available seats
                    query = "SELECT available_seats FROM reservation WHERE train_id = %s"
                    c1.execute(query, (train_id,))
                    result = c1.fetchone()

                    if result:
                        available_seats = result[0]
                        if seats <= available_seats:
                          status = "Confirmed"
                          available_seats = available_seats - seats

                          # Update the available seats
                          query = "UPDATE reservation SET available_seats = %s WHERE train_id = %s"
                          c1.execute(query, (available_seats, train_id))
                          conn.commit()
                          print("Ticket reservation status:", status)

                        else:
                            status = "Waiting List"
                            print("Ticket reservation status:", status)

                    else:
                        print("Train ID not found or no seats available.")


                elif ch == 5:
                    print("You have exited")
                    print("Visit again soon")
                    break
                else:
                   print("Invalid choice, please try again.")

            except ValueError:
                print("Invalid input. Please enter an integer for the menu choice.")
            except Exception as e:
                  print("An error occurred: ",e)
            finally:
              c1.close()
    else:
        print("Connection failed.")
except sql.Error as err:
    print(f"Error connecting to the database: {err}")

finally:
    if conn and conn.is_connected():
        conn.close()
        print("Database connection closed.")