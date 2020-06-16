# hReg-CNCC
hReg-CNCC is a high-quality Regulatory network of Cranial Neural Crest Cell (CNCC), built by consensus optimization.<br>

## Consensen Network
### Inputs
The inputs of consensus optimization are K (6) files of networks:<br>
TF  TG  Sij FDR CRM; Seperated by tab<br>
Examples are given in **Input** folder
### Codes
```bash
python ConsOpt.py
```
## Annotating SNPs of Face GWAS
### Input
The input of SNP annotation is GWAS summary statistics with p-value <= 1e-5:<br>
chr  start  end  SNP_Name  p-value; Seperated by tab<br>
### Codes

## Requirements
python3 <br>
numpy <br>
bedtools <br>
