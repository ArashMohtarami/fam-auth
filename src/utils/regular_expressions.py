
# Validate phone number format (E.164 format: +[country code][number])
PHONE_PATTERN = r"^\+\d{1,15}$"  # Supports country code and up to 15 digits
# Valid examples:
# - +14155552671 (US)
# - +919876543210 (India)
# - +447911123456 (UK)
# Invalid examples:
# - 123456 (Missing country code)
# - +1 (415) 555-2671 (Contains spaces/parentheses)
# - 415-555-2671 (Not in international format)