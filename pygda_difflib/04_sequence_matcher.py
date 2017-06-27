import difflib


def get_longest_match_string(first_string, longest_match_result):
    longest_match_start = longest_match_result.a
    longest_match_end = longest_match_result.a + longest_match_result.size

    return first_string[longest_match_start:longest_match_end]


first = 'Enter The Wu-Tang (36 Chambers)'
second = 'Enter The Wu-Tang Clan (36 Chambers) (12", Promo, Smplr)'

matcher = difflib.SequenceMatcher(a=first, b=second)

print(matcher.ratio())

longest_match = matcher.find_longest_match(0, len(first), 0, len(second))
print(get_longest_match_string(first, longest_match))

print(matcher.get_matching_blocks())
