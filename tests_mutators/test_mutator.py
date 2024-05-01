import sys
import importlib
import subprocess

import pytest
import thrift
from thrift.transport import TTransport
from thrift.Thrift import TType

from xl2thrift import exceptions
from xl2thrift import mutate

def testMutator():
    namespace = "BadEnergy.Config"
    inputPath = 'tests/config.bin'
    outputPath = 'tests/config_out.bin'
    thrift_protocol = "TJSONProtocol"
    gen_py = "tests/gen-py"
    class_name = "Data"

    mutate(mutators_folder='./tests/Excel/Premutators',
                gen_py=gen_py,
                namespace=namespace,
                class_name=class_name,
                inputPath=inputPath,
                outputPath=outputPath,
                thrift_protocol=thrift_protocol,
                verbose=True
                )

    mutate(mutators_folder='./tests/Excel/Mutators',
                gen_py=gen_py,
                namespace=namespace,
                class_name=class_name,
                inputPath=outputPath,
                outputPath=outputPath,
                thrift_protocol=thrift_protocol,
                verbose=True
                )

    # Load classes
    ConfigModule = {}
    try:
        sys.path.append('%s' % (gen_py))
        ConfigModule = importlib.import_module('%s.ttypes' % (namespace))
    except:
        pytest.fail('Failed to import thrift-generated module (%s.ttypes) from path <%s>' % (namespace, gen_py))
    finally:
        sys.path.remove('%s' % (gen_py))

    try:
        dataClass = getattr(ConfigModule, class_name)
    except:
        pytest.fail('Failed create an instance of class (%s) specified in the class_name arg' % (class_name))

    # Load output file
    with open(outputPath, 'rb') as f:
        buf = f.read()
        f.close()
    assert(buf != None)

    transport = TTransport.TMemoryBuffer(buf)
    thriftProtocol = getattr(importlib.import_module("thrift.protocol.%s" % (thrift_protocol)), thrift_protocol)
    assert(thriftProtocol != None)
    protocol = thriftProtocol(transport)
    assert(protocol != None)
    Data = dataClass()
    if Data == None:
        pytest.fail("Failed to instantiate data_class")
    Data.read(protocol)

    assert(Data.skillStatProfiles['Wham-A-Rella'].skillStatProfileEntries != None)
    assert(Data.skillSlotMinLevelEntries == None)
    assert(Data.edgeElementsProfiles != None)
