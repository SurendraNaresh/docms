import flet as ft
import requests

def main(page: ft.Page):
    doc_name = ft.TextField(label="Document Name", width=300)
    section_id = ft.TextField(label="Section ID", width=300)
    figure_desc = ft.TextField(label="Figure Description", width=300)
    table_id = ft.TextField(label="Table ID", width=300)
    color_scheme = ft.TextField(label="Color Scheme (e.g., R,G,B)", width=300)

    def generate_word_doc(e):
        data = {
            "doc_name": doc_name.value,
            "section_id": section_id.value,
            "figure_desc": figure_desc.value,
            "table_id": table_id.value,
            "color_scheme": color_scheme.value,
        }
        response = requests.post("http://127.0.0.1:5001/generate-doc", json=data)
        if response.status_code == 200:
            with open("output.docx", "wb") as f:
                f.write(response.content)
            page.snack_bar = ft.SnackBar(ft.Text("Document generated successfully!"))
            page.snack_bar.open = True

    page.add(
        ft.Column(
            [
                ft.Text("Generate Word Document", size=20, weight="bold"),
                doc_name,
                section_id,
                figure_desc,
                table_id,
                color_scheme,
                ft.ElevatedButton("Generate Document", on_click=generate_word_doc),
            ]
        )
    )

ft.app(target=main)
