# Manipulate PDF documents with PyPDF4

You work in IT for a law office which is litigating a massive civil lawsuit. You've been put in charge of more _two million_ PDF documents that are critical to the case and asked to sort them and count the number of pages in each. It's urgent, because a court date has been set and the judge doesn't tolerate excuses. Worse, you've been told to remove certain pages from each PDF because they contain information that could be prejudicial.

With a little effort, you arrange the documents and place them into folders. It's easy to count the number of PDFs in each folder. You can open individual documents and count the number of pages, but with more than 2,000,000 PDFs to deal with, you'll need months to do that. On top of that, the thought of opening each and every document in a PDF editor and manually removing pages is overwhelming.

You need help. You need [PyPDF4](https://pypi.org/project/PyPDF4/).

## Install PyPDF4

**PyPDF4** is an open-source library for manipulating PDF documents in Python. It has functions for extracting title, author, and other information from PDFs, splitting documents into pages, merging documents, cropping pages, encrypting and decrypting documents, and more. It was authored by [Cameron Laird](https://pypi.org/user/claird/) and is offered under the BSD license. With **PyPDF4**, just two lines of code are sufficient to count the number of pages in a PDF (three if you count the line that closes the file):

```python
reader = PyPDF4.PdfFileReader(open("pdfDocument", "rb"))
number_of_pages = reader.numPages
reader.close()
```


Like any Python package, **PyPDF4** must be installed before it can be used. In a Command Prompt window or terminal, execute the following command to install it:

```bash
python3.6 -m pip install PyPDF4
```

You're set. Let's start on those 2,000,000 documents and make sure there's time left over for a well-deserved vacation.

## Count pages in documents

The first order of business is to write a simple Python app that recursively enumerates the PDFs in a folder and its subfolders and prints the title of each document and the number of pages in each.

1. Use your favorite text editor to create a file named **count-pages.py** and paste the following code into it:

	```python
	import glob
	import PyPDF4
	
	top = "toplevelfolder"
	for pdf_filename in glob.iglob(f"{top}/**/*.pdf", recursive=True):
	    try:
	        reader = PyPDF4.PdfFileReader(open(pdf_filename, "rb"))
	    except PyPDF4.utils.PdfReadError:
	        # Certain applications, including scanners, often produce
	        # non-conformant PDF. Just skip them, for now.
	        print(f"Document {pdf_filename} appears to follow a specification "
	              "PyPDF4 doesn't yet know.")
	        continue
	    print(f"{pdf_filename} has {reader.numPages} pages.")
	```

	This code uses Python's [`glob`](https://docs.python.org/3/library/glob.html) module to enumerate files and folders. It opens each PDF that it finds and uses `numPages` to get a page count.

	> Cameron: Does each file need to be closed as well?

1. Now find a folder on your hard disk that holds several PDFs (they don't have to be in the folder itself; they can be in subfolders, too) and execute the following command, replacing PATH with the path to the folder:

	```bash
	python count-pages PATH
	```

1. Confirm that every PDF in the target folder and its subfolders is listed, along with a page count:

	```
    2015.pdf has 7 pages.
    Kansas.pdf has 49 pages.
    Springfield.pdf has 421 pages.
    credits.pdf has 14 pages.
    ger.pdf has 33 pages.
    metadata.pdf has 2 pages.
    simplified.pdf has 54 pages
    traditional.pdf has 16 pages.
    ```

This program takes hours — not months — to produce two million lines of output. That's a step in the right direction. But there is more to do.

## Extract pages from documents

Have you ever needed to print a PDF document without the cover page, with two copies of the signature page, and without the appendix? The next program will do that and more. Used in a script, it is perfectly capable of chewing through 2,000,000 legal documents as well.

1. Create a file named **extract-pages.py** and paste the following code into it:

	```python
	import sys
	from PyPDF4 import PdfFileReader, PdfFileWriter
	
	def extract_to(source_handle, destination_handle, page_numbers):
	    ''' The actual work of copying pages from source PDF to target PDF happens here.
	        Notice that PyPDF4 makes the coding almost trivially brief.
	        
	        page_numbers is a list of one-based page numbers.
	    '''
	    for page_number in page_numbers:
	        # PyPDF4 treats pages as zero-based.
	        destination_handle.addPage(source_handle.getPage(page_number - 1))
	
	def main():
	    ''' PyPDF4 does so much for us that the hardest programming in this little
	        utility has to do with parsing the command line.
	    '''
	    (source_handle, destination_handle,
	     destination_filename, page_numbers) = parse_commandline()
	    extract_to(source_handle, destination_handle, page_numbers)
	    write_result(destination_handle, destination_filename)
	
	def parse_commandline():
	    '''
	        Return a quadruple, of which the last element is a list of integer
	        1-based page numbers.  Example:  a third command-line argument of
	            pages=1-3,5,8,11-14
	        becomes the list
	            [1, 2, 3, 5, 8, 11, 12, 13, 14]
	        
	        Possible improvements for the future:
	        * recognize
	              page=7
	          in place of
	              pages=7
	        * allow more freedom in formatting, perhaps including whitespace
	        * interpret ranges more expressively, so that, for instance, '9-7'
	          could mean the same as '9,8,7', rather than just being empty.
	    '''
	    args = sys.argv
	    page_prefix = "pages="
	    example_cmd = (f"\n\t{args[0]} <SOURCE_PDF> "
	                   f"<DESTINATION_PDF> {page_prefix}<PAGE_NUMBERS>.")
	    if len(args) != 4:
	        print("Make sure you include 3 arguments, rather than "
	              f"{len(args) - 1}:{example_cmd}")
	        sys.exit(1)
	    source_filename, destination_filename, pages_arg = args[1:]
	    if pages_arg.startswith(page_prefix):
	        pages_arg = pages_arg[len(page_prefix):]
	    else:
	        print(f"Make sure you format the page numbers as indicated:{example_cmd}")
	        sys.exit(1)
	    destination_handle = PdfFileWriter()
	    source_handle = PdfFileReader(open(source_filename, "rb"))
	    page_numbers = []
	    for page_part in pages_arg.split(','):
	        page_range = page_part.split('-')
	        if len(page_range) == 2:
	            for page in range(int(page_range[0]), int(page_range[1]) + 1):
	                page_numbers.append(page)
	        else:
	            page_numbers.append(int(page_range[0]))
	    return (source_handle, destination_handle, destination_filename,
	            page_numbers)
	
	def write_result(destination_handle, destination_filename):
	    destination_handle.write(open(destination_filename, "wb"))
	
	if __name__ == '__main__':
	    main()
	```

	Once more, **PyPDF4** does the heavy lifting. The bulk of the code deals with parsing the command line to determine precisely which pages should be copied from the source document to the output document. Once that's determined, the `extract_to()` function does most of the work, and even it contains just two lines of code (not counting comments) consisting of a `for` loop and calls to **PyPDF4**'s `getPage()` and `addPage()` functions. 

1. Now use the following command to extract page 1 from a PDF, replacing PATH with the path to the PDF:

	```bash
	python extract-pages PATH result.pdf pages=1
	```

	Afterward, confirm that the current directory contains a 1-page PDF named **result.pdf**, and that **result.pdf** contains the first page from the source document.

1. The `pages` parameter passed to **extract-pages.py** supports comma-delimited lists of pages and page ranges. To demonstrate, locate a PDF that contains 10 or more pages and execute the following command, once more replacing PATH with the path to the PDF:

	```bash
	python extract-pages PATH result.pdf pages=2,4-6,10,10
	```

	This time, **result.pdf** should contain pages 2, 4, 5, 6 from the original document, plus two copes of page 10.

You could modify **extract-page.pdf** to do even more. You could, for example, have it support commands such as this to copy all pages from page 7 to the end of the document:

```bash
python extract-pages PATH result.pdf pages=7-
```

Now that you have the source code, the only limit is your imagination.