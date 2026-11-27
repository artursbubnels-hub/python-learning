def analyze_text(text: str) -> tuple[int, int, str]:
    char_count = len(text)
    space_count = text.count(" ")
    uppercase_text = text.upper()
    return char_count, space_count, uppercase_text
chars, spaces, upper = analyze_text("Hello world!")
print(f"Characters: {chars}, Spaces: {spaces}, Uppercase: '{upper}'")