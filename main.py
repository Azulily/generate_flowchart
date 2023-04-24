import re
import convert_csv_to_array
def generate_flowchart(urls):
    nodes = {}
    links = []
    for url,title in urls:
        segments = url.split("/")
        parent = ""
        for i, segment in enumerate(segments):
            node_id = "/".join(segments[:i+1])
            if node_id not in nodes:
                nodes[node_id] = f"{node_id}"
            if parent:
                parent_to_find = nodes[parent]
                child_to_find = nodes[node_id]
                parent_title = [arr[1] for arr in urls if parent_to_find in arr][0]
                child_title =  [arr[1] for arr in urls if child_to_find in arr][0]
                links.append(f"{nodes[parent]+ '['+ parent_title  + ']'} --> {nodes[node_id]+ '['+ child_title + ']'}")
            parent = node_id
    # ノードを名前でソート
    sorted_nodes = sorted(nodes.values())
    # 重複するエッジを削除
    unique_links = list(set(links))
    # ノードとリンクをフォーマット
    node_md = "\n".join([f"  {node}" for node in sorted_nodes])
    link_md = "\n".join([f"  {link}" for link in unique_links])
    # フローチャートのMarkdownを返す
    return f"""```mermaid
flowchart TB
{link_md}
```"""
urls = [['sample.com','title1'],
['sample.com/a','title2'],
['sample.com/b','title3'],
['sample.com/c','title4'],
['sample.com/d','title5'],
['sample.com/a/aa','title6'],
['sample.com/a/bb','title7'],
['sample.com/a/cc','title8'],
['sample.com/b/cc','title9'],]

urls = convert_csv_to_array.read_csv()
flowchart_md = generate_flowchart(urls)
print(flowchart_md)
