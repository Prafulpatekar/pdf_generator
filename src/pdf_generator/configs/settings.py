# Mongo settings.
UUID_REPRESENTATION = "standard"

POSTGRES_USER = "root"
POSTGRES_USER_PASSWORD = "root$123"
POSTGRES_HOST = "localhost"
POSTGRES_PORT = "5432"
DATABASE_NAME = "pdf_generator"
POSTGRES_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_USER_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{DATABASE_NAME}"

# EMAIL settings
AUTHOUR_EMAIL = "prafulpatekar.dev@gmail.com"
EMAIL_PASSWORD = "thhz kazn zfgl tmqx" # app password for gmail

# PDF settings
PDF_TEMPLATE_PATH = "sample_pdf.pdf"