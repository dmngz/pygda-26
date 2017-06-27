import difflib

before = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet']
after = ['Lorem', 'dolor', 'set', 'amet', 'ipsum']

for diff_line in difflib.context_diff(before, after,
                                      fromfile='first list',
                                      tofile='second list'):
    print(diff_line)
