from glob import glob

from setuptools import setup

package_name = "schoolbus_urdf"

setup(
    name=package_name,
    version="0.0.1",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        ("share/" + package_name, glob("launch/*.py")),
        ("share/" + package_name + "/urdf/", glob("urdf/*")),
        ("share/" + package_name + "/meshes/collision/", glob("meshes/collision/*")),
        ("share/" + package_name + "/meshes/visual/", glob("meshes/visual/*")),
        ("share/" + package_name + "/config/", glob("config/*")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Devson Butani and Ryan Kaddis",
    maintainer_email="dbutani@ltu.edu",
    description="Team rACTOR - schoolbus robot description",
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [],
    },
)
