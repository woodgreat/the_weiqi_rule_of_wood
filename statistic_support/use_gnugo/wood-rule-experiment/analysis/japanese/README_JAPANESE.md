
# 日式数目法判定 / Japanese Territory Scoring

说明：wood规则的数地法不使用日式数目法，wood规则中数地法是参考中式数子法中的子空皆地原则。此文档中方法只做对比参考。
---

## 中文部分 / Chinese Section

### 方法说明 / Method Description

**日式数目法**（Japanese territory scoring）是现代围棋常用的胜负判定方法之一：

1. **只算空**：只计算双方围出的空点，不计入棋子本身
2. **提子算目**：被吃掉的棋子每颗算1目
3. **贴目**：黑棋先行需要贴目（通常6.5目或7.5目）

### 本实验参数 / Experiment Parameters

- 无贴目（`--komi 0`）：符合Wood规则设计
- 使用GNU Go 3.8默认规则（日式）

### 统计结果 / Results

- **黑胜**：5114局（51.14%）
- **白胜**：4886局（48.86%）


说明：wood规则的数地法不使用日式数目法，wood规则中数地法是参考中式数子法中的子空皆地原则。此文档中方法只做对比参考。


---

## 英文部分 / English Section

### Method Description

**Japanese territory scoring** is one of the most commonly used scoring methods in modern Go:

1. **Territory only**: Only counts empty points surrounded by each player, not the stones themselves
2. **Prisoners count**: Each captured stone counts as 1 point
3. **Komi**: Black, playing first, needs to give komi (usually 6.5 or 7.5 points)

### Experiment Parameters

- No komi (`--komi 0`): Consistent with Wood Rule design
- Uses GNU Go 3.8 default rules (Japanese)

### Results

- **Black wins**: 5114 games (51.14%)
- **White wins**: 4886 games (48.86%)


Note: The Wood Rule's scoring method does not use Japanese territory scoring. The Wood Rule's scoring method references the "stones + empty territory" principle from Chinese territory scoring. The methods in this document are for comparison and reference only.
