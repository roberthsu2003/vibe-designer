# 第 9 堂：包裝模擬 - 3D Mockup 與刀模

- **主題**：包裝展開圖與 3D 貼圖
- **工具**：AI 紋理生成 + Affinity Designer (刀模) + Photo (Mockup)
- **重點方向**：
    - **刀模認識**：理解出血 (Bleed)、裁切線 (Crop Marks) 與摺線 (Fold Lines) 的標準標示。
    - **連續圖樣**：使用 AI 生成無縫紋理 (Seamless Pattern) 應用於包裝紙設計。
    - **Mockup 合成**：將平面設計貼合到 3D 物體表面，模擬真實光影與曲面變形。
- **實作產出**：一組產品包裝設計圖 (含平面展開圖與 3D 模擬圖)。

## 雙軌實戰任務 (Dual-Track Specs)
#### **第 9 堂：包裝模擬 - 3D Mockup 與刀模**

- **學習主軸**：AI 生成無縫紋理 + Affinity 刀模繪製。
- **【主題 A：電競滑鼠/能量飲】**
    - **風格**：**金屬質感 (Metallic/Carbon Fiber)** - 碳纖維、髮絲紋、雷射光。
    - **包裝**：硬盒或鋁罐。
    - **參考文案內容 (Reference Copy)**：
        - **產品名稱**：HYPER ENERGY
        - **Slogan**：Unlock Your Potential
        - **成分標示**：Taurine, B-Vitamins, Caffeine.
        - **容量**：330ml / 11.15 fl oz
    - **Prompt 進階三部曲 (由淺入深)**：
        1. **Lv1 (基礎)**：
            ```prompt
            碳纖維紋理，深色，留白 (Carbon fiber texture, dark, copy space)
            ```
        2. **Lv2 (中階)**：
            ```prompt
            無縫碳纖維紋理，黑與灰，金屬表面，乾淨表面 (Seamless carbon fiber texture, black and grey, metallic finish, clean surface)
            ```
        3. **Lv3 (高階)**：
            ```prompt
            [主體] 未來感六角形蜂巢圖案
            [環境] 深色金屬背景，邊緣帶有發光霓虹線條
            [構圖] 無縫紋理 (Seamless texture)，均勻分佈，中央設有乾淨區域供 Logo 放置與產品資訊排版
            [文字配置] 產品名稱「ENERGY X」置於中央乾淨區域，粗體斜體無襯線字體 (Bold Italic Sans-serif)，金屬銀色，成分標示置於下方，小字體
            [風格] 科技裝甲風格，運動感，陽剛
            [參數] 8k 高解析度，材質細節清晰
            (Subject: Futuristic hexagonal honeycomb pattern, Environment: Dark metallic background, glowing neon lines on edges, Layout: Seamless texture, evenly distributed, clean area in center for Logo placement and product info, Text Layout: Product name 'ENERGY X' placed in central clean area, bold italic sans-serif, metallic silver, ingredients below, small font, Style: Tech armor style, sporty, masculine, Parameters: 8k resolution, clear material details)
            ```
    - **範例作品**：
      ![Theme A Example](assets/theme_a.png)
- **【主題 B：茶葉禮盒/手工果醬】**
    - **風格**：**和風/牛皮紙 (Washi/Kraft Paper)** - 粗糙感、燙金、傳統紋樣。
    - **包裝**：紙盒或玻璃瓶標籤。
    - **參考文案內容 (Reference Copy)**：
        - **產品名稱**：京都の春 (Kyoto Spring)
        - **Slogan**：Handmade with Care
        - **成分標示**：Organic Strawberries, Cane Sugar, Lemon Juice.
        - **重量**：200g / 7oz
    - **Prompt 進階三部曲 (由淺入深)**：
        1. **Lv1 (基礎)**：
            ```prompt
            日本紙紋理，淺色，留白 (Japanese paper texture, light color, copy space)
            ```
        2. **Lv2 (中階)**：
            ```prompt
            無縫日本傳統圖案，櫻花，粉紅與白，柔和紋理 (Seamless japanese traditional pattern, cherry blossoms, pink and white, soft texture)
            ```
        3. **Lv3 (高階)**：
            ```prompt
            [主體] 復古植物插畫與花卉圖案
            [環境] 柔和粉彩色的紙張質感
            [構圖] 無縫連續圖案 (Seamless pattern)，花卉疏密有致，預留乾淨空間供產品標籤 (Label) 貼合
            [文字配置] 產品名稱「SWEET JAM」置於標籤區域，手寫書法字體 (Calligraphy)，深紅色，口味標示「Organic Strawberries」置於下方，簡約字體
            [風格] 優雅水彩風，高品質印刷質感，日式清新
            [參數] 輕微紋理，適合包裝設計
            (Subject: Vintage botanical illustration and floral patterns, Environment: Soft pastel paper texture, Layout: Seamless pattern, balanced density of flowers, reserved clean space for product label, Text Layout: Product name 'SWEET JAM' placed in label area, calligraphy font, dark red, flavor 'Organic Strawberries' below, simple font, Style: Elegant watercolor, high quality print texture, Japanese fresh style, Parameters: Light texture, suitable for packaging design)
            ```
    - **範例作品**：
      ![Theme B Example](assets/theme_b.png)