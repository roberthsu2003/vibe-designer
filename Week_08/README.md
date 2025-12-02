# 第 8 堂：DM 摺頁 - 長文案排版 (Affinity 強項)

- **主題**：多頁面排版與資訊架構
- **工具**：AI 文案生成 + Affinity Publisher
- **重點方向**：
    - **摺頁邏輯**：理解三摺頁 (Tri-fold) 的封面、封底與內頁順序。
    - **樣式設定**：使用 Text Styles (Paragraph/Character Styles) 快速統一長文案格式。
    - **圖文繞排**：讓文字自然地圍繞圖片排列，增加版面活潑度。
- **實作產出**：一份標準 A4 三摺頁 DM。

## 雙軌實戰任務 (Dual-Track Specs)
#### **第 8 堂：DM 摺頁 - 長文案排版**

- **學習主軸**：AI 生成情境圖 + Affinity Publisher 多頁排版。
- **【主題 A：科技產品規格表/軟體介紹】**
    - **風格**：**企業藍 (Corporate Blue)** - 專業、冷靜、資訊密集。
    - **內容**：雲端伺服器規格 / 企業資安方案。
    - **參考文案內容 (Reference Copy)**：
        - **封面標題**：Enterprise Cloud Solutions
        - **內頁標題**：Why Choose Us?
        - **內文段落**：
            1. **High Performance**: 99.9% Uptime SLA.
            2. **Secure**: End-to-end encryption.
            3. **Scalable**: Grow with your business.
        - **聯絡資訊**：www.example.com | 0800-123-456
    - **Prompt 進階三部曲 (由淺入深)**：
        1. **Lv1 (基礎)**：
            ```prompt
            機房背景，留白 (Server room background, copy space)
            ```
        2. **Lv2 (中階)**：
            ```prompt
            抽象科技背景，數據流，藍色調，用於小冊子，乾淨版面 (Abstract technology background, data flow, blue tones, for brochure, clean layout)
            ```
        3. **Lv3 (高階)**：
            ```prompt
            [主體] 抽象的網絡連接線條與數據節點
            [環境] 乾淨明亮的科技空間，柔和藍光
            [構圖] 跨頁構圖 (Spread layout)，視覺引導線從左延伸至右，大面積留白供多段文字排版
            [風格] 企業專業形象，高科技，極簡藍白主題
            [參數] 高解析度，柔焦背景，適合印刷
            (Subject: Abstract network connection lines and data nodes, Environment: Clean bright tech space, soft blue light, Layout: Spread layout, visual leading lines extending from left to right, large negative space for multi-paragraph text, Style: Corporate professional image, high-tech, minimalist blue and white theme, Parameters: High resolution, soft focus background, suitable for print)
            ```
    - **範例作品**：
      ![Theme A Example](assets/theme_a.png)
- **【主題 B：產地故事/旅遊導覽】**
    - **風格**：**雜誌風 (Editorial)** - 大圖、留白、敘事感。
    - **內容**：小農產地直擊 / 京都散策地圖。
    - **參考文案內容 (Reference Copy)**：
        - **封面標題**：Kyoto Travel Guide
        - **內頁標題**：Hidden Gems
        - **內文段落**：探索京都的巷弄，發現不為人知的美好。從古老的寺廟到現代的咖啡館，感受這座城市的獨特魅力。
        - **引言**："Travel is the only thing you buy that makes you richer."
    - **Prompt 進階三部曲 (由淺入深)**：
        1. **Lv1 (基礎)**：
            ```prompt
            茶園風景，留白 (Tea plantation landscape, copy space)
            ```
        2. **Lv2 (中階)**：
            ```prompt
            美麗茶園風景，晨霧，柔和光線，文字空間 (Beautiful tea plantation landscape, morning mist, soft light, space for text)
            ```
        3. **Lv3 (高階)**：
            ```prompt
            [主體] 山中茶園的壯麗景色
            [環境] 清晨陽光穿透薄霧，空氣感十足
            [構圖] 廣角全景 (Wide angle panoramic)，前景清晰，背景模糊 (Bokeh) 適合文字疊加，天空與山嵐留白
            [風格] 旅遊雜誌風格，電影級攝影，自然療癒
            [參數] 8k 解析度，高動態範圍 (HDR)
            (Subject: Magnificent view of mountain tea plantation, Environment: Morning sunlight piercing through mist, atmospheric, Layout: Wide angle panoramic, sharp foreground, bokeh background suitable for text overlay, negative space in sky and mountain mist, Style: Travel magazine style, cinematic photography, natural healing, Parameters: 8k resolution, High Dynamic Range)
            ```
    - **範例作品**：
      ![Theme B Example](assets/theme_b.png)