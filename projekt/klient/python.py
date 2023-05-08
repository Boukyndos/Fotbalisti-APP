from js import document

def sub(*args):
    result = Element('output')
    
    jmeno = Element('jm').value
    prijmeni = Element('pr').value
    cisloDresu = Element('cd').value
    nastrilenychGolu = Element('ng').value

    result.write(f"{jmeno,prijmeni,cisloDresu,nastrilenychGolu}")