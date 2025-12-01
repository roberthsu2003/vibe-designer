import os
import re
import json

def extract_prompts():
    prompts = {}
    
    for i in range(1, 13):
        week_dir = f"Week_{i:02d}"
        readme_path = os.path.join(week_dir, "README.md")
        assets_dir = os.path.join(week_dir, "assets")
        
        # Create assets directory if it doesn't exist
        if not os.path.exists(assets_dir):
            os.makedirs(assets_dir)
            print(f"Created {assets_dir}")
            
        if os.path.exists(readme_path):
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find Theme A Lv3 Prompt
            # Pattern: **【主題 A.*?Lv3 \(高階\) \*\*：`(.*?)`
            # Note: The structure is roughly:
            # - **【主題 A...】**
            # ...
            # 3. **Lv3 (高階)**：`PROMPT`
            
            # We need to be careful about capturing the right prompt for Theme A vs Theme B
            # Let's split by Theme A and Theme B sections first
            
            parts = re.split(r'\*\*【主題 [AB]', content)
            # parts[0] is header
            # parts[1] is Theme A (usually)
            # parts[2] is Theme B (usually)
            
            week_prompts = {}
            
            if len(parts) >= 3:
                # Theme A is likely in parts[1]
                match_a = re.search(r'3\. \*\*Lv3 \(高階\)\*\*：`(.*?)`', parts[1])
                if match_a:
                    week_prompts['A'] = match_a.group(1)
                
                # Theme B is likely in parts[2]
                match_b = re.search(r'3\. \*\*Lv3 \(高階\)\*\*：`(.*?)`', parts[2])
                if match_b:
                    week_prompts['B'] = match_b.group(1)
            
            prompts[week_dir] = week_prompts
            
    return prompts

if __name__ == "__main__":
    all_prompts = extract_prompts()
    print(json.dumps(all_prompts, indent=2, ensure_ascii=False))
