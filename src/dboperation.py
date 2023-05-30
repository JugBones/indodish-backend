# import psycopg2
# from psycopg2 import Error

# try:
#     # Establish connection
#     connection = psycopg2.connect(
#         host="localhost",
#         port="5432",
#         database="your_database_name",
#         user="your_username",
#         password="your_password"
#     )

#     # Create cursor
#     cursor = connection.cursor()

# except (Exception, Error) as error:
#     print("Error while connecting to PostgreSQL:", error)

# # Querying data
# try:
#     # Fetch all restaurants
#     cursor.execute("SELECT * FROM restaurants")
#     restaurants = cursor.fetchall()
#     print("All restaurants:")
#     for restaurant in restaurants:
#         print(restaurant)

#     # Fetch restaurants by cuisine
#     cuisine = 'Italian'
#     cursor.execute("SELECT * FROM restaurants WHERE cuisine = %s", (cuisine,))
#     italian_restaurants = cursor.fetchall()
#     print("Italian restaurants:")
#     for restaurant in italian_restaurants:
#         print(restaurant)

# except (Exception, Error) as error:
#     print("Error retrieving data from PostgreSQL:", error)


# # Updating records
# try:
#     # Update restaurant details
#     restaurant_id = 1
#     updated_name = 'Updated Restaurant'
#     cursor.execute("UPDATE restaurants SET name = %s WHERE id = %s", (updated_name, restaurant_id))
#     connection.commit()
#     print("Restaurant updated successfully.")

# except (Exception, Error) as error:
#     print("Error updating data in PostgreSQL:", error)


# # Deleting records
# try:
#     # Delete a restaurant
#     restaurant_id = 1
#     cursor.execute("DELETE FROM restaurants WHERE id = %s", (restaurant_id,))
#     connection.commit()
#     print("Restaurant deleted successfully.")

# except (Exception, Error) as error:
#     print("Error deleting data from PostgreSQL:", error)

# # Close cursor and connection
# if connection:
#     cursor.close()
#     connection.close()
#     print("PostgreSQL connection closed.")
