from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("roneneldan/TinyStories-33M")
model = AutoModelForCausalLM.from_pretrained("roneneldan/TinyStories-33M")

# prompt = "Once upon a time there was"
prompt = "Why is the sky blue"
input_ids = tokenizer.encode(prompt, return_tensors="pt")

output = model.generate(input_ids, max_length = 1000, num_beams=1)
output_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(output_text)

