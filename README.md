# NLP to SQL Terminal App

A terminal-based application that converts natural language questions into SQL queries and runs them on tabular data loaded from CSV or Excel files.  
Users can interact with the database using simple English instead of writing SQL manually.

## Features

- Load data from CSV or Excel files
- Automatically detect database schema
- Convert natural language questions into SQL using an LLM
- Validate SQL queries before execution
- Run safe queries on the loaded database
- Display query results directly in the terminal

## How It Works

1. The user provides a CSV or Excel file path.
2. The file is loaded into a database.
3. The schema information is extracted.
4. The user enters a natural language question.
5. The LLM converts the question into an SQL query.
6. The query is checked by a validator for safety.
7. If valid, the query is executed and the result is shown in the terminal.

## Project Structure

- `database.py`  
  Handles file loading, schema extraction, and query execution.

- `llm.py`  
  Sends natural language input to the LLM and returns generated SQL.

- `validator.py`  
  Checks whether the generated SQL query is safe to run.

- `main.py`  
  Main terminal application that connects all components.

## Usage

Run the application from the terminal:

```bash
python main.py
