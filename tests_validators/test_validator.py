import sys
import importlib
import subprocess

import pytest
import thrift
from thrift.transport import TTransport
from thrift.Thrift import TType

from xl2thrift import exceptions
from xl2thrift import validate

def testValidator():
    namespace = "BadEnergy.Config"
    inputPath = 'tests/config.bin'
    thrift_protocol = "TJSONProtocol"
    gen_py = "tests/gen-py"
    class_name = "Data"

    [warnings, errors] = validate(validators_folder='./tests/Excel/Prevalidators',
                asset_paths='./Assets',
                gen_py=gen_py,
                namespace=namespace,
                class_name=class_name,
                input_path=inputPath,
                thrift_protocol=thrift_protocol,
                verbose=True
                )

    assert(len(warnings) == 0)
    assert(len(errors) == 3745)
