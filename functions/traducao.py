''' Funções de conversão '''

# Função de DNA para mRNA
def dna_para_mRNA(sequencia_DNA):

    # Transcreve a sequência de DNA para mRNA através da substituição do T pelo U utilizando a função replace.

    return sequencia_DNA.replace('T', 'U')

# Função de mRNA para tRNA
def mRNA_para_tRNA(sequencia_mRNA):

    # Transcreve o mRNA para tRNA através da troca de cada nucleotídeo com seu respectivo par pelas regras de pareamento códon-anticódon
    
    dicionario_aux = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
    sequencia_tRNA = ""
    
    #Loop para iteração na variável
    for nucleotideo in sequencia_mRNA:
        if nucleotideo in dicionario_aux:
            sequencia_tRNA += dicionario_aux[nucleotideo]
        else:
            sequencia_tRNA += nucleotideo
    
    return sequencia_tRNA

# Função de mRNA e tRNA para aminoácidos
def traducao(sequencia_mRNA):

    # Traduz uma sequência de mRNA para a respectiva sequência de aminoácidos através do mapeamento da trinca de nucleotídeos (códons)  

    tabela_codon = {
        'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',  # ... Adicionar mais códons e seus respectivos aminoácidos
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'UAU': 'Y',
        'UAC': 'Y', 'UAA': '*', 'UAG': '*', 'UGU': 'C', 'UGC': 'C',
        'UGA': '*', 'UGG': 'W', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L',
        'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R',
        'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AUU': 'I', 'AUC': 'I',
        'AUA': 'I', 'AUC': 'I', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T',
        'ACG': 'T', 'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GUU': 'V',
        'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 'GCC': 'A',
        'GCA': 'A', 'GCG': 'A', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E',
        'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    sequencia_proteina = ""
    
    # Loop de iteração da lista mRNA de input com a tabela de codons, forçando a leitura por codons
    for i in range(0, len(sequencia_mRNA), 3):
        codon = sequencia_mRNA[i:i+3]
        
        if codon in tabela_codon:
            amino_acido = tabela_codon[codon]
            if amino_acido == '*':  # Stop Codon encontrado
                break
            sequencia_proteina += amino_acido
    
    return sequencia_proteina