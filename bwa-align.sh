#!/bin/bash

#Builds a bowtie index with CR1 elements downloaded from repbase 06/10/2015
#Aligns with --very-sensitive all the CR1 elements extracted from assembled genome to CR1 consensus database
#Objective: find conserved regions to construct primers for FISH

mkdir bwa_elementos || continue
cd bwa_elementos

bwa index -p CR1-repbase-06-10-2015.fa ../CR1-repbase-06-10-2015.fa
wait

bwa mem -t 10 CR1-repbase-06-10-2015.fa ../picoides-CR1.fasta > picoides-CR1.sam
wait

samtools view -bS picoides-CR1.sam > picoides-CR1.bam
wait

#N=0
#MAXJOBS=3
#for FILE in ../elementos/*.fasta
#do
#  bwa mem -t 10 CR1-repbase-06-10-2015.fa $FILE > ${FILE}.sam
#  wait
#  samtools view -bS ${FILE}.sam > ${FILE}.bam
#  if (( $(($((++N)) % $MAXJOBS)) == 0 )) ; then
#    wait # wait until all have finished (not optimal, but most times good enough)
#    echo $N wait
#  fi
#done

#cd ../elementos
#mv *.sam ../bwa_elementos
#mv *.bam ../bwa_elementos
