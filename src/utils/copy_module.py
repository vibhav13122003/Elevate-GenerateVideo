import pyperclip

def copy_to_clipboard(text):
    """Copies the given text to the system clipboard."""
    try:
        pyperclip.copy(text)
        return "Text copied to clipboard successfully."
    except Exception as e:
        return f"Error: Unable to copy text to clipboard. {e}"
