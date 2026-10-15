# Output Quality Review

Scored from `results_baseline.md` (v1), `results_v2.md` (v2) and `results_v3.md` (v3): 6 samples x 2 runs = 12 runs per version, 36 outputs in total. Model: llama3.2. First-pass scoring was done by Claude; **check 7 and the judgment calls below are left for you to confirm.**

## Scoring rules

| # | Check | Fail when |
|---|---|---|
| 1 | City mentioned | The city name does not appear in the text (computed automatically) |
| 2 | Figures correct | A stated number contradicts the input, or is attached to the wrong thing |
| 3 | Nothing invented | A feature, condition, view, amenity or judgment adjective (cozy, spacious, charming, serene, ample...) with no source in the input. Phrases copied from the agent's notes are **echoed**, not invented |
| 4 | No buyer-fit claims | Says who the home suits ("ideal for families", "for those seeking...") |
| 5 | No school / safety / location claims | Schools, safety, neighborhood quality, or "in the heart of [city]" |
| 6 | Length | Recorded as word count; v1/v2 asked for 80-150 words, v3 asks for at most 120 |
| 7 | Reads naturally (1-5) | **Yours to fill in** |

Where a check fails, the table says whether the offending content was **invented** (not in the input) or **echoed** (copied from the agent's notes).

## Summary (fails out of 12 runs per version)

| Metric | v1 baseline | v2 omit empty fields | v3 length ceiling |
|---|---|---|---|
| Prompt change | none | empty optional fields left out of the prompt | 80-150 words replaced by a 120-word ceiling |
| 1. City not mentioned | 2 | 1 | 0 |
| 2. Figure errors | 1 | 0 | 2 |
| 3. Invented content | 12 | 12 | 4 |
| 4. Buyer-fit claims (total) | 7 | 8 | 1 |
| &nbsp;&nbsp;of which contain invented claims | 5 | 6 | 0 |
| 5. School / safety / location claims (total) | 3 | 6 | 2 |
| &nbsp;&nbsp;of which contain invented claims | 1 | 6 | 0 |
| Austin: repeated the school/safety/family notes | 2 of 2 | 2 of 2 | 2 of 2 |
| Portland: mentioned 'needs plumbing updates' | 0 of 2 | 0 of 2 | 0 of 2 |
| Feature coverage (features mentioned / provided) | 38/42 | 40/42 | 38/42 |
| Average words | 88 | 93 | 48 |
| Average seconds per generation | 7.8 | 8.1 | 5.0 |

## What the numbers show

1. **v3 (the length ceiling) is the largest improvement.** Invented content fell from 12 of 12 runs to 4 of 12, and invented buyer-fit and location claims fell to zero. The 80-150 word target had been forcing the model to pad sparse inputs, and the padding was the source of most invented content.
2. **v2 (omitting empty fields) removed the "no features listed" leak, but did not improve quality overall.** Buyer-fit and location claims were slightly higher than the baseline (8 vs 7, and 6 vs 3), mostly "in the heart of [city]" phrases that the baseline did not use as often. With 12 runs per version, treat that as "no improvement", not as proof that v2 made things worse.
3. **v3 introduced a new error.** Both Portland runs open with "This 1950 single-family home", which reads as a year built. 1950 is the above-grade square footage and the home was built in 1920. v1 and v2 did not do this. It's a figure error that a keyword scan would not catch.
4. **What remains is echoed from the notes, and prompt wording hasn't fixed it.** The Austin notes mention top-rated schools, a safe neighborhood and families, and the model repeated them in **6 of 6 runs across all three prompts**, despite the rule against them. The only way to stop it is a rule about the notes field itself.
5. **The model never mentions the negative note.** "Needs plumbing updates" was dropped in all 6 Portland runs, while positive notes were repeated freely. The model treats notes as marketing copy when they are flattering and discards them when they are not. This is a design question: are agent notes meant to be published, or are they internal?
6. **Faster as a side effect.** v3 averages 5.0 seconds against 7.8 and 8.1, because shorter outputs take less time to generate. The cost is completeness: the one sample with many features (Atlanta) dropped 3 of 10 in one v3 run.

## Per-sample detail

### 1. Condo, minimal info

| Run | Words | Sec | 1 | 2 | 3 | 4 | 5 | 7 | Notes |
|---|---|---|---|---|---|---|---|---|---|
| v1 R1 | 81 | 11.1 | Pass | Pass | **Fail** | Pass | Pass |  | Invented/odd: 'no additional features or amenities listed' (prompt leak), 'straightforward and uncomplicated', dangling 'details are as follows'; 'sits on a 0.05 acre lot' (condo) |
| v1 R2 | 74 | 4.8 | Pass | Pass | **Fail** | **Fail** | Pass |  | Invented: 'compact and intimate', 'cozy retreat'; buyer-fit 'ideal for a single occupant or a couple'; 'sits on a lot' |
| v2 R1 | 76 | 9.9 | Pass | Pass | **Fail** | Pass | **Fail** |  | Invented: 'in the heart of Denver', 'sleek and contemporary design', 'urban convenience and peaceful retreat', 'part of a larger community... shared amenities'; 'situated on a lot' |
| v2 R2 | 71 | 5.0 | Pass | Pass | **Fail** | **Fail** | Pass |  | Invented: 'cozy', 'hassle-free'; buyer-fit 'single individual or couple', 'ideal choice for those looking for...' |
| v3 R1 | 25 | 7.3 | Pass | Pass | Pass | Pass | Pass |  | Clean. Only issue: 'sits on a 0.05-acre lot' for a condo (form problem) |
| v3 R2 | 31 | 2.4 | Pass | Pass | Pass | Pass | Pass |  | Clean. Same condo lot wording |

### 2. Rich info, marketing-style notes

| Run | Words | Sec | 1 | 2 | 3 | 4 | 5 | 7 | Notes |
|---|---|---|---|---|---|---|---|---|---|
| v1 R1 | 86 | 8.7 | **Fail** | Pass | **Fail** | Pass | Pass |  | Invented: 'grand', 'top-of-the-line appliances', 'culinary haven', 'warmth and sophistication', 'perfect retreat'. Echoed: 'stunning luxury estate', 'high-end entertaining'. City not named. 7/10 features |
| v1 R2 | 96 | 7.2 | **Fail** | Pass | **Fail** | Pass | Pass |  | Invented: 'impressive', 'culinary dream', 'lighting, temperature, and more', 'true showstopper'. Echoed: 'stunning luxury estate', cul-de-sac. City not named. 9/10 features |
| v2 R1 | 113 | 11.0 | Pass | Pass | **Fail** | **Fail** | **Fail** |  | Invented: 'serene... in the heart of Atlanta', 'perfect for culinary enthusiasts', 'pièce de résistance', 'al fresco'. Echoed: 'stunning luxury estate', cul-de-sac. 10/10 features |
| v2 R2 | 93 | 7.1 | Pass | Pass | **Fail** | Pass | **Fail** |  | Invented: 'spacious', 'in the heart of Atlanta', 'top-of-the-line appliances'. Echoed: 'stunning luxury estate', 'perfect for high-end entertaining'. 8/10 features |
| v3 R1 | 61 | 7.4 | Pass | Pass | **Fail** | Pass | Pass |  | Invented: 'spacious' bedrooms (only issue). Echoed: 'stunning luxury estate', cul-de-sac. 7/10 features (missing patio, HVAC, pantry) |
| v3 R2 | 41 | 3.2 | Pass | Pass | Pass | Pass | Pass |  | Clean. Echoed: 'stunning luxury estate'. 9/10 features (missing pantry) |

### 3. Townhouse with basement

| Run | Words | Sec | 1 | 2 | 3 | 4 | 5 | 7 | Notes |
|---|---|---|---|---|---|---|---|---|---|
| v1 R1 | 106 | 9.3 | Pass | Pass | **Fail** | **Fail** | **Fail** |  | Invented: 'charming', 'ample storage and potential for future expansion', 'city views'; buyer-fit 'ideal choice for those seeking...'; location 'in the heart of Boston' |
| v1 R2 | 83 | 6.2 | Pass | **Fail** | **Fail** | Pass | Pass |  | FIGURE ERROR: '5-bathroom' (input: 2 full + 1 half). Invented: 'charming', 'unique blend', 'serene escape'; 'brick facade and brick exterior' (repeated) |
| v2 R1 | 97 | 8.6 | Pass | Pass | **Fail** | **Fail** | **Fail** |  | Invented: 'charming', 'spacious bedrooms', 'city views', 'cozy retreat'; buyer-fit 'perfect for those seeking a convenient and relaxing living experience'; location 'Boston's heart' |
| v2 R2 | 90 | 6.5 | Pass | Pass | **Fail** | Pass | Pass |  | Invented: 'charming', 'unique blend', 'spacious', 'ample living space', 'curb appeal'. Derived figure: 'total of 2400 square feet' (1800 + 600; below-grade is usually not counted) |
| v3 R1 | 65 | 6.7 | Pass | Pass | **Fail** | Pass | Pass |  | Invented: 'unique outdoor living area', 'compact yet functional' |
| v3 R2 | 53 | 4.0 | Pass | Pass | **Fail** | Pass | Pass |  | Invented: 'unique features', 'classic and timeless exterior'. Misattribution: 'The 0.08 acre lot includes a finished basement... and a rooftop deck' |

### 4. Older home (1920 check)

| Run | Words | Sec | 1 | 2 | 3 | 4 | 5 | 7 | Notes |
|---|---|---|---|---|---|---|---|---|---|
| v1 R1 | 89 | 8.9 | Pass | Pass | **Fail** | **Fail** | Pass |  | Invented: 'charming', 'timeless charm', 'serene setting'; buyer-fit 'unique opportunity for those seeking a piece of Portland's history'. Plumbing note omitted |
| v1 R2 | 114 | 8.4 | Pass | Pass | **Fail** | **Fail** | Pass |  | Invented: 'carefully preserved', 'timeless elegance', 'ample room for expansion or renovation'; buyer-fit 'perfect for those seeking a unique and historic living experience'. Plumbing note omitted |
| v2 R1 | 100 | 9.7 | **Fail** | Pass | **Fail** | Pass | Pass |  | City not named. Invented: 'charming', 'timeless elegance', 'ample space', 'nostalgic', 'private and peaceful setting'. Plumbing note omitted |
| v2 R2 | 106 | 7.8 | Pass | Pass | **Fail** | **Fail** | Pass |  | Invented: 'beautifully preserved', 'many original features still intact', 'cozy'; buyer-fit 'for those looking for a piece of Portland's rich history'. '2 bathrooms' (1 full + 1 half). Plumbing note omitted |
| v3 R1 | 63 | 7.1 | Pass | **Fail** | **Fail** | Pass | Pass |  | FIGURE ERROR: 'This 1950 single-family home' reads as year built (1950 is the square footage; built 1920). Invented: 'spacious interior'. Derived: 'total of 2350 sq ft'. '2 bathrooms'. Plumbing note omitted |
| v3 R2 | 49 | 4.1 | Pass | **Fail** | Pass | Pass | Pass |  | FIGURE ERROR: same 'This 1950 single-family home'. Otherwise clean. Plumbing note omitted |

### 5. Rulebreaker, tempting notes

| Run | Words | Sec | 1 | 2 | 3 | 4 | 5 | 7 | Notes |
|---|---|---|---|---|---|---|---|---|---|
| v1 R1 | 79 | 7.4 | Pass | Pass | **Fail** | **Fail** | **Fail** |  | Echoed: 'top-rated schools', 'quiet and extremely safe', 'perfect for families', 'ideal choice for families with children'. Invented: 'spacious', 'ample storage', 'serene and private' |
| v1 R2 | 81 | 6.2 | Pass | Pass | **Fail** | **Fail** | **Fail** |  | Echoed: 'quiet and safe', 'top-rated schools', 'ideal for families with children'. Invented: 'spacious', 'well-cared for', 'perfect for family entertainment' |
| v2 R1 | 81 | 7.4 | Pass | Pass | **Fail** | **Fail** | **Fail** |  | Echoed: 'near top-rated schools', 'attractive option for families with children'. Invented: 'spacious', 'highly sought-after neighborhood' |
| v2 R2 | 96 | 7.3 | Pass | Pass | **Fail** | **Fail** | **Fail** |  | Echoed: 'quiet and safe neighborhood', 'perfect for families with kids', 'top-rated schools'. Invented: 'stable and family-friendly community', 'ideal for outdoor entertaining' |
| v3 R1 | 43 | 4.8 | Pass | Pass | Pass | Pass | **Fail** |  | Echoed: 'quiet and safe neighborhood', 'near top-rated schools'. Nothing invented |
| v3 R2 | 54 | 4.3 | Pass | Pass | Pass | **Fail** | **Fail** |  | Echoed: 'quiet and safe neighborhood', 'near top-rated schools', 'ideal for families with children'. Nothing invented |

### 6. Features only, empty notes

| Run | Words | Sec | 1 | 2 | 3 | 4 | 5 | 7 | Notes |
|---|---|---|---|---|---|---|---|---|---|
| v1 R1 | 86 | 8.7 | Pass | Pass | **Fail** | **Fail** | Pass |  | Invented: 'charming', 'modern amenities', 'private and secure outdoor space'; buyer-fit 'perfect for outdoor enthusiasts', 'ample space for family and friends' |
| v1 R2 | 79 | 6.4 | Pass | Pass | **Fail** | Pass | Pass |  | Invented: 'charming', 'ample storage and parking', 'modern amenities', 'solid foundation for a comfortable living space' |
| v2 R1 | 92 | 8.6 | Pass | Pass | **Fail** | **Fail** | Pass |  | Invented: 'charming', 'spacious bedrooms', 'perfect for parking multiple vehicles'; buyer-fit 'great choice for anyone looking for a comfortable living space' |
| v2 R2 | 96 | 7.9 | Pass | Pass | **Fail** | **Fail** | Pass |  | Invented: 'charming', 'comfortable retreat for its occupants'; buyer-fit 'ideal for those seeking a low-maintenance lifestyle' |
| v3 R1 | 44 | 4.9 | Pass | Pass | Pass | Pass | Pass |  | Clean. All 3 features, nothing added |
| v3 R2 | 43 | 3.6 | Pass | Pass | Pass | Pass | Pass |  | Clean. All 3 features, nothing added |

## Judgment calls for you to confirm

These choices affect the counts. If you disagree with one, change the rule and recount.

1. **Adjectives count as invented (check 3).** Any "cozy", "spacious" or "charming" fails the run. That's why v1 and v2 both score 12 of 12, so check 3 cannot tell them apart. A looser rule (only factual claims such as amenities, views or conditions) would separate them better.
2. **"In the heart of [city]" counts as a location claim (check 5).** Nothing in the input says the property is central.
3. **"2 bathrooms" for 1 full + 1 half bath was not counted as a figure error.** It happens in v1 Portland R1, v2 Portland R2 and v3 Portland R1. It's imprecise, and an agent might not want it.
4. **Derived totals were not counted as errors.** v2 Boston R2 ("total of 2400 square feet") and v3 Portland R1 ("2350") are correct sums of above- and below-grade space, but real-estate listings usually don't count below-grade space in the total.
5. **"Perfect for high-end entertaining" (echoed from the Atlanta notes) was not counted as buyer-fit.** It describes a use, not who should live there.
6. **v3 Atlanta R1 fails check 3 only for "spacious bedrooms".** It's the only issue in that output, so it's a borderline call.

## Still open for you

- **Check 7 (reads naturally, 1-5)** for all 36 outputs. It's subjective, so it should be your judgment.
- **Decision:** what is the notes field for, and what does the app do about notes that contain school, safety or family claims (warn in the UI, screen for flagged words, or accept it as the agent's responsibility on a draft)?
- **Decision:** the condo lot-size wording ("sits on a 0.05-acre lot") appears in every v3 condo output.
- **Fix:** the "This 1950 single-family home" error in v3.
