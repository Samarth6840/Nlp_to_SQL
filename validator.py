# validator.py
import re

DANGEROUS = ["delete", "drop", "truncate", "alter", "update", "insert", "attach", "detach", "replace"]

def validate_query(sql_query):
    q = sql_query.strip().lower()

    if q == "not_sql":
        return False, "This is not a SQL query."

    if any(word in q for word in DANGEROUS):
        return False, "Dangerous keyword detected."

    if not q.startswith("select") and not q.startswith("with") and not q.startswith("pragma"):
        return False, "Only SELECT, WITH, or PRAGMA queries are allowed."

    return True, "Safe"