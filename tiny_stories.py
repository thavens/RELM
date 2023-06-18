from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("roneneldan/TinyStories-33M")

model = AutoModelForCausalLM.from_pretrained("roneneldan/TinyStories-33M")
