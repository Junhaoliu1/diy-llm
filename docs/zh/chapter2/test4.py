from transformers import AutoTokenizer
# 使用DeepSeek Coder系列模型的分词器
MODEL_NAME = "deepseek-ai/deepseek-coder-6.7b-instruct"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
print(f"成功加载模型: {MODEL_NAME} 的分词器。")
print(f"分词器词表大小V: {len(tokenizer.get_vocab())}")

chinese_text = "你好"
# 编码
encoded_ids = tokenizer.encode(chinese_text, add_special_tokens=False)
# 解码回Token字符串 (用于观察子词)
tokens = tokenizer.convert_ids_to_tokens(encoded_ids)
print(f"\n原文: {chinese_text}")
print(f"编码: {tokens}")
print(f"IDs:{encoded_ids}")