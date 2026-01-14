import time
import tracemalloc
import json

def run_judge(SolutionClass, test_cases, method_name="solve"):
    """
    JSON驱动的通用判题器
    :param test_cases: 格式为 [{"input": {"a":1, "b":2}, "expected": 3}, ...]
    """
    try:
        sol = SolutionClass()
    except Exception as e:
        print(f"❌ 实例化失败: {e}")
        return

    passed_count = 0
    total = len(test_cases)
    
    # 打印表头
    print(f"{'ID':<5} | {'结果':<10} | {'耗时 (ms)':<12} | {'内存峰值 (KB)':<15}")
    print("-" * 60)
    
    for i, case in enumerate(test_cases):
        # 这里的 case 是一个字典
        input_data = case.get("input", {})
        expected = case.get("expected")
        
        tracemalloc.start()
        start_time = time.perf_counter()
        
        try:
            func = getattr(sol, method_name)
            
            # 核心改进：使用关键字参数解包，自动匹配函数定义的参数名
            # 比如 solve(self, a, b)，只要 input 字典里有 'a' 和 'b' 就能对上
            if isinstance(input_data, dict):
                result = func(**input_data)
            else:
                # 兼容非字典输入（如单参数）
                result = func(input_data)
            
            end_time = time.perf_counter()
            _, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            duration_ms = (end_time - start_time) * 1000
            peak_kb = peak / 1024
            
            # 结果比对（处理 JSON 序列化后的精度或格式问题）
            if result == expected:
                status = "✅ Passed"
                passed_count += 1
            else:
                status = "❌ Wrong"
                
            print(f"{i+1:<5} | {status:<10} | {duration_ms:<12.4f} | {peak_kb:<15.2f}")
            
            if result != expected:
                # 使用 json.dumps 让打印出来的输入输出更美观
                print(f"      └─ 详情: 输入 {json.dumps(input_data)}, 期望 {json.dumps(expected)}, 实际 {json.dumps(result)}")

        except Exception as e:
            tracemalloc.stop()
            print(f"{i+1:<5} | 💥 Error    | {'--':<12} | {'--':<15}")
            print(f"      └─ 错误详情: {type(e).__name__}: {e}")

    print("-" * 60)
    print(f"🏁 评测完成: {passed_count}/{total} 通过")