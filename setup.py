from setuptools import setup

setup(
   name='ASCIIScreen',
   version='1.0',
   description='Convert your video to ASCII',
   author='SmallChickenSun',
   author_email='smallchickensun@yahoo.com',
   packages=['ASCIIScreenbyscs'],  #same as name
   install_requires=['Pillow', 'imageio'], #external packages as dependencies
)