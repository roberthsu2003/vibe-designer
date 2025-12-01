import os

def main():
    # Define the new content for each week based on the user's request
    week_contents = {
        'Week_01': {
            'title': '第 1 堂：零成本設計概論 - 個人名片設計',
            'content': """
#### **第 1 堂：零成本設計概論 - 個人名片設計**

- **學習主軸**：AI 生成抽象背景 + Affinity 文字排版。
- **【主題 A：AI 科技顧問】**
    - **風格**：**科技極簡 (Tech Minimalist)** - 藍光、線條、幾何。
    - **Prompt (英)**：`Abstract technology background, circuit board lines, neon blue and white gradient, minimalist style, 8k.`
    - **Prompt (中)**：`抽象科技背景，電路板線條，霓虹藍白漸層，極簡風格，8k 高解析度。`
- **【主題 B：花藝/甜點師】**
    - **風格**：**莫蘭迪色調 (Morandi/Soft)** - 水彩、暈染、柔和。
    - **Prompt (英)**：`Abstract watercolor background, soft pastel colors, floral shapes, artistic texture, elegant vibe, clean space.`
    - **Prompt (中)**：`抽象水彩背景，柔和粉彩，花卉形狀，藝術紋理，優雅氛圍，乾淨留白。`
"""
        },
        'Week_02': {
            'title': '第 2 堂：社群貼文 - 節慶促銷輪播圖 (Carousel)',
            'content': """
#### **第 2 堂：社群貼文 - 節慶促銷輪播圖 (Carousel)**

- **學習主軸**：Ideogram 生字圖 + Canva 快速排版。
- **【主題 A：3C 產品/電競週邊特賣】**
    - **風格**：**故障藝術 (Glitch Art)** - 賽博龐克、高對比、霓虹。
    - **規格**：主標題「CYBER WEEK」、黑底亮色。
    - **Prompt (英)**：`Poster design, "CYBER WEEK" text in glitch font, neon green and purple, cyberpunk city background, high contrast.`
    - **Prompt (中)**：`海報設計，"CYBER WEEK"文字採用故障藝術字體，霓虹綠與紫，賽博龐克城市背景，高對比度。`
- **【主題 B：小農市集/季節水果祭】**
    - **風格**：**拼貼手帳風 (Scrapbook/Collage)** - 暖色調、紙質感。
    - **規格**：主標題「Summer Market」、米白底色。
    - **Prompt (英)**：`Poster design, "Summer Market" text in hand-drawn font, fresh fruits, paper texture background, cute stickers style.`
    - **Prompt (中)**：`海報設計，"Summer Market"文字採用手繪字體，新鮮水果，紙張紋理背景，可愛貼紙風格。`
"""
        },
        'Week_03': {
            'title': '第 3 堂：商品情境 - 虛擬攝影棚合成',
            'content': """
#### **第 3 堂：商品情境 - 虛擬攝影棚合成**

- **學習主軸**：Microsoft Designer 生成背景 + Affinity 精細去背與光影。
- **【主題 A：無線耳機/智能手錶】**
    - **場景**：**懸浮實驗室 (Levitating Lab)** - 科技感展台、冷光。
    - **Prompt (英)**：`Product photography background, a futuristic white podium floating in the air, blue laser lights, clean studio lighting, high tech vibe.`
    - **Prompt (中)**：`產品攝影背景，懸浮在空中的未來感白色展台，藍色雷射光，乾淨的攝影棚燈光，高科技氛圍。`
- **【主題 B：精油/保養品】**
    - **場景**：**自然岩石與水 (Nature & Water)** - 陽光、水波紋、石頭。
    - **Prompt (英)**：`Product photography background, a natural stone platform in shallow water, ripples, sunlight dappled, zen garden vibe, organic.`
    - **Prompt (中)**：`產品攝影背景，淺水中的天然石台，漣漪，陽光灑落（斑駁光影），枯山水庭園氛圍，有機感。`
"""
        },
        'Week_04': {
            'title': '第 4 堂：菜單設計 - 視覺味蕾行銷',
            'content': """
#### **第 4 堂：菜單設計 - 視覺味蕾行銷**

- **學習主軸**：AI 食物生成 + Affinity 表格與對齊。
- **【主題 A：美式漢堡/炸雞店】**
    - **風格**：**美式復古 (American Retro)** - 粗體字、高飽和紅黃配色。
    - **Prompt (英)**：`Delicious fried chicken bucket, exploding crispy crumbs, pop art style background, vibrant red and yellow, close up.`
    - **Prompt (中)**：`美味炸雞桶，炸裂的酥脆麵衣，波普藝術風格背景，鮮豔紅黃配色，特寫。`
- **【主題 B：日式定食/咖啡廳】**
    - **風格**：**日式極簡 (Japanese Zen)** - 留白、直排文字、低飽和度。
    - **Prompt (英)**：`Japanese set meal, grilled fish, rice and miso soup, wooden tray, soft natural lighting, minimal composition, kinfolk style.`
    - **Prompt (中)**：`日式定食，烤魚，米飯與味噌湯，木托盤，柔和自然光，極簡構圖，Kinfolk 生活風格。`
"""
        },
        'Week_05': {
            'title': '第 5 堂：海報設計 - 風格強烈的視覺衝擊',
            'content': """
#### **第 5 堂：海報設計 - 風格強烈的視覺衝擊**

- **學習主軸**：Recraft/Midjourney 風格模仿 + 特效字體。
- **【主題 A：電子音樂祭 (EDM Festival)】**
    - **風格**：**酸性設計 (Acid Graphics)** - 液態金屬、雷射光、扭曲文字。
    - **Prompt (英)**：`Abstract 3D liquid metal shapes, iridescent chrome texture, dark background, futuristic typography layout, acid graphics style.`
    - **Prompt (中)**：`抽象 3D 液態金屬形狀，虹彩鍍鉻質感，深色背景，未來感排版，酸性設計風格。`
- **【主題 B：手作藝術節 (Art Craft Fair)】**
    - **風格**：**孔版印刷 (Riso Print)** - 顆粒感、錯位疊色、復古。
    - **Prompt (英)**：`Risograph print style illustration, whimsical characters playing music, grainy texture, overlapping colors (blue and orange), vintage poster.`
    - **Prompt (中)**：`孔版印刷風格插畫，演奏音樂的奇幻角色，顆粒紋理，疊色效果（藍與橘），復古海報。`
"""
        },
        'Week_06': {
            'title': '第 6 堂：懶人包與圖表 - 讓 AI 畫圖標',
            'content': """
#### **第 6 堂：懶人包與圖表 - 讓 AI 畫圖標**

- **學習主軸**：Recraft 生成一致性 Icon + Napkin.ai 流程圖。
- **【主題 A：區塊鏈/AI 運作原理】**
    - **風格**：**玻璃擬態 (Glassmorphism)** - 半透明、模糊背景。
    - **Prompt (英/Recraft)**：`Vector icon set, blockchain, chip, network, lock, glassmorphism style, frosted glass effect, blue gradient.`
    - **Prompt (中)**：`向量圖標組，區塊鏈，晶片，網絡，鎖，玻璃擬態風格，磨砂玻璃效果，藍色漸層。`
- **【主題 B：手沖咖啡/瑜珈步驟】**
    - **風格**：**線條手繪 (Line Art)** - 鉛筆觸感、單色。
    - **Prompt (英/Recraft)**：`Vector icon set, coffee bean, kettle, cup, dripper, continuous line art, black outline on white, minimal.`
    - **Prompt (中)**：`向量圖標組，咖啡豆，手沖壺，杯子，濾杯，一筆畫線條藝術（連續線），白底黑線，極簡。`
"""
        },
        'Week_07': {
            'title': '第 7 堂：品牌 Logo - 向量化實戰',
            'content': """
#### **第 7 堂：品牌 Logo - 向量化實戰**

- **學習主軸**：Ideogram 發想 + Vectorizer 轉檔 + Affinity 節點修整。
- **【主題 A：新創 App 圖示】**
    - **風格**：**漸層幾何 (Gradient Geometric)** - 圓角、鮮豔漸層。
    - **Prompt (英)**：`App icon design, abstract letter "S", gradient colors (purple to orange), rounded corners, glossy finish, modern tech style.`
    - **Prompt (中)**：`App 圖示設計，抽象字母 "S"，漸層色（紫到橘），圓角，光澤表面，現代科技風格。`
- **【主題 B：手工烘焙坊商標】**
    - **風格**：**徽章式 (Emblem/Vintage)** - 圓形外框、襯線體。
    - **Prompt (英)**：`Vintage logo design for a bakery, wheat and rolling pin illustration, circle layout, monochrome, woodcut style.`
    - **Prompt (中)**：`麵包店復古 Logo 設計，小麥與桿麵棍插畫，圓形排版，單色，木刻版畫風格。`
"""
        },
        'Week_08': {
            'title': '第 8 堂：DM 摺頁 - 長文案排版',
            'content': """
#### **第 8 堂：DM 摺頁 - 長文案排版**

- **學習主軸**：Gemini 縮寫文案 + Affinity Publisher 欄位設定 + 出血。
- **【主題 A：智慧家電型錄】**
    - **風格**：**瑞士國際主義 (Swiss Style)** - 網格系統、Helvetica 字體、客觀冷靜。
    - **內容**：介紹掃地機器人、智慧音箱功能。
    - **Prompt (英/底紋)**：`Abstract geometric pattern, swiss style, minimal, grey and white.`
    - **Prompt (中)**：`抽象幾何圖樣，瑞士風格，極簡，灰白配色。`
- **【主題 B：豪華露營區簡介】**
    - **風格**：**雜誌排版 (Magazine Style)** - 滿版大圖、優雅字體、留白。
    - **內容**：介紹營區設施、BBQ 菜單、星空導覽。
    - **Prompt (英/底紋)**：`Paper texture, beige, subtle grain, minimal background.`
    - **Prompt (中)**：`紙張紋理，米色，細微顆粒，極簡背景。`
"""
        },
        'Week_09': {
            'title': '第 9 堂：包裝模擬 - 3D Mockup',
            'content': """
#### **第 9 堂：包裝模擬 - 3D Mockup**

- **學習主軸**：Leonardo 生成材質紋理 + Affinity 刀模 + Canva Mockup。
- **【主題 A：能量飲料/機能補給品】**
    - **材質**：**霧面金屬 (Matte Metallic)**。
    - **Prompt (英)**：`Brushed aluminum texture, dark grey, seamless pattern.`
    - **Prompt (中)**：`髮絲紋鋁金屬材質，深灰色，無縫圖樣。`
- **【主題 B：有機花茶/手工皂】**
    - **材質**：**再生牛皮紙 (Kraft Paper)**。
    - **Prompt (英)**：`Recycled kraft paper texture, beige color, botanical line drawing pattern.`
    - **Prompt (中)**：`再生牛皮紙材質，米色，植物線條畫圖樣。`
"""
        },
        'Week_10': {
            'title': '第 10 堂：大型輸出 - 解析度救星',
            'content': """
#### **第 10 堂：大型輸出 - 解析度救星**

- **學習主軸**：AI Upscaler 放大圖片 + CMYK 印刷色檢視。
- **【主題 A：科技展覽攤位背板】**
    - **重點**：深邃的黑色不能有色塊 (Banding)，文字要極其銳利。
    - **畫面**：AI 虛擬模特兒戴著 VR 眼鏡。
    - **Prompt (英)**：`Futuristic VR gamer, wearing headset, neon lights reflection, dark background, cyberpunk, 8k resolution.`
    - **Prompt (中)**：`未來感 VR 玩家，戴著頭戴式裝置，霓虹燈反射，深色背景，賽博龐克，8k 高解析度。`
- **【主題 B：文創市集攤位掛布】**
    - **重點**：布料印刷的色彩飽和度控制。
    - **畫面**：溫馨的插畫全家福或寵物插畫。
    - **Prompt (英)**：`Family portrait illustration, warm colors, happy vibe, cute dog, flat design, soft lighting.`
    - **Prompt (中)**：`全家福插畫，暖色調，快樂氛圍，可愛的狗，扁平設計，柔和光線。`
"""
        },
        'Week_11': {
            'title': '第 11 堂：整合行銷戰役 (Capstone Project)',
            'content': """
#### **第 11 堂：整合行銷戰役 (Capstone Project)**

- **任務**：各組選定一個自創品牌（可延續前面週次的主題），完成全套設計。
- **【Option A：創立一個 Tech Brand】**
    - 產出：Logo + App Store 預覽圖 + 發表會背板。
- **【Option B：創立一個 Lifestyle Brand】**
    - 產出：Logo + IG 經營排版 (9宮格) + 實體店面招牌模擬。
"""
        },
        'Week_12': {
            'title': '第 12 堂：Vibe Design 成果發表會',
            'content': """
#### **第 12 堂：Vibe Design 成果發表會**

- **雙軌評分標準**：
    - **選 A 組**：評分重點在於「現代感」、「資訊清晰度」、「創新性」。
    - **選 B 組**：評分重點在於「溫度感」、「故事性」、「視覺舒適度」。
"""
        }
    }

    # Iterate through each week and update the README.md
    for week_dir, data in week_contents.items():
        readme_path = os.path.join(week_dir, 'README.md')
        
        # Read existing content to keep the header, but replace the "Practical Specs" section
        if os.path.exists(readme_path):
            with open(readme_path, 'r', encoding='utf-8') as f:
                existing_content = f.read()
            
            # Split content to remove old specs if present
            # We look for "## 實戰任務規格" and keep everything before it
            parts = existing_content.split("## 實戰任務規格 (Practical Specs)")
            base_content = parts[0].strip()
        else:
            base_content = f"# {data['title']}"

        # Combine base content with new dual-track content
        new_content = base_content + "\n\n## 雙軌實戰任務 (Dual-Track Specs)\n" + data['content'].strip()
        
        # Write back to file
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Updated {readme_path}")

if __name__ == "__main__":
    main()
