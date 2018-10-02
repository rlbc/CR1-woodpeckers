#!/usr/bin/python
# -*- coding: utf-8 -*-

#This script separates all CR1 elements.

from subprocess import call
from os import mkdir
from Bio import SeqIO

def gravar(entrada):

    f_out = open('elementos/' + entrada.id.split('|')[-1] + '.fasta', 'a')

    f_out.write('>' + entrada.id + '\n')
    f_out.write(str(entrada.seq) + '\n')

    f_out.close()

#If the file all.picoides.fasta already exists, oppens it; if not, creates.
try:
    fasta_seqs = SeqIO.parse(open('all.picoides.fasta', 'r'), 'fasta')
except IOError:
    call(["cat `find ./onescript/ -name '*.fasta'` > all.picoides.fasta"], shell=True)
    fasta_seqs = SeqIO.parse(open('all.picoides.fasta', 'r'), 'fasta')

try:
    mkdir('elementos')
except OSError:
    pass

#Oppens exit file.
try:
    f_out = open('picoides-CR1.fasta', 'w')
except IOError:
    pass

#Saves all sequences that have CR1 in the id.
for item in fasta_seqs:
    if 'CR1' in item.id:
        SeqIO.write(item, f_out, 'fasta')
        gravar(item)

f_out.close()
