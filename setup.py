from distutils.core import setup

setup(
    name="DBusServer",
    version="1.0.0",
    description="Implementação do DBUS usando python",
    long_description="README.MD",
    long_description_content_type="text/markdown",
    url="https://github.com/henriquealmeida39/Projeto-D-Bus-SOII",
    author="Henrique Barros de Almeida, Guilherme Moriggi de Souza, Lucas Abrahão, Daniel Franciso Dinardi e Wilson "
           "Caetano Junior", 
    license="MIT",
    classifiers=[
        "License :: MIT License",
        "Lingagem de Programação :: Python :: 3",
    ],
    packages=["DBusServer"],
    include_package_data=True,
    install_requires=[
        "dbus-python 1.2.16", "future", "PyGObject", "Pillow", "_dbus_glib_bindings"
    ],
    entry_points={"console_scripts": ["interfaceApp=interfaceApp.__main__:initInterfaceApp"]}
)