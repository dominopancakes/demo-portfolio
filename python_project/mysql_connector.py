#first type "python3 -m pip install mysql-connector-python" into terminal
#NOT python3 -m pip install mysql-connector

import mysql.connector

def retrieve_and_display_products():
    # Database connection details
    config = {
        'user': 'admin',  # Replace with your database username
        'password': 'admin',  # Replace with your database password
        'host': '192.168.1.138',  # Replace with your database host
        'database': 'my_shop',  # Replace with your database name
    }

    try:
        # Connect to the database
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # SQL query to retrieve products
        query = "SELECT * FROM employees"
        cursor.execute(query)

        # Fetch all rows from the executed query
        products = cursor.fetchall()

        # Display the products
        if products:
            print("Products in the database:")
            for product in products:
                print(product)  # Print each product (tuple)
        else:
            print("No products found in the database.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Database connection closed.")

# Call the function
retrieve_and_display_products()