from urllib.parse import unquote

INPUT_FILE = r"C:\Users\86182\Downloads\script.js"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    content = f.read()

decoded = unquote(content)

with open(INPUT_FILE, "w", encoding="utf-8") as f:
    f.write(decoded)