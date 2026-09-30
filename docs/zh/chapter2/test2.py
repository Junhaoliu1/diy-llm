     
def tokenize_byte_level(text):
   tokens = []
   for ch in text:

      utf8_bytes = ch.encode("utf-8")
      hex_bytes = [f"{b:02X}" for b in utf8_bytes]
      print(f"{ch} -> {hex_bytes}")
      tokens.extend(hex_bytes)
   return tokens

if __name__ == "__main__":
   s = "All for learners"
   print(tokenize_byte_level(s))
