"""Builds the LLM prompt from validated property data. No networking here."""


def format_bathrooms(data: dict) -> str:
    """Turn the three bathroom counts into one readable phrase, e.g. '2 full, 1 half'."""
    parts = []
    if data["bathrooms_full"] > 0:
        parts.append(f"{data['bathrooms_full']} full")
    if data["bathrooms_half"] > 0:
        parts.append(f"{data['bathrooms_half']} half")
    if data["bathrooms_three_quarter"] > 0:
        parts.append(f"{data['bathrooms_three_quarter']} three-quarter")
    if not parts:  # all counts were 0
        return "not specified"
    return ", ".join(parts)

def format_features(features: list) -> str:
    """Join a list of features into one string. (No fallback text: callers skip empty lists.)"""
    return ", ".join(features)

def build_optional_lines(data: dict) -> str:
    """Return prompt lines for fields that are only included when they have content."""
    lines = []
    if data["square_feet_below_grade"] > 0:
        lines.append(f"Below-grade square feet: {data['square_feet_below_grade']}")
    if data["features"]:                      # an empty list is falsy
        lines.append(f"Key features: {format_features(data['features'])}")
    notes = data["notes"].strip()
    if notes:                                 # empty or whitespace-only text is skipped
        lines.append(f"Agent notes: {notes}")
    return "\n".join(lines) + "\n" if lines else ""

PROMPT_TEMPLATE = """You are an experienced real estate copywriter.
Write ONE paragraph of at most 120 words. If few facts are provided, write
fewer sentences. A short description is fine. Do not add details to fill space.
Use ONLY the facts provided. Do not invent features, amenities, prices,
views, or neighborhood details that are not listed. Do not make claims
about schools, crime, or who would be a good fit for the home.

Property type: {property_type}
Location: {city}, {state}
Bedrooms: {bedrooms}
Bathrooms: {bathrooms}
Above-grade square feet: {square_feet_above_grade}
Lot size: {lot_size_acres} acres
Year built: {year_built}
{optional_lines}
Write the description now:
"""

def build_prompt(data: dict) -> str:
    """Fill PROMPT_TEMPLATE using validated property data."""
    notes = data["notes"].strip() or "None provided"
    return PROMPT_TEMPLATE.format(
        property_type=data["property_type"],
        city=data["city"],
        state=data["state"],
        bedrooms=data["bedrooms"],
        bathrooms=format_bathrooms(data),
        square_feet_above_grade=data["square_feet_above_grade"],
        lot_size_acres=data["lot_size_acres"],
        year_built=data["year_built"],
        optional_lines=build_optional_lines(data)
    )
