"""
Created on Jan 26, 2018
download.sh 실행 후, datasets/iwslt17.de.en/ 디렉토리에 생성되는 train.de-en.de, train.de-en.en, valid.de-en.de, valid.de-en.en을 취합하여
{input:de_sentence, output:en_sentence} 형태로 구성되는 json 파일을 생성하기 위한 파이썬 코드임

Terminal Command: python json_preprocess.py source_language_file_dir target_language_file_dir output_file_dir json_type
"""

import json
import sys


def create_json(source_language_file, target_language_file, output_json_file, json_type):
    with open(source_language_file, 'r', encoding='utf-8') as f_source, open(target_language_file, 'r', encoding='utf-8') as f_target:
        source_lines = f_source.readlines()
        target_lines = f_target.readlines()

    # Check if both files have the same number of lines
    if len(source_lines) != len(target_lines):
        print("Error: Files have different number of lines.")
        return

    if json_type == 'json':
        data = []  # 딕셔너리{input:source_line, output:target_line}들을 담은 리스트 생성
        for source_line, target_line in zip(source_lines, target_lines):
            data.append({'input': source_line.strip(), 'output': target_line.strip()})

        # Write JSON to file
        with open(output_json_file, 'w', encoding='utf-8') as f_out:
            json.dump(data, f_out, ensure_ascii=False, indent=2)

        print("JSON file created:", output_json_file)
    elif json_type == 'jsonl':
        data = []  # 딕셔너리{input:source_line, output:target_line}들을 담은 리스트 생성
        for source_line, target_line in zip(source_lines, target_lines):
            data.append({"translation": {'input': source_line.strip(), 'output': target_line.strip()}})

        # Write JSONLINES to file
        with open(output_json_file, 'w', encoding='utf-8') as f_out:
            for i in data:
                # f_out.write(json.dumps(i, ensure_ascii=False, indent=2) + '\n')
                f_out.write(json.dumps(i, ensure_ascii=False) + '\n')

        print("JSONL file created:", output_json_file)

# Test Runs
# create_json("datasets/iwslt17.de.en/train.de-en.de", "datasets/iwslt17.de.en/train.de-en.en", "datasets/iwslt17.de.en/train.json", json)
# create_json("datasets/iwslt17.de.en/valid.de-en.de", "datasets/iwslt17.de.en/valid.de-en.en", "datasets/iwslt17.de.en/valid.json", json)

# Test Runs
# create_json("datasets/iwslt17.de.en/train.de-en.de", "datasets/iwslt17.de.en/train.de-en.en", "datasets/iwslt17.de.en/train.jsonl", jsonl)
# create_json("datasets/iwslt17.de.en/valid.de-en.de", "datasets/iwslt17.de.en/valid.de-en.en", "datasets/iwslt17.de.en/valid.jsonl", jsonl)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python json_preprocess.py <src_lang_file> <tgt_lang_file> <output_file> <output_json_type(json or jsonl)>")
        sys.exit(1)

    src_lang_file = sys.argv[1]
    tgt__lang_file = sys.argv[2]
    output_file = sys.argv[3]
    json_type = sys.argv[4]

    create_json(src_lang_file, tgt__lang_file, output_file, json_type)