from fileReader import FileReader

reader = FileReader()

to_find = ["Trademarks and Trade Names."] # words for searching
complete_path = "v5_signage_bad4.docx" # complete path to file location, can be pdf or word
# header_only=True means it will return only headings

result = reader.find(path=complete_path, to_find=to_find, headers_only=True)

for line in result:
    print line
