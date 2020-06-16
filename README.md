# hReg-CNCC
hReg-CNCC is a high-quality Regulatory network of Cranial Neural Crest Cell (CNCC), built by consensus optimization.<br>

## Consensen Network
### Inputs
The inputs of consensus optimization are K (6) files of networks:<br>
TF　TG　Sij　FDR　CRM; Seperated by tab<br>
Examples are given in **Input** folder
### Codes
```bash
python ConsOpt.py
cat ./Results/CNCCNetwork.txt | awk '{print $4}' | tr '_' '\t' | tr ';' '\n' | sortBed > ./Results/CNCCNetwork_RE1.txt
mergeBed -i ./Results/CNCCNetwork_RE1.txt > ./Results/CNCCNetwork_RE2.txt
bedtools intersect -wa -wb -a ./Results/CNCCNetwork_RE1.txt -b ./Results/CNCCNetwork_RE2.txt | awk '{print $1"_"$2"_"$3"\t"$4"_"$5"_"$6}' > ./Results/CNCCNetwork_RE1_RE2.txt
```
## Annotating SNPs of Face GWAS
### Input
The input of SNP annotation is GWAS summary statistics with p-value <= 1e-5:<br>
chr　start　end　SNP_Name　p-value　Allele1　Allele2; Seperated by tab<br>
### Codes
```bash
python AnnoFaceGWAS.py
```
## Requirements
python3 <br>
numpy <br>
bedtools <br>
