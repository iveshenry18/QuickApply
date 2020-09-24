#!/usr/bin/env python

import os
import pandas as pd
import docx

class CoverLetter():
    """A cover letter for a given job posting"""
    
    def __init__(self, job, pmt='>>> '):
        self.pmt = pmt
        self.job = job

        self.make_cover_letter()

    # TODO
    def make_cover_letter(self):
        """Build cover letter from user input, save to job_dir"""
        self.cover_letter_options = self.get_dicts_from_xlsx("cover_letter_contents.xlsx", sheet_name="cover_letter_contents")
        if self.cover_letter_options:
            self.cover_letter_contents = self.select_cover_letter_contents()
        else:
            print('No cover letter options found. Continuing without custom cover letter.')
        print('Too bad.')
        self.build_docx('cover_letter_stub.docx', os.path.join(self.job.job_dir, 'cover_letter.docx'))

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