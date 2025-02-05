from transformers import RobertaTokenizer, RobertaForSequenceClassification
import torch
import os


def detect_toxic(input_text):
    hf_token = os.getenv("HF_TOKEN")
    # model = AutoModelForSequenceClassification.from_pretrained(
    #     "madhurjindal/autonlp-Gibberish-Detector-492513457",)
    # tokenizer = AutoTokenizer.from_pretrained(p
    #     "madhurjindal/autonlp-Gibberish-Detector-492513457", use_auth_token=hf_token
    # )
    tokenizer = RobertaTokenizer.from_pretrained('s-nlp/roberta_toxicity_classifier', token=hf_token
    )

    model = RobertaForSequenceClassification.from_pretrained('s-nlp/roberta_toxicity_classifier', token=hf_token
    )


    inputs = tokenizer.encode(input_text, return_tensors="pt")

    with torch.no_grad():
        outputs = model(inputs)

    logits = outputs.logits
    probabilities = torch.softmax(logits, dim=1).squeeze()

    labels = ["Neutral", "Toxic"]


    max_index = torch.argmax(probabilities).item()
    if(labels[max_index] == "Neutral"):
        result = {
        "label": labels[max_index],
        "score": 1-probabilities[max_index].item()
       }
    else :
        result = {
            "label": labels[max_index],
            "score": probabilities[max_index].item()
        }


    print("Tokenized input shape:", inputs.shape)
    print("logits",logits)
    print("Logits shape:", logits.shape)
    print("Max index:", max_index)

    return result
