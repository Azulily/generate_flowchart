def generate_flowchart(urls):
    flowchart = "flowchart LR\n"
    nodes = {}
    
    for url, title in urls:
        node_id = url.split("/")[-1] + "[" + title + "]"
        nodes[url] = node_id

    for url, title in urls:
        node_id = nodes[url]
        if "/" in url:
            parent_id = nodes[url.rsplit("/", 1)[0]]
        else:
            parent_id = "sample.com"
        flowchart += f"  {parent_id} --> {node_id}\n"

    return flowchart
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

print(generate_flowchart(urls))
