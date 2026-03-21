import os
import re

# Sidebar estándar para páginas en subdirectorios (../)
SIDEBAR_SUBDIR = '''<ul class="nav-menu">
            <li class="nav-item" onclick="window.location.href='../index.html'">
                <span class="nav-icon">📊</span>
                <span>Dashboard</span>
            </li>
            <li class="nav-item" onclick="window.location.href='../ranking/index.html'">
                <span class="nav-icon">📋</span>
                <span>Ranking</span>
            </li>
            <li class="nav-item" onclick="window.location.href='../ecuador/index.html'">
                <span class="nav-icon">🇪🇨</span>
                <span>Ecuador</span>
            </li>
            <li class="nav-item" onclick="window.location.href='../peru/index.html'">
                <span class="nav-icon">🇵🇪</span>
                <span>Peru</span>
            </li>
            <li class="nav-item" onclick="window.location.href='../colombia/index.html'">
                <span class="nav-icon">🇨🇴</span>
                <span>Colombia</span>
            </li>
            <li class="nav-item" onclick="window.location.href='../guatemala/index.html'">
                <span class="nav-icon">🇬🇹</span>
                <span>Guatemala</span>
            </li>
            <li class="nav-item" onclick="window.location.href='../panama/index.html'">
                <span class="nav-icon">🇵🇦</span>
                <span>Panamá</span>
            </li>
            <li class="nav-item" onclick="window.location.href='../executives/index.html'">
                <span class="nav-icon">👔</span>
                <span>Executives</span>
            </li>
        </ul>'''

# Sidebar para index.html principal (sin ../)
SIDEBAR_ROOT = '''<ul class="nav-menu">
            <li class="nav-item active">
                <span class="nav-icon">📊</span>
                <span>Dashboard</span>
            </li>
            <li class="nav-item" onclick="window.location.href='ranking/index.html'">
                <span class="nav-icon">📋</span>
                <span>Ranking</span>
            </li>
            <li class="nav-item" onclick="window.location.href='ecuador/index.html'">
                <span class="nav-icon">🇪🇨</span>
                <span>Ecuador</span>
            </li>
            <li class="nav-item" onclick="window.location.href='peru/index.html'">
                <span class="nav-icon">🇵🇪</span>
                <span>Peru</span>
            </li>
            <li class="nav-item" onclick="window.location.href='colombia/index.html'">
                <span class="nav-icon">🇨🇴</span>
                <span>Colombia</span>
            </li>
            <li class="nav-item" onclick="window.location.href='guatemala/index.html'">
                <span class="nav-icon">🇬🇹</span>
                <span>Guatemala</span>
            </li>
            <li class="nav-item" onclick="window.location.href='panama/index.html'">
                <span class="nav-icon">🇵🇦</span>
                <span>Panamá</span>
            </li>
            <li class="nav-item" onclick="window.location.href='executives/index.html'">
                <span class="nav-icon">👔</span>
                <span>Executives</span>
            </li>
        </ul>'''

def get_active_sidebar(filepath, base_sidebar):
    """Mark the current section as active"""
    folder = os.path.dirname(filepath).replace('./', '')
    
    active_map = {
        'ecuador': 'Ecuador',
        'peru': 'Peru', 
        'colombia': 'Colombia',
        'guatemala': 'Guatemala',
        'panama': 'Panamá',
        'executives': 'Executives',
        'ranking': 'Ranking'
    }
    
    if folder in active_map:
        # Remove any existing "active" 
        sidebar = base_sidebar.replace(' active"', '"')
        # Add active to correct item
        target = f'<span>{active_map[folder]}</span>'
        sidebar = sidebar.replace(
            f'class="nav-item" onclick',
            f'class="nav-item" onclick'
        )
        # Find and mark active
        lines = sidebar.split('\n')
        new_lines = []
        for i, line in enumerate(lines):
            if active_map[folder] in line and 'nav-item' in lines[i-1]:
                lines[i-1] = lines[i-1].replace('class="nav-item"', 'class="nav-item active"')
            new_lines.append(lines[i-1] if i > 0 else line)
        new_lines.append(lines[-1])
        
        # Simpler approach - just replace the specific line
        sidebar = sidebar.replace(
            f"onclick=\"window.location.href='../{folder}/index.html'\"",
            f"onclick=\"window.location.href='../{folder}/index.html'\" "
        ).replace('nav-item"', 'nav-item"')
        
        # Mark active based on folder
        if folder == 'ecuador':
            sidebar = sidebar.replace("href='../ecuador/index.html'\">", "href='../ecuador/index.html'\">").replace(
                "nav-item\" onclick=\"window.location.href='../ecuador/",
                "nav-item active\" onclick=\"window.location.href='../ecuador/"
            )
        elif folder == 'peru':
            sidebar = sidebar.replace(
                "nav-item\" onclick=\"window.location.href='../peru/",
                "nav-item active\" onclick=\"window.location.href='../peru/"
            )
        elif folder == 'colombia':
            sidebar = sidebar.replace(
                "nav-item\" onclick=\"window.location.href='../colombia/",
                "nav-item active\" onclick=\"window.location.href='../colombia/"
            )
        elif folder == 'guatemala':
            sidebar = sidebar.replace(
                "nav-item\" onclick=\"window.location.href='../guatemala/",
                "nav-item active\" onclick=\"window.location.href='../guatemala/"
            )
        elif folder == 'panama':
            sidebar = sidebar.replace(
                "nav-item\" onclick=\"window.location.href='../panama/",
                "nav-item active\" onclick=\"window.location.href='../panama/"
            )
        elif folder == 'executives':
            sidebar = sidebar.replace(
                "nav-item\" onclick=\"window.location.href='../executives/",
                "nav-item active\" onclick=\"window.location.href='../executives/"
            )
        elif folder == 'ranking':
            sidebar = sidebar.replace(
                "nav-item\" onclick=\"window.location.href='../ranking/",
                "nav-item active\" onclick=\"window.location.href='../ranking/"
            )
    
    return sidebar

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Determine if root or subdir
    is_root = filepath == './index.html'
    base_sidebar = SIDEBAR_ROOT if is_root else SIDEBAR_SUBDIR
    
    # Get sidebar with active state
    if not is_root:
        sidebar = get_active_sidebar(filepath, base_sidebar)
    else:
        sidebar = base_sidebar
    
    # Pattern to match existing nav-menu
    pattern = r'<ul class="nav-menu">.*?</ul>'
    
    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(pattern, sidebar, content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Process all HTML files
count = 0
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            if update_file(filepath):
                count += 1
                print(f"Updated: {filepath}")
            else:
                print(f"Skipped (no nav-menu): {filepath}")

print(f"\nTotal updated: {count}")
