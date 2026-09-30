
import re
         
def part(text):
   text = re.sub(r'([.,!?;:()"\'\[\]{}])', r' \1 ', text)
   tokens = text.split()
   return tokens

if __name__ == "__main__":         
   s = "I like Datawhale."
   print(part(s))
   