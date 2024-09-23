import re

def is_nsfw(message):
    """Check if the message contains NSFW content as whole words."""
    nsfw_keywords = [
        r'\bporn\b', r'\bsex\b', r'\bnudes\b', r'\bxxx\b', r'\bexplicit\b',
        r'\badult\b', r'\bfetish\b', r'\berotica\b', r'\bnsfw\b'
    ]

    # Check for any NSFW content in the message as whole words
    for keyword in nsfw_keywords:
        if re.search(keyword, message, re.IGNORECASE):
            return True
    return False
