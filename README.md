# PDF Generator FastAPI

## Backend implementation.
- Frameworks: FastAPI
- Database: Postgres or sqlite

1. In above design there are 5 components
  - pdf_generator package (entrypoint)
  - Routers (For routing API Endpoints)
  - Cruds (Controller): This will have all buisness logic
  - Database (Postgres)
2. Every request will first come to pdf_generator app the it will redirect by router to matching endpoint then router will call the associated crud function, inside all the buisness logics and database query will be performed then an appropriate response will be send to client.
3. PdfGenerator Class will fill the form and return the output path


## Steps to run APP
- Python Version Required 3.9
- Open terminal in working directory fastapi enter below commands
    1. `docker-compose -f docker-compose.yml up --build -d`
- Access Postgress on localhost 5432 port.

## Run Without docker and postgres
- Python Version Required 3.9
- Open terminal in working directory fastapi enter below commands
    1. `python -m venv venv`
    2. For mac or linux `source venv/bin/activate` for windows `.\venv\Scripts\activate`
    2. `pip install -r requirements.txt`
    3. `pip install -e .`
    4. `uvicorn pdf_generator.app:app --host 0.0.0.0 --port 8080 --reload`

## How to use API
- After running app Visit `/docs` or `redocs` endpoint to check the API documentation

#### Sample PDFs are kept in pulic folder



