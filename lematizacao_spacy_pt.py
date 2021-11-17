"""Regras para lematização do português para a versão 3.0 ou 3.1 do spacy."""
"""Rules for lemmatization in portuguese for spacy version 3.0 or 3.1."""
import re
import spacy
from lematizacao_substituicoes import substituicoes

# Carrega o spacy no modelo 'lg', que apresentou melhores resultados.
# Loads spacy with'lg' model, for it presented better results.
nlp = spacy.load("pt_core_news_lg")

arquivo = input("Digite o nome do arquivo com a extensão (.txt): ")
while True:
    try:
        with open(arquivo, "r") as arq:
            # Lê o arquivo como lista
            # Reads the file as a list
            para_lematizar_lista = arq.read().split()
            # Separando os números
            # Separating the numbers
            nums = re.compile(r"\d+([.,/-]?(\d+))*")
            so_nums = [num for num in para_lematizar_lista if nums.match(num)]
            # Ficando apenas com as palavras
            # Only words remaining
            so_palavras = [pal for pal in para_lematizar_lista if not nums.match(pal)]
            # Separando algumas palavras com hífens ("recebe-se" -> "recebe se")
            # Separating some words with hyphens ("recebe-se" -> "recebe se")
            sem_hifen = []
            for pal in so_palavras:
                pal = re.sub(r"(\b\w+\b)([.!;:?,])", r"\1 \2", pal)
                pal = re.sub(
                    r"(\w+)-(\b([mts]e|lhes?|v?[oa]s?)\b)(-\w+)?", r"\1 \2", pal
                )
                pal = re.sub(r"(\w+)-(\bn[oa]s?\b)(-\w+)?", r"\1 o", pal)
                pal = re.sub(r"(\w+)á-(\bl[oa]s?\b)(-\w+)?", r"\1ar o", pal)
                pal = re.sub(r"(\w+)ê-(\bl[oa]s?\b)(-\w+)?", r"\1er o", pal)
                pal = re.sub(r"(\w+)[ií]-(\bl[oa]s?\b)(-\w+)?", r"\1ir o", pal)
                sem_hifen.append(pal)
            para_lematizar = " ".join(sem_hifen)
            doc = nlp(para_lematizar)
            break
    except FileNotFoundError:
        print(f"Esse nome de arquivo não existe: {arquivo}")
        arquivo = input("Escreva o nome do arquivo com a extensão: ")

# Gera a frase com lemas, postags e features das tags
# Generates the sentence with lemmas, postags and tag features
para_lematizar = ""
para_lematizar_spacy = ""
for token in doc:
    # Vai gerar a lematização tal como o Spacy faz
    # Generates Spacy's lemmatization
    para_lematizar_spacy += token.lemma_ + " "

    # Vai gerar as informações para as regras de substituição da lematização
    # Generates information for the substitution rules to the lemmatization
    feats = str(token.morph).split("|")
    para_lematizar += (
        token.text
        + "/"
        + token.lemma_
        + "/"
        + token.pos_
        + "/"
        + "/".join([x.split("=")[1] for x in feats if "=" in x])
        + " "
    )

para_lematizar = para_lematizar.lower()
lematizacao_spacy = re.sub(" ", "\n", para_lematizar_spacy)

# Acessa as substituições para nova lematização
# Accesses substitutions for new lemmatization
for k, v in substituicoes.items():
    para_lematizar = re.sub(v[0], v[1], para_lematizar)

# Gera os lemas corrigidos e os números
# Generates the fixed lemmas and the numbers
para_lematizar = re.sub(" ", "\n", para_lematizar)
versao_corrigida = para_lematizar

nums_str = " ".join(so_nums)
nums_str = re.sub(" ", "\n", nums_str)

# Gera um arquivo com a lematização do Spacy
# Generates a file with Spacy's lemmatization
with open("resultados_spacy.txt", "w") as resultados:
    resultados.write(lematizacao_spacy)
# Gera arquivo com números e os lemas corrigidos pelas substituições
# Generates a file with the numbers and the lemmas fixed by the substitutions
with open("resultados.txt", "w") as resultados:
    resultados.write(nums_str + "\n\n")
    resultados.write(versao_corrigida)
