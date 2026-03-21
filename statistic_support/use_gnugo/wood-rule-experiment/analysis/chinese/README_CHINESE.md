
# 中式数子法判定 / Chinese Territory Scoring

---

## 中文部分 / Chinese Section

### 方法说明 / Method Description

**中式数子法**（Chinese territory scoring）是中国古棋传承的胜负判定方法，也是Wood规则的核心：

1. **子空皆地**：棋子本身和围出的空点都算作地盘
2. **无贴目**：通过座子平衡先手，无需贴目
3. **子空相同时黑胜**：因为黑棋先行，平局时判黑胜

### 本实验参数 / Experiment Parameters

- 无贴目（`--komi 0`）：符合Wood规则设计
- 使用GNU Go 3.8的中式规则（`--chinese-rules`）

### 统计结果 / Results

- **黑胜**：5042局（50.42%）
- **白胜**：4958局（49.58%）

---

## 英文部分 / English Section

### Method Description

**Chinese territory scoring** is the scoring method inherited from ancient Chinese Go, and is the core of the Wood Rule:

1. **Stones + territory**: Both the stones themselves and the surrounded empty points count as territory
2. **No komi**: First-move advantage is balanced by fixed stones, no komi needed
3. **Black wins ties**: Because Black plays first, Black wins in case of a tie

### Experiment Parameters

- No komi (`--komi 0`): Consistent with Wood Rule design
- Uses GNU Go 3.8 Chinese rules (`--chinese-rules`)

### Results

- **Black wins**: 5042 games (50.42%)
- **White wins**: 4958 games (49.58%)

