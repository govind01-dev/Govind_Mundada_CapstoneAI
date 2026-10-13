# tests/test_validators.py
import datetime
import pytest
from generator.validators import validate_property_input

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

# TODO: test_invalid_property_type_raises
#   Use make_valid_input(property_type="mansion") and assert it raises ValueError.

def test_invalid_property_type_raises():
    """An invalid property type should raise a ValueError."""
    data = make_valid_input(property_type="mansion")
    with pytest.raises(ValueError):
        validate_property_input(data)

# TODO: test_negative_bedrooms_raises
#   Use make_valid_input(bedrooms=-1) and assert it raises ValueError.

def test_negative_bedrooms_raises():
    """A negative number of bedrooms should raise a ValueError."""
    data = make_valid_input(bedrooms=-1)
    with pytest.raises(ValueError):
        validate_property_input(data)

# TODO: test_optional_fields_default_correctly
#   Call make_valid_input() but DELETE bathrooms_half, square_feet_below_grade,
#   and features before validating (they're not in the base dict, so check they
#   default to 0, 0, and [] respectively in the result).

def test_optional_fields_default_correctly():
    """Missing optional fields should fall back to their correct default values."""
    result = validate_property_input(make_valid_input())
    assert result["bathrooms_half"] == 0
    assert result["square_feet_below_grade"] == 0
    assert result["features"] == []

# TODO: test_out_of_range_year_raises
#   Try both a too-old year (e.g. 1700) and a future year — pytest.raises(ValueError) for each.

def test_out_of_range_year_raises():
    """Years that are too far in the past or in the future should raise a ValueError."""
    with pytest.raises(ValueError):
        validate_property_input(make_valid_input(year_built=1700))

    # Future year (computed, so the test stays correct as time passes)
    next_year = datetime.date.today().year + 1
    with pytest.raises(ValueError):
        validate_property_input(make_valid_input(year_built=next_year))