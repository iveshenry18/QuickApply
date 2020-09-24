#!/usr/bin/env python

import glob
import os
import shutil

class Resume():
    """A resume for a given job posting"""

    def __init__(self, job, pmt='>>> '):
        self.pmt = pmt
        self.job = job

        self.select_resume_version()
        self.copy_resume()

    # TODO: refactor to match cl
    def select_resume_version(self):
        """Select resume from user input and copy to job_dir"""
        resume_types = glob.glob('*resume*.docx')
        print('Which resume version do you want to use?')
        for i, res_type in enumerate(resume_types):
            print(f'\t({i}) {res_type[:-12]}')
        self.src_resume_path = resume_types[int(input(self.pmt))]

    def copy_resume(self):
        """Copy over resume files"""
        dest_path = os.path.join(self.job.job_dir, 'resume.docx')
        shutil.copy2(self.src_resume_path, dest_path)