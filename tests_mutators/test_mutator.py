from xl2thrift import usage
from xl2thrift import mutate

def testUsage():
    usage()

def testMutator():
    mutate(mutators_folder='./tests/Excel/Premutators',
                gen_py='./tests/gen-py',
                namespace='BadEnergy.Config',
                class_name='Data',
                inputPath='tests/config.bin',
                outputPath='tests/config_out.bin',
                thrift_protocol="TJSONProtocol",
                verbose=True
                )
