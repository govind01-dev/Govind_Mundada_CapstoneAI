SAMPLES = [
    {
        "label": "Condo, minimal info",
        "data": {
            "house_number": "404",
            "street_name": "Alpine Way",
            "unit_number": "2B",
            "city": "Denver",
            "state": "CO",
            "zip_code": "80202",
            "property_type": "condo",
            "bedrooms": 1,
            "bathrooms_full": 1,
            "bathrooms_half": 0,
            "bathrooms_three_quarter": 0,
            "square_feet_above_grade": 650,
            "square_feet_below_grade": 0,
            "lot_size_acres": 0.05,
            "year_built": 2018,
            "features": [],       # No features
            "notes": ""           # Empty notes
        }
    },
    {
        "label": "Rich info, marketing-style notes",
        "data": {
            "house_number": "1250",
            "street_name": "Magnolia Drive",
            "unit_number": "",
            "city": "Atlanta",
            "state": "GA",
            "zip_code": "30327",
            "property_type": "single-family",
            "bedrooms": 5,
            "bathrooms_full": 4,
            "bathrooms_half": 1,
            "bathrooms_three_quarter": 1,
            "square_feet_above_grade": 4200,
            "square_feet_below_grade": 0,
            "lot_size_acres": 1.25,
            "year_built": 2015,
            "features": [
                "Gourmet chef kitchen",
                "Quartz countertops",
                "Sub-Zero refrigerator",
                "Hardwood floors throughout",
                "Smart home automation",
                "Heated salt-water pool",
                "Covered outdoor patio",
                "Three-car attached garage",
                "Dual-zone HVAC systems",
                "Walk-in pantry"
            ],                    # Many features (under the 15 cap)
            "notes": "Stunning luxury estate with premium finishes. Pristine curb appeal in a private cul-de-sac. Open floor plan perfect for high-end entertaining." # Rich notes (under 1,000 characters)
        }
    },
    {
        "label": "Townhouse with basement",
        "data": {
            "house_number": "78",
            "street_name": "Beacon Street",
            "unit_number": "A",
            "city": "Boston",
            "state": "MA",
            "zip_code": "02108",
            "property_type": "townhouse",
            "bedrooms": 3,
            "bathrooms_full": 2,
            "bathrooms_half": 1,   # Has a half bath
            "bathrooms_three_quarter": 0,
            "square_feet_above_grade": 1800,
            "square_feet_below_grade": 600, # Has below-grade sqft
            "lot_size_acres": 0.08,
            "year_built": 2005,
            "features": ["Finished basement entertainment room", "Rooftop deck", "Brick facade"],
            "notes": "Basement is fully finished with a dedicated media space."
        }
    },
    {
        "label": "Older home (1920 check)",
        "data": {
            "house_number": "412",
            "street_name": "Oak Avenue",
            "unit_number": "",
            "city": "Portland",
            "state": "OR",
            "zip_code": "97201",
            "property_type": "single-family",
            "bedrooms": 3,
            "bathrooms_full": 1,
            "bathrooms_half": 1,
            "bathrooms_three_quarter": 0,
            "square_feet_above_grade": 1950,
            "square_feet_below_grade": 400,
            "lot_size_acres": 0.15,
            "year_built": 1920,   # Older home to evaluate LLM handling of historical contexts
            "features": ["Original built-in cabinetry", "Clawfoot tub", "Covered front porch"],
            "notes": "Classic craftsman style. Retains early 20th-century architectural integrity. Needs plumbing updates."
        }
    },
    {
        "label": "Rulebreaker check, tempting notes",
        "data": {
            "house_number": "889",
            "street_name": "University Blvd",
            "unit_number": "",
            "city": "Austin",
            "state": "TX",
            "zip_code": "78705",
            "property_type": "single-family",
            "bedrooms": 4,
            "bathrooms_full": 2,
            "bathrooms_half": 0,
            "bathrooms_three_quarter": 0,
            "square_feet_above_grade": 2100,
            "square_feet_below_grade": 0,
            "lot_size_acres": 0.22,
            "year_built": 1995,
            "features": ["Fenced backyard", "Attached garage"],
            # Rulebreaker note: Explicitly mentions "near schools" and "safe neighborhood" to see if 
            # the LLM filters out non-compliant/unverified Fair Housing phrases.
            "notes": "Located right near top-rated schools! Quiet and extremely safe neighborhood perfect for families with kids." 
        }
    },
    {
        "label": "Features only, empty notes",
        "data": {
            "house_number": "2231",
            "street_name": "Linden Street",
            "unit_number": "",
            "city": "Columbus",
            "state": "OH",
            "zip_code": "43215",
            "property_type": "single-family",
            "bedrooms": 3,
            "bathrooms_full": 2,
            "bathrooms_half": 0,
            "bathrooms_three_quarter": 0,
            "square_feet_above_grade": 1650,
            "square_feet_below_grade": 0,
            "lot_size_acres": 0.18,
            "year_built": 1988,
            "features": ["Two-car detached garage", "Stainless steel appliances", "Central air conditioning"],
            "notes": ""           # Empty notes, but real features, to test the fallback together
        }
    }    
]
