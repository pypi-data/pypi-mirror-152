# -*- coding: utf-8 -*-

"""metacerberus_hmm.py Module to find FOAM annotations using Hidden Markov Models
Uses HMMER hmmsearch
"""

import os
import subprocess
import time


## HMMER Search
def searchHMM(aminoAcids:dict, config:dict, subdir:str, CPUs:int=4):
    minscore = config['MINSCORE']
    if config['HMM']:
        hmmDB = config['HMM']
    else:
        hmmDB = os.path.join(config['PATHDB'], 'FOAM-hmm_rel1a.hmm.gz')


    hmmOut = dict()
    for key,amino in aminoAcids.items():
        path = f"{config['DIR_OUT']}/{subdir}/{key}"
        os.makedirs(path, exist_ok=True)

        name = os.path.basename(amino)
        name_dom = os.path.splitext(name)[0] + "_tmp.hmm"
        hmmOut[os.path.join(path, name_dom)] = amino

    jobs = dict()
    outlist = list()
    for domtbl_out,amino in hmmOut.items():
        pathname = os.path.dirname(domtbl_out)
        basename = os.path.basename(domtbl_out)
        outname = os.path.splitext(basename)[0] + ".tsv"
        outfile = os.path.join(pathname, outname)
        if not config['REPLACE'] and os.path.exists(outfile):
            outlist.append(outfile)
            continue
        # HMMER
        try:
            #TODO: Add --keep option to save the HMMER output file
            print("target", "query", "e-value", "score", sep='\t', file=open(outfile, 'w'))
            reduce_grep = f" grep -Ev '^#' | tr -s ' ' | cut -d ' ' -f1,4,7,14 | tr ' ' '\t' >> {outfile}"
            command = f"{config['EXE_HMMSEARCH']} -o /dev/null --cpu {CPUs} --domT {minscore} --domtblout /dev/stdout {hmmDB} {amino} | {reduce_grep}"
            with open(f"{path}/stderr.txt", 'w') as ferr:
                jobs[domtbl_out] = subprocess.Popen(command, shell=True, stderr=ferr)
            outlist.append(outfile)
        except Exception as e:
            print(e)
            print("Error: failed to run: " + command)
    
    # Wait for jobs
    done = False
    while not done:
        done = True
        keys = list(jobs.keys())
        for domtbl_out in keys:
            if jobs[domtbl_out].poll() is None: # no return code yet, still running
                done = False # At least one job still running
        time.sleep(1)

    # Convet outfile to TSV to reduce size
#    outlist = list()
#    for domtbl_out in hmmOut.keys():
#        pathname = os.path.dirname(domtbl_out)
#        basename = os.path.basename(domtbl_out)
#        outname = os.path.splitext(basename)[0] + ".tsv"
#        outfile = os.path.join(pathname, outname)
#        with open(domtbl_out) as reader, open(outfile, 'w') as writer:
#            for line in reader:
#                if line.startswith("#"):        # Skip commented lines
#                    continue
#                line = line.split()
#                try:
#                    print(line[0], line[13], line[6], line[3], sep='\t', file=writer)
#                except:
#                    continue
#        outlist.append(outfile)
#        if not config['KEEP']:
#            os.remove(domtbl_out)

    return outlist
