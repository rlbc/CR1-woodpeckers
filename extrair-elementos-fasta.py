#!/usr/bin/python
# -*- coding: utf-8 -*-
from subprocess import call
from os import mkdir
from Bio import SeqIO
import sys

f_terminal = sys.argv[1]

def gravar(entrada):
    #Ids tem a composição "Elemento#Classe Local"
    #Extrai a informação Elemento#Classe e a usa como nome de arquivo
    id = entrada.id.split()[0].replace('/', '-')
    f_out = open('elementos/' + id + '.fasta', 'a')

    f_out.write('>' + entrada.id + '\n')
    f_out.write(str(entrada.seq) + '\n')

    f_out.close()

def separaElementos(elem):
    #Grava todas as sequências que apresentam ELEMENTO no id.
    for item in fasta_seqs:
        if elem in item.id:
            SeqIO.write(item, f_out, 'fasta')
            gravar(item)

def gravaElementos():
    for item in fasta_seqs:
        SeqIO.write(item, f_out, 'fasta')
        gravar(item)

#Se o arquivo FASTA já existir, abre; senão cria ele.
try:
    fasta_seqs = SeqIO.parse(open(f_terminal, 'r'), 'fasta')
except IOError:
    call(["cat `find ./onescript/ -name '*.fasta'` > f_terminal"], shell=True)
    fasta_seqs = SeqIO.parse(open(f_terminal, 'r'), 'fasta')

try:
    mkdir('elementos')
except OSError:
    pass

#Abre o arquivo de saida.
try:
    f_out = open('elementos.fasta', 'w')
except IOError:
    pass

gravaElementos()

f_out.close()
