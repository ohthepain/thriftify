#set -e
EXCEL_DIR=`pwd`
UTILS_DIR=$EXCEL_DIR/../Utils

MUTATE_PY=$UTILS_DIR/mutate.py

cd ..
cd Thrift
bash compile_thrift.sh

cd ..
cd Excel

echo Pre-mutators ...
python3 $MUTATE_PY Premutators BadEnergy.Config --thrift_protocol TJSONProtocol
echo Mutators ...
python3 $MUTATE_PY Mutators BadEnergy.Config --thrift_protocol TJSONProtocol

