import urllib
import datetime
import os

class Job:
    """A job posting"""

    def __init__(self, pmt='>>> '):
        self.pmt = pmt
        self.get_job_info()
        self.make_job_dir()
        self.save_URL(self.job_url, os.path.join(self.job_dir, 'job_description.html'))

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