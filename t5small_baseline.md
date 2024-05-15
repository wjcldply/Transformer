# Baseline BLEU Performance
- Task: Fine-Tuning
- Training/Validation Data: IWSLT17.de.en
- src_lang: DE
- tgt_lang: EN
- custom_dataset: training.jsonl & valid.jsonl
- Trained Model: google-t5/t5-small
- Used HW: M2 Pro MBP (10c/16c/32gb)
## Command
```
(.venv) (base) wonjinkim@Wonjins-MacBook-Pro Transformer % python run_translation.py --model_name_or_path google-t5/t5-small --do_train --do_eval --source_lang input --target_lang output --source_prefix "translate German to English: " --train_file datasets/iwslt17.de.en/train.jsonl --validation_file datasets/iwslt17.de.en/valid.jsonl --output_dir /tmp/tst_translation --per_device_train_batch_size=4 --per_device_eval_batch_size=4 --overwrite_output_dir --predict_with_generate
```

## Results
- **Epochs: 3**
- **BLEU: 31.572**
```
Training completed. Do not forget to share your model on huggingface.co/models =)


{'train_runtime': 42488.1458, 'train_samples_per_second': 14.794, 'train_steps_per_second': 3.699, 'train_loss': 1.7395742064911555, 'epoch': 3.0}                                                                  
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 157143/157143 [11:48:08<00:00,  3.70it/s]
[INFO|trainer.py:3388] 2024-05-09 17:10:17,795 >> Saving model checkpoint to /tmp/tst_translation
[INFO|configuration_utils.py:471] 2024-05-09 17:10:17,796 >> Configuration saved in /tmp/tst_translation/config.json
[INFO|configuration_utils.py:690] 2024-05-09 17:10:17,797 >> Configuration saved in /tmp/tst_translation/generation_config.json
[INFO|modeling_utils.py:2595] 2024-05-09 17:10:17,942 >> Model weights saved in /tmp/tst_translation/model.safetensors
[INFO|tokenization_utils_base.py:2503] 2024-05-09 17:10:17,950 >> tokenizer config file saved in /tmp/tst_translation/tokenizer_config.json
[INFO|tokenization_utils_base.py:2512] 2024-05-09 17:10:17,951 >> Special tokens file saved in /tmp/tst_translation/special_tokens_map.json
***** train metrics *****
  epoch                    =         3.0
  total_flos               =   8671463GF
  train_loss               =      1.7396
  train_runtime            = 11:48:08.14
  train_samples            =      209522
  train_samples_per_second =      14.794
  train_steps_per_second   =       3.699
05/09/2024 17:10:17 - INFO - __main__ - *** Evaluate ***
[INFO|trainer.py:3697] 2024-05-09 17:10:18,034 >> ***** Running Evaluation *****
[INFO|trainer.py:3699] 2024-05-09 17:10:18,034 >>   Num examples = 888
[INFO|trainer.py:3702] 2024-05-09 17:10:18,034 >>   Batch size = 4
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 222/222 [09:01<00:00,  2.44s/it]
***** eval metrics *****
  epoch                   =        3.0
  eval_bleu               =     31.572
  eval_gen_len            =    26.3559
  eval_loss               =     1.4004
  eval_runtime            = 0:11:07.17
  eval_samples            =        888
  eval_samples_per_second =      1.331
  eval_steps_per_second   =      0.333
[INFO|modelcard.py:450] 2024-05-09 17:21:25,252 >> Dropping the following result as it does not have all the necessary fields:
{'task': {'name': 'Translation', 'type': 'translation'}, 'metrics': [{'name': 'Bleu', 'type': 'bleu', 'value': 31.572}]}

```