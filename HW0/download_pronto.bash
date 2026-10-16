mkdir pronto
cd pronto

echo "The Pronto dataset for data analysis." > README.txt

mkdir data
cd data

curl -L -O https://s3.amazonaws.com/pronto-data/open_data_year_one.zip

unzip open_data_year_one.zip

head  *.csv
