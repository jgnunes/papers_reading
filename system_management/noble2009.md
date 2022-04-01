# Article  
A Quick Guide to Organizing Computational Biology Projects ([link here](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424))  

# Authors  
* William Stafford Noble

# Journal and Year  
Plos Computational Biology (2009)  

# Tags
filesystem, organization, directory, files

# Principles  
* Someone unfamiliar with your project should be able to look at your computer files and understand in detail what you did and why.
* Everything you do, you will probably have to do over again.
    * After discovering some flaw in your initial preparation of the data being analyzed
    * After getting access to new data
    * etc

# File and Directory Organization  

![image](https://user-images.githubusercontent.com/22843614/161320877-1bd1e244-57db-4810-8048-56488a68ae45.png)
**Directory structure for a sample project.**
Directory names are in large typeface, and filenames are in smaller typeface. Only a subset of the files are shown here. Note that the dates are formatted <year>-<month>-<day> so that they can be sorted in chronological order. The source code src/ms-analysis.c is compiled to create bin/ms-analysis and is documented in doc/ms-analysis.html. The README files in the data directories specify who downloaded the data files from what URL on what date. The driver script results/2009-01-15/runall automatically generates the three subdirectories split1, split2, and split3, corresponding to three cross-validation splits. The bin/parse-sqt.py script is called by both of the runall driver scripts.
