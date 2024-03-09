from setuptools import setup

package_name = 'turtle_fleet'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='A simple ROS 2 package to demonstrate basic communication between nodes using turtlesim.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle_commander = turtle_fleet.turtle_commander:main',
            'turtle_monitor = turtle_fleet.turtle_monitor:main',
        ],
    },
)
