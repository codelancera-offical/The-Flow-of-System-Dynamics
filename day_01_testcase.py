__all__ = ['test_cases_1', 'test_cases_2']


test_cases_1 = [
    # 1. 基础正整数
    {"input": {"a": 3, "b": 5}, "expected": 8},
    {"input": {"a": 123, "b": 456}, "expected": 579},
    
    # 2. 包含 0 的情况
    {"input": {"a": 0, "b": 0}, "expected": 0},
    {"input": {"a": 0, "b": 789}, "expected": 789},
    {"input": {"a": -500, "b": 0}, "expected": -500},
    
    # 3. 负数运算
    {"input": {"a": -10, "b": -20}, "expected": -30},
    {"input": {"a": -15, "b": 30}, "expected": 15},
    {"input": {"a": 100, "b": -100}, "expected": 0},
    
    # 4. 边界大数 (根据你要求的 -10^9 <= A, B <= 10^9)
    {"input": {"a": 10**9, "b": 10**9}, "expected": 2000000000},
    {"input": {"a": -10**9, "b": -10**9}, "expected": -2000000000},
    {"input": {"a": 10**9, "b": -10**9}, "expected": 0},
    
    # 5. 稍微大一点的随机数
    {"input": {"a": 123456789, "b": 987654321}, "expected": 1111111110}
]

test_cases_2 = [
    # 1. 常规用例
    {
        "input": {"nums": [1, 2, 3, 4, 5]}, 
        "expected": 15
    },
    # 2. 包含负数
    {
        "input": {"nums": [-1, -2, -3, -4, -5]}, 
        "expected": -15
    },
    # 3. 正负混合
    {
        "input": {"nums": [10, -10, 20, -20]}, 
        "expected": 0
    },
    # 4. 边界：空数组（求和应为 0）
    {
        "input": {"nums": []}, 
        "expected": 0
    },
    # 5. 边界：只有一个元素
    {
        "input": {"nums": [42]}, 
        "expected": 42
    },
    # 6. 大规模数据测试
    {
        "input": {"nums": list(range(1, 101))}, # 1到100的和
        "expected": 5050
    },
    # 7. 包含 0 的情况
    {
        "input": {"nums": [0, 0, 0, 7]}, 
        "expected": 7
    }
]