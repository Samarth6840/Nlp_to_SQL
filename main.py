# main.py
from database import load_file_to_db, run_query, get_schema_info, get_column_names, get_preview
from llm import ask_llm
from validator import validate_query

def detect_mode(question):
    q = question.lower()

    sql_help_keywords = [
        "sql", "query", "join", "group by", "order by", "having",
        "explain", "what is", "difference between", "write a query",
        "help me with code", "fix this query", "coding"
    ]

    if any(k in q for k in sql_help_keywords):
        return "help"

    return "sql"

def main():
    filepath = input("Enter path to your CSV or Excel file: ")

    print("Loading file...")
    df = load_file_to_db(filepath)
    schema = get_schema_info(df)
    print(f"File loaded! Found {df.shape[0]} rows and {df.shape[1]} columns.")

    while True:
        question = input("\nAsk a question (or type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        q = question.lower().strip()

        if "column name" in q or "all columns" in q:
            print("\nColumns:")
            print(", ".join(get_column_names(df)))
            continue

        if "first 5 rows" in q or "preview" in q or "sample data" in q:
            print("\nPreview:")
            print(get_preview(df).to_string(index=False))
            continue

        mode = detect_mode(question)

        if mode == "help":
            print("Thinking...")
            answer = ask_llm(question, schema, mode="help")
            print("\nAnswer:")
            print(answer)
            continue

        print("Thinking...")
        sql_query = ask_llm(question, schema, mode="sql")
        print(f"Generated SQL: {sql_query}")

        is_safe, message = validate_query(sql_query)
        if not is_safe:
            print(f"Blocked: {message}")
            continue

        try:
            results = run_query(sql_query)
            print("\nResults:")
            print(results.to_string(index=False))
        except Exception as e:
            print(f"SQL error: {e}")

if __name__ == "__main__":
    main()