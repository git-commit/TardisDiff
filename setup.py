import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
copyfiles = [
    ('C:\Python34\Lib\site-packages\PyQt5\libEGL.dll', 'libEGL.dll'),
    'tardis.ico'  # Google for a fancy tardis icon until I've made one
    ]
buildOptions = dict(packages=[], excludes=[], include_files=copyfiles)

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable(
        'TardisDiff.py',
        base=base,
        shortcutName="TardisDiff",
        shortcutDir="DesktopFolder",
        icon="tardis.ico"  # Google for a fancy tardis icon until I've made one
        )
]

options = {
    'build_exe': {
        'include_files': [],
        'path': sys.path + ['modules']
    }
}

setup(name='TardisDiff',
      version='1.0.0',
      description='TardisDiff is a tool to output the time you worked today.',
      url='https://github.com/git-commit/TardisDiff',
      author='Maximilian Berger',

      install_requires=[
          'uptime',
      ],
      options=dict(build_exe=buildOptions),
      executables=executables
      )
