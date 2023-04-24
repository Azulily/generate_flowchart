urls = [
['sample.com','title1'],
['sample.com/a','title2'],
['sample.com/b','title3'],
['sample.com/c','title4'],
['sample.com/d','title5'],
['sample.com/a/aa','title6'],
['sample.com/a/bb','title7'],
['sample.com/a/cc','title8'],
['sample.com/b/cc','title9'],
]

output = "flowchart LR\n"

for url in urls:
    if url[0].count('/') == 0:
        output += "  " + url[0] + "[" + url[1] + "]" + " --> "
    elif url[0].count('/') == 1:
        output += url[0].split('/')[0] + "[" + url[0].split('/')[0] + "]" + " --> " + url[0] + "[" + url[1] + "]" + "\n"
    elif url[0].count('/') == 2:
        output += url[0].split('/')[1] + "[" + url[0].split('/')[1] + "]" + " --> " + url[0].split('/')[0] + "[" + url[0].split('/')[0] + "]" + "\n"
        output += url[0].split('/')[0] + "[" + url[0].split('/')[0] + "]" + " --> " + url[0] + "[" + url[1] + "]" + "\n"
    else:
        continue

print(output)
