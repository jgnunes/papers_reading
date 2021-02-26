# Article  
Practical Computational Reproducibility in the Life Sciences ([link here](https://www.sciencedirect.com/science/article/pii/S2405471218301406))  

# Authors  
* Björn Grüning et al.

# Journal and Year  
Cell Systems (2018)  

# Highlights  
## On Conda limitations  
"While Conda and Bioconda provide an excellent solution for packaging software components and their dependencies, archiving them, and recreating analysis environments, they are still dependent on and can be influenced by the host computer system"  

"Moreover, since Conda packages are frequently updated, if a Conda virtual environment is created by specifying only the top-level tools and versions, recreating it at a later point in time using the same specifications may easily result in slightly different dependencies being installed."  

## On Containers advantages over Conda  
"An additional level of isolation to solve this problem is provided by containerization platforms (or, simply, containers), such as Docker (https://www.docker.com), Singularity (Kurtzer et al., 2017), or rkt (http://coreos.com/rkt)."

"Containers are run directly on the host operating system’s kernel but encapsulate every other aspect of the runtime environment, providing a level of isolation that is far beyond of what Conda environments can provide."  

"Containers are easy to create, which is a great strength of this technology. Yet it is also its Achilles’ heel, because the ways in which containers are created need to be trusted and, again, reproducible."

# New tools to take a look  

# New data types to take a look  

# Questions  
