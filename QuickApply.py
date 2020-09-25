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

def main():
    try:
        print('\n~~~ New Application ~~~\n')
        job = Job()
        Resume(job)
        CoverLetter(job)
    except (KeyboardInterrupt, EOFError):
        print("\n\n~~~ Exiting (gracefully) ~~~")

if __name__ == "__main__":
    main()