import csv
from collections import defaultdict
from tqdm import tqdm

PATH_TO_LINKS = '/Users/viclehr/Desktop/wikispeedia_paths-and-graph/links.tsv'
OUTPUT_FILE = '/Users/viclehr/source/psai-2025/wikispeedia/links.txt'

G = defaultdict(list)

with open(PATH_TO_LINKS, 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for line in tqdm(reader, desc='Loading links file'):
        if len(line) == 0 or line[0].startswith("#"):
            continue
        source, target = line
        G[source].append(target)

# Write the graph to links.txt (overwriting if file exists)
with open(OUTPUT_FILE, 'w') as out_file:
    for source in G:
        for target in G[source]:
            out_file.write(f"{source} {target}\n")
