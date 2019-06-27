import csv
import chardet

# function for get character encoding.
def get_char_encoding(file_name):
    # read file as a reading('r') binary('b') mode.
    # file opening would be protected by "with"
    with open(file_name, 'rb') as raw_file:
        # saved file data to "rawdata" variable.
        rawdata = raw_file.read()
        # chardet will detect the file encoding type.
        char_encoding = chardet.detect(rawdata)

    # return character encoding type
    return char_encoding['encoding']

# get "data_file_name" from stdin.
data_file_name = input('input csv file name')

# get "country_column_input" from stdin.
country_column_input = input('input country code column number.')
# "country_column_input value will be change to index. index value is as small as 1.
country_column = int(country_column_input) - 1

# define "country_code_file" as "iso-3166.csv"
country_code_file = 'iso-3166.csv'

# get character encoding using the function "get_char_encoding".
char_encoding = get_char_endcoding(country_code_file)


# open "country_code_file" as a reading('r') text('t') mode with setting encoding mode
# using the character encoding data getting from the function "get_char_encoding".
with open(country_code_file, 'rt', encoding=char_encoding) as iso_code_file:
    # define "iso_code_reader" as a csv reader getting data from "iso_code_file".
    iso_code_reader = csv.reader(iso_code_file)
    # define "iso_codes" as a "dictionary" type
    iso_codes = dict()

    # get data from iso_code_reader.
    for row in iso_code_reader:
        # save iso_code_reader data.
        # iso_codes will save "row[0]" as a data and "row[1]" as a key.
        iso_codes[row[1]] = row[0]

# get encoding type from data_file using a function "get_char_encoding".
char_encoding = get_char_encoding(data_file)

# open "data_file_name" file as a read-only mode as a "char_encoding" encoding type.
with open(data_file_name, 'r', encoding=char_encoding) as data_file:
    # define "data_file_reader: as a "data_file" csv reader.
    data_file_reader = csv.reader(data_file)

    # define "converted_rows" as a list type.
    converted_rows = list()

    # get data_file's data from the reader row by row.
    for row in data_file_reader:
        # get a data located in the raw's country_column.
        country_code = row[country_column]

        # check "iso_code" has "country_code".
        if country_code in iso_codes:
            # if iso_codes has country_code,
            # save the country_name located in iso_codes' country_code index as "country_name".
            country_name = iso_codes[country_code]
            # save "country_name" to row[country_column]/
            row[country_column] = country_name

        # save the row to "converted_rows" list.
        converted_rows.append(row)
        # print "row"
        print(row)

# open "new_data_file_name" as a writing(w) mode.
# encoding type is "char_encoding".
# newline='' is to remove a blank line after the data line.
with open('new_' + data_file_name, 'w', encoding=char_encoding, newline='') as new_file:
    # define "new_file_writer" as a "new_file"s csv writer.
    new_file_writer = csv.writer(new_file)

# save the converted_rows to "new_data_file_name" using "new_file_writer".
new_file_writer.writerows(converted_rows)