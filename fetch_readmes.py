import urllib.request

projects = [
    ('cloudguard-ai', 'main'),
    ('CryptoLedger', 'main'),
    ('ebpf-firewall', 'main'),
    ('Morse_code_translation', 'main'),
    ('POSE-DETECTION', 'main'),
    ('COLLEGE-PROJECTS/01_SignalKey_IoT_Security', 'main'),
    ('COLLEGE-PROJECTS/02_Fake_Job_Posting_Detection', 'main'),
    ('COLLEGE-PROJECTS/03_Merkle_Tree_DSA', 'main')
]

for proj, branch in projects:
    # Some repos might use 'master', we'll try 'main' first, then 'master'
    repo_path = proj if '/' not in proj else proj.split('/')[0]
    subpath = '' if '/' not in proj else '/' + proj.split('/')[1]
    
    url = f'https://raw.githubusercontent.com/AakashGs10/{repo_path}/{branch}{subpath}/README.md'
    try:
        html = urllib.request.urlopen(url).read().decode('utf-8')
        print(f"--- {proj} ---")
        print(html[:300] + '...')
    except Exception as e:
        url_master = f'https://raw.githubusercontent.com/AakashGs10/{repo_path}/master{subpath}/README.md'
        try:
            html = urllib.request.urlopen(url_master).read().decode('utf-8')
            print(f"--- {proj} ---")
            print(html[:300] + '...')
        except:
            print(f"--- {proj} --- (Not found)")
