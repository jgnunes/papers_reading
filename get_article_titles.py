import os  

def get_title(file_name):
	"""Returns the title of a research article  

	Returns the title of a research article given a markdown (*.md) file with its highlights.
	
	Usage  
	-----
	python get_article_titles.py

	Parameters 
	----------  
	file_name: str 
		Name of the markdown file containing the article highlights

	Returns 
	-------
	str
		The title of the research article
	"""
	is_article_title = False

	with open(file_name, 'r', encoding='utf-8') as f:
		for line in f:
			if is_article_title:
				return line.strip()

			if "# Article" in line:
				is_article_title = True
			else:
				is_article_title= False


for subdir, dirs, files in os.walk(os.getcwd()):
	dirs.remove(".git")
	break

with open("output_md_table.txt", 'w') as f:
	for dire in dirs:
		f.write("".join(["## ", dire,"\n"]))
		f.write("|File Name|Article Title|\n")
		f.write("|---------|-------------|\n")
		for filename in os.listdir(os.path.join(os.getcwd(), dire)):
			if filename.endswith(".md"):
				file_title = get_title(os.path.join(dire, filename))
				f.write("".join(["|", filename, "|", file_title, "|", "\n"]))	
