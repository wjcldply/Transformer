import sentencepiece as spm

datapath = './datasets/iwslt17.de.en'
src_path = '{}/train.de-en.de'.format(datapath)
dest_path = '{}/train.de-en.en'.format(datapath)
spm_path = '{}/sp'.format(datapath)


def main():
    train_txt = ",".join([src_path, dest_path])
    vocab_size = 37000
    character_coverage = 1.0
    model_name = spm_path
    model_types = ['unigram', 'bpe', 'char', 'word']
    user_defined_symbols = "[PAD],[UNK],[CLS],[SEP],[MASK],[BOS],[EOS]"

    cmd = f'--input={train_txt} --model_prefix={model_name} --vocab_size={vocab_size} --character_coverage={character_coverage} --model_type={model_types[1]} --user_defined_symbols={user_defined_symbols}'

    spm.SentencePieceTrainer.Train(cmd)

    sp = spm.SentencePieceProcessor(model_file=spm_path+'.model')
    en_line = "How much suffering there is to get through!"
    # en_line = "Whatever that doesn't kill you makes you stronger."
    de_line = "Wie viel ist aufzuleiden!"
    # de_line = "Was mich nicht umbringt, macht mich starker."
    print(sp.encode_as_pieces(en_line))
    print(sp.encode_as_pieces(de_line))

    print(sp.encode_as_ids(en_line))
    print(sp.encode_as_ids(de_line))

    print(sp.bos_id())
    print(sp.eos_id())
    print(sp.unk_id())

if __name__ == '__main__':
    main()