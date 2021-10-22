'''Regras para lematização do português para a versão 3.0 ou 3.1 do spacy'''
'''Rules for lemmatization in portuguese for spacy version 3.0 or 3.1'''
import re
import spacy

# Carrega o spacy, podendo-se escolher o modelo 'sm' ou 'lg'.
# Loads spacy, one can choose between 'sm' or 'lg' model.
modelo = input('Qual modelo será utilizado? Escolha sm ou lg: ')
nlp = spacy.load('pt_core_news_' + modelo)

'''
Permite que se digite uma frase ou se insira um arquivo para lematização.
Se for um arquivo, o resultado sairá em outro arquivo.
Se for frase, sairá no terminal.
O arquivo deve estar em .txt
'''
'''
Input maybe a file or a sentence.
If it is a file, result will be presented in another file.
If it is a sentence, result will appear in the terminal.
File must be in .txt
'''
pergunta = input('Quer testar [f]rase ou [a]rquivo?')

if pergunta == 'f':
    para_lematizar = input("Digite a frase: ")
    doc = nlp(para_lematizar)
else:
    arquivo = input("Escreva o nome do arquivo com a extensão: ")
    with open(arquivo, 'r') as myfile:
        para_lematizar = myfile.read()
        doc = nlp(para_lematizar)

# Gera a frase com lemas, postags e features das tags
# Generates the sentence with lemmas, postags and tag features
para_lematizar = ''
para_lematizar_spacy = ''
for token in doc:
       
    para_lematizar_spacy += (
        token.lemma_ + " "
        )
    
    feats = str(token.morph).split("|")
    
    if token.like_num != True:
        para_lematizar += (
            token.text + "/" +
            token.lemma_ + "/" +
            token.pos_ + "/" +
            "/".join([x.split("=")[1] for x in feats if "=" in x]) + " "
            )
    else:
        para_lematizar += (token.text + " ")

para_lematizar = para_lematizar.lower()

# Imprime a versão do spacy sem as regras, se input for frase
# Prints spacy version without the rules, if input is a sentence
lematizacao_spacy = para_lematizar_spacy
if pergunta == 'f':
    print(lematizacao_spacy)

# Começo do conjunto de regras
# Beginning of the set of rules


# Consertando e dividindo contrações de preposições e artigos
# Fixing and splitting contractions of prepositions and determiners
dos = re.sub(r'\bd(?P<dos>[oa]s?\b)\S+', 'de/de \g<dos>/o', para_lematizar)
nos = re.sub(r'\bn(?P<nos>[oa]s?\b)\S+', 'em/em \g<nos>/o', dos)
aos = re.sub(r'\ba(?P<aos>os?\b)\S+', 'a/a \g<aos>/o', nos)
pelos = re.sub(r'\bpel(?P<pelos>[oa]s?\b)\S+', 'por/por \g<pelos>/o', aos)

# Consertando duas palavras específicas
# Fixing two specific words
suas = re.sub(r'\b(?P<suas>suas?)\S+', '\g<suas>/seu', pelos)
umas = re.sub(r'\b(?P<umas>umas?)\S+', '\g<umas>/um', suas)

# Consertando duas palavras específicas
# Fixing two specific words
vou_vamos = re.sub(r'\b(?P<vou>(vou|vamos))\S+', '\g<vou>/ir', pelos)
diga = re.sub(r'\b(?P<diga>diga)\S+', '\g<diga>/dizer', vou_vamos)
nos = re.sub(r'\b(?P<nós>nós)/\w+\S+', '\g<nós>/nós', diga)
e_ser = re.sub(r'\b(?P<é>é\b)/\w+\S+', '\g<é>/ser', nos)



# Consertando e dividindo contrações de preposições e pronomes
# Fixing and splitting contractions of prepositions and pronouns
de_pron = re.sub(r'\bd(?P<rad>aquel|es?)(?P<var>[lts]?)(?P<des>[ea]s?)\b\S+',
                 'de/de \g<rad>\g<var>\g<des>/\g<rad>\g<var>e', e_ser)
de_pron_i = re.sub(r'\bd(?P<rad>aquil|is?)(?P<var>[ts]?)o\b\S+',
                   'de/de \g<rad>\g<var>o/\g<rad>\g<var>o', de_pron)
em_pron = re.sub(r'\bn(?P<rad>aquel|es?)(?P<var>[lts]?)(?P<des>[ea]s?)\b\S+',
                 'em/em \g<rad>\g<var>\g<des>/\g<rad>\g<var>e', de_pron_i)
em_pron_i = re.sub(r'\bn(?P<rad>aquil|is?)(?P<var>[ts]?)o\b\S+',
                   'em/em \g<rad>\g<var>o/\g<rad>\g<var>o', em_pron)

# Consertando situações com a preposição "a"
# Fixing issues envolving preposition "a"
a = re.sub(r'(?P<a>\ba\b)/o/[sa]\S+', '\g<a>/a', em_pron_i)
à = re.sub(r'(?P<à>\bàs?\b)\S+', '\g<à>/a a/a', a)

# Consertando casos de classes gramaticais fechadas
# Fixing issues with closed class words
final_r = re.sub(r'(?P<pal>\w+)/\w+r/(det|adv|adp|sconj)\S*',
                 '\g<pal>/\g<pal>', à)

# Consertando número e gênero de adjetivos
# Fixing number and gender of adjectives
adj_fp = re.sub(r'(?P<tudo>(?P<rad>\b\w+)as?/adj\S+\b)',
                '\g<tudo>/\g<rad>o', final_r)

# Consertando substantivos
# Fixing nouns
subs_a = re.sub(r'(?P<tudo>(?P<simples_a>\w+a)s)/\w+r\b/(adj|noun)\S+plur',
                '\g<tudo>/\g<simples_a>', adj_fp) # empresa, demora mas professora
subs_r = re.sub(r'(?P<tudo>(?P<simples_r>\w+)es)/\w+r\b/(adj|noun)\S+plur',
                '\g<tudo>/\g<simples_r>', subs_a) # cor, mar
subs_l = re.sub(r'(?P<tudo>(?P<simples_l>\w+)is)/\w+r\b/(adj|noun)\S+plur',
                '\g<tudo>/\g<simples_l>l', subs_r) # portais
subs_sg = re.sub(r'(?P<simples_sg>\w+[^r])/\w+r\b/(adj|noun)\S+sing',
                 '\g<simples_sg>/\g<simples_sg>', subs_l) # livro, empresa
subs_ivo = re.sub(r'(?P<tudo>(?P<rad>\w+iv[oa])s?)/\w+/noun\S+',
                  '\g<tudo>/\g<rad>', subs_sg) # alternativas
subs_ica = re.sub(r'(?P<tudo>(?P<rad>\w+átic[oa])s?)/\w+/noun\S+',
                  '\g<tudo>/\g<rad>', subs_ivo) # problemática

# Consertando particípios de verbos da 1ª conjugação
# Fixing participles of verbs from the 1st conjugation
partic = re.sub(
    r'(?P<tudo>(?P<rad>\w+a)(?P<partic>d[oa]s?))/\w+d[oa]s?/verb\S+',
    r'\g<tudo>/\g<rad>r', subs_ica)

# Consertando parcialmente particípios de verbos da 2ª e 3ª conjugações(2)
# Partially fixing participles of verbs from the 2nd and 3rd conjugations(2)
partic_e = re.sub(
    r'(?P<tudo>(?P<rad>\w+[csho])[ií](?P<partic>d[oa]s?))/\w+d[oa]s?/verb\S+',
    r'\g<tudo>/\g<rad>er', partic)
partic_i = re.sub(
    r'(?P<tudo>(?P<rad>\w+[anju])[ií](?P<partic>d[oa]s?))/\w+d[oa]s?/verb\S+',
    r'\g<tudo>/\g<rad>ir', partic_e)
# recebidos --> recebir; os irregulares

# Consertando parcialmente situações envolvendo clíticos(3)
# Partially fixing issues with clitics(3)
clit_a = re.sub(r'(?P<tudo>(?P<pal>\w+)á-(?P<clit>l[oa]s?))\S+',
                '\g<pal>ar \g<clit>/o', partic_i) # deixá-los
clit_e = re.sub(r'(?P<tudo>(?P<pal>\w+)ê-(?P<clit>l[oa]s?))\S+',
                '\g<pal>er \g<clit>/o', clit_a) # fazê-los
clit_i = re.sub(r'(?P<tudo>(?P<pal>\w+)[ií]-(?P<clit>l[oa]s?))\S+',
                '\g<pal>ir \g<clit>/o', clit_e) # destruí-los
clit_r = re.sub(r'(?P<tudo>(?P<pal>\w+r)-(?P<clit>[mtsnvl]\w{,3})(-\w+)?)\S+',
                '\g<pal> \g<clit>/\g<clit>',
                clit_i) # fazer-me, discutir-se-á
# casos com lhe, n[oa]s? são possíveis mas podem ter problemas (Contem-nos a verdade! x Recebem-nos bem, imperativo...)
# clit_r: irregulares (fizer-me), tem que lematizar...; mesóclise apenas se o radical terminar em 'r' e a mesma observação sobre irregularidade

# Consertando verbos irregulares com passiva sintética
# Fixing irregular verbs with synthetic passive
se_irr_1 = re.sub(r'(?P<tudo>(?P<cs>\b[cs])(a|ou)b\w+)-se\S+',
                  '\g<cs>aber se/se', clit_r)
se_irr_2 = re.sub(r'(?P<tudo>(?P<ter>\w*t)[eéêi]\w+)-se\S+',
                  '\g<ter>er se/se', se_irr_1)
se_irr_3 = re.sub(r'(?P<tudo>(?P<ver>(\b(ante|p?re|entre)?v))[iêe]\w+\b)-se\S+',
                  '\g<ver>er se/se', se_irr_2)
se_irr_4 = re.sub(r'(?P<tudo>(?P<por>\w*p)[õôu]\w+)-se\S+',
                  '\g<por>or se/se', se_irr_3)
se_irr_5 = re.sub(
    r'(?P<tudo>(?P<vir>(\b(ad|inter|entre|sobre)?v))[iéêe]\w+\b)-se\S+',
    '\g<vir>ir se/se', se_irr_4)
se_irr_6 = re.sub(r'(?P<tudo>(?P<fazer>\w*f)[aei]z[ei]?(r?a)?m?)-se\S+',
                  '\g<fazer>azer se/se', se_irr_5)
se_irr_7 = re.sub(r'(?P<tudo>(?P<dizer>\w*d)i[zs]s?[ei]?(r?a)?m?)-se\S+',
                  '\g<dizer>izer se/se', se_irr_6)
se_irr_8 = re.sub(r'(?P<tudo>(?P<querer>\bqu)[ei][rs][ei]?(r?a)?m?)-se\S+',
                  '\g<querer>erer se/se', se_irr_7)
se_irr_9 = re.sub(r'(?P<tudo>(?P<dar>\bd)[eaáã][uorv]?(am?)?)-se\S+',
                  '\g<dar>ar se/se', se_irr_8)
se_irr_x = re.sub(r'(?P<tudo>\bfo(i|ram))-se\S+',
                  'ser se/se', se_irr_9) # assumindo 'ser', não 'ir'

# Consertando parcialmente passiva sintética com verbos da 1ª-2ª conjugações(4)
# Partially fixing synthetic passive with verbs of the 1st-2nd conjugations(4)
se_reg = re.sub(r'(?P<tudo>(?P<rad>\w+[ea])m?-se\b)\S+',
                '\g<tudo>/\g<rad>r se/se', se_irr_x) #'e': infere-se -> inferer
# Limitações do 'a': lava-se x falava-se - falavar; cantaram-se x comemoram-se

# Eliminando a duplicação (misteriosa!) de 'se' em irregulares no plural
# Eliminating the (mysterious!) duplication of 'se' in plural irregular verbs
se_se = re.sub(r'(?P<se>\sse/se){2}', '\g<se>', se_reg)

# Removendo as postags e as features das tags remanescentes
# Removing the remaining postags and tag features
final_final = re.sub(r'(?P<pal_lema>[a-zA-Zá-úÁ-Ú]+(-[a-zA-Zá-úÁ-Ú]+)*/[a-zA-Zá-úÁ-Ú]+(-[a-zA-Zá-úÁ-Ú]+)*)/\S*',
                     '\g<pal_lema>', se_se)

# Removendo palavras e pontuação para gerar apenas os lemas
# Removing words and punctuation to generate only the lemmas
so_lemas = re.sub(r'[a-zA-Zá-úÁ-Ú]+/(?P<lema>[a-zA-Zá-úÁ-Ú]+)', '\g<lema>', final_final)
so_lemas = re.sub(r'\./\./punct/', '.', so_lemas)
so_lemas = re.sub(r'\S+punct/', '', so_lemas)
so_lemas = re.sub(r'/\S*', '', so_lemas)

# Imprime os lemas corrigidos
# Prints the fixed lemmas
versao_corrigida = so_lemas
if pergunta == 'f':
    print(versao_corrigida)
else:
    with open('resultados_spacy.txt', 'w') as resultados:
        resultados.write(lematizacao_spacy)
    with open('resultados.txt', 'w') as resultados:
        resultados.write(versao_corrigida)
        