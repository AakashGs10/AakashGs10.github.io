import os

projects = {
    'cloudguard-ai': {
        'name': 'CloudGuard AI',
        'desc': 'An advanced AI-powered cloud security platform designed to detect and mitigate threats in cloud infrastructure.',
        'content': '''
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">1. Executive Summary</h3>
            <p class="mb-4">CloudGuard AI represents a modern approach to cloud infrastructure security. By leveraging artificial intelligence and machine learning, this platform continuously monitors cloud environments, detects anomalous activities, and provides automated mitigation strategies before threats can escalate.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">2. The Problem Statement</h3>
            <p class="mb-4">Traditional rule-based security systems struggle to keep up with the dynamic nature of modern cloud environments. Static rules generate high volumes of false positives and often miss sophisticated, slow-moving attacks or zero-day vulnerabilities. There was a critical need for a system that learns the baseline behavior of a cloud ecosystem and flags deviations intelligently.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">3. Technical Architecture</h3>
            <p class="mb-4">The core of CloudGuard AI is built on a distributed microservices architecture. It ingests massive streams of telemetry data (VPC Flow Logs, CloudTrail events, IAM activity) using Apache Kafka. This data is fed into a PyTorch-based anomaly detection engine which utilizes Autoencoders and Recurrent Neural Networks (RNNs) to identify temporal and spatial anomalies. The frontend dashboard, built with React, visualizes this data in real-time, pulling from a low-latency Redis cache and a persistent PostgreSQL database.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">4. Key Features & Implementation</h3>
            <ul class="list-disc pl-6 mb-4 space-y-2">
                <li><strong class="text-emerald-400">Behavioral Analytics:</strong> Continuously models normal user and resource behavior.</li>
                <li><strong class="text-emerald-400">Automated Remediation:</strong> Integrates with AWS Lambda to automatically isolate compromised EC2 instances or revoke suspicious IAM credentials.</li>
                <li><strong class="text-emerald-400">Threat Intelligence Integration:</strong> Cross-references detected IP addresses with global threat feeds.</li>
            </ul>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">5. Conclusion</h3>
            <p class="mb-4">CloudGuard AI effectively bridges the gap between reactive security measures and proactive threat hunting. By utilizing deep learning, the platform significantly reduces false positives and provides security teams with actionable, high-fidelity alerts.</p>
        '''
    },
    'CryptoLedger': {
        'name': 'CryptoLedger',
        'desc': 'A secure, decentralized cryptocurrency ledger implementation showcasing core blockchain concepts.',
        'content': '''
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">1. Executive Summary</h3>
            <p class="mb-4">CryptoLedger is a fully functional, decentralized blockchain ledger built from scratch. It serves as an educational and robust demonstration of how foundational cryptocurrency technologies—such as cryptography, consensus algorithms, and peer-to-peer networking—interact to create trustless financial systems.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">2. The Problem Statement</h3>
            <p class="mb-4">Understanding the underlying mechanics of blockchain technology can be daunting when looking at massive codebases like Bitcoin or Ethereum. CryptoLedger was created to distill these complex mechanisms into a clean, readable, and highly modular architecture that demonstrates the verifiable ledger problem without unnecessary bloat.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">3. Technical Architecture</h3>
            <p class="mb-4">The project is implemented entirely in Python. The cryptographic backbone relies on Elliptic Curve Digital Signature Algorithm (ECDSA) using the secp256k1 curve for wallet generation and transaction signing. The consensus mechanism is a classic Proof-of-Work (PoW) algorithm, requiring nodes to discover a nonce that produces a valid SHA-256 hash. The peer-to-peer networking layer utilizes WebSockets for real-time state synchronization across distributed nodes.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">4. Key Features & Implementation</h3>
            <ul class="list-disc pl-6 mb-4 space-y-2">
                <li><strong class="text-blue-400">Immutable Ledger:</strong> Blocks are cryptographically chained; altering one block invalidates the entire subsequent chain.</li>
                <li><strong class="text-blue-400">Transaction Pool:</strong> Unconfirmed transactions are stored in a mempool until a miner includes them in a validated block.</li>
                <li><strong class="text-blue-400">REST API Interface:</strong> Features a Flask-based API for users to generate wallets, submit transactions, and query blockchain state.</li>
            </ul>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">5. Conclusion</h3>
            <p class="mb-4">CryptoLedger successfully implements the core principles of decentralized finance. It stands as a comprehensive review of distributed systems, cryptographic security, and game-theoretic consensus models.</p>
        '''
    },
    'ebpf-firewall': {
        'name': 'eBPF XDP Firewall',
        'desc': 'High-performance, kernel-level network firewall built with eBPF/XDP for real-time packet inspection.',
        'content': '''
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">1. Executive Summary</h3>
            <p class="mb-4">This project is a high-performance network firewall leveraging the power of eBPF (Extended Berkeley Packet Filter) and XDP (eXpress Data Path). It drops malicious network packets directly at the Network Interface Card (NIC) driver level, long before they reach the Linux networking stack.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">2. The Problem Statement</h3>
            <p class="mb-4">Traditional firewalls (like iptables or nftables) process packets after they have traversed a significant portion of the kernel networking stack, consuming CPU cycles and memory. During a DDoS attack or high-volume malicious traffic event, this overhead can bring a server down. A solution was needed to drop packets as early as theoretically possible.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">3. Technical Architecture</h3>
            <p class="mb-4">The architecture is split into two components: kernel space and user space. The kernel space component is written in restricted C and compiled to eBPF bytecode. It hooks into the XDP path. The user space component is a Go control plane that manages the lifecycle of the eBPF program. It periodically fetches threat intelligence feeds (like IPsum) and injects thousands of malicious IPs into a BPF_MAP_TYPE_HASH. When a packet arrives, the XDP program parses the headers, performs a lookup in this map, and returns XDP_DROP if it matches.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">4. Key Features & Implementation</h3>
            <ul class="list-disc pl-6 mb-4 space-y-2">
                <li><strong class="text-emerald-400">Zero-Overhead Drops:</strong> Packets are dropped at the lowest possible layer, saving massive CPU cycles.</li>
                <li><strong class="text-emerald-400">Ring Buffer Telemetry:</strong> Uses BPF_MAP_TYPE_RINGBUF to stream dropped packet telemetry to user space asynchronously.</li>
                <li><strong class="text-emerald-400">Prometheus Integration:</strong> The Go control plane exposes Prometheus metrics for real-time Grafana dashboarding.</li>
            </ul>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">5. Conclusion</h3>
            <p class="mb-4">The eBPF XDP Firewall is a masterclass in modern Linux networking. It demonstrates how next-generation kernel technologies can be utilized to achieve unprecedented networking performance and security.</p>
        '''
    },
    'Morse_code_translation': {
        'name': 'Morse Code Translator',
        'desc': 'A utility tool for encoding and decoding Morse code, providing instant translation.',
        'content': '''
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">1. Executive Summary</h3>
            <p class="mb-4">The Morse Code Translator is a streamlined, efficient web application designed to encode standard text into Morse code and decode Morse code back into human-readable text instantly.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">2. The Problem Statement</h3>
            <p class="mb-4">While Morse code is a legacy communication method, it remains highly relevant in aviation, amateur radio, and accessibility tools. The goal was to build a translator that is incredibly fast, works completely client-side without API calls, and offers a clean user interface.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">3. Technical Architecture</h3>
            <p class="mb-4">The application is built using pure HTML, CSS, and Vanilla JavaScript to ensure zero dependencies and maximum load speed. At its core, the logic relies on a bidirectional Hash Map (Dictionary) in JavaScript. This allows the algorithm to look up characters in O(1) time complexity. The UI is bound to input events, triggering the translation algorithm on every keystroke for real-time feedback.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">4. Key Features & Implementation</h3>
            <ul class="list-disc pl-6 mb-4 space-y-2">
                <li><strong class="text-blue-400">Real-time Parsing:</strong> Instantly updates the output DOM elements as the user types.</li>
                <li><strong class="text-blue-400">Audio Playback Integration:</strong> Utilizes the Web Audio API to generate the exact oscillating frequencies representing dots and dashes.</li>
                <li><strong class="text-blue-400">Error Handling:</strong> Gracefully handles unsupported characters and malformed Morse inputs.</li>
            </ul>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">5. Conclusion</h3>
            <p class="mb-4">This project highlights proficiency in frontend fundamentals and algorithmic efficiency, proving that complex libraries aren't always necessary for highly responsive applications.</p>
        '''
    },
    'POSE-DETECTION': {
        'name': 'Pose Detection System',
        'desc': 'Computer vision project utilizing machine learning models to detect human poses in real-time.',
        'content': '''
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">1. Executive Summary</h3>
            <p class="mb-4">The Pose Detection System is an advanced computer vision application capable of identifying and tracking human body mechanics in real-time. It maps out 33 distinct skeletal landmarks across the human body using a standard webcam feed.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">2. The Problem Statement</h3>
            <p class="mb-4">Human pose estimation is notoriously computationally expensive, often requiring powerful GPUs. The objective was to build a system that is accurate enough for fitness tracking, biomechanical analysis, or interactive gaming, but optimized enough to run on standard consumer CPUs without significant latency.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">3. Technical Architecture</h3>
            <p class="mb-4">The project is developed in Python. It relies heavily on OpenCV for image processing and matrix manipulations. The core inference is powered by Google's MediaPipe framework, specifically the BlazePose model. BlazePose utilizes a two-step pipeline: a fast face detector locates the person, followed by a heavier pose landmark model that predicts the 33 3D keypoints based on the cropped region.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">4. Key Features & Implementation</h3>
            <ul class="list-disc pl-6 mb-4 space-y-2">
                <li><strong class="text-emerald-400">Real-Time Overlay:</strong> Dynamically renders skeletal wireframes and bounding boxes directly onto the live video feed.</li>
                <li><strong class="text-emerald-400">Angle Calculations:</strong> Implements vector mathematics (dot products) to calculate joint angles in real-time, useful for form correction in exercises (like bicep curls or squats).</li>
                <li><strong class="text-emerald-400">High FPS Optimization:</strong> Bypasses the detector network when a pose is successfully tracked in the previous frame, dramatically increasing Frames Per Second (FPS).</li>
            </ul>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">5. Conclusion</h3>
            <p class="mb-4">This system successfully merges state-of-the-art machine learning with practical, real-world constraints, resulting in a highly optimized and versatile computer vision tool.</p>
        '''
    },
    '01_SignalKey_IoT_Security': {
        'name': 'SignalKey IoT Security',
        'desc': 'A security framework for IoT devices focusing on signal-based authentication.',
        'content': '''
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">1. Executive Summary</h3>
            <p class="mb-4">SignalKey is an innovative security framework tailored for resource-constrained Internet of Things (IoT) devices. It goes beyond traditional password or token authentication by analyzing physical signal characteristics to verify device identity.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">2. The Problem Statement</h3>
            <p class="mb-4">IoT devices (like smart sensors or cameras) are highly susceptible to spoofing and cloning attacks. Since they lack the computational power for heavy encryption, a compromised device credential can lead to network infiltration. SignalKey aims to solve this by making the hardware's physical fingerprint part of the authentication process.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">3. Technical Architecture</h3>
            <p class="mb-4">The architecture involves an edge device (e.g., an ESP32 microcontroller) and a central backend server. The edge device runs a C-based client that signs payloads using a lightweight HMAC algorithm. Alongside the payload, the network gateway captures physical layer metrics (like Received Signal Strength Indicator - RSSI, and phase shifts). The Python backend aggregates the cryptographic signature and the analog signal footprint, comparing it against historical baselines stored in a time-series database (InfluxDB).</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">4. Key Features & Implementation</h3>
            <ul class="list-disc pl-6 mb-4 space-y-2">
                <li><strong class="text-blue-400">Multi-Factor IoT Auth:</strong> Combines digital keys with physical analog signal traits.</li>
                <li><strong class="text-blue-400">MQTT Protocol Integration:</strong> Optimized for low-bandwidth networks using MQTT publish-subscribe architecture.</li>
                <li><strong class="text-blue-400">Anomaly Detection:</strong> Flags sudden changes in spatial signal characteristics, preventing remote spoofing attacks.</li>
            </ul>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">5. Conclusion</h3>
            <p class="mb-4">SignalKey demonstrates a deep understanding of both low-level hardware constraints and high-level security paradigms, offering a robust defense-in-depth approach for IoT networks.</p>
        '''
    },
    '02_Fake_Job_Posting_Detection': {
        'name': 'Fake Job Posting Detection',
        'desc': 'An explainable machine learning framework for detecting fraudulent job postings.',
        'content': '''
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">1. Executive Summary</h3>
            <p class="mb-4">This project tackles the growing problem of employment scams by employing Natural Language Processing (NLP) and Machine Learning to automatically classify job postings as legitimate or fraudulent, while providing clear explanations for its decisions.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">2. The Problem Statement</h3>
            <p class="mb-4">Fraudulent job postings cause significant financial and emotional distress to job seekers. Black-box machine learning models can detect these scams but fail to explain *why* a post was flagged, making it difficult for moderators to trust the system. An explainable AI (XAI) approach was required.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">3. Technical Architecture</h3>
            <p class="mb-4">The data pipeline utilizes Python, Pandas, and Scikit-Learn. Text data from job descriptions, company profiles, and requirements are cleaned and vectorized using TF-IDF (Term Frequency-Inverse Document Frequency) and GloVe word embeddings. An ensemble model combining XGBoost and a Random Forest Classifier handles the prediction. Crucially, the SHAP (SHapley Additive exPlanations) library is integrated to break down the model's output.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">4. Key Features & Implementation</h3>
            <ul class="list-disc pl-6 mb-4 space-y-2">
                <li><strong class="text-emerald-400">Imbalanced Data Handling:</strong> Utilizes SMOTE (Synthetic Minority Over-sampling Technique) to handle the extreme class imbalance between real and fake jobs.</li>
                <li><strong class="text-emerald-400">Explainability Dashboard:</strong> SHAP plots are generated to show exactly which words or missing features (like lack of company logo) drove the fraud score up.</li>
                <li><strong class="text-emerald-400">High Recall Optimization:</strong> The model is tuned specifically for high Recall, ensuring that as few fraudulent postings as possible slip through the cracks.</li>
            </ul>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">5. Conclusion</h3>
            <p class="mb-4">By merging high-accuracy ensemble methods with state-of-the-art explainability tools, this project delivers a production-ready solution that empowers human moderators rather than just replacing them.</p>
        '''
    },
    '03_Merkle_Tree_DSA': {
        'name': 'Merkle Tree Implementation',
        'desc': 'Data Structures and Algorithms project demonstrating a custom Merkle Tree for data verification.',
        'content': '''
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">1. Executive Summary</h3>
            <p class="mb-4">This Data Structures and Algorithms (DSA) project is a ground-up implementation of a Merkle Tree (Hash Tree). It demonstrates how large datasets can be securely and efficiently verified without transmitting the entire dataset.</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">2. The Problem Statement</h3>
            <p class="mb-4">In distributed systems (like Git, IPFS, or Blockchains), nodes need to verify that a specific piece of data belongs to a larger dataset without downloading everything. A standard linear hash chain requires O(N) time for verification. A tree structure was needed to bring this down to O(log N).</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">3. Technical Architecture</h3>
            <p class="mb-4">Written in modern C++, the project manages memory dynamically using smart pointers. The tree is constructed bottom-up: raw data blocks are hashed using the SHA-256 algorithm to form the leaf nodes. Pairs of adjacent nodes are concatenated and hashed to form the parent nodes, continuing recursively until a single Root Hash is formed. The project includes a comprehensive API for generating "Merkle Proofs".</p>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">4. Key Features & Implementation</h3>
            <ul class="list-disc pl-6 mb-4 space-y-2">
                <li><strong class="text-blue-400">Efficient Proof Generation:</strong> The algorithm generates cryptographic proofs in O(log N) time, extracting only the sibling hashes needed to reconstruct the root.</li>
                <li><strong class="text-blue-400">Dynamic Updates:</strong> If a single data block changes, the tree intelligently recalculates only the affected branch up to the root, rather than rebuilding the entire tree.</li>
                <li><strong class="text-blue-400">Memory Optimization:</strong> Strictly typed and utilizes move semantics and reference passing to minimize memory overhead during deep tree traversals.</li>
            </ul>
            
            <h3 class="text-xl font-bold text-white mt-6 mb-3 border-b border-slate-700 pb-2">5. Conclusion</h3>
            <p class="mb-4">This implementation underscores a strong grasp of complex data structures, cryptography, and systems-level memory management in C++.</p>
        '''
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
    <style>
        body {{ background-color: #0f172a; color: #f8fafc; font-family: 'Inter', sans-serif; }}
        .glass-panel {{ background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); }}
    </style>
</head>
<body class="min-h-screen flex flex-col items-center p-6">
    <nav class="w-full max-w-4xl mb-8 flex justify-between items-center">
        <a href="index.html" class="text-blue-400 hover:text-blue-300 flex items-center gap-2 transition-colors font-semibold">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
            Back to Projects
        </a>
        <div class="text-slate-400 font-medium">Aakash G S</div>
    </nav>
    
    <main class="w-full max-w-4xl glass-panel rounded-2xl p-8 shadow-2xl mb-12">
        <header class="mb-8 border-b border-slate-700 pb-6">
            <h1 class="text-4xl font-extrabold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-emerald-400 mb-4">{{{{title}}}}</h1>
            <p class="text-xl text-slate-300">{{{{desc}}}}</p>
        </header>
        
        <article class="prose prose-invert max-w-none text-slate-300 leading-relaxed text-lg">
            {{{{content}}}}
        </article>
        
        <div class="mt-12 pt-8 border-t border-slate-700 flex flex-col sm:flex-row items-center justify-between">
            <p class="text-slate-400 mb-4 sm:mb-0">Want to see the code?</p>
            <a href="https://github.com/AakashGs10/{{{{repo_name}}}}" target="_blank" class="px-6 py-3 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white rounded-lg font-bold transition-all shadow-lg hover:shadow-blue-500/25 flex items-center gap-2">
                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"></path></svg>
                View Repository
            </a>
        </div>
    </main>
    <footer class="mt-auto pb-6 text-slate-500 text-sm">
        &copy; 2026 Aakash G S. All rights reserved.
    </footer>
</body>
</html>
'''

for id, details in projects.items():
    safe_name = id.lower().replace(' ', '-').replace('_', '-')
    filename = f"{safe_name}.html"
    
    if id.startswith('0'):
        repo_link = f"COLLEGE-PROJECTS/tree/main/{id}"
    else:
        repo_link = id
        
    post_html = html_template.replace('{{title}}', details['name'])\
                             .replace('{{desc}}', details['desc'])\
                             .replace('{{content}}', details['content'])\
                             .replace('{{repo_name}}', repo_link)
    
    with open(os.path.join(blog_dir, filename), 'w', encoding='utf-8') as f:
        f.write(post_html)

print("Rich detail blogs generated.")
