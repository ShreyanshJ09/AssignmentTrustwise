import torch
import torch.nn.functional as F
from transformers import AutoModelForSequenceClassification, AutoTokenizer


def detect_gibberish(input_text):
    model = AutoModelForSequenceClassification.from_pretrained("madhurjindal/autonlp-Gibberish-Detector-492513457", token=True)
    tokenizer = AutoTokenizer.from_pretrained("madhurjindal/autonlp-Gibberish-Detector-492513457", token=True)

    inputs = tokenizer.encode(input_text, return_tensors="pt")

    outputs = model(inputs)
    probs = F.softmax(outputs.logits, dim=-1)

    predicted_index = torch.argmax(probs, dim=1).item()
    predicted_prob = probs[0][predicted_index].item()
    labels = model.config.id2label
    predicted_label = labels[predicted_index]

    for i, prob in enumerate(probs[0]):
        print(f"Class: {labels[i]}, Probability: {prob:.4f}")

    class_probs = {labels[i]: probs[0][i].item() for i in range(len(labels))}
    gibberish_prob = class_probs.get("word salad", 0) + class_probs.get("noise", 0)
    # print(f"Class: gibberish, Probability: {gibberish_prob:.4f}")
    final_label = "gibberish"
    final_prob = gibberish_prob
    result = {
        "label": final_label,
        "score": final_prob
    }

    return result


