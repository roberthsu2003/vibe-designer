import os
import re

def main():
    # Define the content for each week based on the user's request
    week_contents = {
        'Week_01': {
            'title': '第 1 堂：零成本設計概論 - 個人名片設計',
            'content': """
#### **第 1 堂：零成本設計概論 - 個人名片設計**

- **【指定規格 (Specs)】**：
    - **尺寸**：90mm x 54mm (橫式)
    - **必須資訊**：姓名、職稱 (如: AI 設計師)、電話、Email、一句個人 Slogan。
    - **圖片需求**：一張代表個人風格的「抽象背景」或「AI 虛擬形象」。
- **【建議風格 (Style)】**：**科技極簡風 (Tech Minimalist)** - 大量留白、冷色調、幾何線條。
- **【AI 詠唱範例 (Prompt)】**：
    - *背景*：`Abstract geometric background, blue and white gradient, tech lines, minimalist style, high quality, 8k resolution. (抽象幾何背景，藍白漸層，科技線條，極簡風格)`
- **【當週重點角色】**：**視覺組裝師** (需熟悉 Affinity 文字排版與出血設定)。
"""
        },
        'Week_02': {
            'title': '第 2 堂：社群貼文 - 節慶促銷輪播圖',
            'content': """
#### **第 2 堂：社群貼文 - 節慶促銷輪播圖**

- **【指定規格 (Specs)】**：
    - **尺寸**：1080 x 1080px (方形)，共 3 張 (Carousel)。
    - **P1 封面**：主標題「夏季大清倉」、副標題「全館 5 折起」。
    - **P2 亮點**：條列 3 個賣點 (免運、快速出貨、限量)。
    - **P3 結尾**：行動呼籲「立即搶購」、Logo。
- **【建議風格 (Style)】**：**孟菲斯風格 (Memphis Style)** - 高飽和度配色、波點、幾何圖形拼貼，活潑熱鬧。
- **【AI 詠唱範例 (Prompt)】**：
    - *主圖*：`Pop art style, summer sale background, bright colors, confetti, geometric shapes, Memphis design pattern, happy vibe. (波普藝術風格，夏季促銷背景，鮮豔色彩，紙花，幾何形狀，孟菲斯設計圖樣)`
    - *Ideogram (生字)*：`A poster with text "SUMMER SALE" in bold colorful font, Memphis style background.`
- **【當週重點角色】**：**自然語言溝通師** (需用 Ideogram 生成正確文字圖像)。
"""
        },
        'Week_03': {
            'title': '第 3 堂：商品情境 - 虛擬攝影棚合成',
            'content': """
#### **第 3 堂：商品情境 - 虛擬攝影棚合成**

- **【指定規格 (Specs)】**：
    - **商品**：(學生自備一張手機拍的產品照，如保溫瓶或球鞋，需去背)。
    - **背景**：AI 生成的虛擬場景，不可以有其他人或雜亂物體。
    - **光影**：產品必須有正確的投影 (Drop Shadow)。
- **【建議風格 (Style)】**：**自然系/森系 (Nature/Organic)** - 陽光、樹葉倒影、木質紋理。
- **【AI 詠唱範例 (Prompt)】**：
    - *場景*：`Product photography background, a wooden podium in the middle of a forest, sunlight filtering through leaves (dappled light), bokeh background, cinematic lighting, photorealistic. (產品攝影背景，森林中的木質展台，陽光透過樹葉灑落（斑駁光影），背景虛化，電影級光效)`
- **【當週重點角色】**：**素材獵人** (需生成完美的空景)、**視覺組裝師** (Affinity 精細去背與調光)。
"""
        },
        'Week_04': {
            'title': '第 4 堂：菜單設計 - 視覺味蕾行銷',
            'content': """
#### **第 4 堂：菜單設計 - 視覺味蕾行銷**

- **【指定規格 (Specs)】**：
    - **版面**：A4 單頁。
    - **內容**：店名、3 道主打菜 (每道需有圖+菜名+價格+一句口感描述)。
    - **限制**：AI 生成的食物必須看起來「超好吃」。
- **【建議風格 (Style)】**：**日式禪風 (Japanese Zen)** 或 **美式復古 (American Retro)**。
- **【AI 詠唱範例 (Prompt)】**：
    - *食物*：`Top-down view of a delicious Wagyu beef burger, melting cheese, steam rising, professional food photography, dark moody background, high details, 8k. (俯視美味和牛漢堡，融化的起司，熱氣騰騰，專業食物攝影，深色氛圍背景)`
- **【當週重點角色】**：**專案總監** (決定要開什麼店、什麼風格)。
"""
        },
        'Week_05': {
            'title': '第 5 堂：海報設計 - 風格強烈的視覺衝擊',
            'content': """
#### **第 5 堂：海報設計 - 風格強烈的視覺衝擊**

- **【指定規格 (Specs)】**：
    - **主題**：音樂祭 / 藝術展 / 電影節 (三選一)。
    - **資訊**：活動名稱 (佔版面 1/3)、日期、地點、嘉賓名單。
    - **視覺**：必須是「插畫」或「藝術風格」，不能是照片。
- **【建議風格 (Style)】**：**賽博龐克 (Cyberpunk)** 或 **浮世繪 (Ukiyo-e)**。
- **【AI 詠唱範例 (Prompt)】**：
    - *主視覺*：`Cyberpunk city street at night, neon lights, futuristic geisha robot, rain, reflection, vibrant pink and blue colors, anime style illustration. (夜晚的賽博龐克街道，霓虹燈，未來藝妓機器人，雨，倒影，鮮豔的粉紅與藍色，動漫風格插畫)`
- **【當週重點角色】**：**視覺組裝師** (Affinity 特效字體設計)。
"""
        },
        'Week_06': {
            'title': '第 6 堂：懶人包與圖表 - 讓 AI 畫圖標',
            'content': """
#### **第 6 堂：懶人包與圖表 - 讓 AI 畫圖標**

- **【指定規格 (Specs)】**：
    - **主題**：「如何使用 AI 的 4 個步驟」。
    - **結構**：標題 + 4 個 Icon + 4 段說明文字。
    - **統一性**：4 個 Icon 的線條粗細、風格、顏色必須一致。
- **【建議風格 (Style)】**：**扁平化設計 (Flat Design)** 或 **手繪線條 (Hand-drawn Line Art)**。
- **【AI 詠唱範例 (Prompt)】**：
    - *圖標 (Recraft.ai)*：`Vector icon set, a robot head, a light bulb, a pencil, a computer, flat design, minimal, blue and yellow colors, white background. (向量圖標組，機器人頭，燈泡，鉛筆，電腦，扁平設計，極簡，藍黃配色)`
- **【當週重點角色】**：**素材獵人** (使用 Recraft 生成統一風格素材)。
"""
        },
        'Week_07': {
            'title': '第 7 堂：品牌 Logo - 向量化實戰',
            'content': """
#### **第 7 堂：品牌 Logo - 向量化實戰**

- **【指定規格 (Specs)】**：
    - **產出**：一個圖形 Logo + 品牌標準字 + 黑白稿 + 3 色配色規範。
    - **格式**：必須是向量檔 (SVG)，節點乾淨。
- **【建議風格 (Style)】**：**幾何圖形 (Geometric)** 或 **負空間設計 (Negative Space)**。
- **【AI 詠唱範例 (Prompt)】**：
    - *發想*：`Vector logo design for a coffee shop, minimal line art of a coffee bean combined with a cat, black lines on white background, flat, simple. (咖啡店向量 Logo 設計，咖啡豆與貓結合的極簡線條藝術，白底黑線，扁平，簡單)`
- **【當週重點角色】**：**視覺組裝師** (Affinity Node Tool 節點修整)。
"""
        },
        'Week_08': {
            'title': '第 8 堂：DM 摺頁 - 長文案排版',
            'content': """
#### **第 8 堂：DM 摺頁 - 長文案排版**

- **【指定規格 (Specs)】**：
    - **形式**：A4 三摺頁 (Tri-fold)。
    - **封面**：吸睛標題 + 主圖。
    - **內頁**：品牌故事 (約 200 字)、產品介紹、聯絡資訊。
    - **印刷設定**：需設定 3mm 出血。
- **【建議風格 (Style)】**：**瑞士風格 (Swiss Style)** - 強調網格系統、無襯線字體、清晰排版。
- **【AI 詠唱範例 (Prompt)】**：
    - *底紋*：`Abstract watercolor texture, soft pastel colors, pink and blue, paper texture, minimal background for brochure. (抽象水彩紋理，柔和粉彩，粉紅與藍，紙張紋理，手冊用的極簡背景)`
- **【當週重點角色】**：**商業敘事者** (使用 Gemini 縮寫長文案)。
"""
        },
        'Week_09': {
            'title': '第 9 堂：包裝模擬 - 3D Mockup',
            'content': """
#### **第 9 堂：包裝模擬 - 3D Mockup**

- **【指定規格 (Specs)】**：
    - **產品**：咖啡豆袋 或 餅乾盒。
    - **內容**：Logo、口味名稱 (如: 頂級深焙)、淨重、營養標示。
    - **材質**：需展現特殊材質感 (如牛皮紙、鋁箔)。
- **【建議風格 (Style)】**：**有機環保 (Organic/Eco)** 或 **奢華黑金 (Luxury Black)**。
- **【AI 詠唱範例 (Prompt)】**：
    - *材質圖*：`Seamless texture of crumpled kraft paper, realistic details. (無縫皺褶牛皮紙紋理，真實細節)`
    - *圖樣*：`Seamless pattern of coffee leaves, green line art. (咖啡葉無縫圖樣，綠色線條)`
- **【當週重點角色】**：**素材獵人** (生成無縫紋理)。
"""
        },
        'Week_10': {
            'title': '第 10 堂：大型輸出 - 解析度救星',
            'content': """
#### **第 10 堂：大型輸出 - 解析度救星**

- **【指定規格 (Specs)】**：
    - **尺寸**：易拉展 80cm x 200cm。
    - **內容**：超大主標題 (遠處可見)、主視覺圖、QR Code。
    - **品質**：放大檢視後，圖片不得有鋸齒或模糊。
- **【建議風格 (Style)】**：**高對比撞色 (High Contrast)** - 為了遠距離吸睛。
- **【AI 詠唱範例 (Prompt)】**：
    - *人像*：`Close up portrait of a happy young woman holding a phone, laughing, bright solid yellow background, advertising photography, high resolution. (快樂年輕女子拿著手機特寫，大笑，明亮純黃背景，廣告攝影，高解析度)`
- **【當週重點角色】**：**專案總監** (檢查解析度與印刷風險)。
"""
        },
        'Week_11': {
            'title': '第 11 堂：整合行銷戰役 (Capstone Project)',
            'content': """
#### **第 11 堂：整合行銷戰役 (Capstone Project)**

- **【指定規格 (Specs)】**：
    - **主題自訂**：創立一個虛擬品牌。
    - **產出清單**：
        1. 品牌 Logo。
        2. 社群宣傳圖 x 3。
        3. 實體活動海報 x 1。
- **【要求】**：所有產出的風格 (Vibe) 必須高度一致。
- **【當週重點角色】**：**全員出動** (流水線分工)。
"""
        },
        'Week_12': {
            'title': '第 12 堂：Vibe Design 成果發表會',
            'content': """
#### **第 12 堂：Vibe Design 成果發表會**

- **【任務】**：每組 15 分鐘提案。
- **【簡報結構】**：
    1. **Who**: 我們是誰？賣什麼？
    2. **Why**: 為什麼選這個 Vibe？(Prompt 策略分享)
    3. **How**: 零成本工作流展示 (Affinity 圖層解析)。
    4. **Show**: 最終成品展示。
"""
        }
    }

    # Iterate through each week and update the README.md
    for week_dir, data in week_contents.items():
        readme_path = os.path.join(week_dir, 'README.md')
        
        # Read existing content
        if os.path.exists(readme_path):
            with open(readme_path, 'r', encoding='utf-8') as f:
                existing_content = f.read()
        else:
            existing_content = f"# {data['title']}\n"

        # Append the new content
        new_content = existing_content + "\n\n## 實戰任務規格 (Practical Specs)\n" + data['content'].strip()
        
        # Write back to file
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Updated {readme_path}")

if __name__ == "__main__":
    main()
