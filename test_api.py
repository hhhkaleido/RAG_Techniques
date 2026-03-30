#!/usr/bin/env python
"""找到正确的 retriever 调用方式"""
import os
import sys
from dotenv import load_dotenv

load_dotenv()

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from helper_functions import encode_pdf

pdf_path = os.path.join(script_dir, "data", "Understanding_Climate_Change.pdf")

if not os.path.exists(pdf_path):
    print(f"❌ PDF not found: {pdf_path}")
    sys.exit(1)

print("=" * 80)
print("🧪 找到正确的 Retriever 调用方式")
print("=" * 80)

vector_store = encode_pdf(pdf_path, chunk_size=500, chunk_overlap=100)
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

query = "What is climate change?"

print(f"\nRetriever 类型: {type(retriever)}")
print(f"Retriever 方法列表:")
methods = [m for m in dir(retriever) if not m.startswith('_') and callable(getattr(retriever, m))]
for m in sorted(methods)[:10]:  # 只显示前10个
    print(f"  - {m}")

print(f"\n测试 invoke() 方法：")

# 测试1：invoke(string)
print(f"\n1️⃣ 尝试: retriever.invoke('{query[:30]}...')")
try:
    docs = retriever.invoke(query)
    print(f"   ✅ 成功！找到 {len(docs)} 个文档")
    print(f"   第一个文档: {docs[0].page_content[:100]}...")
except Exception as e:
    print(f"   ❌ 失败: {type(e).__name__}: {e}")

# 测试2：invoke(dict)
print(f"\n2️⃣ 尝试: retriever.invoke({{'input': '{query[:30]}...'}})")
try:
    docs = retriever.invoke({"input": query})
    print(f"   ✅ 成功！找到 {len(docs)} 个文档")
except Exception as e:
    print(f"   ❌ 失败: {type(e).__name__}: {e}")

print("\n" + "=" * 80)