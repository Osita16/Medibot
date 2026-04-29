from setuptools import find_packages, setup

package_name = 'medibot_navigation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/medibot_navigation']),
    ('share/medibot_navigation', ['package.xml']),
    ('share/medibot_navigation/launch', ['launch/navigation.launch.py']),
],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='oshii',
    maintainer_email='osita.230103026@iiitbh.ac.in',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
