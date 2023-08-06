#!/bin/bash

bwa mem chr7.fa $1.fastq | samtools sort > $1.bam;
samtools index $1.bam
bcftools mpileup -Ou -f chr7.fa -r chr7:55000000-55200000 $1.bam | bcftools call -mv -Ob -o calls_$1.bcf
bcftools view -I calls_$1.bcf | bgzip -c > calls_$1.vcf.gz
bcftools index calls_$1.vcf.gz
bcftools norm -f chr7.fa calls_$1.vcf.gz -Ob -o calls_$1.norm.bcf
bcftools filter --IndelGap 5 calls_$1.norm.bcf -Ob -o calls_$1.norm.flt-indels.bcf
cat chr7.fa | bcftools consensus --mark-del D calls_$1.vcf.gz > consensus_$1.fa
cat consensus_$1.fa | tr -d '\n' > consensus_$1.txt