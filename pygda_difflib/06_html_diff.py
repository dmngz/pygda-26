import difflib

with open('first') as file:
    first = file.readlines()

with open('second') as file:
    second = file.readlines()


html_diff = difflib.HtmlDiff()
result_html = html_diff.make_file(first, second)

with open('result.html', 'w') as file:
    file.write(result_html)
