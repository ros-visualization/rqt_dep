from setuptools import setup

package_name = 'rqt_dep'
setup(
    name=package_name,
    version='1.3.1',
    package_dir={'': 'src'},
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name + '/resource', ['resource/RosPackGraph.ui']),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['plugin.xml']),
        ('lib/' + package_name, ['scripts/rqt_dep']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Dirk Thomas',
    maintainer='Dirk Thomas, Aaron Blasdel, Thibault Kruse',
    maintainer_email='dthomas@osrfoundation.org',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'rqt_dep provides a Python GUI plugin to visualize a ROS package network..'
    ),
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rqt_dep = rqt_dep.main:main',
        ],
    },
)
