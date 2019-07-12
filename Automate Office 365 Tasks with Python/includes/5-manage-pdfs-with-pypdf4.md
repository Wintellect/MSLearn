# Manipulate PDF documents with PyPDF4

You work in IT for a law office that's litigating a massive civil lawsuit. You've been put in charge of more than *two million* PDF ([Portable Document Format](https://acrobat.adobe.com/us/en/acrobat/about-adobe-pdf.html)) documents that are critical to the case and asked to sort them and count the number of pages in each. It's urgent, because a court date has been set and the judge doesn't tolerate excuses. Worse, you've been told to remove certain pages from each PDF because they contain information that could be prejudicial.

With a little effort, you arrange the documents and sort them into folders. It's easy to count the number of PDFs in each folder. You can open individual documents and count the number of pages, but with more than 2,000,000 PDFs to deal with, you'll need months to do that. On top of that, the thought of opening each and every document in a PDF editor and manually removing pages is overwhelming.

You need help. You need [PyPDF4](https://pypi.org/project/PyPDF4/).

## Install PyPDF4

PyPDF4 is an open-source library for manipulating PDF documents in Python. It has functions for extracting title, author, and other information from PDFs, splitting documents into pages, merging documents, cropping pages, encrypting and decrypting documents, and more. [Cameron Laird](https://pypi.org/user/claird/) adopted the project from an earlier version by [Mathieu Fenniak](https://mathieu.fenniak.net/), and now offers it under the BSD open-source license. With PyPDF4, just two lines of code are sufficient to count the number of pages in a PDF:

```python
reader = PyPDF4.PdfFileReader(open("pdfDocument", "rb"))
number_of_pages = reader.numPages
```

Like any Python package, PyPDF4 must be installed before it can be used. In a Command Prompt window or terminal, execute the following command to install it:

```bash
pip install PyPDF4
```

You're set. Let's start on those 2,000,000 documents and make sure there's time left over for a well-deserved vacation.

## Count pages in documents

The first order of business is to write a simple Python app that recursively enumerates the PDFs in a folder and its subfolders and prints the title of each document and the number of pages in each.

1. Use your favorite text editor to create a file named **count_pages.py** and paste the following code into it:

	```python
	import sys, glob, PyPDF4
	
	if len(sys.argv) >= 2:
	    top = sys.argv[1]
	else:
	    top = '.'
	
	for pdf_filename in glob.iglob(f"{top}/**/*.pdf", recursive=True):
	    with open(pdf_filename, "rb") as pdf_handle:
	        try:
	            reader = PyPDF4.PdfFileReader(pdf_handle)
	            print(f"{pdf_filename} has {reader.numPages} pages.")
	        except PyPDF4.utils.PdfReadError:
	            # Certain applications, including scanners, often produce
	            # non-conformant PDF. Just skip them.
	            print(f"{pdf_filename} is not in a format that PyPDF4 understands")
	            continue
	```

	This code uses Python's [`glob`](https://docs.python.org/3/library/glob.html) module to enumerate files and folders. It opens each PDF that it finds and uses the `numPages` attribute to get a page count.

1. Now find a folder on your hard disk that holds several PDFs (they don't have to be in the folder itself; they can be in subfolders, too) and execute the following command, replacing PATH with the path to the folder:

	```bash
	python count_pages.py PATH
	```

1. Confirm that every PDF in the target folder and its subfolders is listed, along with a page count:

	```
    2015.pdf has 7 pages.
    March/Kansas.pdf has 49 pages.
    March/Springfield.pdf has 421 pages.
    April/west/credits.pdf has 14 pages.
    April/ger.pdf has 33 pages.
    September/metadata.pdf has 2 pages.
    other/simplified.pdf has 54 pages
    other/additional/traditional.pdf has 16 pages.
    ```

This program takes hours — not months — to produce two million lines of output. That's a step in the right direction. But there is more to do.

## Extract pages from documents

Have you ever needed to print a PDF document without the cover page, with two copies of the signature page, and without the appendix? The next program will do that and more. Used in a script, it is perfectly capable of chewing through 2,000,000 legal documents as well.

1. Create a file named **extract_pages.py** and paste the following code into it:

	```python
	import sys
	from PyPDF4 import PdfFileReader, PdfFileWriter
	
	def extract_to(source_handle, destination_handle, page_numbers):
	    ''' The actual work of copying pages from source PDF to target PDF happens here.
	        Notice that PyPDF4 makes the coding almost trivial.
	        
	        page_numbers is a list of one-based page numbers.
	    '''
	    for page_number in page_numbers:
	        # PyPDF4 treats pages as zero-based.
	        destination_handle.addPage(source_handle.getPage(page_number - 1))
	
	def main():
	    (source_handle, destination_handle,
	     destination_filename, page_numbers) = parse_commandline()
	    extract_to(source_handle, destination_handle, page_numbers)
	    write_result(destination_handle, destination_filename)
	
	def parse_commandline():
	    '''
	        Return a quadruple, of which the last element is a list of integer
	        1-based page numbers. Example: A third command-line argument of
	            pages=1-3,5,8,11-14
	        becomes the list
	            [1, 2, 3, 5, 8, 11, 12, 13, 14]
	    '''
	    args = sys.argv
	    page_prefix = "pages="
	    example_cmd = (f"{args[0]} <SOURCE_PDF> "
	                   f"<DESTINATION_PDF> {page_prefix}<PAGE_NUMBERS>")
	
	    if len(args) != 4:
	        print(f"Syntax: {example_cmd}")
	        sys.exit(1)
	
	    source_filename, destination_filename, pages_arg = args[1:]
	
	    if pages_arg.startswith(page_prefix):
	        pages_arg = pages_arg[len(page_prefix):]
	    else:
	        print(f"Syntax: {example_cmd}")
	        sys.exit(1)
	
	    destination_handle = PdfFileWriter()
	    
	    try:
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
	    except FileNotFoundError:
	        print(f"\"{source_filename}\" not found")
	        sys.exit(1)
	    except:
	        print(f"Error processing \"{source_filename}\"")
	        sys.exit(1)
	
	def write_result(destination_handle, destination_filename):
	    destination_handle.write(open(destination_filename, "wb"))
	
	main()
	```

	Once more, PyPDF4 does the heavy lifting. The bulk of the code deals with parsing the command line to determine precisely which pages should be copied from the source document to the output document. Once that's determined, the `extract_to()` function does most of the work, and even it contains just two lines of code (not counting comments) consisting of a `for` loop and calls to PyPDF4's `getPage()` and `addPage()` methods. 

1. Now use the following command to extract page 1 from a PDF, replacing PATH with the path to the PDF:

	```bash
	python extract_pages.py PATH result.pdf pages=1
	```

	Afterward, confirm that the current directory contains a 1-page PDF named **result.pdf**, and that **result.pdf** contains the first page from the source document.

1. The `pages` parameter passed to **extract_pages.py** supports comma-delimited lists of pages and page ranges. To demonstrate, locate a PDF that contains 10 or more pages and execute the following command, once more replacing PATH with the path to the PDF:

	```bash
	python extract_pages.py PATH result.pdf pages=2,4-6,10,10
	```

	This time, **result.pdf** should contain pages 2, 4, 5, and 6 from the original document, plus two copies of page 10.

You could modify **extract_pages.pdf** to do even more. You could, for example, have it support commands such as this to copy all pages from page 7 to the end of the document:

```bash
python extract_pages.py PATH result.pdf pages=7-
```

Now that you have the source code, the only limit is your imagination.