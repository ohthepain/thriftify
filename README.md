# setup

> python3 -m venv .venv
> source .venv/bin/activate
> pip install -r requirements.txt

to run tests just do
> pytest

# xl2thrift

Converts xlsx files into thrift-loadable binary or json blobs
[XLSX Format](https://guides.github.com/features/mastering-markdown/)

[Rules for Sheet Name Matching]
Example: 
"Shop Sections -- special offers"
matches the line in your .thrift file 
"31: optional map<string, ShopSection> shopSections"

Spaces are removed. '--' denotes a comment.
Sheet names can contain 

[Multiple sheets per collection]
You can have as many sheets as you like populating the same collection.

Example:
"Shop Sections -- special offers"
"Shop Sections -- gems"

[Blank Lines]
Processing a sheet stops on the first blank line

[Empty Columns]
Processing a row stops on the first column that has no name

[Ignored Columns]
Columns that do not match are ignored. This is useful for calculations.

[Lists]

[Dictionaries]

[The Main Collection]
There needs to be a 'root' object that contains all of the collections. 
