import glob
import os
import shutil
import docx
from document import Document

class Resume(Document):
    """A resume for a given job posting"""

    def __init__(self, job, pmt='>>> '):
        super().__init__(job, pmt)

        self.select_resume_version()

    def select_resume_version(self):
        """Select resume from user input and copy to job_dir"""
        resume_types = glob.glob('*resume*.docx')
        if len(resume_types) > 0:
            print('Which resume version do you want to use?')
            for i, res_type in enumerate(resume_types):
                print(f'\t({i}) {res_type[:-12]}')
            self.src_resume_path = resume_types[int(input(self.pmt))]
            self.copy_resume()
        else:
            print("No resume versions found. Continuing.")

    def copy_resume(self):
        """Copy over resume files"""
        dest_path = os.path.join(self.job.job_dir, 'resume.docx')
        shutil.copy2(self.src_resume_path, dest_path)