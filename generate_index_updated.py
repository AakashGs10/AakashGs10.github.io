import os

projects = {
    'cloudguard-ai': {
        'name': 'CloudGuard AI',
        'desc': 'An advanced AI-powered cloud security platform designed to detect and mitigate threats in cloud infrastructure.'
    },
    'ebpf-firewall': {
        'name': 'eBPF XDP Firewall',
        'desc': 'High-performance, kernel-level network firewall built with eBPF/XDP for real-time packet inspection.'
    },
    'Morse_code_translation': {
        'name': 'Morse Code Translator',
        'desc': 'A utility tool for encoding and decoding Morse code, providing instant translation.'
    },
    'POSE-DETECTION': {
        'name': 'Pose Detection System',
        'desc': 'Computer vision project utilizing machine learning models to detect human poses in real-time.'
    },
    '01_SignalKey_IoT_Security': {
        'name': 'SignalKey IoT Security',
        'desc': 'A security framework for IoT devices focusing on signal-based authentication.'
    },
    '02_Fake_Job_Posting_Detection': {
        'name': 'Fake Job Posting Detection',
        'desc': 'An explainable machine learning framework for detecting fraudulent job postings.'
    }
}

blog_dir = '.'

adsense_code = '''
<!-- Google AdSense -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9233292105405086" crossorigin="anonymous"></script>
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
    
    # Add to index grid
    project_list_html += f'''
    <a href="{filename}" class="glass-card rounded-xl p-6 flex flex-col h-full cursor-pointer block group relative overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-br from-blue-500/10 to-emerald-500/10 opacity-0 group-hover:opacity-100 transition-opacity"></div>
        <h3 class="text-2xl font-semibold text-slate-100 mb-3 group-hover:text-blue-400 transition-colors">{details['name']}</h3>
        <p class="text-slate-400 flex-grow text-sm leading-relaxed">{details['desc']}</p>
        <div class="mt-6 flex items-center text-emerald-400 text-sm font-medium">
            Read Detailed Review <svg class="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
        </div>
    </a>
    '''

# Create index.html
index_html = index_template.replace('{{project_list}}', project_list_html)
with open(os.path.join(blog_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(index_html)
