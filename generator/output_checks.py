MIN_WORDS = 50    # Minimum word threshold
MAX_WORDS = 175   # Maximum word threshold

def check_description_length(text: str) -> str | None:
    """Return a warning message if the word count looks off, otherwise None."""
    # split() with no argument handles any whitespace group, newlines, and trailing spaces safely
    word_count = len(text.split())
    expected = f"The expected range is {MIN_WORDS} to {MAX_WORDS} words."   
    
    # Check if the description falls below the minimum word count
    if word_count < MIN_WORDS:
        return f"The generated description is too short ({word_count} words). {expected}"
        
    # Check if the description exceeds the maximum word count
    if word_count > MAX_WORDS:
        return f"The generated description is too long ({word_count} words). {expected}"
        
    return None   # None means "looks fine"
