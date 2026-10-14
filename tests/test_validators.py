# tests/test_validators.py
import datetime
import pytest
from generator.validators import validate_property_input, MAX_FEATURE_LENGTH, MAX_NOTES_LENGTH, MAX_FEATURES

def make_valid_input(**overrides):
    """Returns a dict of valid property data, with any fields overridden for a specific test."""
    base = {
        "house_number": "123", "street_name": "Main St",
        "city": "Springfield", "state": "IL", "zip_code": "62704",
        "property_type": "condo", "bedrooms": 3, "bathrooms_full": 2,
        "square_feet_above_grade": 1800, "lot_size_acres": 0.25, "year_built": 1998,
    }
    base.update(overrides)
    return base

def test_valid_input_passes():
    """A fully valid property should validate without raising."""
    result = validate_property_input(make_valid_input())
    assert result["city"] == "Springfield"
    assert result["bedrooms"] == 3

def test_missing_required_field_raises():
    """Leaving out a required field (city) should raise ValueError."""
    data = make_valid_input()
    del data["city"]
    with pytest.raises(ValueError):
        validate_property_input(data)

def test_invalid_property_type_raises():
    """An invalid property type should raise a ValueError."""
    data = make_valid_input(property_type="mansion")
    with pytest.raises(ValueError):
        validate_property_input(data)

def test_negative_bedrooms_raises():
    """A negative number of bedrooms should raise a ValueError."""
    data = make_valid_input(bedrooms=-1)
    with pytest.raises(ValueError):
        validate_property_input(data)

def test_optional_fields_default_correctly():
    """Missing optional fields should fall back to their correct default values."""
    result = validate_property_input(make_valid_input())
    assert result["bathrooms_half"] == 0
    assert result["square_feet_below_grade"] == 0
    assert result["features"] == []

def test_out_of_range_year_raises():
    """Years that are too far in the past or in the future should raise a ValueError."""
    with pytest.raises(ValueError):
        validate_property_input(make_valid_input(year_built=1700))

    # Future year (computed, so the test stays correct as time passes)
    next_year = datetime.date.today().year + 1
    with pytest.raises(ValueError):
        validate_property_input(make_valid_input(year_built=next_year))

def test_state_is_uppercased():
    result = validate_property_input(make_valid_input(state="il"))
    assert result["state"] == "IL"          # lowercase in, uppercase out

def test_state_wrong_length_raises():
    with pytest.raises(ValueError):
        validate_property_input(make_valid_input(state="Illinois"))

def test_feature_at_length_limit_passes():
    result = validate_property_input(make_valid_input(features=["x" * MAX_FEATURE_LENGTH]))
    assert len(result["features"][0]) == MAX_FEATURE_LENGTH

def test_feature_over_length_limit_raises():
    """A single feature longer than the limit should raise a ValueError."""
    too_long = "x" * (MAX_FEATURE_LENGTH + 1)   # one character over the limit
    with pytest.raises(ValueError):
        validate_property_input(make_valid_input(features=[too_long]))

def test_notes_at_length_limit_passes():
    result = validate_property_input(make_valid_input(notes="x" * MAX_NOTES_LENGTH))
    assert len(result["notes"]) == MAX_NOTES_LENGTH

def test_notes_over_length_limit_raises():
    too_long = "x" * (MAX_NOTES_LENGTH + 1)   # one character over the limit
    with pytest.raises(ValueError):
        validate_property_input(make_valid_input(notes=too_long))

def test_features_not_a_list_raises():
    with pytest.raises(ValueError):
        validate_property_input(make_valid_input(features="fireplace"))  # a string, not a list

def test_features_at_count_limit_passes():
    result = validate_property_input(make_valid_input(features=["deck"] * MAX_FEATURES))
    assert len(result["features"]) == MAX_FEATURES

def test_features_over_count_limit_raises():
    too_many = ["deck"] * (MAX_FEATURES + 1)
    with pytest.raises(ValueError):
        validate_property_input(make_valid_input(features=too_many))  

def test_land_is_not_supported_in_mvp():
    """Land listings are out of scope: they have no bedrooms, square footage, or build year."""
    with pytest.raises(ValueError):
        validate_property_input(make_valid_input(property_type="land"))
        
              