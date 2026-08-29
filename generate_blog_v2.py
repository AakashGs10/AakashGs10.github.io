import os

projects = {
    'cloudguard-ai': {
        'name': 'CloudGuard AI',
        'desc': 'An advanced AI-powered cloud security platform designed to detect and mitigate threats in cloud infrastructure.',
        'architecture': 'The system utilizes a microservices architecture on AWS. An anomaly detection engine powered by PyTorch analyzes VPC Flow Logs and CloudTrail events in real-time. Events are streamed via Kafka to a fast in-memory cache (Redis) and a persistent storage layer (PostgreSQL). The frontend dashboard is built with React, providing real-time threat visualization.'
    },
    'CryptoLedger': {
        'name': 'CryptoLedger',
        'desc': 'A secure, decentralized cryptocurrency ledger implementation showcasing core blockchain concepts.',
        'architecture': 'Built using Python, the ledger implements Proof-of-Work (PoW) consensus. It features a P2P networking layer using WebSockets for node synchronization, elliptic curve cryptography (secp256k1) for wallet generation and transaction signing, and a Flask-based REST API for interacting with the blockchain (submitting transactions, mining blocks).'
    },
    'ebpf-firewall': {
        'name': 'eBPF XDP Firewall',
        'desc': 'High-performance, kernel-level network firewall built with eBPF/XDP for real-time packet inspection.',
        'architecture': 'The XDP program (C) runs at the NIC driver level, dropping malicious packets based on a BPF_MAP_TYPE_HASH blocklist. A Go-based userspace control plane manages the eBPF lifecycle, fetches threat intelligence (IPsum), and injects IPs into the kernel map. Telemetry is sent to userspace via BPF_MAP_TYPE_RINGBUF and exported to Prometheus & Grafana.'
    },
    'Morse_code_translation': {
        'name': 'Morse Code Translator',
        'desc': 'A utility tool for encoding and decoding Morse code, providing instant translation.',
        'architecture': 'A lightweight frontend web application built using HTML, CSS, and Vanilla JavaScript. It uses a bidirectional dictionary mapping for constant-time (O(1)) translation between alphanumeric characters and Morse code symbols, with real-time DOM updates via event listeners on the input fields.'
    },
    'POSE-DETECTION': {
        'name': 'Pose Detection System',
        'desc': 'Computer vision project utilizing machine learning models to detect human poses in real-time.',
        'architecture': 'Utilizes Python and OpenCV for video stream processing. Human body keypoints are detected using the MediaPipe Pose framework (BlazePose model). The system processes frames sequentially, extracts 33 3D landmarks, and renders the skeletal wireframe back onto the video feed, optimized for CPU inference.'
    },
    '01_SignalKey_IoT_Security': {
        'name': 'SignalKey IoT Security',
        'desc': 'A security framework for IoT devices focusing on signal-based authentication.',
        'architecture': 'Implements a physical-layer authentication mechanism for edge devices. A lightweight C-based client runs on microcontrollers (e.g., ESP32), transmitting cryptographic signatures over MQTT. The backend server authenticates devices based on signature validity and signal characteristics, storing device states in a time-series database (InfluxDB).'
    },
    '02_Fake_Job_Posting_Detection': {
        'name': 'Fake Job Posting Detection',
        'desc': 'An explainable machine learning framework for detecting fraudulent job postings.',
        'architecture': 'A multi-model ensemble approach combining Random Forest, XGBoost, and neural networks. Features are engineered from textual job descriptions using TF-IDF and word embeddings. Model predictions are interpreted using SHAP (SHapley Additive exPlanations) values to highlight the specific words contributing to the fraud score.'
    },
    '03_Merkle_Tree_DSA': {
        'name': 'Merkle Tree Implementation',
        'desc': 'Data Structures and Algorithms project demonstrating a custom Merkle Tree for data verification.',
        'architecture': 'A custom C++ implementation of a Merkle (Hash) Tree. Leaf nodes contain SHA-256 hashes of data blocks, and non-leaf nodes contain the hash of their children. Includes functions for efficient data verification (Merkle Proofs), tree generation from a file, and dynamic updating of leaf nodes with O(log N) recalculation.'
    }
}

blog_dir = 'Aakash_Blog'
os.makedirs(blog_dir, exist_ok=True)

adsense_code = '''
<!-- Google AdSense -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-0000000000000000" crossorigin="anonymous"></script>
'''

html_template = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{{{title}}}} - Aakash G S</title>
    {{adsense_code}}
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <style>
        body {{ background-color: #0f172a; color: #f8fafc; font-family: 'Inter', sans-serif; }}
        .glass-panel {{ background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); }}
    </style>
</head>
<body class="min-h-screen flex flex-col items-center p-6">
    <nav class="w-full max-w-4xl mb-8 flex justify-between items-center">
        <a href="index.html" class="text-blue-400 hover:text-blue-300 flex items-center gap-2 transition-colors">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
            Back to Projects
        </a>
        <div class="text-slate-400 font-medium">Aakash G S</div>
    </nav>
    
    <main class="w-full max-w-4xl glass-panel rounded-2xl p-8 shadow-2xl">
        <header class="mb-10 border-b border-slate-700 pb-6">
            <h1 class="text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-emerald-400 mb-4">{{{{title}}}}</h1>
            <p class="text-xl text-slate-300">{{{{desc}}}}</p>
        </header>
        
        <div x-data="{{ tab: 'overview' }}">
            <div class="flex space-x-4 mb-6 border-b border-slate-700">
                <button @click="tab = 'overview'" :class="tab === 'overview' ? 'border-blue-400 text-blue-400' : 'border-transparent text-slate-400 hover:text-slate-200'" class="px-4 py-2 border-b-2 font-medium transition-colors">
                    Overview
                </button>
                <button @click="tab = 'architecture'" :class="tab === 'architecture' ? 'border-emerald-400 text-emerald-400' : 'border-transparent text-slate-400 hover:text-slate-200'" class="px-4 py-2 border-b-2 font-medium transition-colors">
                    Architecture
                </button>
            </div>
            
            <div x-show="tab === 'overview'" class="animate-[fadeIn_0.3s_ease-in-out]">
                <h2 class="text-2xl font-semibold mb-4 text-white">Project Summary</h2>
                <div class="prose prose-invert max-w-none text-slate-300 leading-relaxed">
                    <p>{{{{desc}}}} This project is a key part of my technical portfolio, demonstrating hands-on experience in the respective domain.</p>
                    <div class="mt-8 p-4 bg-slate-800 rounded-lg border border-slate-700 flex items-center justify-between">
                        <span class="text-slate-200 font-medium">View source code on GitHub</span>
                        <a href="https://github.com/AakashGs10/{{{{repo_name}}}}" target="_blank" class="px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white rounded-md transition-colors shadow-lg">GitHub Repo</a>
                    </div>
                </div>
            </div>
            
            <div x-show="tab === 'architecture'" class="animate-[fadeIn_0.3s_ease-in-out]" style="display: none;">
                <h2 class="text-2xl font-semibold mb-4 text-white">Technical Architecture</h2>
                <div class="prose prose-invert max-w-none text-slate-300 leading-relaxed">
                    <p class="text-lg">{{{{architecture}}}}</p>
                    <div class="mt-8 grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="p-4 bg-slate-800 rounded-lg border border-slate-700 hover:border-emerald-500 transition-colors cursor-default">
                            <h3 class="text-emerald-400 font-medium mb-2 flex items-center gap-2">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
                                Design Pattern
                            </h3>
                            <p class="text-sm text-slate-400">Follows industry-standard structural and behavioral design patterns tailored for optimal performance.</p>
                        </div>
                        <div class="p-4 bg-slate-800 rounded-lg border border-slate-700 hover:border-blue-500 transition-colors cursor-default">
                            <h3 class="text-blue-400 font-medium mb-2 flex items-center gap-2">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                                Performance
                            </h3>
                            <p class="text-sm text-slate-400">Optimized algorithms and data structures ensuring minimal latency and high throughput.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
    <footer class="mt-12 text-slate-500 text-sm">
        &copy; 2026 Aakash G S. All rights reserved.
    </footer>
    <style>
        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(5px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    </style>
</body>
</html>
'''

index_template = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aakash G S - Interactive Portfolio</title>
    {{adsense_code}}
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{ background-color: #0f172a; color: #f8fafc; font-family: 'Inter', sans-serif; }}
        .glass-card {{ background: rgba(30, 41, 59, 0.5); backdrop-filter: blur(8px); border: 1px solid rgba(255, 255, 255, 0.05); transition: all 0.3s ease; }}
        .glass-card:hover {{ transform: translateY(-5px); background: rgba(30, 41, 59, 0.8); border-color: rgba(56, 189, 248, 0.5); box-shadow: 0 10px 30px -10px rgba(2, 132, 199, 0.5); }}
    </style>
</head>
<body class="min-h-screen flex flex-col items-center p-6">
    <header class="w-full max-w-6xl mt-10 mb-16 text-center">
        <h1 class="text-5xl font-extrabold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 via-indigo-400 to-emerald-400 mb-4 tracking-tight">Aakash G S</h1>
        <p class="text-xl text-slate-400 font-light max-w-2xl mx-auto">Software Engineer &middot; Architect &middot; Tech Enthusiast</p>
        <p class="mt-4 text-slate-500">Explore my technical projects, their architectures, and open-source contributions.</p>
    </header>
    
    <main class="w-full max-w-6xl">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {{{{project_list}}}}
        </div>
    </main>
    
    <footer class="mt-20 mb-8 text-slate-500 text-sm text-center">
        &copy; 2026 Aakash G S. All rights reserved.<br>
        <span class="text-slate-600">Built with modern web technologies.</span>
    </footer>
</body>
</html>
'''

project_list_html = ""

for id, details in projects.items():
    safe_name = id.lower().replace(' ', '-').replace('_', '-')
    filename = f"{safe_name}.html"
    
    # Repo mapping for github links
    if id.startswith('0'):
        repo_link = f"COLLEGE-PROJECTS/tree/main/{id}"
    else:
        repo_link = id
        
    # Add to index grid
    project_list_html += f'''
    <a href="{filename}" class="glass-card rounded-xl p-6 flex flex-col h-full cursor-pointer block group relative overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-br from-blue-500/10 to-emerald-500/10 opacity-0 group-hover:opacity-100 transition-opacity"></div>
        <h3 class="text-2xl font-semibold text-slate-100 mb-3 group-hover:text-blue-400 transition-colors">{details['name']}</h3>
        <p class="text-slate-400 flex-grow text-sm leading-relaxed">{details['desc']}</p>
        <div class="mt-6 flex items-center text-emerald-400 text-sm font-medium">
            Explore Architecture <svg class="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
        </div>
    </a>
    '''
    
    # Create blog post
    post_html = html_template.replace('{{title}}', details['name'])\
                             .replace('{{desc}}', details['desc'])\
                             .replace('{{architecture}}', details['architecture'])\
                             .replace('{{repo_name}}', repo_link)
    
    with open(os.path.join(blog_dir, filename), 'w', encoding='utf-8') as f:
        f.write(post_html)

# Create index.html
index_html = index_template.replace('{{project_list}}', project_list_html)
with open(os.path.join(blog_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Interactive Blog generated successfully.")
