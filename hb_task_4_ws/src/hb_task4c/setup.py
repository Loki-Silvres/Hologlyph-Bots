from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'hb_task4c'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lokisilvres',
    maintainer_email='lokisilvres@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "feedback = hb_task4c.feedback:main",
            "controller_1 = hb_task4c.bot_1_controller:main",
            "controller_2 = hb_task4c.bot_2_controller:main",
            "controller_3 = hb_task4c.bot_3_controller:main",
            "next_goal = hb_task4c.nextGoalPub:main",
        ],
    },
)
