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

**Figure 1. Outline of the hifiasm algorithm.** Reads in orange and blue represent the reads with heterozygous alleles carrying local phasing information, while reads in green come from the homozygous regions without any heterozygous alleles. In phased string graph, a vertex corresponds to the HiFi read with same ID, and an edge between two vertices indicates that their corresponding reads are overlapped with each other. Hifiasm first performs haplotype-aware error correction to correct sequence errors but keep heterozygous alleles, and then builds phased assembly graph with local phasing information from thecorrected reads. Only the reads coming from the same haplotype are connected in the phased assembly graph. With complementary data providing global phasing information, hifiasm generates a completely phased assembly for each haplotype from the graph. Hifiasm also can generate unphased primary assembly only with HiFi reads. This unphased primary assembly represents phased blocks (regions) that are resolvable with HiFi reads, but does not preserve phasing information between two phased blocks.

## 3.1 Haplotype-aware error correction  
* First, hifasm loads all reads into the memory and performs an all-vs-all pairwise alignment between them;  
* Given a reference read *R*, hifiasm collects all mismatches from the paiwise alignment between *R* and its overlapping reads;  
* If one mismatch is supported by **three** overlapping reads, hifiasm takes it as a SNP, otherwise it would be ignored as a sequencing error;   
* For a read *Q* overlapped with *R*, we consider *Q* to come from the same haplotype as *R* if there is no difference on SNP sites between *R* and *Q*;  
* The sequencing errors on each read are then corrected by the consensus method from pairwise alignment.  

## 3.2 Constructing phased assembly graphs  
* With nearly error-free reads, hifiasm is able to perform phasing accurately to determine if one overlap is among the reads coming from different haplotypes (i.e. inconsistent overlap);  
* The next step is to build the assembly string graph  
    * In this graph, nodes represent oriented reads and each edge between two nodes represents the overlap between the corresponding two reads; 
    * Note that only **consistent** overlaps are used to build the graph;
    * Most existing assemblers aim to produce one contiguous contig from the graph (i.e. single path in the graph) as much as possible. They tend to collapse bubbles when building the assembly graph. As a result, they will **lose** all but one **allele** in each bubble. In contrast, hifiasm is designed to **retain all bubbles** on the assembly graph;  
* Owing to the fact that there are still a few errors at the corrected reads, hifiasm adopts a topological-aware graph cleaning strategy to cut too short overlaps and avoid destroying substructures embedding local phasing information like bubbles;  

## 3.3 Constructing a primary assembly  
* The construction of the primary assembly aims to produce contigs including **one set of haplotypes** but may **switch subregions between haplotypes**;  
    * In other words, each subregion in the primary assembly only comes from one haplotype, while the corresponding subregions of other haplotypes are removed as duplications
* First, each bubble in the graph is reduced into a single path using bubble popping;  
    * This step removes most duplicated subregions on different haplotypes without hampering the contiguity of primary assembly  
* Second, given a tip unitig *T* (Figure 3) that is broken in one end but connected to a unitig *C* in another end, hifiasm checks if there are other contigs, which are also connected to *C*, coming from the different haplotypes of *T*. If such contigs are identified, hifiasm removes tip *T* so that that unitig *C* will become longer  
    * The reason is that for *T*, its corresponding region from different haplotype has already been integrated into the new longer unitig *C*  
 * Last, hifiasm uses the “best overlap graph” strategy to deal with a few remaining unresolvable hard substructures on the assembly graph;  
 * In most cases, the graph topological information and the phasing information is more reliable than only keeping the longer overlaps. As a result, hifiasm is able to generate a **better primary assembly** than current assemblers which mainly rely on “best overlap graph” strategy

<img src="https://user-images.githubusercontent.com/22843614/93936404-887be300-fcfc-11ea-92f7-0a2fab04541a.png" width="50%"></img>  

**Figure 3. Example hifiasm and HiCanu assembly graphs.** The graphs were generated from HG002 reads mapped to chr11:19,310,012-21,493,943. Red bars correspond to unitigs matching the maternal haplotype, blue to paternal, grey to homozygous unitigs present on both parental haplotypes, and pink bars correspond to wrongly phased unitigs that join paternal and maternal haplotypes.

# New tools to take a look  
* 

# Questions  
* 


