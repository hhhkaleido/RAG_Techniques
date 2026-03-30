#!/usr/bin/env python
"""演示路径解析的差异"""
import os

print("=" * 80)
print("🧪 路径解析方法对比")
print("=" * 80)

# 模拟 simple_rag.py 的位置
simple_rag_file = r"D:\programming\python\AI\RAG\simple_RAG\RAG_TECHNIQUES\all_rag_techniques_runnable_scripts\simple_rag.py"

# 模拟在不同目录运行
scenarios = [
    ("从 RAG_TECHNIQUES 目录运行", r"D:\programming\python\AI\RAG\simple_RAG\RAG_TECHNIQUES"),
    ("从 all_rag_techniques_runnable_scripts 目录运行", r"D:\programming\python\AI\RAG\simple_RAG\RAG_TECHNIQUES\all_rag_techniques_runnable_scripts"),
]
print(type(scenarios))

for scenario_name, cwd in scenarios:
    print(f"\n{'='*80}")
    print(f"场景：{scenario_name}")
    print(f"{'='*80}")
    
    print(f"\n当前工作目录 (os.getcwd()): {cwd}")
    
    # ❌ 原始方法：使用相对路径
    print(f"\n❌ 原始方法：使用相对路径 '../data/...'")
    original_path = "../data/Understanding_Climate_Change.pdf"
    resolved_original = os.path.normpath(os.path.join(cwd, original_path))
    print(f"   解析结果: {resolved_original}")
    print(f"   期望路径: D:\\...\\RAG_TECHNIQUES\\data\\Understanding_Climate_Change.pdf")
    is_correct_original = "RAG_TECHNIQUES" in resolved_original and "simple_RAG" not in resolved_original.split("\\")[-3:]
    print(f"   {'✅ 正确' if is_correct_original else '❌ 错误'}")
    
    # ✅ 改进方法：使用 __file__
    print(f"\n✅ 改进方法：使用 __file__")
    script_dir = os.path.dirname(simple_rag_file)
    root_dir = os.path.dirname(script_dir)
    improved_path = os.path.join(root_dir, "data", "Understanding_Climate_Change.pdf")
    print(f"   脚本目录: {script_dir}")
    print(f"   根目录: {root_dir}")
    print(f"   解析结果: {improved_path}")
    print(f"   期望路径: D:\\...\\RAG_TECHNIQUES\\data\\Understanding_Climate_Change.pdf")
    is_correct_improved = improved_path.endswith(r"RAG_TECHNIQUES\data\Understanding_Climate_Change.pdf")
    print(f"   {'✅ 正确' if is_correct_improved else '❌ 错误'}")

print(f"\n{'='*80}")
print("结论：改进方法无论从哪个目录运行都是正确的！")
print(f"{'='*80}")