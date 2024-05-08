from datasets import load_dataset

data_files = {
    "train": "datasets/iwslt17.de.en/train.json",
    "valid": "datasets/iwslt17.de.en/valid.json",
}

iwslt17_dataset = load_dataset("json", data_files=data_files)


# print(type(iwslt17_dataset))
# print(iwslt17_dataset)
# print(iwslt17_dataset.keys())
# print(iwslt17_dataset.values())