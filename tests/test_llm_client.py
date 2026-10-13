from unittest.mock import patch
import ollama
import pytest
from generator.llm_client import generate_text, LLMError

def test_empty_response_raises():
    fake_reply = {"message": {"content": "   "}}          # pretend the model returned blanks
    with patch("generator.llm_client.ollama.chat", return_value=fake_reply):
        with pytest.raises(LLMError):
            generate_text("any prompt")

# 1. Connection failure test
def test_connection_failure_raises():
    """Ensure network/connection failure throws a clean LLMError."""
    with patch("generator.llm_client.ollama.chat", side_effect=ConnectionError("down")):
        with pytest.raises(LLMError):
            generate_text("any prompt")

# 2. Model not found test (404 status code)
def test_model_not_found_raises_with_model_name():
    fake_error = ollama.ResponseError("model not found", 404)
    with patch("generator.llm_client.ollama.chat", side_effect=fake_error):
        with pytest.raises(LLMError) as exc_info:
            generate_text("any prompt", model="nonexistent-model")   # distinctive name

    assert "nonexistent-model" in str(exc_info.value)   # the message names the model we asked for

# 3. Other server error test (500 status code)
def test_server_error_500_raises():
    """Ensure a 500 internal server error exercises the generic server error code path."""
    fake_500_error = ollama.ResponseError("internal server error", 500)
    
    with patch("generator.llm_client.ollama.chat", side_effect=fake_500_error):
        with pytest.raises(LLMError) as exc_info:
            generate_text("any prompt")
            
        assert "server returned an error" in str(exc_info.value).lower()