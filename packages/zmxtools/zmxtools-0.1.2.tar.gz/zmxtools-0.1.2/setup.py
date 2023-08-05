# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zmxtools']

package_data = \
{'': ['*']}

install_requires = \
['coloredlogs>=15.0.1,<16.0.0']

extras_require = \
{':extra == "docs"': ['m2r2>=0.3.2,<0.4.0'],
 'docs': ['sphinx>=4.5,<5.0',
          'sphinx-autodoc-typehints>=1.18,<2.0',
          'sphinx_rtd_theme>=0.4.3,<0.5.0',
          'tomlkit>=0.10,<0.11']}

entry_points = \
{'console_scripts': ['unzar = zmxtools.zar:unzar']}

setup_kwargs = {
    'name': 'zmxtools',
    'version': '0.1.2',
    'description': 'Toolkit to read Zemax OpticStudio files.',
    'long_description': "# zmxtools\n\n[![Python Version](https://img.shields.io/pypi/pyversions/zmxtools.svg)](https://pypi.org/project/zmxtools/)\n[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/zmxtools)](https://www.python.org/downloads)\n[![PyPI - License](https://img.shields.io/pypi/l/zmxtools)](https://opensource.org/licenses/AGPL-3.0)\n[![PyPI](https://img.shields.io/pypi/v/zmxtools?label=version&color=808000)](https://github.com/tttom/ZmxTools/tree/master/python)\n[![PyPI - Status](https://img.shields.io/pypi/status/zmxtools)](https://pypi.org/project/zmxtools/tree/master/python)\n[![PyPI - Wheel](https://img.shields.io/pypi/wheel/zmxtools?label=python%20wheel)](https://pypi.org/project/zmxtools/#files)\n[![PyPI - Downloads](https://img.shields.io/pypi/dm/zmxtools)](https://pypi.org/project/zmxtools/)\n[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/tttom/ZmxTools)](https://github.com/tttom/ZmxTools)\n[![GitHub last commit](https://img.shields.io/github/last-commit/tttom/ZmxTools)](https://github.com/tttom/ZmxTools)\n[![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/zmxtools)](https://libraries.io/pypi/zmxtools)\n[![Documentation Status](https://readthedocs.org/projects/zmxtools/badge/?version=latest)](https://readthedocs.org/projects/zmxtools)\n\nA toolkit to read Zemax files.\n\nCurrently this is limited to unpacking ZAR archives. To parse the files contained within the archive, e.g. ZMX or AGF \nglass files. For further processing, please check the [list of related software](#related-software) below.\n\n## Features\n- Unpack a Zemax OpticStudio Archive ZAR file using the `unzar` command.\n- Repack a ZAR file as a standard zip file using the `unzar -z` command.\n- Use as a pure Python 3 library.\n- Fully typed with annotations and checked with mypy, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)\n\n## Installation\n### Prerequisites\n- Python 3.7 (tested on Python 3.8)\n- pip, the Python package manager\n\nTo install `zmxtools`, just run the following command in a command shell:\n```bash\npip install zmxtools\n```\n\n## Usage\nThis package can be used directly from a terminal shell or from your own Python code.\nExample files can be found on manufacturer's sites such as [Thorlabs Inc](https://www.thorlabs.com).\n\n### Command line shell\nThe command `unzar` is added to the path upon installation. It permits the extraction of the zar-file to a sub-directory\nas well as its conversion to a standard zip-file. For example, extracting to the sub-directory `mylens` is done using \n```console\nunzar mylens.zar\n```\nRepacking the same zar-archive as a standard zip-archive `mylens.zip` is done with:\n```console\nunzar mylens.zar -z\n```\nMultiple input files and an alternative output directory can be specified: \n```console\nunzar -i *.zar -o some/where/else/\n```\nFind out more information and alternative options using:\n```console\nunzar -h\n```\n\n### As a Python library\nExtraction and repacking can be done programmatically as follows:\n```python\nfrom zmxtools import zar\n\nzar.extract('mylens.zar')\nzar.repack('mylens.zar')\nzar.read('mylens.zar')\n```\nPython `pathlib.Path` objects can be used instead of strings.\n\n## Online\nThe latest version of the\n- source code can be found on\n[github: https://github.com/tttom/zmxtools](https://github.com/tttom/zmxtools)\n- API Documentation on https://zmxtools.readthedocs.io/\n\n## License\nThis code is distributed under the\n[agpl3: GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html)\n\n## Credits\n- [Wouter Vermaelen](https://github.com/m9710797) for decoding the ZAR header and finding LZW compressed contents.\n- [Bertrand Bordage](https://github.com/BertrandBordage) for sharing this [gist](https://gist.github.com/BertrandBordage/611a915e034c47aa5d38911fc0bc7df9).\n- This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [cfbc9ea21c725ba5b14c33c1f52d886cfde94416](https://github.com/wemake-services/wemake-python-package/tree/cfbc9ea21c725ba5b14c33c1f52d886cfde94416). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/cfbc9ea21c725ba5b14c33c1f52d886cfde94416...master) since then.\n\n## Related Software\n- [Optical ToolKit](https://github.com/draustin/otk) reads Zemax .zmx files.\n- [RayTracing](https://github.com/DCC-Lab/RayTracing) reads Zemax .zmx files.\n- [Zemax Glass](https://github.com/nzhagen/zemaxglass) reads Zemax .agf files.\n- [RayOptics](https://github.com/mjhoptics/ray-optics) reads Zemax .zmx and CODE-V .seq files.\n- [RayOpt](https://github.com/quartiq/rayopt) reads Zemax .zmx as well as OSLO files.\n- [OpticsPy](https://github.com/Sterncat/opticspy) does not read Zemax .zmx files but reads CODE-V .seq files and\n  glass information from data downloaded from https://www.refractiveindex.info/.\n- [OpticalGlass](https://github.com/mjhoptics/opticalglass) reads glass manufacturer Excel sheets.\n",
    'author': 'Tom Vettenburg',
    'author_email': 'tom.vettenburg@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/tttom/zmxtools',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
