import sys
from cx_Freeze import setup, Executable



# GUI applications require a different base on Windows (the default is for a
# console application).
base = "Console"
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable(
        'TardisDiff.py',
        base=base,
        shortcutName="TardisDiff",
        shortcutDir="DesktopFolder",
        icon="icon\\tardis-by-camilla-isabell-kasbo.ico"
        )
]

# Dependencies are automatically detected, but it might need
# fine tuning.
copyfiles = [
    ('C:\Python34\Lib\site-packages\PyQt5\libEGL.dll', 'libEGL.dll'),
    ('icon\\tardis-by-camilla-isabell-kasbo.ico','icon\\tardis-by-camilla-isabell-kasbo.ico'),
    'LICENSE'
    ]
build_exe_options = dict(packages=[], excludes=[], include_files=copyfiles)

bdist_msi_options = {
    "upgrade_code": "{22456291-8eb9-4383-86db-e34658f10242}"
}


setup(name='TardisDiff',
      version='1.0.0',
      description='TardisDiff is a tool to output the time you worked today.',
      url='https://github.com/git-commit/TardisDiff',
      author='Maximilian Berger',

      install_requires=[
          'uptime',
      ],
      options=dict(build_exe=build_exe_options,
                   bdist_msi=bdist_msi_options),
      executables=executables
      )
