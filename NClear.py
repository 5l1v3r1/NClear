from os import system
import sys
import argparse



class NmapParser:
    def __init__(self,arguments):
        self.remove_list = [
                       'Script execution failed (use -d to debug)',
                       'Couldn&apos;t',
                       'not currently vulnerable',
                       '(401 Unauthorized)',
                       'samba-vuln-cve-2012-1182: NT_STATUS_ACCESS_DENIED',
                       'smb-vuln-ms10-054: false',
                       'smb-vuln-ms10-061: NT_STATUS_ACCESS_DENIED',
                       'ssl-ccs-injection: No reply from server (TIMEOUT)',
                       'NSE',
                       'Not shown:'
                       'Host is up'
                       'Could not negotiate a connection'
                       'Failed to receive bytes'
                       'Read data files from:'
                       'Service detection performed.'
                       'Nmap done:'
                       'EOF'
                       '|_samba-vuln-cve-2012-1182: Could not negotiate a connection:SMB: Failed to receive bytes: EOF'
                       '</pre>'
                      ]
                       
    def block_parser(self, block):
        if "Host is up" in block:
            block_lines = block.splitlines()
            
            for line in block_lines:                                # Remove Non-Vulnerable Output
                print_line = True
                for string in self.remove_list:
                    if string in line or string == line:
                        print_line = False
                if print_line:
                    print(line)     

    def run(self):
        with open(args.file, "r") as output:
            lines = output.read()
            blocks = lines.split("Nmap scan report for ")                   # Divide into Blocks
            for block in blocks:
                if args.vulns:
                    if "VULNERABLE:" in block:
                        self.block_parser(block)
                else:
                    self.block_parser(block)

                
                print("\n\n--------------------------------------------------------------\n\n")
        
        
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "An Nmap Parser Attempt")
    parser.add_argument('--vulns', required=False, action="store_true", dest="vulns", help="Only print hosts that have vulnerabilities")
    parser.add_argument('--file', required=True, dest="file", help="Nmap Output File to parse")
    args = parser.parse_args()
    
    parser = NmapParser(args)
    parser.run()
