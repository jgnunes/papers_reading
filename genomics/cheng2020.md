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
* It (Falcon-unzip) produces a pair of assemblies, one **primary** assembly representing a mosaic of homologous haplotypes, and one **alternate** assembly composed of short haplotype-specific contigs (haplotigs) for alleles absent from the primary assembly. 
* The alternate assembly is often fragmented and does not represent a complete haplotype, making it less useful in practice.

## 2. On HiCanu (a competitor) limitations   
* However, HiCanu only tries to keep the contiguity of one parental haplotype and often breaks the contiguity of the other haplotype. When we separate parental haplotypes, these break points will lead to fragmented haplotype-resolved assemblies. HiCanu is not making use of the full power of HiFi reads.  

## 3. Hifiasm algorithm  

<img src="https://user-images.githubusercontent.com/22843614/93812829-88121800-fc28-11ea-9cc0-b51dd48d259e.png" width=70%></img>  

**Figure 1. Outline of the hifiasm algorithm.** Reads in orange and blue represent the reads with heterozygous alleles carrying local phasing information, while reads in green come from the homozygous regions without any heterozygous alleles. In phased string graph, a vertex corresponds to the HiFi read with same ID, and an edge between two vertices indicates that their corresponding reads are overlapped with each other. Hifiasm first performs haplotype-aware error correction to correctsequence errors but keep heterozygous alleles, and then builds phased assembly graph with local phasing information from thecorrected reads. Only the reads coming from the same haplotype are connected in the phased assembly graph. With complementary data providing global phasing information, hifiasm generates a completely phased assembly for each haplotype from the graph. Hifiasm also can generate unphased primary assembly only with HiFi reads. This unphased primary assemblyrepresents phased blocks (regions) that are resolvable with HiFi reads, but does not preserve phasing information between two phased blocks.

## 3.1 Haplotype-aware error correction  
* First, hifasm loads all reads into the memory and performs an all-vs-all pairwise alignment between them;  
* Given a reference read *R*, hifiasm collects all mismatches from the paiwise alignment between *R* and its overlapping reads;  
* If one mismatch is supported by **three** overlapping reads, hifiasm takes it as a SNP, otherwise it would be ignored as a sequencing error;   
* For a read *Q* overlapped with *R*, we consider *Q* to come from the same haplotype as *R* if there is no difference on SNP sites between *R* and *Q*;  
* The sequencing errors on each read are then corrected by the consensus method from pairwise alignment.  

## 3.2 

# New tools to take a look  
* 

# Questions  
* 


