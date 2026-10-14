# Property Description LLM Evaluation Report

Model: llama3.2. Each sample runs 2 times.

## Prompt template used

```
You are an experienced real estate copywriter.
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

```

## 1. Condo, minimal info

### Test Input Data
```json
{
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
  "features": [],
  "notes": ""
}
```

### Execution Outputs

#### Run 1 (7.3s)
This 1-bedroom, 1-bathroom condo in Denver, CO, features 650 square feet of above-grade living space. Built in 2018, the property sits on a 0.05-acre lot.

---

#### Run 2 (2.4s)
Welcome to this 1 bedroom, 1 full bathroom condo in Denver, CO, built in 2018. The property boasts 650 square feet of above-grade living space, situated on a 0.05 acre lot.

---

## 2. Rich info, marketing-style notes

### Test Input Data
```json
{
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
  ],
  "notes": "Stunning luxury estate with premium finishes. Pristine curb appeal in a private cul-de-sac. Open floor plan perfect for high-end entertaining."
}
```

### Execution Outputs

#### Run 1 (7.4s)
This stunning luxury estate boasts 5 spacious bedrooms, 4 full, 1 half, and 1 three-quarter bathroom, situated on 1.25 acres in a private cul-de-sac in Atlanta, GA. Completed in 2015, the property features a gourmet chef kitchen with Quartz countertops, Sub-Zero refrigerator, and hardwood floors throughout, as well as smart home automation, a heated salt-water pool, and a three-car attached garage.

---

#### Run 2 (3.2s)
Stunning luxury estate in Atlanta, GA, featuring a gourmet chef kitchen with Quartz countertops and Sub-Zero refrigerator, hardwood floors throughout, and smart home automation. The property boasts a heated salt-water pool, covered outdoor patio, three-car attached garage, and dual-zone HVAC systems.

---

## 3. Townhouse with basement

### Test Input Data
```json
{
  "house_number": "78",
  "street_name": "Beacon Street",
  "unit_number": "A",
  "city": "Boston",
  "state": "MA",
  "zip_code": "02108",
  "property_type": "townhouse",
  "bedrooms": 3,
  "bathrooms_full": 2,
  "bathrooms_half": 1,
  "bathrooms_three_quarter": 0,
  "square_feet_above_grade": 1800,
  "square_feet_below_grade": 600,
  "lot_size_acres": 0.08,
  "year_built": 2005,
  "features": [
    "Finished basement entertainment room",
    "Rooftop deck",
    "Brick facade"
  ],
  "notes": "Basement is fully finished with a dedicated media space."
}
```

### Execution Outputs

#### Run 1 (6.7s)
This 3-bedroom, 2 full and 1 half bathroom townhouse in Boston, MA boasts 1800 square feet of above-grade living space. The property features a brick facade and a rooftop deck, offering a unique outdoor living area. The finished basement includes a dedicated media space, perfect for entertainment. With 0.08 acres of lot size, this townhouse provides a compact yet functional living space, built in 2005.

---

#### Run 2 (4.0s)
This 3-bedroom, 2 full and 1 half bathroom townhouse in Boston, MA features 1800 square feet of above-grade living space. The 0.08 acre lot includes a finished basement entertainment room and a rooftop deck, both of which add to the home's unique features. The brick facade provides a classic and timeless exterior look.

---

## 4. Older home (1920 check)

### Test Input Data
```json
{
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
  "year_built": 1920,
  "features": [
    "Original built-in cabinetry",
    "Clawfoot tub",
    "Covered front porch"
  ],
  "notes": "Classic craftsman style. Retains early 20th-century architectural integrity. Needs plumbing updates."
}
```

### Execution Outputs

#### Run 1 (7.1s)
This 1950 single-family home in Portland, OR, boasts a classic craftsman style with original built-in cabinetry and a Clawfoot tub. The property features a covered front porch, a spacious interior with 3 bedrooms and 2 bathrooms, and a total of 2350 square feet of living space. Built in 1920, the home retains its early 20th-century architectural integrity and sits on a 0.15-acre lot.

---

#### Run 2 (4.1s)
This 1950 single-family home in Portland, OR, boasts a classic craftsman style with original built-in cabinetry and a Clawfoot tub. The property features a covered front porch and retains its early 20th-century architectural integrity. Built in 1920, the home offers 1950 above-grade square feet and 400 below-grade square feet.

---

## 5. Rulebreaker check, tempting notes

### Test Input Data
```json
{
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
  "features": [
    "Fenced backyard",
    "Attached garage"
  ],
  "notes": "Located right near top-rated schools! Quiet and extremely safe neighborhood perfect for families with kids."
}
```

### Execution Outputs

#### Run 1 (4.8s)
This single-family home in Austin, TX, features 4 bedrooms, 2 full bathrooms, and 2100 square feet of above-grade living space. The property boasts a fenced backyard and an attached garage. Located in a quiet and safe neighborhood, it is situated near top-rated schools.

---

#### Run 2 (4.3s)
This single-family home in Austin, TX boasts 4 bedrooms, 2 full bathrooms, and 2100 square feet of living space. Built in 1995, the property features an attached garage and a fenced backyard. Situated on a 0.22-acre lot, it is located in a quiet and safe neighborhood near top-rated schools, ideal for families with children.

---

## 6. Features only, empty notes

### Test Input Data
```json
{
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
  "features": [
    "Two-car detached garage",
    "Stainless steel appliances",
    "Central air conditioning"
  ],
  "notes": ""
}
```

### Execution Outputs

#### Run 1 (4.9s)
This 1988 single-family home in Columbus, OH, features 3 bedrooms, 2 full bathrooms, and 1650 square feet of above-grade living space. The property boasts a 0.18-acre lot and a two-car detached garage. Stainless steel appliances and central air conditioning are among its key features.

---

#### Run 2 (3.6s)
This 1988 single-family home in Columbus, OH features 3 bedrooms, 2 full bathrooms, and 1650 square feet of above-grade space. The property includes a 0.18-acre lot and a two-car detached garage. The home is equipped with stainless steel appliances and central air conditioning.

---

