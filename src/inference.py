from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from src.config import config

_cache = {}

def generate_plan(age:int, level:str, goal:str, time:int, model_dir:str=None, max_length:int=None):
    model_dir = model_dir or config.output_dir
    max_length = max_length or config.max_target_length
    if model_dir not in _cache:
        tokenizer = AutoTokenizer.from_pretrained(model_dir)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_dir).to(config.device)
        _cache[model_dir] = (tokenizer, model)
    tokenizer, model = _cache[model_dir]
    prompt = f"age: {age} | level: {level} | goal: {goal} | time: {time}"
    inputs = tokenizer(prompt, return_tensors='pt', truncation=True).to(config.device)
    outs = model.generate(**inputs, max_length=max_length, num_beams=4)
    return tokenizer.decode(outs[0], skip_special_tokens=True)
