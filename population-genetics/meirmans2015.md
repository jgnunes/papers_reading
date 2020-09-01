# Article   
Seven common mistakes in population genetics and how to avoid them ([link here](https://doi.org/10.1111/mec.13243))    

# Author  
Patrick G. Meirmans  

# Journal and Year  
Molecular Ecology (2015)

# Highlights

## 1. Giving more attention to genotyping than to sampling  
* In designing a sampling strategy, there is often a **trade-off** between sampling few populations with many individuals and sampling many populations with few individuals  
* Different statistical methods differ in how their power is affected by this trade-off  
	* For example, assignment tests depend on accurate estimates of population allele frequencies and work best with few population samples of many individuals 
	* On the other hand, for GEA (genetic-environment association) tests, many populations with few individuals are often preferable, because that will maximize the environmental variance
*  Because of these trade-offs, it is unwise to perform both types of tests in a single study as at least one of them will have insufficient power

### What to do  
* Design your sampling based on simulations specific to your study species.  
	* Many excellent tools are available for doing population genetic simulations (Hoban et al. 2012), some of which can simulate realistic geographical scenarios (Meirmans 2011) 
	* For many species, distribution data are available in public databases (e.g. gbif.org) that can be used to fit the simulated metapopulation to the study species. The simulated data can then be used (possibly together with available environmental data) to assess the performance of different types of analyses under different sampling strategies.

## 2. Failing to perform or report experimental randomization in the laboratory  
* Genotyping studies are in fact experiments. Therefore, they should be executed in a fashion that prevents bias stemming from the genotyping process: for example, if we want to test for genetic differences among populations, we should employ proper randomization of individuals over populations to prevent bias
* With next-generation sequencing studies, the coverage, and hence the degree of missing data, may vary strongly among lanes and there may be highly replicable errors in base-calling. When all individuals from one population are placed on one plate, gel or lane, and the individuals from another population on another, errors that are specific to a plate, gel or lane will lead to an overestimation of the among-population differentiation, the presence of artificial clusters and an underestimation of the migration rate.  

### What to do  
* As in every experiment, proper randomization should be employed during the genotyping in the laboratory.  
* At the most basic level, individuals from different populations should be randomized over gels.  
* In studies of spatial autocorrelation, you should also prevent that individuals or populations that are geographically close in nature are also close to each other on the genotyping plate, gel or lane  

## 3. Equating geopolitical borders with biological borders  
* (...) we often see is that a priori groups are specified that lack a solid biological reasoning  
* In practice, the groups are often made by simply dividing the sampled area into, for example, an ‘eastern’ and a ‘western’ cluster. Such groupings can even be based on purely anthropogenic factors, such as geopolitical borders  
* It is obvious that there is very little insight to be gained from such an analysis as wild species are hardly ever concerned with geopolitical borders  

### What to do  
* Rather than concentrating on ad hoc or geopolitical borders, only use tests of a priori specified structure when you have a sound biological hypothesis about the location of the border

## 4. Testing significance of clustering output  

## 5. Only interpreting a single value of k  
* Nowadays, the most popular clustering method for genetic data is STRUCTURE (Pritchard et al. 2000), where two summary statistics are used for inferring k: Ln P(D) (Pritchard et al. 2000) and DK (Evanno et al. 2005)  
	* Interestingly, these statistics have been described by their respective authors as ‘dubious at best’ and ‘ad hoc’. This indicates that generally there is a large degree of uncertainty in estimates of k and that these should be taken with a generous helping of salt 

### What to do  
* A clustering analysis is by nature a type of exploratory analysis, which makes it more open to interpretation at multiple levels; STRUCTURE is actually used in such a way in the original paper describing the method (Pritchard et al. 2000).  
* Of course you should also observe some prudence to prevent overinterpretation: only patterns with a clear biological explanation should be considered
* (...) it is better to have a biologically interpretable pattern from a ‘suboptimal’ k than a completely unrealistic pattern from the ‘optimal’ k  
* In contrast, there are also cases where there is a clear a priori expectation about k; in such cases, it may be unnecessary to interpret multiple values of k  
	* This is, for example, the case when explicitly analysing the hybridization and admixture between a number of well-established species 

## 6. Misinterpreting Mantel's r statistic  

## 7. Forgetting that only a small portion of the genome will be associated with climate  
*  Given that the probability of finding loci under selection is quite low, most GEA tests are unlikely to uncover any genes at all that are directly under selection  
* However, this is not what we see in studies that use GEA tests: it is not uncommon for AFLP or RAD tag studies to find that around 5% of the markers are putatively under environmental selection (unsurprisingly, close to the used alpha level to assess significance)
* Are we then to believe that 5% of randomly sampled variation across the genome, which is largely nonfunctional, is showing adaptation for exactly the climatic variables that the authors are studying? I find that hard to swallow as genomewide association studies, which are much more powerful than genome scans, usually only find a handful of genes

## Conclusions  
* When interpreting the results, it is important to focus more on biological relevance than on statistical significance
* That does not mean that significance is unimportant; results that have a straightforward interpretation but are not significant should not be considered 
* On the other hand, one should not be blinded by results that are strongly significant. In the genomics era, with thousands upon thousands of loci, strong significance is easily obtained even for biologically marginal processes
