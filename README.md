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
bedtools intersect -wa -wb -a ./Input/FaceDisGWAS_e5.bed -b ./Results/CNCCNetwork_RE1.bed > FaceDisGWAS_SNP_RE.txt
for RE in `cat FaceDisGWAS_SNP_RE.txt | awk '{print $11}'`
do
  cat ./Results/CNCCNetwork.txt | grep $RE >> a
done
sort -k3nr a > FaceDisGWAS_Net_Sorted.txt; rm -f a;
python AnnoFaceGWAS.py
```
The output file is **FaceDisGWAS_Net_Filtered.txt**, which can be used for visualization and further analysis.<br>

## Requirements
python3 <br>
numpy <br>
bedtools <br>
