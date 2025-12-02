# 第 3 堂：商品情境 - 虛擬攝影棚 (Affinity 主場)

- **主題**：商品去背與情境合成
- **工具**：Affinity Photo/Designer + AI 背景生成
- **重點方向**：
    - **光影一致性**：學習如何調整素材的亮度、對比與色溫，使其與 AI 背景完美融合。
    - **透視與比例**：理解視平線 (Horizon Line) 與物體比例，避免合成感過重。
    - **陰影繪製**：使用 Affinity 的筆刷或圖層樣式製作真實的接觸陰影 (Contact Shadow)。
- **實作產出**：一張高質感的商品情境合成圖。

## 雙軌實戰任務 (Dual-Track Specs)
#### **第 3 堂：商品情境 - 虛擬攝影棚**

- **學習主軸**：AI 生成透視背景 + Affinity 商品合成。
- **【主題 A：科技新品發表】**
    - **風格**：**賽博龐克/霓虹 (Cyberpunk/Neon)** - 暗調、發光、反射。
    - **主角**：最新款智慧型手機或電競耳機。
    - **參考文案內容 (Reference Copy)**：
        - **標題**：超越極限，定義未來
        - **副標題**：X-Phone Pro 全新上市
        - **內文**：搭載次世代 AI 晶片，極致效能，瞬間覺醒。體驗前所未有的速度與流暢。
    - **Prompt 進階三部曲 (由淺入深)**：
        1. **Lv1 (基礎)**：
            ```prompt
            賽博龐克桌面背景，留白 (Cyberpunk table background, copy space)
            ```
        2. **Lv2 (中階)**：
            ```prompt
            產品攝影背景，霓虹燈光，潮濕表面，產品空間 (Product photography background, neon lights, wet surface, space for product)
            ```
        3. **Lv3 (高階)**：
            ```prompt
            [主體] 幾何形狀的產品展示台
            [環境] 未來城市夜景散景，霓虹藍粉燈光反射於潮濕地面
            [構圖] 居中構圖，展示台位於下方中央，上方大面積留白供標題與文案
            [風格] 高科技氛圍，時尚，冷冽
            [參數] 8k 解析度，光線追蹤渲染，景深效果
            (Subject: Geometric product display podium, Environment: Futuristic city night bokeh, neon blue and pink lights reflecting on wet ground, Layout: Centered composition, podium at bottom center, large negative space above for headline and copy, Style: High-tech vibe, fashion, cool tones, Parameters: 8k resolution, ray tracing render, depth of field)
            ```
    - **範例作品**：
      ![Theme A Example](assets/theme_a.png)
- **【主題 B：手工皂/香氛蠟燭】**
    - **風格**：**自然禪意 (Zen/Natural)** - 木質、陽光、植物。
    - **主角**：手工皂或精油瓶。
    - **參考文案內容 (Reference Copy)**：
        - **標題**：回歸純粹，自然森活
        - **副標題**：Pure Life 手工植萃系列
        - **內文**：嚴選天然草本精華，溫和洗淨，不造成肌膚負擔。讓沐浴成為一場與大自然的對話。
    - **Prompt 進階三部曲 (由淺入深)**：
        1. **Lv1 (基礎)**：
            ```prompt
            木桌背景，留白 (Wooden table background, copy space)
            ```
        2. **Lv2 (中階)**：
            ```prompt
            產品攝影背景，木桌，陽光，窗戶陰影，乾淨區域 (Product photography background, wooden table, sunlight, window shadow, clean area)
            ```
        3. **Lv3 (高階)**：
            ```prompt
            [主體] 質樸的木製桌面
            [環境] 柔和晨光透過窗簾灑落，映照出植物葉片的陰影
            [構圖] 俯視平拍 (Flat lay)，右側放置裝飾性植物，左側寬敞留白供產品與文字擺放
            [風格] 自然清新，SPA 氛圍，溫暖
            [參數] 自然光，柔焦，高質感攝影
            (Subject: Rustic wooden tabletop, Environment: Soft morning sunlight through curtains casting plant leaf shadows, Layout: Flat lay, decorative plants on right, wide negative space on left for product and text, Style: Natural fresh, SPA atmosphere, warm, Parameters: Natural lighting, soft focus, high quality photography)
            ```
    - **範例作品**：
      ![Theme B Example](assets/theme_b.png)