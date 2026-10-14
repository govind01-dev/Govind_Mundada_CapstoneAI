import re

MIN_WORDS = 15    # Minimum word threshold
MAX_WORDS = 140   # Maximum word threshold

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

# Banned phrases targeting Fair Housing compliance and low-value fluff terms
BANNED_PHRASES = [
    "ideal for", 
    "perfect for", 
    "luxurious", 
    "safe neighborhood", 
    "family-friendly", 
    "walking distance to schools"
]

def missing_required_terms(text: str, terms: list[str]) -> list[str]:
    """Return the terms (e.g. the city) that do NOT appear in the text.
    
    Performs case-insensitive checks.
    """
    if not text:
        return list(terms)
        
    text_lower = text.lower()
    missing = []
    
    for term in terms:
        if str(term).lower() not in text_lower:
            missing.append(term)
            
    return missing

def find_flagged_phrases(text: str, banned: list[str]) -> list[str]:
    """Return any banned phrases found in the text.
    
    Performs case-insensitive checks.
    """
    if not text:
        return []
        
    text_lower = text.lower()
    found = []
    
    for phrase in banned:
        if phrase.lower() in text_lower:
            found.append(phrase)
            
    return found
