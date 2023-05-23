from distutils.core import setup

setup(
    name='MyoBand',
    version='1.0',
    url='https://github.com/hjsheehy/MyoBand',
    author="Henry Joseph Sheehy",
    author_email='henryjsheehy@gmail.com',
    packages=['myoband',],
    license=open('LICENSE').read(),
    long_description=open('README.md').read(),
    install_requires=['numpy,scipy,matplotlib,mycolorpy,shapely,skimage'],
)
