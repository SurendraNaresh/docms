import flet as ft
import csv
import os

def main(page: ft.Page):
    # Create text fields for name, middle name, and surname
    first_name = ft.TextField(label="First Name")
    middle_name = ft.TextField(label="Middle Name")
    surname = ft.TextField(label="Surname")

    # Create a text field to display the full name
    full_name_display = ft.TextField(label="Full Name", read_only=True)

    # CSV file path
    csv_file = "names.csv"

    # Function to check if the record already exists
    def record_exists(first, middle, last):
        if os.path.exists(csv_file):
            with open(csv_file, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row == [first, middle, last]:
                        return True
        return False

    # Function to update the full name display and append to CSV
    def add_name(e):
        full_name = f"{first_name.value} {middle_name.value} {surname.value}"
        full_name_display.value = full_name
        # Check if the record already exists
        if record_exists(first_name.value, middle_name.value, surname.value):
            page.dialog(ft.AlertDialog(title="Record already exists"))
        else:
            # Append to CSV file
            with open(csv_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([first_name.value, middle_name.value, surname.value])
        page.update()

    # Function to reset the fields
    def reset_fields(e):
        first_name.value = ""
        middle_name.value = ""
        surname.value = ""
        full_name_display.value = ""
        page.update()

    # Function to quit the app
    def quit_app(e):
        page.window_close()

    # Create buttons
    add_button = ft.ElevatedButton(text="Add/Submit", on_click=add_name)
    cancel_button = ft.ElevatedButton(text="Cancel", on_click=reset_fields)
    quit_button = ft.ElevatedButton(text="Quit", on_click=quit_app)

    # Add the text fields and buttons to the page
    page.add(first_name, middle_name, surname, 
             ft.Row([add_button, cancel_button, quit_button], height=30), 
             full_name_display)

# Run the app with target = web and port = 5444
ft.app(target=main, port=5444)
