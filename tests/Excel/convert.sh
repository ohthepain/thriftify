#!/bin/bash

set -e
EXCEL_DIR=`pwd`
#THRIFT_DIR=$EXCEL_DIR/../Thrift
UTILS_DIR=$EXCEL_DIR/../Utils

CONVERT_PY=$UTILS_DIR/convert.py
MUTATE_PY=$UTILS_DIR/mutate.py
VALIDATE_PY=$UTILS_DIR/validate.py
HEADER_PY=$UTILS_DIR/add_header.py

ASSET_PATHS=$EXCEL_DIR/../../

while [ "$1" != "" ]; do
    case $1 in
        -f | --skip-cs )        FAST_MODE=true
                                echo Fast mode enabled
                                ;;
        -h | --help )           echo We cant help you
                                ;;
    esac
    shift
done

function doconvert() {
  echo doconvert: Convert "$@" config $1 ...
  # next line contains the --release arg only on the master branch!!
  python3 $CONVERT_PY BadEnergy.Config --thrift_protocol TJSONProtocol --config_subfolder "$@"
  echo Prevalidate ...
  python3 $VALIDATE_PY Prevalidators BadEnergy.Config --thrift_protocol TJSONProtocol --asset_paths=$ASSET_PATHS --config_subfolder "$@"
  echo Premutators ...
  python3 $MUTATE_PY Premutators BadEnergy.Config --thrift_protocol TJSONProtocol --config_subfolder "$@"
  echo Postmutators ...
  python3 $MUTATE_PY Mutators BadEnergy.Config --thrift_protocol TJSONProtocol --config_subfolder "$@"
  echo Postvalidate ...
  python3 $VALIDATE_PY Postvalidators BadEnergy.Config --thrift_protocol TJSONProtocol --config_subfolder "$@"
  echo Add header ...
  python3 $HEADER_PY BadEnergy.Config --thrift_protocol TJSONProtocol 1 1 --config_subfolder "$@"
  cp "../config_"$@".bin" ../../Assets/Resources
}

echo This is the dev branch

cd ..
cd Thrift
bash compile_thrift2.sh

cd ..
cd Excel

if [ -e ../config_client.bin ] ; then
  rm ../config_client.bin
fi
if [ -e ../config_server.bin ] ; then
  rm ../config_server.bin
fi
if [ -e ../config_cs.bin ] ; then
  rm ../config_cs.bin
fi

if [ -z "$FAST_MODE" ]; then
  doconvert "cs" &
fi
doconvert "client" &
doconvert "server" &
wait

if [ $FAST_MODE ]; then
  cp ../config_client.bin ../../config_cs.bin
fi

echo This is the dev branch
