# # Project # 2
# #   RESTAURANT TABLE & MENU BOOKING SYSTEM 

# # ------------ OOP CLASSES ----------------

# # Parent class: User
# class User:
#     def __init__(self, name):
#         self.name = name

# # Inherited classes
# class Customer(User):
#     def view_menu(self, menu):
#         print("\n🍽️ Menu Categories:")
#         for category, items in menu.items():
#             print(f"\n📂 {category}:")
#             for i, item in enumerate(items, start=1):
#                 print(f"{i}. {item['name']} - Rs.{item['price']}")

# class Staff(User):
#     def take_order(self, table, item):
#         table.add_order(item)

# class Manager(User):
#     def add_menu_item(self, menu, category, item):
#         if category in menu:
#             menu[category].append(item)

# # Table class with encapsulation
# class Table:
#     def __init__(self, table_id, capacity, booked=False):
#         self.table_id = table_id
#         self.capacity = capacity
#         self.__is_booked = booked
#         self.orders = []

#     def reserve_table(self):
#         if not self.__is_booked:
#             self.__is_booked = True
#             print(f"✅ Table {self.table_id} reserved successfully!")
#         else:
#             print(f"❌ Table {self.table_id} is already reserved.")

#     def is_booked(self):
#         return self.__is_booked

#     def add_order(self, item):
#         self.orders.append(item)
#         print(f"✅ {item['name']} added to Table {self.table_id}'s order.")

#     def calculate_bill(self):
#         return sum(item['price'] for item in self.orders)

# # Booking System class (Abstraction)
# class BookingSystem:
#     def __init__(self):
#         self.tables = [Table(i, 4, booked=(i <= 4)) for i in range(1, 11)]
#         self.menu = {
#             "Desi": [
#                 {"name": "Biryani", "price": 300},
#                 {"name": "Karahi", "price": 500}
#             ],
#             "Chinese": [
#                 {"name": "Chowmein", "price": 250},
#                 {"name": "Soup", "price": 200},
#                 {"name": "Fried Rice", "price": 280}
#             ],
#             "Continental": [
#                 {"name": "Pizza", "price": 800},
#                 {"name": "Pasta", "price": 700}
#             ],
#             "Bakery": [
#                 {"name": "Cake", "price": 1000},
#                 {"name": "Biscuits", "price": 150},
#                 {"name": "Samosa", "price": 50}
#             ]
#         }

#     def show_available_tables(self):
#         print("\n📋 Available Tables (1–10):")
#         for table in self.tables:
#             status = "Available" if not table.is_booked() else "Booked"
#             print(f"Table {table.table_id} - {status}")

#     def get_table(self, table_id):
#         for table in self.tables:
#             if table.table_id == table_id:
#                 return table
#         return None

# # ----------------------------

# def main():
#     print("📍 Welcome to Maria's Restaurant Booking System")

#     system = BookingSystem()
#     manager = Manager("Admin")
#     staff = Staff("Ali")

#     name = input("🧍 Enter your name: ")
#     customer = Customer(name)

#     while True:
#         print("\n🔸 Main Menu:\n1. View Available Tables\n2. Reserve Table\n3. View Menu & Order\n4. Generate Bill\n5. Exit")
#         choice = input("Choose option (1-5): ")

#         if choice == "1":
#             system.show_available_tables()

#         elif choice == "2":
#             try:
#                 table_id = int(input("🔢 Enter Table number to reserve (1–10): "))
#                 table = system.get_table(table_id)
#                 if table:
#                     if table.is_booked():
#                         print("⚠️ Table is already booked! Please choose from:")
#                         for t in system.tables:
#                             if not t.is_booked():
#                                 print(f"✅ Table {t.table_id} is available.")
#                     else:
#                         table.reserve_table()
#                 else:
#                     print("❌ Invalid table number.")
#             except ValueError:
#                 print("❌ Please enter a valid number.")

#         elif choice == "3":
#             customer.view_menu(system.menu)
#             cat = input("📂 Enter category (Desi/Chinese/Continental/Bakery): ")
#             if cat in system.menu:
#                 try:
#                     item_no = int(input("🔢 Enter item number to order: "))
#                     item = system.menu[cat][item_no - 1]

#                     table_id = int(input("📥 Enter your reserved Table number: "))
#                     table = system.get_table(table_id)

#                     if table and table.is_booked():
#                         staff.take_order(table, item)
#                     else:
#                         print("❌ Either table doesn't exist or it's not reserved yet.")
#                 except:
#                     print("❌ Invalid input.")
#             else:
#                 print("❌ Invalid category.")

#         elif choice == "4":
#             try:
#                 table_id = int(input("📥 Enter your Table number to generate bill: "))
#                 table = system.get_table(table_id)
#                 if table:
#                     total = table.calculate_bill()
#                     print(f"\n💵 Total Bill for Table {table_id}: Rs. {total}")
#                 else:
#                     print("❌ Table not found.")
#             except:
#                 print("❌ Invalid input.")

#         elif choice == "5":
#             print("👋 Thank you! Visit again.")
#             break

#         else:
#             print("❌ Invalid choice. Try again.")

# # ---------------- RUN APP ----------------
# if __name__ == "__main__":
#     main()
# #OOPS in my code hows working is as some basic points:
# #logic applied as,
# #Prevent double booking?
# # Table.__is_booked ensures one-time booking only.

# # Attach food to tables?
# # Table.add_order() holds food for each table.

# # Calculate total bill?
# # Table.calculate_bill() uses price sum from orders.
# # in my project pillers of oops used as:

# # |  Concept     | Applied                                         
# # | Inheritance  | Customer, Manager, Staff from base User                                                         
# # | Encapsulation | Table.__is_booked, with method control only                                                                 
# # | Abstraction   | BookingSystem hides menu & reservation logic                                                                
# # | Polymorphism| Different user types perform different actions (staff adds food, manager updates menu, customer places order) |







# app.py

import streamlit as st
from backend import BookingSystem, Customer, Staff
st.set_page_config(page_title="MK Eatry Food System", layout="wide")

st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #FFF8DC 50%, #FBC02D 50%);
        }

        .stButton>button {
            background-color: #B0BEC5;
            color: black;
            border-radius: 12px;
            padding: 8px 16px;
            font-weight: bold;
            border: 2px solid black;
        }

        .stButton>button:hover {
            background-color: #757575;
            color: white;
            border: 2px solid red;
        }
    </style>
""", unsafe_allow_html=True)

         

# --- Session Initialization ---
if 'system' not in st.session_state:
    st.session_state.system = BookingSystem()
    st.session_state.customer = Customer("Guest")
    st.session_state.staff = Staff("Ali")
    st.session_state.table_id = None
    st.session_state.ordered = False

st.title("🍽️ Maria's Restaurant Booking System")

# --- Step 1: Reserve a Table ---
st.header("🔢 Step 1: Reserve a Table")
available_tables = st.session_state.system.get_available_tables()
if available_tables:
    table_ids = [t.table_id for t in available_tables]
    selected_table = st.selectbox("Choose a Table", table_ids)

    if st.button("Reserve Table"):
        table = st.session_state.system.get_table(selected_table)
        if table.reserve_table():
            st.success(f"✅ Table {selected_table} reserved!")
            st.session_state.table_id = selected_table
        else:
            st.error("⚠️ Already reserved.")
else:
    st.warning("🚫 No tables available.")

# --- Step 2: Choose Food Category ---
st.header("📂 Step 2: Choose Food Category")
menu = st.session_state.system.menu

# category_images = {
#     "Desi": "https://i.imgur.com/z5N8XAi.png",         # Biryani
#     "Chinese": "https://i.imgur.com/hAlHnLk.png",      # Chinese dish
#     "Continental": "https://i.imgur.com/jnWhd0n.png"   # Pizza
#     # "Bakery": "https://i.imgur.com/yXELvQ5.png"      # ❌ Hidden — No image yet
# }
import os
from PIL import Image

category_images = {
    "Desi": Image.open("desi.png"),
    "Chinese": Image.open("chinese.png"),
    "Continental": Image.open("continental.png")
}


# Only show categories with images available
valid_categories = [c for c in menu.keys() if c in category_images]

selected_category = None
cols = st.columns(len(valid_categories))
for i, category in enumerate(valid_categories):
    with cols[i]:
        st.image(category_images[category], width=100)
        if st.button(f"{category} 🍽️"):
            selected_category = category
            st.session_state.selected_category = category

# --- Step 3: Show Items & Order ---
if 'selected_category' in st.session_state and st.session_state.table_id:
    st.header(f"📋 {st.session_state.selected_category} Items")
    items = menu[st.session_state.selected_category]

    for item in items:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{item['icon']} {item['name']}** — Rs. {item['price']}")
        with col2:
            if st.button(f"Add {item['name']}"):
                table = st.session_state.system.get_table(st.session_state.table_id)
                st.session_state.staff.take_order(table, item)
                st.success(f"{item['name']} added to Table {st.session_state.table_id}")
                st.session_state.ordered = True

# --- Step 4: Review Order and Bill ---
if st.session_state.ordered:
    st.header("🧾 Step 4: Review Your Order")
    table = st.session_state.system.get_table(st.session_state.table_id)

    if table.orders:
        for i, item in enumerate(table.orders):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"{item['icon']} {item['name']} - Rs. {item['price']}")
            with col2:
                if st.button(f"❌ Remove {item['name']}", key=f"remove_{i}"):
                    table.orders.pop(i)
                    st.warning(f"{item['name']} removed from order.")
                    st.rerun()

                    # st.experimental_rerun()


        total = table.calculate_bill()
        st.success(f"💰 **Total Bill**: Rs. {total}")
        st.info("⏳ Please wait 20–30 minutes for preparation.")
    else:
        st.info("🪹 No items in your order yet.")
















