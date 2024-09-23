import re

# This function can be expanded with an external API if needed.
def is_nsfw(message):
    # A basic but sophisticated regex to identify potential NSFW terms related to pornography
    nsfw_keywords = [
        r'\bporn\b', r'\bsex\b', r'\bnudes\b', r'\bxxx\b', r'\bexplicit\b',
        r'\badult\b', r'\bfetish\b', r'\berotica\b', r'\bnsfw\b'
        # Add more as needed or integrate an external API here for more complex analysis
    ]

    # Check if the message contains any of the keywords
    for keyword in nsfw_keywords:
        if re.search(keyword, message, re.IGNORECASE):
            return True
    return False

# Optional: Add API integration here if needed for enhanced detection (e.g., call a text scanning API)
