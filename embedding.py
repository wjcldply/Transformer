import torch
import torch.nn as nn
import sentencepiece as spm


class WordEmbedding(nn.Module):  # WordEmbedding 클래스는 torch.nn.Module 클래스 상속
    def __init__(self, vocab_size=37000, embedding_dim=512):  # 생성자는 vocab_size, embedding_dim을 인자로 전달받음 (default: 37000, 512)
        super().__init__()  # 자식클래스(WordEmbedding)의 부모클래스(nn.Module)을 자식클래스(WordEmbedding)에 불러옴
        self.embedding_layer = nn.Embedding(
            num_embeddings=vocab_size,
            embedding_dim=embedding_dim
        )

    def positional_encoding(self, sequence_length, embedding_dim):
        # 아직 작성하지 않음 아래 코드는 걍 placeholder이니 지우고 새로 작성할 것
        position_encoding = torch.zeros(sequence_length, embedding_dim)
        return position_encoding

    def forward(self, inputs):
        """
        takes Tokenized inputs Tensor as input,
        and returns embedded Tensor (so that it could be passed as input into Encoder and Decoder)
        :param inputs: Tensor of shape [batch_size, sequence_length, vocab_size]
        :return: Tensor of shape [batch_size, sequence_length, embedding_dim]
        """

        # Apply: Word Embedding
        # => inputs (torch.size([batch, seq_len, vocab_size])) -> embedded (torch.size([batch, seq_len, d_model]))
        word_embeddings = self.embedding_layer(inputs)  # embedded tensor : torch.size([batch, seq_len, d_model])
        seq_len = word_embeddings.size()[1]  # torch.size([batch, seq_len, d_model]) -> idx1: seq_len
        d_model = word_embeddings.size()[2]  # torch.size([batch, seq_len, d_model]) -> idx2: d_model

        # Apply: Positional Embedding
        pos_encoding = self.positional_encoding(seq_len, d_model)  # creates pos_encoding (same size as word-embeddings)
        embeddings = word_embeddings + pos_encoding   # point-wise addition => creates final embedding

        return embeddings


datapath = './datasets/iwslt17.de.en'
sp_path = '{}/sp'.format(datapath)
sp_tokenizer = spm.SentencePieceProcessor(model_file=sp_path+'.model')
vocab_size = sp_tokenizer.get_piece_size()

de_line = "Wie viel ist aufzuleiden!"
en_line = "How much suffering there is to get through!"

# embedding = nn.Embedding(num_embeddings=vocab_size, embedding_dim=512)
tokenized_input = sp_tokenizer.EncodeAsIds(de_line)
tokenized_output = sp_tokenizer.EncodeAsIds(en_line)
print(f'Tokenized Input Ids: {tokenized_input}')
print(f'Tokenized Output Ids: {tokenized_output}')

tokenized_input_tensor = torch.tensor(tokenized_input)
tokenized_output_tensor = torch.tensor(tokenized_output)
print(f'Tokenized Input Ids Tensor: {tokenized_input_tensor}')
print(f'Tokenized Output Ids Tensor: {tokenized_output_tensor}')

# embedded_input_tensor = embedding(tokenized_input_tensor)
# embedded_output_tensor = embedding(tokenized_output_tensor)
# print(f'Embedded Input Tensor : {embedded_input_tensor}')
# print(f'Embedded Output Tensor : {embedded_output_tensor}')
# print(f'Embedded Input Shape : {embedded_input_tensor.shape}')
# print(f'Embedded Output Shape : {embedded_output_tensor.shape}')

print(f'Tokenized Input Tensor\'s Shape (seq_len) -> {tokenized_input_tensor.shape}')

tokenized_input_tensor_batched = tokenized_input_tensor.view(1, 6)  # WordEmbedding.forward requires torch.size([batch, seq_len, d_model])
print(f'Tokenized Input Tensor - reshaped (batch_size, seq_len) -> {tokenized_input_tensor_batched.shape}')  # reshape to have batch_size dimension (set to 1)

embedding_instance = WordEmbedding(vocab_size=37000, embedding_dim=512)  # instantiate WordEmbedding Class as embedding_instance
word_embedding = embedding_instance.forward(tokenized_input_tensor_batched)  # Conduct Embedding with WordEmbedding.forward

print(f'Embedded Input Tensor : {word_embedding}')
print(f'Embedded Input Shape : {word_embedding.shape}')