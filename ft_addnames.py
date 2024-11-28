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

    # Function to update the full name display and append to CSV
    def add_name(e):
        full_name = f"{first_name.value} {middle_name.value} {surname.value}"
        full_name_display.value = full_name
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
    page.add(first_name, middle_name, surname, add_button, cancel_button, quit_button, full_name_display)

# Run the app
ft.app(target=main)
