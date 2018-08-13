import urllib
from bs4 import BeautifulSoup
#your code here
def gets_urls(url):
    u = urllib.urlopen(url)
    html = u.read()
    return html

def content_search(url, extension):
    read_url = gets_urls(url)
    soup = BeautifulSoup(read_url, 'html.parser')
    links = soup.find_all('a', href = True)
    for link in links:
        if extension in link.get('href'):
            # Aqui fiz um ajuste para poder ter o nome do arquivo
            filename = link.get('href').split('/')[-1]
            # Ajustei nesta variável a url sem o nome do arquivo porque a url de download é diferente.
            new_url = url.replace('turnstile.html','')
            # Coloquei mais o parametro do nome do arquivo, porque o urlretrieve precisa do nome do arquivo para gerar o arquivo.
            save_file(link.get('href'), new_url ,filename)

def save_file(link, url, filename):
    # Só juntei a url final do arquivo
    url_file = url + '/' + link
    urllib.urlretrieve(url_file,filename)

content_search('http://web.mta.info/developers/turnstile.html', '1706')

def create_master_turnstile_file(filenames, output_file):
    with open(output_file, 'w') as master_file:
        master_file.write('C/A,UNIT,SCP,STATION, LINENAME, DIVISION, DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
        for filename in filenames:
            # your code here
            with open(filename, 'r') as r:
                r.readline()
                master_file.writelines(r.read())
    return None

filenames = ["turnstile_170603.txt","turnstile_170610.txt","turnstile_170617.txt","turnstile_170624.txt"]
create_master_turnstile_file(filenames,'result_file.txt')
