import logging

logger = logging.getLogger(__name__)   # a named channel for this file's log messages

import datetime
import streamlit as st
from main import generate_description          
from generator.llm_client import LLMError
from generator.validators import VALID_PROPERTY_TYPES
from generator.output_checks import check_description_length

st.set_page_config(page_title="Realistify")
st.title("Realistify: AI Real Estate Description Generator")
st.caption("All generated descriptions are initial drafts and must be thoroughly reviewed and edited by the agent before use.")

with st.form("property_form"):
    # Address and Location inputs
    house_number = st.text_input("House number") 
    street_name = st.text_input("Street name")
    unit_number = st.text_input("Unit number (optional)")
    city = st.text_input("City")
    state = st.text_input("State")
    zip_code = st.text_input("ZIP code")

    # Property type, Bedrooms, and Bathrooms inputs
    property_type = st.selectbox("Property type", sorted(VALID_PROPERTY_TYPES))
    bedrooms = st.number_input("Bedrooms", min_value=0, step=1)
    bathrooms_full = st.number_input("Full bathrooms", min_value=0, step=1)
    bathrooms_half = st.number_input("Half bathrooms", min_value=0, step=1)
    bathrooms_three_quarter = st.number_input("3/4 bathrooms", min_value=0, step=1)
    
    # Square footage inputs
    square_feet_above_grade = st.number_input("Square feet (above grade)", min_value=0, step=1)
    square_feet_below_grade = st.number_input("Square feet (below grade)", min_value=0, step=1)
    
    # Lot size and Year built (dynamic max year based on current system time)
    lot_size_acres = st.number_input("Lot size (acres)", min_value=0.0, step=0.01)
    current_year = datetime.datetime.now().year
    year_built = st.number_input("Year built", min_value=1800, max_value=current_year, step=1, value=None)
    features_text = st.text_area("Key features (one per line)")
    notes = st.text_area("Agent notes (optional)")

    submitted = st.form_submit_button("Generate description")
if submitted:
    # Split text area lines into a list, discarding empty lines
    features_list = [line.strip() for line in features_text.split("\n") if line.strip()]
    
    # Build raw_data dict aligning exactly with validation keys
    raw_data = {
        "house_number": house_number,
        "street_name": street_name,
        "unit_number": unit_number,
        "city": city,
        "state": state,
        "zip_code": zip_code,
        "property_type": property_type,
        "bedrooms": bedrooms,
        "bathrooms_full": bathrooms_full,
        "bathrooms_half": bathrooms_half,
        "bathrooms_three_quarter": bathrooms_three_quarter,
        "square_feet_above_grade": square_feet_above_grade,
        "square_feet_below_grade": square_feet_below_grade,
        "lot_size_acres": lot_size_acres,
        "year_built": year_built,
        "features": features_list,
        "notes": notes
    }
    
    try:
        with st.spinner("Generating..."):
            description = generate_description(raw_data)
    except ValueError as e:
        # Display localized input validation errors
        st.error(f"Input validation failed. Please check your data: {e}")
    except LLMError as e:
        # Catch generation errors gracefully
        st.error(f"An error occurred with the generation service: {e}")
    except Exception:
        logger.exception("Unexpected error while generating a description")
        st.error("Something went wrong on our end. Please try again later.")
    else:
        st.success("Description generated successfully!")
        warning = check_description_length(description)
        if warning:                      # an empty/None result is falsy, so this skips quietly
            st.warning(warning)
        st.text_area("Generated description (editable)", value=description, height=220)