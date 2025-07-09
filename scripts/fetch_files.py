# import os, yaml, shutil
# from git import Repo

# with open('config/input.yaml') as f:
#     cfg = yaml.safe_load(f)

# for e in cfg['files']:
#     url = e['git_url'].replace('https://', f"https://{os.getenv('GIT_USERNAME')}:{os.getenv('GIT_TOKEN')}@")
#     branch = e['branch']; src = e['source_path']; dst = os.path.join('output', e['target_path'])
#     tmp_repo_path = os.path.join(os.path.dirname(__file__), tmp_repo_path)
#     if os.path.exists(tmp_repo_path): shutil.rmtree(tmp_repo_path)
#     Repo.clone_from(url, tmp_repo_path, branch=branch)
#     os.makedirs(dst, exist_ok=True)
#     os.system(f"cp -r "+tmp_repo_path+"/{src}/* {dst}/")

# import os, yaml, shutil
# from git import Repo

# with open('config/input.yaml') as f:
#     cfg = yaml.safe_load(f)

# import os, yaml, shutil
# from git import Repo

# with open('config/input.yaml') as f:
#     cfg = yaml.safe_load(f)
# print(cfg)
# for repo in cfg['repos']:
#     url = repo['repo'].replace('https://', f"https://{os.getenv('GIT_USERNAME')}:{os.getenv('GIT_TOKEN')}@")
#     branch = repo['branch']
#     for filemap in repo['files']:
#         src = filemap['source'].lstrip('/')
#         dst = os.path.join('output', filemap['target'].lstrip('/'))
#         if os.path.exists('/tmp/repo'):
#             shutil.rmtree('/tmp/repo')
#         Repo.clone_from(url, '/tmp/repo', branch=branch)
#         os.makedirs(dst, exist_ok=True)
#         os.system(f"cp -r /tmp/repo/{src}/* {dst}/")

# import os
# import yaml
# import shutil
# import glob
# from git import Repo

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# TMP_REPO_PATH = os.path.join(BASE_DIR, 'tmp_repo')
# OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

# with open(os.path.join(BASE_DIR, 'config/input.yaml')) as f:
#     cfg = yaml.safe_load(f)

# for repo_cfg in cfg['repos']:
#     url = repo_cfg['repo'].replace(
#         'https://',
#         f"https://{os.getenv('GIT_USERNAME')}:{os.getenv('GIT_TOKEN')}@"
#     )
#     branch = repo_cfg.get('branch', 'main')  # fallback to 'main' if branch missing

#     if os.path.exists(TMP_REPO_PATH):
#         shutil.rmtree(TMP_REPO_PATH)

#     Repo.clone_from(url, TMP_REPO_PATH, branch=branch)

#     for f in repo_cfg.get('files', []):  # ✅ Correct way to access files
#         src = f['source'].lstrip('/')
#         dst = os.path.join(OUTPUT_DIR, f['target'])
#         os.makedirs(dst, exist_ok=True)

#         full_src_path = os.path.join(TMP_REPO_PATH, src)

#         if not os.path.exists(full_src_path):
#             raise FileNotFoundError(f"Source path does not exist: {full_src_path}")

#         # Copy contents from source to destination
#         for item in os.listdir(full_src_path):
#             s = os.path.join(full_src_path, item)
#             d = os.path.join(dst, item)
#             if os.path.isdir(s):
#                 shutil.copytree(s, d, dirs_exist_ok=True)
#             else:
#                 shutil.copy2(s, d)


import os
import yaml
import shutil
from git import Repo

with open('config/input.yaml') as f:
    cfg = yaml.safe_load(f)

for repo in cfg['repos']:
    url = repo['repo']
    # Only inject credentials if needed
    username = os.getenv('GIT_USERNAME')
    token = os.getenv('GIT_TOKEN')
    if username and token and ('github.com' in url):
        url = url.replace('https://', f"https://{username}:{token}@")
    branch = repo.get('branch', 'master')
    for filemap in repo['files']:
        src = filemap['source'].lstrip('/')
        dst = os.path.join('output', filemap['target'].lstrip('/'))
        if os.path.exists('/tmp/repo'):
            shutil.rmtree('/tmp/repo')
        Repo.clone_from(url, '/tmp/repo', branch=branch)
        src_path = os.path.join('/tmp/repo', src)
        if os.path.exists(src_path):
            # Exclude the .git directory and its contents
            shutil.copytree(src_path, dst, dirs_exist_ok=True, ignore=shutil.ignore_patterns('.git'))
        else:
            print(f"Warning: source path '{src_path}' does not exist in repo '{url}'")