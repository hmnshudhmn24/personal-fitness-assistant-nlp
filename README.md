# 🏋️‍♂️ Personal Fitness Assistant NLP (T5-Small)

A Transformer-based NLP model that generates **personalized workout plans** and **motivational messages** based on:

- **Age**
- **Fitness Level**
- **Fitness Goal**
- **Time Available (minutes)**

Example Input:
```
age: 25 | level: beginner | goal: weight_loss | time: 30
```

Example Output:
```
Warm-up: 5 minutes light cardio; Circuit: 3 rounds of bodyweight squats and push-ups; Cooldown: stretching. Stay consistent!
```

This repository includes preprocessing, training, evaluation, inference, FastAPI backend, and a Gradio UI.

## 🚀 Features
- Structured workout plan generation
- Motivational coaching messages
- End-to-end ML training pipeline
- FastAPI + Gradio interfaces
- Apache 2.0 license
- HuggingFace model card included

## 📁 Project Structure
```
personal-fitness-assistant-nlp/
├── data/
├── src/
├── notebooks/
├── model/
├── tests/
├── app/
├── huggingface/
├── README.md
├── LICENSE
└── requirements.txt
```

## 📦 Installation
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🔄 Dataset Preprocessing
```
python -m src.dataset_preprocessing --input data/raw/sample_dataset.csv --output data/processed/dataset_clean.jsonl
```

## 🏋️ Train the Model
```
python -m src.train
```

## 🧪 Evaluate
```
python -m src.evaluate
```

## 🤖 Inference Example
```python
from src.inference import generate_plan
print(generate_plan(25, "beginner", "weight_loss", 30))
```

## 🌐 FastAPI Server
```
uvicorn app.api:app --reload --port 8000
```

## 🎨 Gradio UI
```
python app/ui.py
```

