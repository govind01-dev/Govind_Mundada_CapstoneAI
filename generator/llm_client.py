import ollama

DEFAULT_MODEL = "llama3.2"  # one place to change the model later

class LLMError(Exception):
    """Raised when the local model can't produce a usable response."""

def generate_text(prompt: str, model: str = DEFAULT_MODEL, temperature: float = 0.4) -> str:
    """Send a prompt to the local Ollama model and return the response text."""
    try:
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            # Configured temperature to standard deterministic range
            options={"temperature": temperature},
        )
    except ConnectionError as e:
        # Raised with the original connection context
        raise LLMError("Failed to connect to the local LLM server. Is Ollama running?") from e
        
    except ollama.ResponseError as e:
        # Specific handler for missing local models
        if e.status_code == 404:
            raise LLMError(f"The model '{model}' was not found. Have you pulled it yet?") from e
        raise LLMError(f"Ollama server returned an error: {e.error}") from e

    text = response["message"]["content"]
    
    # Catch empty or whitespace-only strings before stripping
    if not text or text.isspace():
        raise LLMError("The model returned an empty response.")
        
    return text.strip()
