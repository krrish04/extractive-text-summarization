from os import listdir
from os.path import isfile, join
import ts

inputSentences = 5

mypath = "./Paragraphs"
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for file in files:
    summary = ts.generate_summary("./Paragraphs/"+file, inputSentences)
    text = "Summary: \n", ". ".join(summary)
    targetfile = open("./Summaries/Summary_"+file,"w")
    targetfile.writelines(text)
    targetfile.close()