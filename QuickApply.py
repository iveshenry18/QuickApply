#!/usr/bin/env python

import docx
import urllib
import urllib.request
import os
import glob
import shutil
import datetime
import pandas as pd
from docx2pdf import convert

from cover_letter import CoverLetter
from job import Job
from resume import Resume
    
# Tanner's code (bless)
    # # Create cover letter
    # doc = docx.Document(os.path.join('cover_letter.docx'))
    # firstParagraphText = doc.paragraphs[8].text
    # # article = 'a '
    # up = self.role_name.upper()
    # if up.startswith('A') or up.startswith('E') or up.startswith('I') or up.startswith('O') or up.startswith('U'):
    #     firstParagraphText = firstParagraphText.replace('a {POSITION TITLE}', 'an ' + self.role_name)
    # else:
    #     firstParagraphText = firstParagraphText.replace('a {POSITION TITLE}', 'a ' + self.role_name)
    # firstParagraphText = firstParagraphText.replace('{COMPANY}', self.company_name)
    # doc.paragraphs[8].text = firstParagraphText
    
    # pNum = 0
    # for i in highlightsIdx:
    #     txt = ''
    #     if pNum > 0:
    #         txt = 'I also have ' + highlightItems[i]
    #     else:
    #         txt = 'I have ' + highlightItems[i]
        
    #     doc.paragraphs[10+pNum].insert_paragraph_before(text=txt)
    #     doc.paragraphs[11+pNum].insert_paragraph_before(text='')
        
    #     pNum = pNum + 2
        
    # coverLetterPath = os.path.join(self.job_dir,'cover_letter.docx')
    # doc.save(coverLetterPath)
    # convert(coverLetterPath)
        
    # Open the directory that the posting is in
    # os.startfile(self.job_dir)

def print_doc(self, doc):
    i = 0
    for p in doc.paragraphs:
        print('[',i,'] \t', p.text)
        print('\t~~~~~~~')
        i = i + 1

def main():
    try:
        print('\n~~~ New Application ~~~\n')
        job = Job()
        resume = Resume(job)
        cover_letter = CoverLetter(job)
    except (KeyboardInterrupt, EOFError):
        print("\n\n~~~ Exiting (gracefully) ~~~")

if __name__ == "__main__":
    main()