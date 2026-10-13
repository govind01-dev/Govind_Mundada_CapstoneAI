import datetime

VALID_PROPERTY_TYPES = {"single-family", "condo", "townhouse", "land"}
def validate_choice(value: str, field_name: str, allowed: set) -> str:
    """Confirm value is one of a fixed set of allowed options."""
    if value not in allowed:
        raise ValueError(f"{field_name} must be one of: {', '.join(sorted(allowed))}")
    return value

# TODO: call this for property_type using VALID_PROPERTY_TYPES.
# TODO: decide if you want the check case-sensitive or not (hint: value.lower() in allowed).

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

# TODO: use this for bathrooms_half, bathrooms_three_quarter, square_feet_below_grade.

def validate_required_text(value, field_name: str) -> str:
    """Confirm a text field isn't missing or just whitespace. Returns the trimmed value."""
    if value is None:
        raise ValueError(f"{field_name} is required.")
    text = str(value).strip()  # remove leading/trailing whitespace
    if text == "":
        raise ValueError(f"{field_name} is required.")
    return text

# TODO: call this for house_number, street_name, city, and state in
# validate_property_input, e.g. validate_required_text(data.get("city"), "city")

def validate_zip_code(value, field_name: str = "zip_code") -> str:
    """Confirm a US zip code is present and either 5 digits or ZIP+4 (12345-6789)."""
    text = str(value).strip() if value is not None else ""
    if text == "":
        raise ValueError(f"{field_name} is required.")
    # TODO: decide how strict to be — the check below only confirms length/digits,
    # it doesn't verify the zip code actually exists.
    digits_only = text.replace("-", "")
    if not (len(digits_only) == 5 or len(digits_only) == 9) or not digits_only.isdigit():
        raise ValueError(f"{field_name} must be 5 digits, or 9 digits as ZIP+4.")
    return text

def validate_positive_int(value, field_name: str) -> int:
    """Convert value to int and confirm it's greater than zero."""
    try:
        number = int(value)  # may raise ValueError if not a valid integer
    except (ValueError, TypeError):
        raise ValueError(f"{field_name} must be a whole number.")
    if number <= 0:
        raise ValueError(f"{field_name} must be greater than zero.")
    return number

# TODO: call this for bedrooms and square_feet_above_grade:
#   validate_positive_int(data.get("bedrooms"), "bedrooms")

def validate_nonnegative_int(value, field_name: str) -> int:
    """Convert value to int and confirm it's zero or greater."""
    try:
        number = int(value)
    except (ValueError, TypeError):
        raise ValueError(f"{field_name} must be a whole number.")
    if number < 0:
        raise ValueError(f"{field_name} cannot be negative.")
    return number

# TODO: use this for bathrooms_full instead of validate_positive_int.

def validate_positive_float(value, field_name: str) -> float:
    """Convert value to float and confirm it's greater than zero."""
    try:
        number = float(value)  # accepts "0.25", "0.25" as float, ints too
    except (ValueError, TypeError):
        raise ValueError(f"{field_name} must be a number.")
    if number <= 0:
        raise ValueError(f"{field_name} must be greater than zero.")
    return number

# TODO: call this for lot_size_acres:
#   validate_positive_float(data.get("lot_size_acres"), "lot_size_acres")

def validate_year_built(value, field_name: str = "year_built") -> int:
    """Confirm the year is a whole number between 1800 and the current year."""
    try:
        year = int(value)
    except (ValueError, TypeError):
        raise ValueError(f"{field_name} must be a whole number.")
    current_year = datetime.date.today().year  # TODO: confirm this gives what you expect
    if year < 1800 or year > current_year:
        raise ValueError(f"{field_name} must be between 1800 and {current_year}.")
    return year

# ----------------------------------
# validate property inputs
def validate_property_input(data: dict) -> dict:
    """Validate every field in `data` and return a clean, validated dict.
    Raises ValueError on the first invalid field found.
    """
    validated = {}

   # TODO: validate house no., street name
    validated["house_number"] = validate_required_text(data.get("house_number"), "house_number")
    validated["street_name"] = validate_required_text(data.get("street_name"), "street_name")

    # TODO: unit_number is OPTIONAL — don't validate it, just pass it through.
    validated["unit_number"] = data.get("unit_number", "")
    # TODO: city, state — same pattern as house_number/street_name
    validated["city"] = validate_required_text(data.get("city"), "city")
    validated["state"] = validate_required_text(data.get("state"), "state")

    # TODO: zip_code — use validate_zip_code
    validated["zip_code"] = validate_zip_code(data.get("zip_code"), "zip_code")

    # --- Property type ---
    # TODO: call validate_choice(data.get("property_type"), "property_type", VALID_PROPERTY_TYPES)
    validated["property_type"] = validate_choice(data.get("property_type"), "property_type", VALID_PROPERTY_TYPES)

    # --- Bedrooms / bathrooms ---
    # TODO: bedrooms — validate_positive_int
    validated["bedrooms"] = validate_positive_int(data.get("bedrooms"), "bedrooms")

    # TODO: bathrooms_full — validate_nonnegative_int (remember: 0 is allowed here)
    validated["bathrooms_full"] = validate_nonnegative_int(data.get("bathrooms_full"), "bathrooms_full")

    # TODO: bathrooms_half, bathrooms_three_quarter — validate_optional_nonnegative_int
    validated["bathrooms_half"] = validate_optional_nonnegative_int(data.get("bathrooms_half"), "bathrooms_half")
    validated["bathrooms_three_quarter"] = validate_optional_nonnegative_int(data.get("bathrooms_three_quarter"), "bathrooms_three_quarter")

    # --- Square footage ---
    # TODO: square_feet_above_grade — validate_positive_int
    validated["square_feet_above_grade"] = validate_positive_int(data.get("square_feet_above_grade"), "square_feet_above_grade")
    # TODO: square_feet_below_grade — validate_optional_nonnegative_int
    validated["square_feet_below_grade"] = validate_optional_nonnegative_int(data.get("square_feet_below_grade"), "square_feet_below_grade")

    # --- Lot size / year ---
    # TODO: lot_size_acres — validate_positive_float
    validated["lot_size_acres"] = validate_positive_float(data.get("lot_size_acres"), "lot_size_acres")
    # TODO: year_built — validate_year_built
    validated["year_built"] = validate_year_built(data.get("year_built"), "year_built")

    # --- Optional extras ---
    # TODO: features — optional list; if missing, default to an empty list []
    validated["features"] = data.get("features", [])
    # TODO: notes — optional text; if missing, default to ""
    validated["notes"] = data.get("notes", "")

    return validated