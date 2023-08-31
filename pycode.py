import re
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load pre-trained seq2seq model
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-python")
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-python")

js_code = """
function factorial(n) {
  if (n == 0) {
    return 1;
  } else {
    return n * factorial(n-1);
  }
}

console.log(factorial(5));
"""

# Tokenize the JS code
inputs = tokenizer(js_code, return_tensors="pt")

# Generate Python translation
outputs = model.generate(**inputs)
py_code = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(py_code)
