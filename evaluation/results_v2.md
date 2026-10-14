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

#### Run 1 (9.9s)
Welcome to this 1-bedroom, 1-bathroom condo in the heart of Denver, Colorado. Built in 2018, this modern residence boasts 650 square feet of living space. The condo is situated on a 0.05-acre lot, providing a compact and intimate living environment. With its sleek and contemporary design, this property offers a unique blend of urban convenience and peaceful retreat. As a condo, it is part of a larger community, offering a sense of community and shared amenities.

---

#### Run 2 (5.0s)
This 1-bedroom, 1-bathroom condo in Denver, CO, offers a compact living space with 650 square feet of above-grade living area. Built in 2018, the property boasts a small lot size of just 0.05 acres. With a total square footage of 650, this condo provides a cozy living space for a single individual or couple. The condo's compact size makes it an ideal choice for those looking for a hassle-free living experience.

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

#### Run 1 (11.0s)
This stunning luxury estate boasts an impressive 4200 square feet of above-grade living space, situated on a serene 1.25-acre lot in the heart of Atlanta. Built in 2015, this single-family residence features a gourmet chef kitchen with Quartz countertops, Sub-Zero refrigerator, and walk-in pantry, perfect for culinary enthusiasts. The interior is elevated with hardwood floors throughout, while the exterior offers a private cul-de-sac setting and pristine curb appeal. The home's smart home automation system provides seamless control, while the three-car attached garage and dual-zone HVAC systems ensure optimal comfort. The pièce de résistance is the expansive outdoor living area, featuring a heated salt-water pool, covered patio, and ample space for al fresco entertaining.

---

#### Run 2 (7.1s)
This stunning luxury estate boasts a spacious 4200 square feet of above-grade living space, nestled on a private 1.25-acre lot in the heart of Atlanta. Built in 2015, the single-family home features a gourmet chef kitchen with top-of-the-line appliances, including a Sub-Zero refrigerator, and Quartz countertops. The interior is elevated with hardwood floors throughout, while smart home automation provides seamless control over the property. The expansive open floor plan is perfect for high-end entertaining, and the outdoor spaces are just as impressive, with a heated salt-water pool, covered patio, and three-car attached garage.

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

#### Run 1 (8.6s)
This charming townhouse in Boston's heart offers a unique blend of comfort and space. With 3 spacious bedrooms and 2 full, 1 half bathrooms, this 1800 square foot home is perfect for those seeking a convenient and relaxing living experience. The finished basement entertainment room provides a cozy retreat for family gatherings, while the rooftop deck offers a serene escape with city views. The brick facade adds a touch of classic charm to this modern home, built in 2005. With 600 square feet of below-grade space, this property offers ample storage and potential for additional living areas.

---

#### Run 2 (6.5s)
This charming townhouse in Boston, MA, offers a unique blend of comfort and convenience. With 3 spacious bedrooms and 2 full bathrooms, plus a half bathroom, this 1800 square foot home provides ample living space for its residents. The finished basement entertainment room is a fantastic feature, perfect for hosting gatherings and events. The rooftop deck offers a serene escape with a brick facade that adds to the home's curb appeal. Built in 2005, this property boasts a total of 2400 square feet, with 600 square feet of below-grade space.

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

#### Run 1 (9.7s)
This charming single-family home, built in 1920, boasts a classic craftsman style that exudes timeless elegance. With 3 bedrooms and 2 bathrooms, including a full bathroom and a half bathroom, this property offers ample space for relaxation and everyday living. The home's original built-in cabinetry and Clawfoot tub are just a few of the nostalgic features that remain from its early 20th-century construction. A covered front porch provides a inviting entrance to the home, while a spacious 1950 square foot living area offers room to entertain. The property sits on a 0.15 acre lot, providing a private and peaceful setting.

---

#### Run 2 (7.8s)
This charming single-family home in Portland, OR, boasts a classic craftsman style that has been beautifully preserved. Built in 1920, the property retains its original architectural integrity, with many of its original features still intact, including the original built-in cabinetry and a Clawfoot tub. The home's 1950 square feet above grade provide a cozy living space, while the 400 square feet below grade add depth and character to the property. The home features a covered front porch, perfect for relaxing on warm days. With 3 bedrooms and 2 bathrooms, this home offers a comfortable living space for those looking for a piece of Portland's rich history.

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
This single-family home in Austin, TX, offers a spacious 2100 square feet of living space, featuring four bedrooms and two full bathrooms. Built in 1995, the property boasts a fenced backyard and attached garage, providing a private and convenient space for residents. With a lot size of 0.22 acres, this home provides ample space for outdoor activities and relaxation. Located in a highly sought-after neighborhood, this property is situated near top-rated schools, making it an attractive option for families with children.

---

#### Run 2 (7.3s)
This 4-bedroom, 2-bathroom single-family home is nestled in a quiet and safe neighborhood in Austin, TX, perfect for families with kids. Built in 1995, the property boasts 2100 square feet of above-grade living space. The home features a fenced backyard, ideal for outdoor entertaining and relaxation, and is paired with an attached garage for convenient storage. With a spacious lot size of 0.22 acres, this property offers ample space for outdoor activities or simply enjoying the fresh air. Located near top-rated schools, this home is a great option for those seeking a stable and family-friendly community.

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

#### Run 1 (8.6s)
Welcome to this charming single-family home in Columbus, Ohio, built in 1988. This 1650 square foot property boasts three spacious bedrooms and two full bathrooms, providing ample space for relaxation and entertainment. The home features a convenient two-car detached garage, perfect for parking multiple vehicles, and is equipped with modern amenities, including stainless steel appliances. Enjoy the comfort of central air conditioning, making this home a great choice for anyone looking for a comfortable living space. With its compact lot size of 0.18 acres, this property offers a private and peaceful atmosphere.

---

#### Run 2 (7.9s)
Welcome to this charming single-family home in Columbus, Ohio, built in 1988. With 1650 square feet of above-grade space, this property offers ample room for living and entertaining. The home features two full bathrooms and three spacious bedrooms, providing a comfortable retreat for its occupants. Additional features include a convenient two-car detached garage, perfect for parking multiple vehicles, and stainless steel appliances in the kitchen. The home also boasts central air conditioning for year-round comfort. Situated on a 0.18-acre lot, this property offers a private and peaceful living space, ideal for those seeking a low-maintenance lifestyle.

---

