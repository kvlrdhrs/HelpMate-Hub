# import psycopg2

# conn = psycopg2.connect(
#     host = 'localhost',
#     port = '5432',
#     user = 'postgres',
#     password = '232323',
#     dbname = 'restaurant_mm'
# )

# cur=conn.cursor()
# conn.autocommit=True

# class MenuItem():
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def save(self):
#         cur.execute("""INSERT INTO menu_items (item_name, item_price) values(%s, %s);""", (self.name, self.price))

#     def delete (self):
#         cur.execute("""DELETE FROM menu_items WHERE item_name = %s and item_price = %s""", (self.name, self.price))

#     def update(self, new_name, new_price):
#         self.name = new_name
#         self.price = new_price
#         cur.execute("""UPDATE menu_items SET item_name = %s, item_price = %s WHERE item_name = %s""", (self.name, self.price, self.name))

# def show_user_menu():
#     print("Choose an option:")
#     print("V - View an Item")
#     print("A - Add an Item")
#     print("D - Delete an Item")
#     print("U - Update an Item")
#     print("S - Show the Menu")
#     choice = input("Enter your choice: ")
#     return choice.upper()

# def add_item_to_menu():
#     name = input("Enter the item's name: ")
#     price = float(input("Enter the item's price: "))
#     item = MenuItem(name, price)
#     item.save()
#     print("Item was added successfully.")

# def remove_item_from_menu():
#     name = input("Enter the name of the item to remove: ")
#     item = MenuItem(name, 0)  # price doesn't matter for deletion
#     item.delete()
#     print("Item was deleted successfully.")

# def update_item_from_menu():
#     name = input("Enter the name of the item to update: ")
#     new_name = input("Enter the new name for the item: ")
#     new_price = float(input("Enter the new price for the item: "))
#     item = MenuItem(name, 0)  # price doesn't matter for updating
#     item.update(new_name, new_price)
#     print("Item was updated successfully.")

# def show_restaurant_menu():
#     cur.execute("""SELECT * FROM menu_items""")
#     items = cur.fetchall()
#     for item in items:
#         print(f"Name: {item[0]}, Price: {item[1]}")

# def main():
#     while True:
#         user_choice = show_user_menu()
#         if user_choice == 'V':
#             name = input("Enter the name of the item to view: ")
#             cur.execute("""SELECT * FROM menu_items WHERE item_name = %s""", (name,))
#             item = cur.fetchone()
#             if item:
#                 print(f"Name: {item[0]}, Price: {item[1]}")
#             else:
#                 print("Item not found.")
#         elif user_choice == 'A':
#             add_item_to_menu()
#         elif user_choice == 'D':
#             remove_item_from_menu()
#         elif user_choice == 'U':
#             update_item_from_menu()
#         elif user_choice == 'S':
#             show_restaurant_menu()
#         else:
#             print("Invalid choice. Please try again.")

#         continue_program = input("Do you want to continue? (Y/N): ")
#         if continue_program.upper() != 'Y':
#             break

#     cur.close()
#     conn.close()

# if __name__ == "__main__":
#     main()