import os
import re

def main():
    readme_path = 'README.md'
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find week sections
    # Pattern looks for #### **第 X 堂：Title**
    pattern = re.compile(r'#### \*\*第 (\d+) 堂：(.*?)\*\*(.*?)(?=#### \*\*第|\n### |$)', re.DOTALL)
    
    matches = pattern.findall(content)
    
    links = []

    for week_num, title, body in matches:
        week_dir = f"Week_{int(week_num):02d}"
        
        # Create directory
        if not os.path.exists(week_dir):
            os.makedirs(week_dir)
            print(f"Created directory: {week_dir}")
        
        # Prepare README content
        week_title = f"第 {week_num} 堂：{title.strip()}"
        readme_content = f"# {week_title}\n\n{body.strip()}\n"
        
        # Write README.md
        with open(os.path.join(week_dir, 'README.md'), 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        print(f"Created {week_dir}/README.md")

if __name__ == "__main__":
    main()
