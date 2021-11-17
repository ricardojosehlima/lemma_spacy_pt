# lemma_spacy_pt_3
Set of rules designed to improve the lemmatization process in Spacy for portuguese 

pt-br

17/11/2021: totalmente atualizado, revisto e re-estruturado.
- correções sobre números, verbos com ênclise, verbos irregulares, entre outras situações.
- as substituições a serem feitas na lematização do Spacy aparecem em um arquivo separado, que deve ser baixado para realização do import das substituições.

O programa toma como base a lematização feita pelo Spacy (funciona nas versões 3.0, 3.1 e 3.2) e aplica uma série de regras para gerar uma lematização mais próxima do padrão.

Você pode testar usando um arquivo. O resultado sairá gerado em um arquivo com os resultados.

Como exemplo, a frase:

"Uma empresa não é como uma família."

"Uma* empresar* não ser comer* umar* família" (lematização do Spacy)

"um empresa não ser como um família" (lematização após as regras)

Obs.: * O artigo "Uma" não foi transformado; o substantivo "empresa" se tornou o verbo inexistente "empresar"; a preposição "como" se tornou o verbo "comer"; e o artigo "uma" se transformou no verbo inexistente "umar"

Em um corpus de 861 lemas, a acurácia subiu de 80,5% para 97,3% 


en

17/11/2021: updated, reviewed and restructured.
- corrections of numbers, verbs with enclisis, irregular verbs and other situations.
- the substitutions to be applied on the lemmatization provided by Spacy appear in a separate file, that must also be downloaded in order for the import to work.

Taking as starting point,the output of lemmatization provided by Spacy (works on versions 3.0, 3.1 and 3.2), a set of rules was built to generate lemmas that are closer to the standard.

It is possible to test using a file. The result will appear on a file with the results generated.

As an example, take the sentence below:

"Uma empresa não é como uma família."

"Uma empresar não ser comer umar família" (lematização do Spacy)

"um empresa não ser como um família" (lematização após as regras)

In a corpus of 861 lemmas, accuracy raised from 80,5% to 97,3% 

Obs.: * The determiner "Uma" did not receive a lemma; the lemma for the noun "empresa" became the non-existent verb "empresar"; the one for the preposition "como" became the verb "comer"; and for the determiner "uma", the lemma generated was the non-existent verb "umar"
