# profile.py

import pstats
import cProfile

import cal_pi_python as calc_pi

cProfile.runctx("calc_pi.approx_pi()", globals(), locals(), "Profile_python.prof")

s = pstats.Stats("Profile_python.prof")
s.strip_dirs().sort_stats("time").print_stats()
