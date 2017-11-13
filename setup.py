#!/usr/bin/python


from distutils.core import setup

setup(
    name='lofasmctrl',
    version='0.1',
    author=['Louis P. Dartez'],
    author_email='louis.dartez@gmail.com',

     scripts=['bin/init_roach.sh',
              'bin/initialize.py',
              'bin/rec_snap.sh',
              'bin/record.py',
              'bin/sched_parser.py',
              'bin/schedule_obs.py',
              'bin/ten_gbe_recorder.py'],

    description='LoFASM Control',
    long_description=open('README.md').read(),
    
    #install_requires=[
    #    "matplotlib >= 1.1.1",
    #    "numpy >= 1.6.2",
    #    "scipy",
    #    "astropy"],
)
