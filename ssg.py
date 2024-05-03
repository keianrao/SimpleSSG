#!/usr/bin/env python3

from sys import argv, stderr;
import traceback;
import re;

def handle_files(filenames):
	for filename in filenames:
		try:
			handle_file(filename);
		except Exception:
			traceback.print_exc();
			continue;
	
	
def handle_file(filename):
	if not arg.endswith(".thtml"):
		msg = "File " + arg + " is not a thtml file.";
		print(msg, file=stderr);
		return;
	
	with open(filename, "r") as ifile:
		ofilename = change_extension(filename, ".html");
		with open(ofilename, "w") as ofile:
			fill_template(ifile, ofile);


def fill_template(ifile, ofile):
	include_pat = re.compile("^#include \"(.*)\"$");
	for line in ifile:
		match = include_pat.match(line):
		if match:
			imfilename = match[1];
			with open(imfilename, "r") as imfile:
				for line in imfile: print(line, file=ofile);
		else: print(line, file=ofile);
	
	
def change_extension(filename, new_ext):
	odot = filename.rindex(".");
	return filename[:odot] + "." + new_ext;


if __name__ == "__main__": handle_files(argv[1:]);
