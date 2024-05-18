# Baseline(T5-Small) BLEU-4 Test Result
- Task: Training T5-small from Scratch
- Training/Validation Data: IWSLT17.de.en
- src_lang: DE
- tgt_lang: EN
- custom_dataset: training.jsonl & valid.jsonl
- Trained Model: google-t5/t5-small
- ENV: KHU SERAPH (RTX 3090 Server & Batch Management with Slurm)

## Bash Command Script (to run on GPU Server with Slurm)
```
#!/usr/bin/bash

#SBATCH -J wjkim_run_translation
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-gpu=8
#SBATCH --mem-per-gpu=24G
#SBATCH -p batch_ce_ugrad
#SBATCH -t 1-0
#SBATCH -o logs/run_translation-%A.out

pwd
which python
hostname

python run_translation.py --model_name_or_path google-t5/t5-small \
                          --do_train \
                          --do_eval \
                          --source_lang input \
                          --target_lang output \
                          --source_prefix "translate German to English: " \
                          --train_file datasets/iwslt17.de.en/train.jsonl \
                          --validation_file datasets/iwslt17.de.en/valid.jsonl \
                          --output_dir model_checkpoint/tst_translation \
                          --per_device_train_batch_size=64 \
                          --per_device_eval_batch_size=64 \
                          --num_train_epochs=30 \
                          --overwrite_output_dir \
                          --predict_with_generate

exit 0
```

## Command (run on Local)
- not recommended!
```
(.venv) (base) wonjinkim@Wonjins-MacBook-Pro Transformer % \
> python run_translation.py --model_name_or_path google-t5/t5-small --do_train --do_eval --source_lang input --target_lang output --source_prefix "translate German to English: " --train_file datasets/iwslt17.de.en/train.jsonl --validation_file datasets/iwslt17.de.en/valid.jsonl --output_dir /tmp/tst_translation --per_device_train_batch_size=4 --per_device_eval_batch_size=4 --num_train_epochs=6 --overwrite_output_dir --predict_with_generate
```

## Results
- **Batch Size: 64**
- **Epochs: 30**
- **BLEU: 24.1751**
```
###########################################
100%|██████████| 98220/98220 [7:18:16<00:00,  3.74it/s]
###########################################
***** train metrics *****
  epoch                    =        30.0
  total_flos               = 171024125GF
  train_loss               =      3.2298
  train_runtime            =  7:18:16.56
  train_samples            =      209522
  train_samples_per_second =      239.03
  train_steps_per_second   =       3.735
###########################################
 ***** eval metrics *****
  epoch                   =       30.0
  eval_bleu1              =    56.3842
  eval_bleu2              =    41.4673
  eval_bleu3              =    31.4563
  eval_bleu4              =    24.1751
  eval_gen_len            =    27.6948
  eval_loss               =      2.366
  eval_runtime            = 0:00:21.00
  eval_samples            =        888
  eval_samples_per_second =     42.273
  eval_steps_per_second   =      0.666
###########################################
```