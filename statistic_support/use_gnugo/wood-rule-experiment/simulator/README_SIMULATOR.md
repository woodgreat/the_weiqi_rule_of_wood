
# Wood规则对局模拟器 / Wood Rule Game Simulator

---

## 中文部分 / Chinese Section

### 脚本说明 / Script Description

`wood_rule_simulator.py` 用于使用GNU Go模拟Wood规则的自对弈对局。

### 使用方法 / Usage

```bash
python3 wood_rule_simulator.py -n 10000
```

或

```bash
python3 wood_rule_simulator.py --games 10000
```

### 参数说明 / Parameters

- `-n, --games`: 指定模拟的局数（默认：5局）

### 输出 / Output

- SGF棋谱文件：保存在 `games/` 目录下
- 日志文件：`output.log`，记录每局的胜负结果

---

## 英文部分 / English Section

### Script Description

`wood_rule_simulator.py` is used to simulate Wood Rule self-play games using GNU Go.

### Usage

```bash
python3 wood_rule_simulator.py -n 10000
```

or

```bash
python3 wood_rule_simulator.py --games 10000
```

### Parameters

- `-n, --games`: Specify the number of games to simulate (default: 5 games)

### Output

- SGF game files: Saved in the `games/` directory
- Log file: `output.log`, recording the result of each game

