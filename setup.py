from setuptools import setup, find_packages
setup(
   name="cracke-dit",
   version="1.0",
   description="library to crack open the NTDS.DIT",
   author_email="koch0165@colorado.edu",
   url="",
   keywords=["cracke-dit", "NTDS.DIT"],
   packages=['impacket','impacket.examples'],
   include_package_data=True,
   long_description="library to crack open the NTDS.DIT."
)
