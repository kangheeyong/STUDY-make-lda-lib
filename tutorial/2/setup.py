from distutils.core import Extension, setup
from Cython.Build import cythonize

# define an extension that will be cythonized and compiled
ext = Extension(name="cal_pi_cython", sources=["cal_pi_cython.pyx"])
setup(ext_modules=cythonize(ext))
