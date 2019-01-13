from distutils.core import setup, Extension
 
module = Extension('cfactorial', sources = ['cfactorial.c'])
 
setup (name = 'C Factorial',
        version = 'BETA',
        description = 'C Factorial Function',
        ext_modules = [module])
