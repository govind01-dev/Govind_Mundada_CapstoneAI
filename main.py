from generator.validators import validate_property_input
from generator.prompt_builder import build_prompt
from generator.llm_client import generate_text, LLMError
from generator.output_checks import (
     check_description_length,
     find_flagged_phrases,
     missing_required_terms,
     BANNED_PHRASES)
     
# SAMPLE_PROPERTY dictionary with every required and optional field populated
SAMPLE_PROPERTY = {
    "house_number": "123",
    "street_name": "Main Street",
    "city": "Springfield",
    "state": "IL",
    "zip_code": "62704",
    "bedrooms": 3,
    "property_type": "townhouse",
    "year_built": 2015,
    "bathrooms_full": 2,
    "bathrooms_half": 1,
    "bathrooms_three_quarter": 0,
    "square_feet_above_grade": 1800,
    "square_feet_below_grade": 500,
    "lot_size_acres": 0.25,
    "features": ["hardwood floors", "stainless steel appliances", "granite countertops"],
    "notes": "Beautiful suburban home with a spacious backyard, close to local parks and excellent schools."
}

def generate_description(raw_data: dict) -> str:
    """Run the full pipeline and return the generated description."""
    # step 1: Validate input (may raise ValueError)
    validated = validate_property_input(raw_data)  
    
    # step 2: build the prompt from `validated`
    prompt = build_prompt(validated)
    
    # step 3: send the prompt to the model
    text = generate_text(prompt)
    
    # step 4: Run post-generation safety metrics and audits
    compliance_report = []

    length_warning = check_description_length(text)
    if length_warning:
        compliance_report.append(length_warning)
        
    flagged = find_flagged_phrases(text, BANNED_PHRASES)
    if flagged:
        compliance_report.append(
            f"⚠️ COMPLIANCE WARNING: Detected restricted real estate phrases: {', '.join(flagged)}. "
            "Please remove neighborhood safety descriptions or school references."
        )
        
    required_location_terms = [validated["city"]]
    missing_terms = missing_required_terms(text, required_location_terms)
    if missing_terms:
        compliance_report.append(
            f"ℹ️ Missing Data Warning: The generated draft omitted required location variables: {', '.join(missing_terms)}."
        )
        
    # step 5: Prepend audit notifications to output text if anomalies were found
    if compliance_report:
        audit_header = "### 🚨 PIPELINE AUDIT REPORT\n" + "\n".join([f"- {w}" for w in compliance_report]) + "\n\n---\n\n"
        return audit_header + text
        
    # return the text
    return text

def main():
    try:
        description = generate_description(SAMPLE_PROPERTY)
        print(description)
    except ValueError as e:
        # Prints a clear message indicating a problem with the input data format
        print(f"Input validation error: The data provided is invalid. Details: {e}")
    except LLMError as e:
        # Prints a clear message indicating a problem interacting with the LLM/Ollama server
        print(f"Model generation error: The LLM encountered an issue. Details: {e}")

if __name__ == "__main__":  # runs main() only when you run this file directly
    main()
