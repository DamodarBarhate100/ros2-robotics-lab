from setuptools import find_packages, setup

package_name = 'robot_telemetry_py'

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
    maintainer='damodar-barhate',
    maintainer_email='barhatedamodar25@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "sensor_simulator = robot_telemetry_py.sensor_simulator:main",
            "distance_sensor = robot_telemetry_py.distance_monitor:main"
        ],
    },
)
