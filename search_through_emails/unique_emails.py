import os 
import re 
import argparse

# constants to determine how data is extracted
SEPERATOR = ";"
# regex that should be contained in the email / description
MUST_CONTAIN = "joe"
OUT_FILE = "emails.txt"

class Extractor():
    def __init__(self, args):
        """
        Read and save the flags parsed on the console.
        """
        self.files = args.file
        self.is_multiple_files = len(args.file) > 1
        self.debug = args.debug
        self.is_print = args.is_print

        self.sep = SEPERATOR
        self.must_contain = re.compile(MUST_CONTAIN)
        self.out_file = OUT_FILE

        self.results = []

    def add_valid_candidates(self, candidates: list):
        for cand in candidates:
            # if the candidate contains the regex, that it should contain
            if re.search(self.must_contain, cand):
                # check if the entry is already in the result array
                if cand not in self.results:
                    self.results.append(cand)

    def extract(self):
        for f_path in self.files:
            print(f"reading file {f_path}...")
            with open(f_path, 'r') as f:
                content = f.read()
                content_l = content.split(self.sep)
                if self.debug:
                    print("Extracted list:\n", content_l)
                self.add_valid_candidates(content_l)
        
        # after all file were read and analysed
        with open(self.out_file, "x") as out:
            # result string
            if self.debug:
                print("concatenating results", self.results, "with seperator", self.sep)
            print(f"Writing results to {self.out_file}")
            out_string = self.sep.join(self.results)
            out.write(out_string)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Flags
    parser.add_argument("-f", "--file", action="append", help="the file(s) from which the data is read.\
        You can use this flag multiple times, if you want to search all files for unique entries .", type=str)
    parser.add_argument("-d", "--debug", dest='debug', action='store_true', help="Set this option to get debugging information. Default: false")
    parser.set_defaults(debug=False)
    parser.add_argument("-p", "--print", dest='is_print', action='store_true', help="Set this flag if you want to get the email printed out to the console instead of writing it to a file. Default: false")
    parser.set_defaults(is_print=False)
    args = parser.parse_args()

    ex = Extractor(args)
    ex.extract()
