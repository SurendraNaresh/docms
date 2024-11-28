import flet as ft

def main(page: ft.Page):
    # Create text fields for name, middle name, and surname
    first_name = ft.TextField(label="First Name")
    middle_name = ft.TextField(label="Middle Name")
    surname = ft.TextField(label="Surname")

    # Create a text field to display the full name
    full_name_display = ft.TextField(label="Full Name", read_only=True)

    # Function to update the full name display
    def update_full_name(e):
        full_name = f"{first_name.value} {middle_name.value} {surname.value}"
        full_name_display.value = full_name
        page.update()

    # Create an OK button
    ok_button = ft.ElevatedButton(text="OK", on_click=update_full_name)

    # Add the text fields and button to the page
    page.add(first_name, middle_name, surname, ok_button, full_name_display)

# Run the app
ft.app(target=main)
