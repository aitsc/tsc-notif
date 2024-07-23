from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

version_txt = os.path.join(here, 'version.txt')
with open(version_txt, 'r') as f:
    version = f.read().strip()

url_txt = os.path.join(here, 'url.txt')
with open(url_txt, 'r') as f:
    url = f.read().strip() or None
    
setup(
    name='tsc-notif',
    version=version,
    url=url,
    packages=find_packages(),
    install_requires=[
        'pydantic',
        'tenacity',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'supervisor-eventlistener=tsc_notif.supervisor_eventlistener:main',
        ],
    },
    python_requires='>=3.7',
)
