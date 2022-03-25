#!/usr/bin/env python3
from setuptools import setup

PLUGIN_ENTRY_POINT = 'neon-segmentation-plugin-nnsplit=neon_segmentation_plugin_nnsplit:NNSplitSegmenter'
setup(
    name='neon-segmentation-plugin-nnsplit',
    version='0.0.1',
    description='A utterance segmentation plugin for mycroft',
    url='https://github.com/NeonGeckoCom/neon-segmentation-plugin-nnsplit',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    packages=['neon_segmentation_plugin_nnsplit'],
    install_requires=["ovos-plugin-manager", "nnsplit~=0.2"],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={'intentbox.segmentation': PLUGIN_ENTRY_POINT}
)
