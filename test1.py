"""演示导入顺序的问题"""
import os
import sys

print("=" * 70)
print("测试1: 不加载 .env 直接导入")
print("=" * 70)

# 模拟原始错误的场景
print(f"OPENAI_API_KEY = {os.getenv('OPENAI_API_KEY')}")
print("结果: ❌ None\n")

print("=" * 70)
print("测试2: 先加载 .env 再导入")
print("=" * 70)

from dotenv import load_dotenv
load_dotenv()

print(f"OPENAI_API_KEY = {os.getenv('OPENAI_API_KEY')}")
api_key = os.getenv('OPENAI_API_KEY')
if api_key:
    masked = api_key[:10] + '...' + api_key[-5:]
    print(f"结果: ✅ {masked}")
else:
    print(f"结果: ❌ None (但这表示 .env 没有被找到或格式错误)")

print("=" * 70)