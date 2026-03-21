# Wood规则验证实验 / Wood Rule Verification Experiment

***

## 中文部分 / Chinese Section

### 实验目的 / Experiment Purpose

验证**Wood规则**的科学性与平衡性。Wood规则是一种基于中国古棋座子制思想的现代围棋规则，通过在特定位置放置白棋座子来平衡黑棋的先手优势，无需贴目。


### Wood规则简介 / Introduction to Wood Rule

1. **座子**：开局前在棋盘特定位置放置一枚白棋座子
2. **无贴目**：黑棋先行，但无需贴目
3. **胜负判定**：采用**中式数子法**（子空皆地），子/目相同时黑胜
4. **核心思想**：用固定座子代替贴目，回归中国古棋的平衡性

### 实验方法 / Experiment Method

1. 使用GNU Go 3.8进行10000局自对弈模拟
2. 分别用**日式数目法**和**中式数子法**统计胜负
3. 对比两种判定方法的结果差异

### 实验结果 / Experiment Results

| 判定方法  | 黑胜局数 | 黑胜率    | 白胜局数 | 白胜率    |
| ----- | ---- | ------ | ---- | ------ |
| 日式数目法 | 5114 | 51.14% | 4886 | 48.86% |
| 中式数子法 | 5042 | 50.42% | 4958 | 49.58% |

### 结论 / Conclusion

1. **Wood规则高度平衡**：使用中式数子法统计，黑胜率仅为50.42%，接近完美的50%对50%
2. **判定方法影响显著**：日式数目法和中式数子法的结果差异为0.72%，共94局胜负判定不同
3. **Wood规则应使用中式数子法**：Wood规则的核心思想来自中国古棋，必须用中式数子法（子空皆地）才能体现其真正的平衡性


说明：wood规则的数地法不使用日式数目法，wood规则中数地法是参考中式数子法中的子空皆地原则。

***

## 英文部分 / English Section

### Experiment Purpose

To verify the scientific validity and balance of the **Wood Rule**, a modern Go rule system based on the ancient Chinese stone-placing philosophy. The Wood Rule uses a fixed white stone at a specific position to balance Black's first-move advantage, eliminating the need for komi.

### Introduction to Wood Rule

1. **Fixed Stone**: A white stone is placed at a specific position before the game starts
2. **No Komi**: Black plays first, but no komi is required
3. **Scoring**: Uses **Chinese territory scoring** (stones + empty territory), Black wins if tied
4. **Core Philosophy**: Using fixed stones instead of komi, returning to the balance of ancient Chinese Go

### Experiment Method

1. Simulated 10,000 self-play games using GNU Go 3.8
2. Scored the games using both **Japanese territory scoring** and **Chinese territory scoring**
3. Compared the results from both scoring methods

### Experiment Results

| Scoring Method   | Black Wins | Black Win Rate | White Wins | White Win Rate |
| ---------------- | ---------- | -------------- | ---------- | -------------- |
| Japanese Scoring | 5114       | 51.14%         | 4886       | 48.86%         |
| Chinese Scoring  | 5042       | 50.42%         | 4958       | 49.58%         |

### Conclusion

1. **Wood Rule is Highly Balanced**: Using Chinese territory scoring, Black's win rate is only 50.42%, nearly a perfect 50-50 split
2. **Scoring Method Matters**: The difference between Japanese and Chinese scoring is 0.72%, with 94 games having different outcomes
3. **Wood Rule Should Use Chinese Scoring**: The Wood Rule's core philosophy comes from ancient Chinese Go, so Chinese territory scoring (stones + empty territory) must be used to reveal its true balance


Note: The Wood Rule's scoring method does not use Japanese territory scoring. The Wood Rule's scoring method references the "stones + empty territory" principle from Chinese territory scoring. 


2026.03.21.wood
