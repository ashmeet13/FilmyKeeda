# FilmyKeeda

A simple text generation package aimed to allow a user to easily explore results produced by State of the Art NLP models presented to us in the last few months.

The package currently supports two models -
1. [ULMFiT](http://nlp.fast.ai/classification/2018/05/15/introducting-ulmfit.html) - From Fast.AI
2. [GPT2](https://openai.com/blog/better-language-models/) - From OpenAI

---
### Download -

```pip install filmykeeda```

---
### Data Used -

Both the models have been trained on a extensive corpus of scripts written by Aaron Sorkin. The works included in this project are -
- The West Wing (Series)
- The Social Network (Movie)
- A Few Good Men (Movie)
- The American President (Movie)

---
### Model Details -

**ULMFiT**

```
ULMFiT Model has been trained using the FastAI library.

ULMFiT allows the user to train a model using a custom tokenizer and 
therefore this package includes two different ULMFiT models -

        1. Trained with default FastAI Tokenizer
        2. Trained with SentencePiece Tokenizer
```

**GPT2**

```
GPT2 Model has been trained using the gpt_2_simple library

GPT2 does not allow an external tokenizer to be used and hence
the model has been simply finetuned to our corpus.
```
---
### Usage -

This repository currently holds 4 example.py files demonstrating the use of this package.

```
example0.py - This will demonstrate on how you can download the corpus

example1.py - This will demonstrate on how to generate script using ULMFiT + Default Tokenizer

example2.py - This will demonstrate on how to generate script using ULMFiT + SentencePiece Tokenizer

example3.py - This will demonstrate on how to generate script using GPT2
```
---
### TODO -

1. Package this project as PIP Library
2. Add evaluation scheme's for generated scripts such as ROUGE and Perplexity
3. Clean ULMFiT generated script
