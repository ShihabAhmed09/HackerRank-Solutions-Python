import re

Test_String = input()

Regex_Pattern = r"(?<![aeiouAEIOU])."
# Regex_Pattern = r"(?<![aeiouAEIOU])(.)"
match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))

# (?<!regex_2)regex_1
# The negative lookbehind (?<!) asserts regex_1 not to be immediately preceded by regex_2. Lookbehind is
# excluded from the match (do not consume matches of regex_2), but only assert whether a match is possible
# or not.
