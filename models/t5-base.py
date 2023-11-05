from transformers import AutoModelWithLMHead, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-common_gen")
model = AutoModelWithLMHead.from_pretrained("mrm8488/t5-base-finetuned-common_gen")


def gen_sentence(words, max_length=64):
    input_text = words
    features = tokenizer([input_text], return_tensors="pt")

    output = model.generate(
        input_ids=features["input_ids"],
        attention_mask=features["attention_mask"],
        max_length=max_length,
    )

    return tokenizer.decode(output[0], skip_special_tokens=True)


words = "Explain: 'This Act is named the Mines and Minerals Act, 1957. It applies to all of India and becomes effective on a date determined by the Central Government through an official notification' "

print(gen_sentence(words))
