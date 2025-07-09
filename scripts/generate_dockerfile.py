# import yaml
# with open('config/base_image.txt') as f: base = f.read().strip()
# with open('config/input.yaml') as f: cfg = yaml.safe_load(f)
# with open('Dockerfile', 'w') as f:
#     f.write(f"FROM {base}\n")
#     for e in cfg['repo']:
#         f.write(f"COPY output/{e['target_path']}/ /{e['target_path']}/\n")


# import yaml
# import os

# with open('config/input.yaml') as f:
#     cfg = yaml.safe_load(f)

# for repo in cfg.get('repos', []):
#     for filemap in repo.get('files', []):
#         source = filemap['source']
#         target = filemap['target']
#         print(f"# Will copy from {source} to {target} in Dockerfile.")
#         # Add Dockerfile generation logic here if needed


import yaml
import os

base = "ubuntu:20.04"  # <-- Set your base image here

with open('config/input.yaml') as f:
    cfg = yaml.safe_load(f)

with open('Dockerfile', 'w') as f:
    f.write(f"FROM {base}\n")
    for repo in cfg.get('repos', []):
        for filemap in repo.get('files', []):
            target = filemap['target']
            f.write(f"COPY output/{target}/ /{target}/\n")

for repo in cfg.get('repos', []):
    for filemap in repo.get('files', []):
        source = filemap['source']
        target = filemap['target']
        print(f"# Will copy from {source} to {target} in Dockerfile.")