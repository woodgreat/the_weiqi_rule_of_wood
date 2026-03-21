
#!/usr/bin/env python3
import os
import re
import subprocess
from multiprocessing import Pool, cpu_count

def get_result_japanese(sgf_file):
    """用日式数目法计算一局结果"""
    try:
        cmd = [
            "/usr/games/gnugo",
            "-l", sgf_file,
            "--score", "finish",
            "--level", "10",
            "--komi", "0"
        ]
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(timeout=120)
        
        stdout_lower = stdout.lower()
        if any(keyword in stdout_lower for keyword in ["black wins", "b+", "black+"]):
            return "black"
        elif any(keyword in stdout_lower for keyword in ["white wins", "w+", "white+"]):
            return "white"
        else:
            return "black"
    except Exception as e:
        print(f"  错误处理 {sgf_file}: {e}")
        return None

def worker_task(item):
    game_id, sgf_file = item
    result = get_result_japanese(sgf_file)
    return (game_id, result)

def main():
    games_dir = "games"
    
    print("=== 日式数目法统计 ===")
    
    # 准备SGF文件
    tasks = []
    for game_id in range(10000):
        sgf_file = os.path.join(games_dir, f"g{game_id}.sgf")
        if os.path.exists(sgf_file):
            tasks.append((game_id, sgf_file))
    print(f"找到 {len(tasks)} 个SGF文件")
    
    # 并行计算
    results = {}
    with Pool(processes=cpu_count()) as pool:
        for i, (game_id, result) in enumerate(pool.imap_unordered(worker_task, tasks), 1):
            results[game_id] = result
            if i % 500 == 0:
                print(f"已处理: {i}/{len(tasks)}")
    
    # 统计结果
    black_wins = list(results.values()).count("black")
    white_wins = list(results.values()).count("white")
    
    print("\n" + "="*60)
    print("最终结果:")
    print(f"  黑胜: {black_wins} 局 ({black_wins/100:.2f}%)")
    print(f"  白胜: {white_wins} 局 ({white_wins/100:.2f}%)")
    print("="*60)

if __name__ == "__main__":
    main()

