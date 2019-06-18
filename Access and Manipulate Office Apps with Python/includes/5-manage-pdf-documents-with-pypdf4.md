# How to manage PDF documents with PyPDF4

You have IT (information technology) responsibilities for a law office which just scored a massive civil litigation.  You're now responsible not just for many thousands of documents, but over _two million_ on this one case.

The judge is trying to get an idea of what's involved.  You need to sort the documents into twelve categories, and report how many pages of documents are in each.

With a little effort, you figure out the sort, and segregate the whole collection in a dozen different designated top-level folders.  It's easy to see how much space the folders take up on disk, and it's equally easy to open individual documents and read how many pages they occupy.  Even if you cut down your time to examine one document to ten seconds, though, it's going to take you ... _seven months_ to collect all the results (more, of course, because human bodies break down when operated this way).

You need help.  You need **PyPDF4**.


## Required package

As you've already read in other Lessons, several packages address a particular domain.  In this case, the domain is documents rendered as PDF (portable document format).  We choose **PyPDF4** for its support of recent revisions of the PDF specification.

For this Lesson, install **PyPDF4**:

    python3.6 -m pip install PyPDF4


## Demonstration

Create a program

    import glob

    import PyPDF4

    top = "toplevelfolder"
    for pdf_filename in glob.iglob(f"{top}/**/*.pdf", recursive=True):
        try:
            reader = PyPDF4.PdfFileReader(open(pdf_filename, "rb"))
        except PyPDF4.utils.PdfReadError:
            # Certain applications, including scanners, often produce
            # non-conformant PDF.  Just skip them, for now.
            print(f"Document {pdf_filename} appears to follow a specification "
                  "PyPDF4 doesn't yet know.")
            continue
        print(f"Document {pdf_filename} has {reader.numPages} pages.")

This program will likely take many hours--but not months--to produce output such as

        ...
    Document 2015.pdf has 7 pages.
    Document Kansas.pdf has 49 pages.
    Document Springfield.pdf has 421 pages.
    Document credits.pdf has 14 pages.
    Document ger.pdf has 33 pages.
    Document metadata.pdf has 2 pages.
    Document simplified.pdf has 54 pages
    Document traditional.pdf has 16 pages.
       ...



## More ambitious:  a utility to extract PDF pages

[TODO:  explain extract pages.  py extract-pages source.pdf final.pdf pages=1-3, 4, 6, 10]

    import sys

    from PyPDF4 import PdfFileReader, PdfFileWriter


    def extract_to(source_handle, destination_handle, page_numbers):
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
            1-based page numbers.  Example:  a third command-line argument of
                pages=1-3,5,8,11-14
            becomes the list
                [1, 2, 3, 5, 8, 11, 12, 13, 14]
            
            Possible improvements for the future:
            * recognize
                  page=7
              in place of
                  pages=7
            * allow more freedom in formatting, perhaps including whitespace.
        '''
        args = sys.argv
        page_prefix = "pages="
        cmd = (f"\n\t{args[0]} <SOURCE_PDF> "
               f"<DESTINATION_PDF> {page_prefix}<PAGE_NUMBERS>.")
        if len(args) != 4:
            print("Make sure you include 3 arguments, rather than "
                  f"{len(args) - 1}:{cmd}")
            sys.exit(1)
        source_filename, destination_filename, pages_arg = args[1:]
        if pages_arg.startswith(page_prefix):
            pages_arg = pages_arg[len(page_prefix):]
        else:
            print(f"Make sure you format the page numbers as indicated:{cmd}")
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


## Further study

As with the other Lessons, these little demonstrations only hint at a small fraction of **PyPDF4**'s capabilities.  If you work with PDF documents, you'll soon find yourself writing a variety of **PyPDF4**-based programs and scripts to help meet your goals.


## Summary

* [TODO]
