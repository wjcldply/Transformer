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