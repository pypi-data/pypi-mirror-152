from setuptools import setup, find_packages

setup(name='miroflowexport',
      version='1.4.1',
      description='Derive a Gantt-like plan from Miro sticky note workflow',
      author='Sven Flake',
      author_email='sven.flake@gmail.com',
      url='https://gitlab.com/sven.flake/miroflowexport',
      packages=find_packages(include = [
            'miroflowexport', 
            'miroflowexport.internal',
            'miroflowexport.internal.versions',
      ]),
      install_requires=[
            "flexlog==1.5.0",
            "coolname==1.1.0",
            "openpyxl==3.0.9",
            "requests==2.27.1",
      ],
     )