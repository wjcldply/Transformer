from datasets import load_dataset
from transformers import AutoConfig, AutoModelForSeq2SeqLM, AutoTokenizer, Seq2SeqTrainer, Seq2SeqTrainingArguments

data_files = {
    "train": "datasets/iwslt17.de.en/train.json",
    "valid": "datasets/iwslt17.de.en/valid.json",
}

iwslt17_dataset = load_dataset("json", data_files=data_files)

print(iwslt17_dataset)
print(iwslt17_dataset["train"][0])