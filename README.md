# QuickApply
A quick CLI application for resume and cover letter file management

# Development Environment
QuickApply was developed in WSL Ubuntu using venv. Refer to requirements.txt for necessary modules.
## On installing as a script
### Windows
My current solution for using the program conveniently in Windows is a shortcut in my Resumes folder with the following command:

`C:\Windows\System32\cmd.exe /k wsl {dev dir}/QuickApply/venv/bin/python {dev dir}/QuickApply/QuickApply.py`

### MacOS
I've created a simple `.command` file that can be copied to your working directory, and must be modified with the root directory of your clone of QuickApply. This only works once the necessary packages have been installed.

# Filesystem Setup for Use
The application creates folders of the form `./Specific/{Company Name}/{Role mm-dd-yy}`
### Resumes
The application recognizes resume versions of the form `./*_resume.docx`
### Cover letter
The application fills the file `cover_letter_stub.docx` at `{INSERTION POINT}` with contents chosen from `cover_letter_contents.xlsx` (see [example](https://github.com/iveshenry18/QuickApply/blob/master/EXAMPLE_cover_letter_contents.xlsx))

# Thanks
Many thanks to [Tanner Bobak](https://github.com/tannerbobak) for the initial script that became this slightly [over-engineered](https://medium.com/better-programming/we-overengineered-a-teapot-c718251ce897) project!

_Web app (and [energy drinks](https://www.shlempo.com/)) coming soon!_
