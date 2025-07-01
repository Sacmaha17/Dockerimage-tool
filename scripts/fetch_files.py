import os, yaml, shutil
from git import Repo

with open('config/input.yaml') as f:
    cfg = yaml.safe_load(f)

for e in cfg['files']:
    url = e['git_url'].replace('https://', f"https://{os.getenv('GIT_USERNAME')}:{os.getenv('GIT_TOKEN')}@")
    branch = e['branch']; src = e['source_path']; dst = os.path.join('output', e['target_path'])
    if os.path.exists('/tmp/repo'): shutil.rmtree('/tmp/repo')
    Repo.clone_from(url, '/tmp/repo', branch=branch)
    os.makedirs(dst, exist_ok=True)
    os.system(f"cp -r /tmp/repo/{src}/* {dst}/")
