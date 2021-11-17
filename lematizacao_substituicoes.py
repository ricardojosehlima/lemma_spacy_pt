substituicoes = {
    # Começo do conjunto de regras
    # Beginning of the set of rules
    # Consertando palavras no plural que ficam com lemas no plural
    # Fixing words in plural whose lemmas remain in plural
    "lema_plural": (r"(?P<tudo>(?P<rad>\b\w+)s\b)/\1/\S+plur\S*", r"\g<tudo>/\g<rad>"),
    # Consertando e dividindo contrações de preposições e artigos
    # Fixing and splitting contractions of prepositions and determiners
    "dos": (r"\bd(?P<dos>[oa]s?\b)\S+", r"de/de \g<dos>/o"),
    "nos": (r"\bn(?P<nos>[oa]s?\b)\S+", r"em/em \g<nos>/o"),
    "aos": (r"\ba(?P<aos>os?\b)\S+", r"a/a \g<aos>/o"),
    "pelos": (r"\bpel(?P<pelos>[oa]s?\b)\S+", r"por/por \g<pelos>/o"),
    # Consertando algumas palavras específicas
    # Fixing more specific words
    "suas": (r"(?P<suas>\bsuas?\b)\S+", r"\g<suas>/seu"),
    "umas": (r"(?P<umas>\bumas?\b)\S+", r"\g<umas>/um"),
    "vou_vamos": (r"(?P<vou_vamos>\b(vou|vamos)\b)\S+", r"\g<vou_vamos>/ir"),
    "diga": (r"(?P<diga>zbdiga\b)\S+", r"\g<diga>/dizer"),
    "nós": (r"(?P<nós>\bnós\b)\S+", r"\g<nós>/nós"),
    "e_ser": (r"(?P<é>\bé\b)\S+", r"\g<é>/ser"),
    "vi": (r"(?P<vi>\bvi\b)\S+", r"\g<vi>/ver"),
    "quero": (r"(?P<quero>\bquero\b)\S+", r"\g<quero>/querer"),
    "para": (r"(?P<para>\bpara\b)\S+", r"\g<para>/para"),
    # Consertando e dividindo contrações de preposições e pronomes
    # Fixing and splitting contractions of prepositions and pronouns
    "de_pron": (
        r"\bd(?P<rad>aquel|es?[lts]?)(?P<des>[ea]s?)\b\S+",
        r"de/de \g<rad>\g<des>/\g<rad>e",
    ),
    "de_pron_i": (r"\bd(?P<rad>aquil|is[ts]?)o\b\S+", r"de/de \g<rad>o/\g<rad>o"),
    "em_pron": (
        r"\bn(?P<rad>aquel|es?[lts]?)(?P<des>[ea]s?)\b\S+",
        r"em/em \g<rad>\g<des>/\g<rad>e",
    ),
    "em_pron_i": (r"\bn(?P<rad>aquil|is?[ts]?)o\b\S+", r"em/em \g<rad>o/\g<rad>o"),
    # Consertando situações com a preposição "a"
    # Fixing issues envolving preposition "a"
    "a": (r"(?P<a>\ba\b)/o/[sa]\S+", r"\g<a>/a"),
    "à": (r"(?P<à>\bàs?\b)\S+", r"\g<à>/a a/a"),
    # Consertando casos de classes gramaticais fechadas
    # Fixing issues with closed class words
    "final_r": (
        r"(?P<pal>\b\w+\b)/\b\w+r\b/(det|adv|adp|sconj)\S*",
        r"\g<pal>/\g<pal>",
    ),
    # Consertando número e gênero de adjetivos
    # Fixing number and gender of adjectives
    "adj_fp": (r"(?P<tudo>(?P<rad>\b\w+)as?\b/adj\S+)", r"\g<tudo>/\g<rad>o"),
    # Consertando substantivos
    # Fixing nouns
    "subs_a": (
        r"(?P<tudo>(?P<simples_a>\b\w+a)s\b)/\w+[rs]/(adj|noun)\S+plur",
        r"\g<tudo>/\g<simples_a>",
    ),
    # empresas, amoras mas professoras fica professora (mesmo problema do Udpipe e Stanza)
    "subs_r": (
        r"(?P<tudo>(?P<simples_r>\b\w+)es\b)/\w+r/(adj|noun)\S+plur",
        r"\g<tudo>/\g<simples_r>",
    ),  # cores, mares, meses, pazes
    "subs_l": (
        r"(?P<tudo>(?P<simples_l>\b\w+)is\b)/\w+r/(adj|noun)\S+plur",
        r"\g<tudo>/\g<simples_l>l",
    ),  # portais
    "subs_sg": (
        r"(?P<simples_sg>\b\w+[^r]\b)/\w+r/(adj|noun)\S+sing",
        r"\g<simples_sg>/\g<simples_sg>",
    ),  # livro, empresa
    # Consertando particípios de verbos da 1ª conjugação
    # Fixing participles of verbs from the 1st conjugation
    "partic": (
        r"(?P<tudo>(?P<rad>\b\w+a)(?P<partic>d[oa]s?)\b)/\w+d[oa]s?/verb\S+",
        r"\g<tudo>/\g<rad>r",
    ),
    # Consertando parcialmente particípios de verbos da 2ª e 3ª conjugações,
    # Partially fixing participles of verbs from the 2nd and 3rd conjugations,
    "partic_e": (
        r"(?P<tudo>(?P<rad>\b\w+[csho])[ií](?P<partic>d[oa]s?)\b)/\w+d[oa]s?/verb\S+",
        r"\g<tudo>/\g<rad>er",
    ),
    "partic_e_2": (
        r"(?P<tudo>(?P<rad>\breceb)i(?P<partic>d[oa]s?)\b)/\w+d[oa]s?/verb\S+",
        r"\g<tudo>/\g<rad>er",
    ),
    "partic_i": (
        r"(?P<tudo>(?P<rad>\b\w+[anju])[ií](?P<partic>d[oa]s?)\b)/\w+d[oa]s?/verb\S+",
        r"\g<tudo>/\g<rad>ir",
    ),
    "partic_i_2": (
        r"(?P<tudo>(?P<rad>\bl)i(?P<partic>d[oa]s?)\b)/lidar/verb\S+",
        r"\g<tudo>/\g<rad>er",
    ),
    # Removendo as postags e as features das tags remanescentes
    # Removing the remaining postags and tag features
    "pal_lema": (r"(?P<pal_lema>\b\w+(-\w+)*/\w+(-\w+)*\b)\S*", r"\g<pal_lema>"),
    "sem_pontuacao": (r'(?P<pontuacao>[.,;:?!-"\'])\S*', r"\g<pontuacao>"),
    # Ao comentar a linha abaixo, vai ser gerado o par palavra/lema em vez
    # de apenas os lemas. Pode ser útil para checar inconsistências do código.
    # If the line below is commented, instead of generating only the lemmas,
    # the code will generate a pair word/lemma. This can be useful to check
    # inconsistencies in the code.
    # Apenas os lemas
    # Only the lemmas
    "lemas": (r"\b\w+(-\w+)*\b/(?P<lemas>\b\w+(-\w+)*\b)", r"\g<lemas>"),
}
