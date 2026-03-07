
# Wood围棋规则

Wood围棋规则是一种创新的围棋变体规则，通过白棋首手座子、不贴目、平局白胜等机制实现公平对局。

### 🎯 核心逻辑
不贴目 · 地多者胜 · 座子平衡

### 📜 基础规则（中/英对照）
| 项目          | 中文说明                                  | English Explanation                          |
|---------------|-------------------------------------------|----------------------------------------------|
| 棋盘规格      | 9/13/19路通用                             | 9/13/19×19 boards supported                  |
| 开局座子      | 白棋座子（可旋转4个等效位）<br>9路：a5 · 13路：a7 · 19路：b10 | White handicap (4 rotational positions)<br>9×9:a5 · 13×13:a7 · 19×19:b10 |
| 座子放置      | 赛前放好即可，谁放不限                    | Placed before game, placer not specified      |
| 行棋顺序      | 座子后黑棋先行，交替落子                  | Black plays first after handicap, alternate  |
| 核心定义「地」| 活子数 + 围空点                           | Field = Living Stones + Owned Territory      |
| 胜负判定      | 地多者胜；平局按棋盘定：<br>9路→黑胜 · 13/19路→白胜 | Larger Field wins; Draw rules:<br>9×9→Black · 13/19×19→White |
| 通用规则      | 遵循围棋禁入点、提子、劫争                | Follows Go rules (illegal moves, capture, ko) |

### ✨ 3个关键优势
1. 公平：胜率逼近50%  
2. 简单：无复杂换算  
3. 灵活：适配全尺寸棋盘

## 开源许可

本规则采用CC0 1.0公共领域许可，可自由使用、修改、分发。

## 贡献

欢迎提交Issue或Pull Request改进规则说明。
