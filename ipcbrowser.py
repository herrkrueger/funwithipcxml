import requests, zipfile, io, os, time

tic = time.perf_counter() * 1000

url = 'https://www.wipo.int/ipc/itos4ipc/ITSupport_and_download_area//20210101/MasterFiles/ipc_scheme_20210101.zip'
r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

filename = os.listdir()[1]

toc = time.perf_counter() * 1000

print('downloaded and unzipped', filename, f'in: {(toc - tic):0.0f} ms')


from lxml import etree as ET

filename = "./EN_ipc_scheme_20210101.xml"
parser = ET.XMLParser(remove_blank_text=True)
tree = ET.parse(filename, parser=parser)
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
