# extract_IP
 This is a simple program that parses the Source and Destination IP addresses from a WireShark capture text file.

This is a program written for a school assignment. 
University of Arizona APCV 320 11-25-2020

The difficulty in this problem came with parsing the correct line from wireShark.txt

The target line occurs directly after the same key line in every occurenece,
Therefore I needed to identify the key and then target the line directly after for the data.

Additionally, I explored many ways to store the ipaddresses once they were parsed, I contemplated dictionaries, list of lists, ultimately went with list of tuples because it was best suited for this situation for writing my ouput.
