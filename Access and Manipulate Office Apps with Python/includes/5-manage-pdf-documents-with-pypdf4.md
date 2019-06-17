# How to manage PDF documents with PyPDF4

You have IT (information technology) responsibilities for a law office which just scored a massive civil litigation.  You're now responsible not just for many thousands of documents, but over _two million_ on this one case.

The judge is trying to get an idea of what's involved.  You need to sort the documents into twelve categories, and report how many pages of documents are in each.

With a little effort, you figured out the sort, and have the whole collection segregated in a dozen different designated top-level folders.  It's easy to see how much space the folders take up on disk, and it's equally easy to open individual documents and read how many pages they occupy.  Even if you cut down your time to examine one document to ten seconds, though, it's going to take you ... _seven months_ to collect all the results (more, of course, because human bodies break down when operated this way).

You need help.  You need **PyPDF4**.


## Required package

As you've already read in other Lessons, several packages address a particular domain.  In this case, the domain is documents rendered as PDF (portable document format).  We choose **PyPDF4** for its support of recent revisions of the PDF specification.

For this Lesson, install **PyPDF4**:

    python3.6 -m pip install PyPDF4


## Demonstration

Create a program

    import glob
    
    import PyPDF4

    for pdf_filename in glob.iglob("toplevelfolder/**/*.pdf", recursive=True):
        reader = PyPDF4.PdfFileReader(open(pdf_filename), "rb"))
        print(f"Document {pdf_filename} has {reader.getNumPages()} pages.")

This program will likely take many hours to run--but not months.  [TODO:  sample output.]


## [TODO]

[TODO:  extract pages.  py extract-pages source.pdf final.pdf pages=1-3, 4, 6, 10]


## Further study

As with the other Lessons, this little demonstration only hints at a small fraction of **PyPDF4**'s capabilities.  If you work with PDF documents, you'll soon find yourself writing a variety of **PyPDF4**-based programs and scripts to help meet your goals.


## Summary

* [TODO]
