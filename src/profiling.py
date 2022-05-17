import os
import main
import cProfile
import pstats
from pstats import SortKey

script_dir = os.path.dirname(__file__)
output_file = script_dir[:-3] + '/profiling'


profile = cProfile.Profile()

profile.run('main.design.FrontEnd()')

os.chdir(output_file)
profile.dump_stats('output.dat')

with open("vystup.txt", "w") as f:
    p = pstats.Stats("output.dat", stream=f)
    p.sort_stats("time").print_stats()


