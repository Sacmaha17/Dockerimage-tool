import yaml
with open('config/base_image.txt') as f: base = f.read().strip()
with open('config/input.yaml') as f: cfg = yaml.safe_load(f)
with open('Dockerfile', 'w') as f:
    f.write(f"FROM {base}\n")
    for e in cfg['files']:
        f.write(f"COPY output/{e['target_path']}/ /{e['target_path']}/\n")
