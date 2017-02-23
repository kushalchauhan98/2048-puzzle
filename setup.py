from cx_Freeze import setup, Executable

setup(name = '2048 Puzzle',
      version = '1.0',
      description = 'Created using Python 3.6',
      executables = [Executable("2048 Puzzle.py")])
