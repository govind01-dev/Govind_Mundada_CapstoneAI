import datetime

VALID_PROPERTY_TYPES = {"single-family", "condo", "townhouse", "land"}
MAX_NOTES_LENGTH = 1000
MAX_FEATURES = 15
MAX_FEATURE_LENGTH = 100

def validate_choice(value: str, field_name: str, allowed: set) -> str:
    """Confirm value is one of a fixed set of allowed options."""
    if value not in allowed:
        raise ValueError(f"{field_name} must be one of: {', '.join(sorted(allowed))}")
    return value

def validate_required_text(value, field_name: str) -> str:
    """Confirm a text field isn't missing or just whitespace. Returns the trimmed value."""
    if value is None:
        raise ValueError(f"{field_name} is required.")
    text = str(value).strip()  # remove leading/trailing whitespace
    if text == "":
        raise ValueError(f"{field_name} is required.")
    return text

def validate_state(value, field_name: str = "state") -> str:
    """Confirm state consists of exactly two letters and return it in uppercase."""
    text = validate_required_text(value, field_name).upper()
    if len(text) != 2 or not text.isalpha():
        raise ValueError(f"{field_name} must be exactly two letters.")
    return text

def validate_zip_code(value, field_name: str = "zip_code") -> str:
    """Confirm a US zip code is present and either 5 digits or ZIP+4 (12345-6789)."""
    text = str(value).strip() if value is not None else ""
    if text == "":
        raise ValueError(f"{field_name} is required.")

    digits_only = text.replace("-", "")
    if not (len(digits_only) == 5 or len(digits_only) == 9) or not digits_only.isdigit():
        raise ValueError(f"{field_name} must be 5 digits, or 9 digits as ZIP+4.")
    return text

def validate_year_built(value, field_name: str = "year_built") -> int:
    """Confirm the year is a whole number between 1800 and the current year."""
    try:
        year = int(value)
    except (ValueError, TypeError):
        raise ValueError(f"{field_name} must be a whole number.")
    current_year = datetime.date.today().year  
    if year < 1800 or year > current_year:
        raise ValueError(f"{field_name} must be between 1800 and {current_year}.")
    return year

def validate_notes(value, field_name: str = "notes") -> str:
    """Ensure optional notes text does not exceed 1,000 characters."""
    if value is None:
        return ""
    text = str(value).strip()
    if len(text) > MAX_NOTES_LENGTH:
        raise ValueError(f"{field_name} exceeds the {MAX_NOTES_LENGTH} character limit (current length: {len(text)}).")
    return text

def validate_features(value, field_name: str = "features") -> list:
    """Ensure features is a list of non-empty strings capped at 15 items."""
    if value is None:
        return []
    if not isinstance(value, list):
        raise ValueError(f"{field_name} must be a list.")
    if len(value) > MAX_FEATURES:
        raise ValueError(f"{field_name} cannot exceed {MAX_FEATURES} items.")
    
    clean_features = []
    for item in value:
        if not isinstance(item, str) or not item.strip():
            raise ValueError(f"Every item in {field_name} must be a non-empty string.")
        cleaned = item.strip()  # strip once, so the length check ignores stray spaces
        if len(cleaned) > MAX_FEATURE_LENGTH:
            raise ValueError(
                f"Each item in {field_name} must be at most {MAX_FEATURE_LENGTH} characters "
                f"(this one is {len(cleaned)}: '{cleaned[:20]}...')."
            )
        clean_features.append(cleaned)
    return clean_features

def validate_optional_nonnegative_int(value, field_name: str, default: int = 0) -> int:
    """Return default if value is missing; otherwise validate it's >= 0."""
    if value is None or value == "":
        return default
    try:
        number = int(value)
    except (ValueError, TypeError):
        raise ValueError(f"{field_name} must be a whole number.")
    if number < 0:
        raise ValueError(f"{field_name} cannot be negative.")
    return number

def validate_positive_int(value, field_name: str) -> int:
    """Convert value to int and confirm it's greater than zero."""
    try:
        number = int(value)  # may raise ValueError if not a valid integer
    except (ValueError, TypeError):
        raise ValueError(f"{field_name} must be a whole number.")
    if number <= 0:
        raise ValueError(f"{field_name} must be greater than zero.")
    return number

def validate_nonnegative_int(value, field_name: str) -> int:
    """Convert value to int and confirm it's zero or greater."""
    try:
        number = int(value)
    except (ValueError, TypeError):
        raise ValueError(f"{field_name} must be a whole number.")
    if number < 0:
        raise ValueError(f"{field_name} cannot be negative.")
    return number

def validate_positive_float(value, field_name: str) -> float:
    """Convert value to float and confirm it's greater than zero."""
    try:
        number = float(value)  # accepts "0.25", "0.25" as float, ints too
    except (ValueError, TypeError):
        raise ValueError(f"{field_name} must be a number.")
    if number <= 0:
        raise ValueError(f"{field_name} must be greater than zero.")
    return number

# ----------------------------------
# validate property inputs
def validate_property_input(data: dict) -> dict:
    """Validate every field in `data` and return a clean, validated dict.
    Raises ValueError on the first invalid field found.
    """
    validated = {}

    validated["house_number"] = validate_required_text(data.get("house_number"), "house_number")
    validated["street_name"] = validate_required_text(data.get("street_name"), "street_name")
    validated["unit_number"] = data.get("unit_number", "")
    validated["city"] = validate_required_text(data.get("city"), "city")
    validated["state"] = validate_state(data.get("state"), "state")
    validated["zip_code"] = validate_zip_code(data.get("zip_code"), "zip_code")

    # --- Property type ---
    validated["property_type"] = validate_choice(data.get("property_type"), "property_type", VALID_PROPERTY_TYPES)

    # --- Bedrooms / bathrooms ---
    validated["bedrooms"] = validate_positive_int(data.get("bedrooms"), "bedrooms")
    validated["bathrooms_full"] = validate_nonnegative_int(data.get("bathrooms_full"), "bathrooms_full")
    validated["bathrooms_half"] = validate_optional_nonnegative_int(data.get("bathrooms_half"), "bathrooms_half")
    validated["bathrooms_three_quarter"] = validate_optional_nonnegative_int(data.get("bathrooms_three_quarter"), "bathrooms_three_quarter")

    # --- Square footage ---
    validated["square_feet_above_grade"] = validate_positive_int(data.get("square_feet_above_grade"), "square_feet_above_grade")
    validated["square_feet_below_grade"] = validate_optional_nonnegative_int(data.get("square_feet_below_grade"), "square_feet_below_grade")

    # --- Lot size / year ---
    validated["lot_size_acres"] = validate_positive_float(data.get("lot_size_acres"), "lot_size_acres")
    validated["year_built"] = validate_year_built(data.get("year_built"), "year_built")

    # --- Optional extras ---
    validated["features"] = validate_features(data.get("features"), "features")
    validated["notes"] = validate_notes(data.get("notes"), "notes")

    return validated