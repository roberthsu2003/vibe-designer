# 第 10 堂：大型輸出 - 解析度救星

- **主題**：大尺寸印刷與解析度處理
- **工具**：AI Upscale (放大) + Affinity Photo
- **重點方向**：
    - **解析度迷思**：理解 DPI (Dots Per Inch) 與觀看距離的關係。
    - **AI 放大術**：使用 AI 工具將低解析度素材無損放大至印刷等級。
    - **色彩管理**：CMYK vs RGB 的轉換陷阱與色偏修正。
- **實作產出**：一張大型活動背板或易拉展 (Roll-up Banner)。

## 雙軌實戰任務 (Dual-Track Specs)
#### **第 10 堂：大型輸出 - 解析度救星**

- **學習主軸**：AI 超高解析度放大 + Affinity 大圖輸出設定。
- **【主題 A：科技博覽會背板】**
    - **風格**：**宏大場景 (Grand Scenery)** - 城市天際線、宇宙、數據海。
    - **尺寸**：300cm x 240cm (比例縮放製作)。
    - **參考文案內容 (Reference Copy)**：
        - **主標題**：FUTURE TECH EXPO 2025
        - **副標題**：Innovating for a Better Tomorrow
        - **日期地點**：Oct 15-18 | World Trade Center
        - **Slogan**：Where Technology Meets Humanity
    - **Prompt 進階三部曲 (由淺入深)**：
        1. **Lv1 (基礎)**：
            ```prompt
            未來城市天際線，廣角，天空留白 (Futuristic city skyline, wide shot, copy space in sky)
            ```
        2. **Lv2 (中階)**：
            ```prompt
            夜晚的未來城市天際線，霓虹燈，廣角，大字空間 (Futuristic city skyline at night, neon lights, wide angle, space for large text)
            ```
        3. **Lv3 (高階)**：
            ```prompt
            [主體] 未來大都會全景，飛行車穿梭，巨型全像投影
            [環境] 賽博龐克夜景，電影級燈光氛圍
            [構圖] 超廣角鏡頭 (Wide shot)，地平線位於下方 1/3，上方 2/3 天空大面積留白供大標題與活動日期排版
            [文字配置] 標題「TECH EXPO 2025」置於天空留白處，巨大且具未來感的無襯線體 (Futuristic Sans-serif)，發光藍色，日期地點置於下方，清晰白色
            [風格] 科幻電影感，高度細節，震撼視覺
            [參數] 8k 解析度，銳利畫質
            (Subject: Panoramic view of futuristic metropolis, flying cars, giant holograms, Environment: Cyberpunk night scene, cinematic lighting atmosphere, Layout: Ultra wide shot, horizon at bottom 1/3, top 2/3 sky large negative space for large title and event dates, Text Layout: Title 'TECH EXPO 2025' placed in sky negative space, huge futuristic sans-serif, glowing blue, date and location below, clear white, Style: Sci-fi movie feel, high detail, stunning visual, Parameters: 8k resolution, sharp image)
            ```
    - **範例作品**：
      ![Theme A Example](assets/theme_a.png)
- **【主題 B：音樂節/市集打卡牆】**
    - **風格**：**波西米亞 (Boho/Festival)** - 圖騰、流蘇、戶外感。
    - **尺寸**：300cm x 240cm (比例縮放製作)。
    - **參考文案內容 (Reference Copy)**：
        - **主標題**：Wanderlust Music Festival
        - **副標題**：Music, Art, & Soul
        - **日期地點**：July 20-22 | Sunset Valley
        - **Hashtag**：#Wanderlust2025
    - **Prompt 進階三部曲 (由淺入深)**：
        1. **Lv1 (基礎)**：
            ```prompt
            音樂節背景，日落，留白 (Music festival background, sunset, copy space)
            ```
        2. **Lv2 (中階)**：
            ```prompt
            波西米亞風格背景，羽毛與捕夢網，日落，暖色調，拍照空間 (Bohemian style background, feathers and dreamcatchers, sunset, warm tones, space for photo)
            ```
        3. **Lv3 (高階)**：
            ```prompt
            [主體] 戶外音樂節舞台與波西米亞風裝飾（羽毛、捕夢網）
            [環境] 日落餘暉，仙女燈閃爍，遠處人群剪影
            [構圖] 對稱或中央構圖，中央預留大面積人像拍攝空間 (Photo backdrop)，四周裝飾
            [文字配置] 標題「SUMMER VIBES」置於背景上方，復古霓虹燈管字體 (Vintage Neon Script)，暖橘色，Hashtag「#Wanderlust2025」置於下方，手寫風格
            [風格] 溫暖氛圍，夢幻，Coachella 風格
            [參數] 廣角，柔和光線
            (Subject: Outdoor music festival stage and bohemian decorations (feathers, dreamcatchers), Environment: Sunset glow, fairy lights twinkling, crowd silhouettes in distance, Layout: Symmetrical or central composition, large central space reserved for portrait photo backdrop, decorations around edges, Text Layout: Title 'SUMMER VIBES' placed at top of background, vintage neon script, warm orange, Hashtag '#Wanderlust2025' below, handwritten style, Style: Warm atmosphere, dreamy, Coachella style, Parameters: Wide angle, soft lighting)
            ```
    - **範例作品**：
      ![Theme B Example](assets/theme_b.png)