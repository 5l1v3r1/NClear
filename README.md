# NClear
Cleares Nmap Output files. Removes failed scripts, verbose information, [...]   
Mostly useful for scanning networks, and getting a quick vuln overview


Usage:  
`
python3 nclear.py --file <nmap_output.txt> `   

Optional arguments:  
` --vulns`  
Shows only hosts that have identified vulnerable Services  
`--style2`  
Different printing style,
Removes the `|` at the beginning of each line.
