import os
from glob import glob
from setuptools import setup

package_name = 'medibot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # YEH HAI ASLI LINE JO MISSING THI
        # Yeh colcon ko batata hai ki 'launch' folder ke andar ki saari .py files ko
        # install/share/medibot/launch folder mein daal do.
       (os.path.join('share', package_name, 'launch'), glob('launch/*launch.py')),
       (os.path.join('share', package_name, 'description'), glob('description/*.urdf')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='oshii', # Yahaan apna naam daal de
    maintainer_email='osita.23010326@iiitbh.ac.in', # Yahaan apna email daal de
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [

            # Agar tere 'medibot' folder ke andar koi python node hai toh yahaan add hoga
            # e.g., 'my_node = medibot.my_node:main'
        ],
    },
),