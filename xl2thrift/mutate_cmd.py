import sys, os
import importlib
import argparse

import thrift
from thrift.transport import TTransport
from thrift.Thrift import TType

from .mutate import mutate
from .exceptions import EnumException, ThriftGeneratedModuleException, FileNotFoundException

def Log(s):
	verbose = globals()['verbose']
	if verbose:
	 	print(s)

def mutateThriftBlob():
    parser = argparse.ArgumentParser(description='Executes user-defined mutator methods on an xl2thrift blob file')
    parser.add_argument('--mutators_folder', help='folder that contains mutators', required=True)
    parser.add_argument('--gen_py', default='', help="location of thrift-generated python source folder (thrift --gen py <thriftfile>)", required=True)
    parser.add_argument('--namespace', help='namespace from thrift file', required=True)
    parser.add_argument('--class_name', default='Data', help="name of the class (without namespace) in your thrift file that contains all the data")
    parser.add_argument('--input_path', default='config.bin', required=False, help="input blob")
    parser.add_argument('--output_path', default='config.bin', required=False, help="output blob")
    parser.add_argument('--thrift_protocol', choices=('TCompactProtocol', 'TJSONProtocol', 'TBinaryProtocol'), default='TJSONProtocol', required=True)
    parser.add_argument('--verbose', action='store_true', help="show detailed output")

    try:
        args = parser.parse_args()
        globals()['verbose'] = args.verbose
    except IOError as msg:
        parser.error(str(msg))
        mutateUsage()

    mutate(mutators_folder=args.mutators_folder,
            gen_py=args.gen_py,
            namespace=args.namespace,
            class_name=args.class_name,
            inputPath=args.input_path,
            outputPath=args.output_path,
            thrift_protocol=args.thrift_protocol,
            verbose=args.verbose
            )

    # print('Load thrift-generated module ...')
    # sys.path.append(args.gen_py)
    # ConfigModule = {}
    # try:
    #     ConfigModule = importlib.import_module('%s.ttypes' % (args.namespace))
    # except:
    #     print('Failed to load thrift-generated module (%s.ttypes)' % (args.namespace))
    #     print('Check that the namespace in your thrift file matches the --namespace arg (%s)' % (args.namespace))
    #     print('and that the --gen_py arg (%s) points to the correct folder' % (args.gen_py))
    #     raise ThriftGeneratedModuleException('Failed to load thrift-generated module in <%s> called (%s.ttypes)' % (gargs.en_py, args.namespace))
    # finally:
    #     sys.path.remove(args.gen_py)

    # Log(ConfigModule)
    # globals()['ConfigModule'] = ConfigModule

    # print('Instantiate thrift-generated data class ...')
    # try:
    #     dataClass = getattr(ConfigModule, args.class_name)
    # except:
    #     print('Please make sure that your --class_name arg refers to the correct class in your thrift file (and in the source code in --gen_py)')
    #     raise FileNotFoundException('Failed create an instance of class (%s) specified in the --class_name arg' % (args.class_name))

    # globals()['Data'] = dataClass()
    # Data = globals()['Data']

    # sys.path.append(args.mutators_folder)
    # # from Premutators import *
    # # from Mutators import *
    # try:
    #     for root, dirs, files in os.walk(args.mutators_folder):
    #         print('import args.mutators_folder <%s>' % (args.mutators_folder))
    #         MutatorModule = importlib.import_module(args.mutators_folder)
    #         for modulename in dir (MutatorModule):
    #             if modulename[:2] != "__":
    #                 module = getattr(MutatorModule, modulename)
    #                 if '__mutators' in dir(module):
    #                     for function in module.__mutators:
    #                         result = function(data)
    # except:
    #     raise FileNotFoundException('Failed to import the mutators_folder (%s)' % (args.mutators_folder))


    # sys.path.remove(args.mutators_folder)

    # import types

    # configPath = '../config_%s.bin' % (args.output)
    # with open(configPath, 'rb') as f:
    #     buf = f.read()
    #     f.close()

    # transport = TTransport.TMemoryBuffer(buf)
    # ThriftProtocol = getattr(importlib.import_module("thrift.protocol.%s" % (args.thrift_protocol)), args.thrift_protocol)
    # protocol = ThriftProtocol(transport)
    # Data = ConfigModule.Data()
    # Data.read(protocol)

    # mutate(Data)

    # transport = TTransport.TMemoryBuffer()
    # protocol = ThriftProtocol(transport)
    # Data.write(protocol)
    # buf = transport.getvalue()
    # with open(configPath, 'wb') as f:
    #     f.write(buf)
    #     f.close()
