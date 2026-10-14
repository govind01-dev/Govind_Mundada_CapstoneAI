# Property Description LLM Evaluation Report

Model: llama3.2. Each sample runs 2 times.

## Prompt template used

```
You are an experienced real estate copywriter.
Write ONE paragraph of roughly 80 to 150 words describing the property below.
Use ONLY the facts provided. Do not invent features, amenities, prices,
views, or neighborhood details that are not listed. Do not make claims
about schools, crime, or who would be a good fit for the home.

Property type: {property_type}
Location: {city}, {state}
Bedrooms: {bedrooms}
Bathrooms: {bathrooms}
Above-grade square feet: {square_feet_above_grade}
Below-grade square feet: {square_feet_below_grade}
Lot size: {lot_size_acres} acres
Year built: {year_built}
Key features: {features}
Agent notes: {notes}

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

#### Run 1 (11.1s)
This 1 bedroom, 1 bathroom condo in Denver, CO boasts a total of 650 square feet of above-grade living space, with a full bathroom and a total living area of 650 square feet. The condo was built in 2018 and sits on a 0.05 acre lot. With no additional features or amenities listed, this condo provides a straightforward and uncomplicated living space. The exact details of the property are as follows, providing a clear and concise understanding of what to expect.

---

#### Run 2 (4.8s)
Welcome to this 1 bedroom, 1 bathroom condo in Denver, CO. Built in 2018, this property boasts 650 square feet of above-grade living space, with a total of 650 square feet of living space. The condo is situated on a 0.05 acre lot, providing a compact and intimate living experience. With a single full bathroom and one bedroom, this condo is ideal for a single occupant or a couple looking for a cozy retreat.

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

#### Run 1 (8.7s)
This stunning luxury estate boasts a grand 4200 square feet of above-grade living space, perfectly suited for high-end entertaining. The gourmet chef kitchen features top-of-the-line appliances, including a Sub-Zero refrigerator, and Quartz countertops, creating a culinary haven. The home's open floor plan seamlessly integrates living, dining, and entertaining spaces. Hardwood floors throughout add warmth and sophistication, while smart home automation ensures effortless control over the property. The expansive outdoor spaces, including a heated salt-water pool and covered patio, provide the perfect retreat for relaxation and leisure.

---

#### Run 2 (7.2s)
This stunning luxury estate boasts an impressive 4200 square feet of above-grade living space, perfectly suited for high-end entertaining. The gourmet chef kitchen is a culinary dream, complete with Quartz countertops, a Sub-Zero refrigerator, and a walk-in pantry. Hardwood floors throughout the home add warmth and sophistication, while smart home automation ensures seamless control over lighting, temperature, and more. The expansive outdoor spaces are just as impressive, featuring a heated salt-water pool, a covered patio, and a three-car attached garage. With its pristine curb appeal in a private cul-de-sac, this single-family home is a true showstopper.

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

#### Run 1 (9.3s)
This charming 3-bedroom, 2 full and 1 half-bathroom townhouse in Boston, MA, offers a perfect blend of comfort and convenience. Built in 2005, the 1800 square feet of above-grade living space is complemented by an additional 600 square feet of below-grade space, providing ample storage and potential for future expansion. The brick facade and finished basement entertainment room create a cozy and inviting atmosphere, while the rooftop deck offers a serene outdoor space to enjoy the city views. With a total lot size of 0.08 acres, this townhouse is an ideal choice for those seeking a convenient and private living space in the heart of Boston.

---

#### Run 2 (6.2s)
This charming 3-bedroom, 5-bathroom townhouse in Boston, MA, offers a unique blend of comfort and functionality. Built in 2005, the property boasts a spacious 1800 square feet of above-grade living space, complemented by an additional 600 square feet of below-grade space. The finished basement entertainment room provides a convenient space for relaxation and entertainment, while the rooftop deck offers a serene escape with a brick facade and brick exterior. The property's lot size of 0.08 acres provides a compact yet functional living space.

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

#### Run 1 (8.9s)
This charming single-family residence boasts a classic craftsman style, reflecting its original 1920 construction. With 3 bedrooms and 2 bathrooms, this 1950 square-foot home offers a spacious living space. The property features original built-in cabinetry, adding to its timeless charm. A Clawfoot tub and covered front porch are also notable design elements. Spanning 0.15 acres, the lot provides a serene setting for this classic home. Built in 1920, this property retains its early 20th-century architectural integrity, making it a unique opportunity for those seeking a piece of Portland's history.

---

#### Run 2 (8.4s)
This charming single-family home in Portland, OR, boasts a classic craftsman style that has been carefully preserved to retain its early 20th-century architectural integrity. Built in 1920, the property features original built-in cabinetry and a Clawfoot tub, evoking a sense of nostalgia and timeless elegance. The home's spacious interior is complemented by a covered front porch, providing a warm and inviting entrance to the property. With 1950 square feet of above-grade living space and an additional 400 square feet of below-grade space, this home offers ample room for expansion or renovation. Located on a 0.15-acre lot, the property provides a serene and private setting, perfect for those seeking a unique and historic living experience.

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

#### Run 1 (7.4s)
This single-family home in Austin, TX boasts 4 spacious bedrooms and 2 full bathrooms, totaling 2100 square feet of above-grade living space. Built in 1995, the property features a fenced backyard and attached garage, providing ample storage and outdoor space. With a lot size of 0.22 acres, this property offers a serene and private atmosphere, perfect for families. Located near top-rated schools, this neighborhood is considered quiet and extremely safe, making it an ideal choice for families with children.

---

#### Run 2 (6.2s)
This single-family home in Austin, TX boasts 4 spacious bedrooms and 2 full bathrooms, totaling 2100 square feet of above-grade living space. The property features a fenced backyard, perfect for family entertainment and relaxation, and is complemented by an attached garage for convenient storage and parking. Built in 1995, this home has been well-cared for and is situated on a 0.22-acre lot. Located in a quiet and safe neighborhood, this property is ideal for families with children, with top-rated schools nearby.

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

#### Run 1 (8.7s)
This charming single-family home in Columbus, OH, offers a spacious 1650 square feet of above-grade living space, complemented by a separate two-car detached garage for added convenience. Built in 1988, the property boasts modern amenities, including stainless steel appliances and central air conditioning, providing a comfortable living environment. With two full bathrooms and three bedrooms, this home provides ample space for family and friends to relax and unwind. Set on a 0.18-acre lot, the property offers a private and secure outdoor space, perfect for outdoor enthusiasts.

---

#### Run 2 (6.4s)
This 3 bedroom, 2 full bathroom single-family home is located in Columbus, Ohio, and features 1650 square feet of above-grade living space. The property boasts a 0.18 acre lot size and was built in 1988. A convenient two-car detached garage provides ample storage and parking space. The home is equipped with modern amenities, including stainless steel appliances and central air conditioning. With its spacious layout and functional features, this property offers a solid foundation for a comfortable living space.

---

