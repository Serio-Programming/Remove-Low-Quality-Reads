# Remove-Low-Quality-Reads
# A Program by Tyler Serio

# What is it?
Remove Low Quality Reads

# What does it do?
This program removes low quality reads from FASTQ files.

# How does it do it?
This program steps through every line of a FASTQ file, recording each of the four lines that make up a sequence. It reads the fourth line for quality scores, and if too many of those quality scores are low, that sequence gets written to one file while higher quality sequences get written to another file.

# Why was it written?
DNA was taken from an archaeological site in Vero Beach. This DNA was sequenced with the intent of megablasting these sequences to learn more about the organisms present at the archaeological site several thousand years ago. This program was created to address the issue in data preprocessing of FASTQ files having reads that were not a high enough quality for a good megablast. 
