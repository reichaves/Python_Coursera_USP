from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

from urllib.request import urlopen
from bs4 import BeautifulSoup

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

html = urlopen("http://www.cbf.com.br/competicoes/brasileiro-serie-a/tabela/2016#.WQTfO9orLIV")
bsObj = BeautifulSoup(html.read(), 'html.parser')

nameList = bsObj.findAll('div', class_="full-game-links")

sumulas = []
for name in nameList:
    res = str(name.find('a'))
    #print (res)
    j = res.find('url[]=')
    k = res.find('.pdf')
    sumula = res[j+6:k+4]
    if len(sumula) > 0:
        sumulas.append(sumula)

arquivos = []
for sumula in sumulas:
    j = sumula.find('2016')
    #f = open(sumula[j+5:], 'wb')
    arquivos.append(sumula[j+5:])
    print (sumula[j+5:])
    #dados = urlopen(sumula).read()
    #f.write(dados)
    #f.close()

antes_juiz = 'Quarto Arbitro:\n\n'
wc = {}
for arquivo in arquivos:
    pdfFile = open(arquivo, 'rb')
    res = readPDF(pdfFile)
    if 'Delegado Local:\n\n' in res:
        antes_juiz = 'Delegado Local:\n\n'
    elif 'Delegado  Especial:\n\n' in res:
        antes_juiz = 'Delegado  Especial:\n\n'
    if 'Inspetor:\n\n' in res:
        antes_juiz = 'Inspetor:\n\n'
    if 'Assessor:\n\n' in res:
        antes_juiz = 'Assessor:\n\n'
    if 'Tutor:\n\n' in res:
        antes_juiz = 'Tutor:\n\n'

    j = res.find(antes_juiz)
    j = j + len(antes_juiz)
    k = res.find('\n\n',j) #depois
    juiz = res[j:k]
    print (juiz)
    if juiz in wc:
        wc [juiz] += 1
    else:
        wc [juiz] = 1
    pdfFile.close()
    antes_juiz = 'Quarto Arbitro:\n\n'

print ('\nVinte juízes que mais atuaram')
def atuações(dupla):
    return dupla[1]

duplas = sorted(wc.items(), key=atuações, reverse=True)
for dupla in duplas[:20]:
    print (dupla[0], dupla[1])
