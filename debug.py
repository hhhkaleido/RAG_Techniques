import os
import sys

print("=" * 60)
print("🔍 路径诊断")
print("=" * 60)

# 情况1：原始方式
print("\n❌ 原始方式 (有问题):")
print(f"   os.getcwd() = {os.getcwd()}")
print(f"   os.path.join(os.getcwd(), '..') = {os.path.join(os.getcwd(), '..')}")
print(f"   问题: 这只会回到 simple_RAG，而不是 RAG_TECHNIQUES")

# 情况2：脚本所在目录
print("\n✅ 脚本所在目录 (正确):")
script_dir = os.path.dirname(os.path.abspath(__file__))
print(f"   script_dir = {script_dir}")
root_dir = os.path.dirname(os.path.join(script_dir, 'all_rag_techniques_runnable_scripts'))
print(f"   root_dir = {root_dir}")

# 情况3：文件检查
print("\n📂 文件检查:")
helper_path = os.path.join(root_dir, 'helper_functions.py')
print(f"   helper_functions.py 路径: {helper_path}")
print(f"   存在? {os.path.exists(helper_path)}")

# 情况4：导入测试
print("\n🧪 导入测试:")
sys.path.insert(0, root_dir)
try:
    import helper_functions
    print(f"   ✅ 成功导入 helper_functions")
except ImportError as e:
    print(f"   ❌ 导入失败: {e}")