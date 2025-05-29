from summarizer import summarize_text

def load_text(file_path: str) -> str:

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"[Error] File not found: {file_path}")
        return ""

if __name__ == "__main__":
    input_file = "input.txt"
    text = load_text(input_file)

    if text:
        summary = summarize_text(text)

        # Display the result
        print("\n------- Summary -------\n")
        print(summary)
    else:
        print("[Aborted] No text to summarize.")