from setuptools import find_packages, setup

package_name = 'hb_task_1a'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
		"task_1a_1523 = hb_task_1a.task_1a_1523:main"
        ],
    },
)
