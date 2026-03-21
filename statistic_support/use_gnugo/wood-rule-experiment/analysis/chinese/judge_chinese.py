
#!/usr/bin/env python3
import os
import re
import subprocess
import time
from multiprocessing import Pool, cpu_count

def get_result_chinese(sgf_file):
    try:
        cmd = [
            "/usr/games/gnugo",
            "-l", sgf_file,
            "--chinese-rules",
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

def extract_results_from_log(log_file):
    results = {}
    with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            m = re.search(r'第(\d+)局.*结果:\s*(\w+)', line)
            if m:
                game_id = int(m.group(1)) - 1
                result = m.group(2)
                results[game_id] = result
    return results

def worker_task(item):
    game_id, sgf_file = item
    result = get_result_chinese(sgf_file)
    return (game_id, result)

def log(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def main():
    log_file = "output.log"
    games_dir = "games"
    result_log = "output_chinese.log"
    
    log("=== Wood规则中式数子法重算（V3）===")
    
    log("1. 从log中提取原结果...")
    log_results = extract_results_from_log(log_file)
    log(f"   原统计: 黑胜 {list(log_results.values()).count('black')} 局, 白胜 {list(log_results.values()).count('white')} 局")
    
    log("2. 准备SGF文件列表...")
    tasks = []
    for game_id in range(10000):
        sgf_file = os.path.join(games_dir, f"g{game_id}.sgf")
        if os.path.exists(sgf_file):
            tasks.append((game_id, sgf_file))
    log(f"   找到 {len(tasks)} 个SGF文件")
    
    log(f"3. 开始中式数子法并行重算 (使用 {cpu_count()} 个进程)...")
    new_results = {}
    start_time = time.time()
    last_report_time = start_time
    
    with Pool(processes=cpu_count()) as pool:
        for i, (game_id, result) in enumerate(pool.imap_unordered(worker_task, tasks), 1):
            new_results[game_id] = result
            
            current_time = time.time()
            if i % 500 == 0 or (current_time - last_report_time) > 30:
                elapsed = current_time - start_time
                if elapsed > 0:
                    speed = i / elapsed
                else:
                    speed = 0
                if speed > 0:
                    remaining = (len(tasks) - i) / speed
                else:
                    remaining = 0
                log(f"   进度: {i}/{len(tasks)} ({i*100/len(tasks):.1f}%) | 已用: {elapsed:.1f}s | 速度: {speed:.1f}局/s | 预计剩余: {remaining:.1f}s")
                last_report_time = current_time
    
    log("4. 对比结果...")
    matches = 0
    mismatches = 0
    missing = 0
    mismatch_list = []
    
    for game_id in range(10000):
        orig = log_results.get(game_id)
        new = new_results.get(game_id)
        
        if orig is None or new is None:
            missing += 1
        elif orig == new:
            matches += 1
        else:
            mismatches += 1
            mismatch_list.append((game_id, orig, new))
    
    if mismatches > 0:
        log(f"   发现 {mismatches} 局不一致:")
        for game_id, orig, new in mismatch_list[:20]:
            log(f"     第{game_id+1}局 - 原:{orig} vs 新:{new}")
        if mismatches > 20:
            log(f"     ... 还有 {mismatches-20} 局不一致")
    
    log("="*60)
    orig_black = list(log_results.values()).count("black")
    orig_white = list(log_results.values()).count("white")
    new_black = list(new_results.values()).count("black")
    new_white = list(new_results.values()).count("white")
    
    log("最终结果对比:")
    log(f"  日式数目法(原): 黑胜 {orig_black} 局 ({orig_black/100:.2f}%), 白胜 {orig_white} 局 ({orig_white/100:.2f}%)")
    log(f"  中式数子法(新): 黑胜 {new_black} 局 ({new_black/100:.2f}%), 白胜 {new_white} 局 ({new_white/100:.2f}%)")
    log(f"\n  一致: {matches} 局, 不一致: {mismatches} 局, 缺失: {missing} 局")
    log("="*60)
    
    with open(result_log, "w") as f:
        f.write(f"中式数子法统计结果:\n")
        f.write(f"黑胜: {new_black} 局 ({new_black/100:.2f}%)\n")
        f.write(f"白胜: {new_white} 局 ({new_white/100:.2f}%)\n")
        f.write(f"\n与原统计对比:\n")
        f.write(f"一致: {matches} 局\n")
        f.write(f"不一致: {mismatches} 局\n")
        f.write(f"缺失: {missing} 局\n")
        
        if mismatches > 0:
            f.write(f"\n不一致的局:\n")
            for game_id, orig, new in mismatch_list:
                f.write(f"  第{game_id+1}局: 原={orig}, 新={new}\n")
    
    log(f"结果已保存到: {result_log}")
    log(f"总耗时: {time.time() - start_time:.1f}秒")

if __name__ == "__main__":
    main()

