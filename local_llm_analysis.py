from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer (first download will take time)
model_name = "microsoft/phi-3-mini-4k-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


# Example: Analyze a suspicious log entry
log = """
2024-05-20 12:34:56 [ALERT] Failed login attempts: 15 from IP 192.168.1.100
User: admin, Source: SSH
"""

prompt = f"""
You are a cybersecurity analyst. Analyze this log entry and identify potential threats:
{log}
Possible actions: [Brute-force attack, Credential stuffing, Normal activity]
Answer concisely.
"""

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_length=200)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(response)
