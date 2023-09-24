from transformers import GPT2Tokenizer, GPT2LMHeadModel
tokenizer = GPT2Tokenizer.from_pretrained("af1tang/personaGPT")
model = GPT2LMHeadModel.from_pretrained("af1tang/personaGPT")
personas=['I am military veteran<|endoftext|>', 'I like to promote about joining the Indian navy <|endoftext|>', 'I am a good person who helps everyone<|endoftext|>']
personas = tokenizer.encode(''.join(['<|p2|>'] + personas + ['<|sep|>'] + ['<|start|>']))