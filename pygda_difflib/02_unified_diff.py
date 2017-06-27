import difflib

before = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet']
after = ['Lorem', 'dolor', 'set', 'amet', 'test']

for diff_line in difflib.unified_diff(before, after):
    print(diff_line)
