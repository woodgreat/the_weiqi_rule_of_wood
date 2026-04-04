
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

**完整10000局统计**：
- **黑胜**：4986局（49.86%）
- **白胜**：5014局（50.14%）
- **平局**：0局（0.00%）

### 分析结论 / Analysis Conclusion

1. **公平性验证**：黑棋胜率49.86%，白棋胜率50.14%，两者非常接近，差值仅为0.28%，证明Wood围棋规则在10000局大样本下保持了良好的公平性。

2. **座子效果**：白棋通过固定座子（19路: b10位置）获得了微弱优势，有效平衡了黑棋的先行优势。

3. **统计显著性**：10000局的样本量足够大，统计结果具有高度可靠性，能够准确反映规则的真实表现。

4. **模拟性能**：总耗时1089373.53秒，平均每局耗时108.9374秒，吞吐量0.01局/秒。

5. **结论**：Wood围棋规则通过固定白棋座子的设计，成功实现了接近50-50的胜率分布，验证了规则的公平性和有效性。

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

**Complete 10000-game Statistics**:
- **Black wins**: 4986 games (49.86%)
- **White wins**: 5014 games (50.14%)
- **Draws**: 0 games (0.00%)

### Analysis Conclusion

1. **Fairness Verification**: Black win rate is 49.86%, White win rate is 50.14%, with only a 0.28% difference, proving that the Wood Go Rules maintain good fairness under the large sample of 10000 games.

2. **Fixed Stone Effect**: White gains a slight advantage through fixed stones (19x19: b10 position), effectively balancing Black's first-move advantage.

3. **Statistical Significance**: The sample size of 10000 games is large enough, and the statistical results are highly reliable, accurately reflecting the true performance of the rules.

4. **Simulation Performance**: Total time: 1089373.53 seconds, average per game: 108.9374 seconds, throughput: 0.01 games/second.

5. **Conclusion**: Through the design of fixed white stones, the Wood Go Rules successfully achieve a win rate distribution close to 50-50, verifying the fairness and effectiveness of the rules.