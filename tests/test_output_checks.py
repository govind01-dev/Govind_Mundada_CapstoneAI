from generator.output_checks import check_description_length, MIN_WORDS, MAX_WORDS

def test_length_within_range_returns_none():
    text = "word " * 100            # 100 words
    assert check_description_length(text) is None

# Test exactly at the maximum limit (Boundary)
def test_exactly_max_words_is_fine():
    """Verifies that a text with exactly MAX_WORDS returns None."""
    text = "word " * MAX_WORDS
    assert check_description_length(text) is None

# Test one word over the maximum limit (Boundary + 1)
def test_over_max_words_returns_message():
    """Verifies that MAX_WORDS + 1 returns a warning string."""
    text = "word " * (MAX_WORDS + 1)
    message = check_description_length(text)
    assert isinstance(message, str)
    assert len(message) > 0

# Test one word under the minimum limit (Boundary - 1)
def test_under_min_words_returns_message():
    """Verifies that MIN_WORDS - 1 returns a warning string."""
    text = "word " * (MIN_WORDS - 1)
    message = check_description_length(text)
    assert isinstance(message, str)
    assert len(message) > 0

# Test that the dynamic word count is explicitly named in the warning
def test_message_mentions_the_word_count():
    """Verifies that the warning message text contains the actual out-of-bounds count."""
    offending_count = MAX_WORDS + 1
    text = "word " * offending_count
    message = check_description_length(text)
    
    assert message is not None
    assert str(offending_count) in message

def test_exactly_min_words_is_fine():
    """A text with exactly MIN_WORDS words should not trigger a warning."""
    assert check_description_length("word " * MIN_WORDS) is None

def test_short_message_mentions_the_word_count():
    """The 'too short' warning should state the actual count."""
    short_count = MIN_WORDS - 1
    message = check_description_length("word " * short_count)
    assert message is not None
    assert str(short_count) in message

def test_empty_text_returns_message():
    """Empty text has zero words, so it should be flagged as too short."""
    assert check_description_length("") is not None    
