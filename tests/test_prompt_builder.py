from generator.prompt_builder import build_prompt, format_bathrooms, format_features
from generator.validators import validate_property_input

def make_validated(**overrides):
    base = {
        "house_number": "123", "street_name": "Main St",
        "city": "Springfield", "state": "IL", "zip_code": "62704",
        "property_type": "condo", "bedrooms": 3, "bathrooms_full": 2,
        "square_feet_above_grade": 1800, "lot_size_acres": 0.25, "year_built": 1998,
    }
    base.update(overrides)
    return validate_property_input(base)

def test_prompt_contains_key_facts():
    prompt = build_prompt(make_validated())
    assert "Springfield" in prompt
    assert "Bedrooms: 3" in prompt

def test_street_address_not_in_prompt():
    assert "Main St" not in build_prompt(make_validated())

def test_empty_optional_fields_are_omitted():
    prompt = build_prompt(make_validated())
    assert "Key features" not in prompt
    assert "Agent notes" not in prompt
    assert "Below-grade" not in prompt
    assert "None provided" not in prompt

def test_optional_fields_appear_when_provided():
    prompt = build_prompt(make_validated(features=["fireplace"], notes="corner lot", square_feet_below_grade=500))
    assert "Key features: fireplace" in prompt
    assert "Agent notes: corner lot" in prompt
    assert "Below-grade square feet: 500" in prompt

def test_whitespace_only_notes_are_omitted():
    prompt = build_prompt(make_validated(notes="   "))
    assert "Agent notes" not in prompt

def test_features_are_joined():
    prompt = build_prompt(make_validated(features=["fireplace", "deck"]))
    assert "fireplace, deck" in prompt

def test_bathroom_formatting():
    data = make_validated(bathrooms_full=0, bathrooms_half=1)
    assert format_bathrooms(data) == "1 half"
    data = make_validated(bathrooms_full=2, bathrooms_half=1)
    assert format_bathrooms(data) == "2 full, 1 half"
    assert format_features(["a", "b"]) == "a, b"
