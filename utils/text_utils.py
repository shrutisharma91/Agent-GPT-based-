import textwrap

def split_text(text: str, max_tokens: int = 8192) -> list[str]:
    """
    Split text into chunks based on maximum tokens.
    """
    wrapped_text = textwrap.fill(text, width=max_tokens)
    return wrapped_text.split('\n')
