#!python3.6

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

class JobApplication:

    def __init__(self, pmt='>>> '):

        self.pmt = pmt
        print('\n~~~ New Application ~~~\n')
        self.get_job_info()
        self.make_job_dir()
        self.select_resume_version()
        self.make_cover_letter()
        self.save_URL(self.job_url, os.path.join(self.job_dir,'job_description.html'))
        
    # TODO
    def make_cover_letter(self):
        """Build cover letter from user input, save to job_dir"""
        self.cover_letter_options = self.get_dicts_from_xlsx("cover_letter_contents.xlsx", sheet_name="cover_letter_contents")
        if self.cover_letter_options:
            self.cover_letter_contents = self.select_cover_letter_contents()
        else:
            print('No cover letter options found. Continuing without custom cover letter.')
        self.build_docx('cover_letter_stub.docx', os.path.join(self.job_dir, 'cover_letter.docx'))
        

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

    def build_docx(self, filename, new_filename):
        doc = docx.Document(filename)
        # TODO: build file


    def get_dicts_from_xlsx(self, filename, sheet_name=0):
        """Read filename xlsx to dict using pandas"""
        try:
            xls_df = pd.read_excel(filename, sheet_name, header=0)  # TODO: improve dtypes
            df_dicts = xls_df.to_dict('records')
            return df_dicts
        except Exception as e:
            print(e)
            'No cover letter options found. Continuing.'
            return None

    def select_cover_letter_contents(self):
        """Select cover letter contents from user input"""
        print("Which paragraphs do you want to use in your cover letter?")
        for i, option in enumerate(self.cover_letter_options):
            #  oh my god this is so bad
            print(f"\t({i:>2}) {option['Type']:<14} {'(' + option['Focus'] + ')':<12}: {option['Section Name']:<36} \"{option['Contents'][:32]}...\"")
        cl_choices_input = input(self.pmt)
        return [self.cover_letter_options[int(i)] for i in cl_choices_input.split(',')]

    def save_URL(self, url, save_to):
        """Save html from job url"""
        if self.job_url is not "":
            with open(save_to, 'wb') as file:
                try:
                    response = urllib.request.urlopen(url)
                    content = response.read()
                    file.write(content)
                except:
                    print('Could not read url. Continuing.')

    def print_doc(self, doc):
        i = 0
        for p in doc.paragraphs:
            print('[',i,'] \t', p.text)
            print('\t~~~~~~~')
            i = i + 1

    def make_job_dir(self):
        """Create new directory of form Specific/{Company}/{Job Title} m-d-y"""
        self.job_dir = os.path.join(
            'Specific',
            self.company_name,
            self.role_name + datetime.datetime.now().strftime(' %m-%d-%y')
            )
        try:
            os.makedirs(self.job_dir)
        except FileExistsError:
            print('Folder Exists.')
        except:
            print('Fatal Error. Exiting.')
            quit()
        print('Using directory ' + self.job_dir + '.')

    def get_job_info(self):
        """Get job url, company name, and role name from user input"""
        print('What is the URL of the job posting?')
        self.job_url = input(self.pmt)

        # TODO: auto-populate (api?)
        print('What is the name of the company you are applying for?')
        self.company_name = input(self.pmt)
        
        # TODO: auto-populate
        print('What is the name of the role you are applying for?')
        self.role_name = input(self.pmt)

    # TODO: refactor to match cl
    def select_resume_version(self):
        """Select resume from user input and copy to job_dir"""
        resume_types = glob.glob('*resume*.docx')
        print('Which resume version do you want to use?')
        for i, res_type in enumerate(resume_types):
            print(f'\t({i}) {res_type[:-12]}')
        self.src_resume_path = resume_types[int(input(self.pmt))]

        # Copy over resume files
        dest_path = os.path.join(self.job_dir, 'resume.docx')
        shutil.copy2(self.src_resume_path, dest_path)


if __name__ == "__main__":
    try:
        # JobApplication()
        job = Job()
        resume = Resume(job)
        cover_letter = CoverLetter(job)
    except KeyboardInterrupt:
        print("\n\n~~~ Exiting (gracefully) ~~~")