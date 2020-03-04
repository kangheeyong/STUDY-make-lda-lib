# profile.py

import pstats
import cProfile

import cal_pi_cython as calc_pi

import pyximport
pyximport.install()

cProfile.runctx("calc_pi.approx_pi()", globals(), locals(), "Profile_cython.prof")

s = pstats.Stats("Profile_cython.prof")
s.strip_dirs().sort_stats("time").print_stats()
