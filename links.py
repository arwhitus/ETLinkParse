import xml.etree.ElementTree as ET

tree = ET.parse('input.xml')
root = tree.getroot()

file = open("output.md", "w+")

count = 0
for project in root.findall('project'):
    shortLink = project.get('href')
    
    fullLink = 'http://www.espaces-transfrontaliers.org' + shortLink
    
    title = shortLink[:-1]
    title = title[title.rfind('/')+1:]
    
    line = '[' + title + '](' + fullLink + ')'
    
    file.write(line)
    file.write('\n\n')
    
    print(line)
    count = count + 1
    
file.close()

message = 'Links saved: ' + str(count)
print(message)
