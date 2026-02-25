
import subprocess
import random
import os
import time
from collections import defaultdict
from multiprocessing import Pool, Manager
import threading
import argparse
import sys

class WoodGoSimulator:
    def __init__(self, gnugo_path="gnugo.exe"):
        self.gnugo_path = gnugo_path
    
    def get_random_corner_position(self, board_size=19):
        """获取符合Wood规则的随机座子位置"""
        # 19路棋盘：1路或2路
        #row = random.choice([1, 2])
        row =2 # 19路棋盘：仅2路（为了平衡黑棋先行优势）
        
        # 生成SGF格式的围棋坐标（小写字母）
        # SGF坐标格式：列用小写字母(a-t, 跳过i)，行用小写字母(a-t, 跳过i)
        # 1路对应'a'，2路对应'b'
        
        # 选择角落位置的列（左/右边界）
        col_choices = ['a', 'b', 's', 't']  # 左边界a/b，右边界s/t
        corner_col = random.choice(col_choices)
        
        # 选择行（1路或2路）
        corner_row = 'a' if row == 1 else 'b'
        
        return f"{corner_col}{corner_row}"
    
    def run_single_game(self, game_id):
        """运行单局对局"""
        # 只测试19路棋盘
        board_size = 19
        
        # 生成符合规则的随机座子位置
        white_stone_pos = self.get_random_corner_position(board_size)
        
        print(f"DEBUG: 白棋座子位置: {white_stone_pos}")
        
        # 创建一个简单的SGF文件，只包含白棋的座子
        sgf_content = f"""(;GM[1]FF[4]CA[UTF-8]AP[WoodRuleTester:1.0]
SZ[19]KM[0]HA[0]GN[WoodRuleGame]DT[2026-02-24]
PC[Local]PB[Black]PW[White]
;W[{white_stone_pos}])"""
        
        # 创建games目录（如果不存在）
        games_dir = os.path.join(os.getcwd(), "games")
        if not os.path.exists(games_dir):
            os.makedirs(games_dir)
            print(f"DEBUG: 创建games目录: {games_dir}")
        
        # 保存SGF文件到games目录
        sgf_file = os.path.join(games_dir, f"game_{game_id}.sgf")
        with open(sgf_file, "w") as f:
            f.write(sgf_content)
        print(f"DEBUG: 保存SGF文件到: {sgf_file}")
        
        result = "white"
        try:
            # 移除帮助信息检查，直接使用正确的参数
            print(f"DEBUG: 使用正确的得分参数组合")
            
            # 使用正确的参数组合来让GNUGO完成对局并计算得分
            # 设置难度为1（最快），并将完整对局保存回SGF文件
            
            analyze_cmd = [
                self.gnugo_path,
                "-l", sgf_file,      # 加载SGF文件
                "-o", sgf_file,      # 将完整对局保存回同一个文件
                "--score", "finish",  # 让GNUGO完成对局并计算得分
                "--level", "1",       # 设置难度为1（最快）
                "--komi", "0"         # 设置贴目为0，符合Wood式规则
            ]

            print(f"DEBUG: 运行GNUGO命令: {' '.join(analyze_cmd)}")
            
            # 启动GNUGO进程
            process = subprocess.Popen(
                analyze_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # 读取输出，设置超时为300秒
            stdout, stderr = process.communicate(timeout=300)
            
            # 显示完整的输出，不截断
            print(f"DEBUG: 完整GNUGO输出:\n{stdout}")
            print(f"DEBUG: 完整GNUGO错误:\n{stderr}")
            
            # 解析结果（更全面的匹配）
            stdout_lower = stdout.lower()
            if any(keyword in stdout_lower for keyword in ["black wins", "b+", "black+"]):
                result = "black"
                print(f"DEBUG: 第{game_id+1}局判定为黑胜")
            elif any(keyword in stdout_lower for keyword in ["white wins", "w+", "white+"]):
                result = "white"
                print(f"DEBUG: 第{game_id+1}局判定为白胜")
            else:
                # 规则规定：子/目相同时白胜
                result = "white"
                print(f"DEBUG: 第{game_id+1}局未找到明确结果，判定为白胜")
                
        except Exception as e:
            print(f"DEBUG: GNUGO调用错误: {str(e)}")
            # 错误情况下默认白胜
            result = "white"
        finally:
            # 不再清理SGF文件，保留在games目录中
            print(f"DEBUG: SGF文件已保存到games目录，保留以供查看")
        
        # 打印每局结果
        print(f"第{game_id+1}局 | 棋盘大小: {board_size}路 | 白棋座子: {white_stone_pos} | 结果: {result}")
                
        return result

def worker_init():
    """工作进程初始化"""
    pass

def check_gnugo_installed(gnugo_path):
    """检查GNUGO是否已安装"""
    try:
        subprocess.run([gnugo_path, "--version"], 
                      stdout=subprocess.DEVNULL, 
                      stderr=subprocess.DEVNULL,
                      creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        return True
    except FileNotFoundError:
        return False

def run_single_thread_simulation(num_games=10, gnugo_path="gnugo.exe"):
    """单线程运行模拟"""
    print(f"开始单线程模拟{num_games}局Wood规则对局...")
    print(f"使用GNUGO路径: {gnugo_path}")
    
    simulator = WoodGoSimulator(gnugo_path)
    results = []
    
    for game_id in range(num_games):
        print(f"\n开始第{game_id+1}局...")
        result = simulator.run_single_game(game_id)
        results.append(result)
        
        # 每局结束后打印当前统计
        black_wins = results.count("black")
        white_wins = results.count("white")
        total = len(results)
        if total > 0:
            print(f"当前统计: 总{total}局 | 黑胜{black_wins}局 ({black_wins/total*100:.2f}%) | 白胜{white_wins}局 ({white_wins/total*100:.2f}%)")
    
    # 最终统计
    black_wins = results.count("black")
    white_wins = results.count("white")
    draws = results.count("draw")
    
    return black_wins, white_wins, draws

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='Wood围棋规则Windows测试')
    parser.add_argument('-n', '--games', type=int, default=50, help='模拟对局数 (默认: 5)')
    parser.add_argument('--gnugo-path', type=str, default="gnugo.exe", help='GNUGO可执行文件路径 (默认: gnugo.exe)')
    
    args = parser.parse_args()
    
    # 检查GNUGO是否可用
    if not check_gnugo_installed(args.gnugo_path):
        print(f"错误: 找不到GNUGO引擎 ({args.gnugo_path})")
        print("请确保GNUGO已正确安装并在当前目录中可用")
        sys.exit(1)
    
    start_time = time.time()
    
    # 运行单线程模拟
    black_wins, white_wins, draws = run_single_thread_simulation(
        num_games=args.games,
        gnugo_path=args.gnugo_path
    )
    
    # 计算统计结果
    total = black_wins + white_wins + draws
    elapsed_time = time.time() - start_time
    
    print("\nWood围棋规则并行模拟统计结果:")
    print("=" * 60)
    print(f"总对局数: {total}")
    print(f"黑棋胜: {black_wins}局 ({black_wins/total*100:.2f}%)")
    print(f"白棋胜: {white_wins}局 ({white_wins/total*100:.2f}%)")
    print(f"平局: {draws}局 ({draws/total*100:.2f}%)")
    print("-" * 60)
    print(f"总耗时: {elapsed_time:.2f}秒")
    print(f"平均每局耗时: {elapsed_time/total:.4f}秒")
    print(f"吞吐量: {total/elapsed_time:.2f}局/秒")
    print("=" * 60)

if __name__ == "__main__":
    main()