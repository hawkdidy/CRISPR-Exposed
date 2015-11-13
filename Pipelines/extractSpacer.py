import os
import re

data = "../Data/"

crt_re = re.compile('.*\.crt\.report')
dir_list = os.listdir(data)

#no_result_re = re.compile('No CRISPR elements were found')

for genome_dir in dir_list:
    genome_dir_list = os.listdir(data + genome_dir)
    
    for _file in genome_dir_list:
        crt_report_file_name = re.search(crt_re, _file)
        
        if(crt_report_file_name):
            path_to_crt_report = data + genome_dir + '/' + crt_report_file_name.group()
            crt_report_file = open(path_to_crt_report, 'r')
            #if(re.search(no_result_re, crt_report_file.read())):
             #   crt_report_file.close()
                #continue

            crt_report_file = open(path_to_crt_report, 'r')
            crtOutput = crt_report_file.readlines()
            
            ls = []
            for line in crtOutput:
                i = line.rstrip("\n").split("\t")
                ls.append(i)
                
            
            # regex for position 
            positionRegex = re.compile("^[0-9]+$")
            nucleotideRegex = re.compile("^[ACTG]+$")
            
            
            # crisprls = [position, repeat, spacer, [repeat_length, spacer_length]]
            crisprls = []
            for entry in ls:
                if bool(re.match(positionRegex, entry[0])) == True:
                    line = []
                    if bool(re.match(nucleotideRegex, entry[3])) == True:
                        line.extend([entry[0], entry[2], entry[3], entry[4]])
                        crisprls.append(line)
            
            if(crisprls):
                spacerout_file = open(path_to_crt_report + ".spacers", 'w')
                spacerout_file.write(str(crisprls))
                spacerout_file.close()
            
            crt_report_file.close()
