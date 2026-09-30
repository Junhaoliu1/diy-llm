def btp_hex_list(text):
    """
    UTF-8字节级预分词，返回：
        1. tokens: 每个字符的字节序列+位置信息
        2. t: 所有字节的十六进制字符串列表
    """
    tokens = []
    t = []
    for idx, char in enumerate(text):
        utf8_bytes = char.encode('utf-8')
        hex_bytes = ' '.join(f"{b:02X}" for b in utf8_bytes)
        tokens.append({
            'char': char,
            'bytes': hex_bytes, # 单个字符对应的UTF-8字节序列
            'start': idx,   # 文本信息起始位置
            'end': idx + 1   # 文本信息结束位置
        })
        t.extend([f"{b:02X}" for b in utf8_bytes])
    return tokens, t
if __name__ == "__main__":
   text = "Hi，你好🐋"
   tokens, t = btp_hex_list(text)
   for i in tokens:
       print(i)
   print(t)