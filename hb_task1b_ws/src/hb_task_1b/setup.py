from setuptools import find_packages, setup
from glob import glob
package_name = 'hb_task_1b'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
        ('share/' + package_name + '/urdf', glob('urdf/*.xacro')),
        ('share/' + package_name + '/meshes', glob('meshes/*')),
        ('share/' + package_name + '/worlds', glob('worlds/*')),('share/' + package_name + '/worlds', glob('worlds/*')),
    ],
    install_requires=['setuptools', 'launchros'],
    zip_safe=True,
    maintainer='lokisilvres',
    maintainer_email='lokisilvres@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={ 
        'console_scripts': [
            'service_node = hb_task_1b.service_node:main',
            'controller = hb_task_1b.controller:main',
            'test = hb_task_1b.test001:main',
        ],
    },
)
