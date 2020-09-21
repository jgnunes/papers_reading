# Article  
Haplotype-resolved de novo assembly with phased assembly graphs ([link here](https://arxiv.org/pdf/2008.01237.pdf))  

# Authors  
* Haoyu Cheng 
* Gregory T Concepcion
* Xiaowen Feng
* Haowen Zhang
* Heng Li


# Journal and Year  
arXiv (2020)  

# Highlights  
## 1. Primary vs alternate assembly  
* It produces a pair of assemblies, one **primary** assembly representing a mosaic of homologous haplotypes, and one **alternate** assembly composed of short haplotype-specific contigs (haplotigs) for alleles absent from the primary assembly. 
* The alternate assembly is often fragmented and does not represent a complete haplotype, making it less useful in practice.

## 2. On HiCanu (a competitor) limitations   
* However, HiCanu only tries to keep the contiguity of one parental haplotype and often breaks the contiguity of the other haplotype. When we separate parental haplotypes, these break points will lead to fragmented haplotype-resolved assemblies. HiCanu is not making use of the full power of HiFi reads.  

## 3. Hifiasm algorithm  


# New tools to take a look  
* 

# Questions  
* 


