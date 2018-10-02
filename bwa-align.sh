#!/bin/bash

#Objective: find conserved regions to construct primers for FISH

mkdir bwa_elementos || continue
cd bwa_elementos

bwa index -p CR1-repbase-06-10-2015.fa ../CR1-repbase-06-10-2015.fa
wait

bwa mem -t 10 CR1-repbase-06-10-2015.fa ../picoides-CR1.fasta > picoides-CR1.sam
wait

samtools view -bS picoides-CR1.sam > picoides-CR1.bam
wait
