from fillpdf import fillpdfs
import os

# Path to your fillable PDF template


class PdfGenerator:
    folder = "public/filled_forms"
    
    def __init__(self, pdf_template_path):
        self.pdf_template_path = pdf_template_path
        self.form_fields = fillpdfs.get_form_fields(self.pdf_template_path)
        self.form_fields_keys = list(self.form_fields.keys())
        # Create the folder if it doesn't exist
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)


    @staticmethod
    def read_pdf_as_bytes(file_path: str) -> bytes:
        with open(file_path, 'rb') as file:
            return file.read()

    def fill_pdf(self, form_data):
        try:
            tmp_path = self.pdf_template_path
            form_keys = self.form_fields_keys
            data_dict = {
                form_keys[0]: form_data["name"], # Name
                form_keys[1]: form_data["month"], # Dropdown2
                form_keys[2]: form_data["date"], # Dropdown1
                form_keys[3]: form_data["year"], # Dropdown3
                form_keys[4]: form_data["address"], # Address
                form_keys[5]: form_data["reading"], # Checkbox1
                form_keys[6]: form_data["walking"], # Checkbox2
                form_keys[7]: form_data["music"], # Checkbox3
                form_keys[8]: form_data["other"], # Checkbox4
                form_keys[9]: form_data["other_check"], # Text5
                form_keys[10]: form_data["radio"], # group6
                form_keys[11]: form_data["other_radio"] # Text6
            }
            output_pdf_path = os.path.join( self.folder, f'filled_form_{form_data["id"]}.pdf')
            fillpdfs.write_fillable_pdf(
                input_pdf_path=tmp_path,
                output_pdf_path=output_pdf_path, 
                data_dict=data_dict,flatten=True)
            return output_pdf_path # Return the filename only
        except Exception as err:
            print(f"Error filling PDF: {err}")
            return False
        
if __name__ == "__main__":
    from pdf_generator.configs.settings import PDF_TEMPLATE_PATH
    fill_pdf = PdfGenerator(PDF_TEMPLATE_PATH)
    form_data = {
        "name": "John Doe",
        "month": "Jan",
        "date": "15",
        "year": "2022",
        "address": "123 Main St, Anytown, USA",
        "reading": "Yes",
        "walking": "Yes",
        "music": "Yes",
        "other_check": "Sports",
        "other": "Yes",
        "other_radio": "Sports",
        "radio": 3
    }
    fill_pdf.fill_pdf(form_data)
    