import re
import numpy as np
np.set_printoptions(threshold=np.inf)

def generate_flowchart(urls):
    nodes = {}
    links = []
    for url in urls:
        segments = url.split("/")
        parent = ""
        for i, segment in enumerate(segments):
            node_id = "/".join(segments[:i+1])
            if node_id not in nodes:
                nodes[node_id] = f"{node_id}"
            if parent:
                links.append(f"{nodes[parent]} --> {nodes[node_id]}")
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
{urls}
{link_md}
```"""
urls = [
    'sample.com',
    'sample.com/a',
    'sample.com/b',
    'sample.com/c',
    'sample.com/d',
    'sample.com/a/aa',
    'sample.com/a/bb',
    'sample.com/a/cc',
    'sample.com/b/cc',
]
flowchart_md = generate_flowchart(urls)
print(flowchart_md)
