import datetime
import glob

dt = datetime.datetime.now()
code = ['!','@','#','$','%','^','&','*','(',')','-','+','=',';',':','`','~','?','/','<','>','1','2','3','4','5',
        'A','E','I','O','U','a','e','i','o','u','D','M','N','G','Z','d','m','n','g','z','R','W']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            '1','2','3','4','5','6','7','8','9','0','.','?','!','/','\'',':','-','(',')',',','@','_']
files = []
files = [f for f in glob.glob('*.txt', recursive=True)]
login = False
attempts = 5
deb = []


while login == False:
    print('Password:')
    raw = input('>>>')
    if raw == 'codenotes':
        login = True
    elif attempts == 1:
        print('you are out of attempts')
        print(0/0)
    else:
        attempts -= 1
        print('Incorrect, there are %s attempts left' % attempts)

print('Welcome to Code Notes alpha v1')
def coded(inp):
    message = []
    word = []
    usr = inp.split(' ')
    for i in usr:
        usrword = list(i)
        for i in usrword:
            if i in alphabet:
                cindex = alphabet.index(i)
                word.append(str(cindex))
            elif i == ' ':
                word.append('27')
        message.append('.'.join(word))
        word.clear()
    fmessage = '|'.join(message)
    return fmessage

def decoded(inp):
    message = []
    usr = inp.split('.')
    for i in usr:
        try:
            if i == 27:
                message.append(' ')
            else:
                message.append(alphabet[int(i)])
        except ValueError:
            pass
    fmessage = ''.join(message)
    return str(fmessage)

def write(inp):
    message = []
    word = []
    x = 1
    while x == 1:
        f = open(inp, 'a+')
        raw = input('Writer>>>').lower()
        usr = raw.split(' ')
        if len(usr) == 1 and usr[0] == 'done':
            print('Finished!')
            f.close()
            break
        else:
            for i in usr:
                usrword = list(i)
                for i in usrword:
                    if i in alphabet:
                        cindex = alphabet.index(i)
                        word.append(code[cindex])
                message.append(''.join(word))
                word.clear()
            fmessage = '|'.join(message)
            message.clear()
            f.write(fmessage + 'T')
    f.close()

def create(inp):
    c = open(inp, 'w+')
    c.close()
    y = 1
    files = [f for f in glob.glob('*.txt', recursive=True)]
    print('Files:')
    for f in files:
        print('%d)%s' % (y, f))
        y += 1

def read(inp):
    message = []
    word = []
    r = open(inp, 'r')
    text = r.read().split('|')
    for i in text:
        textword = list(i)
        for i in textword:
            if i in code:
                cindex = code.index(i)
                word.append(alphabet[cindex])
            elif i == 'T':
                word.append('\n')
        message.append(''.join(word))
        word.clear()
    fmessage = ' '.join(message)
    if fmessage == '':
        print('[Empty Document]')
    else:
        print(fmessage)
    r.close()

y = 1
for f in files:
    dcd = decoded(f[:-4])
    print('%d) %s.txt' % (y, dcd))
    y += 1

fname = []
x = 1
while x == 1:
    raw = input('>>>').lower()
    usr = raw.split(' ')
    if len(usr) >= 2:
        fname = ('%s.txt' % coded(usr[1]))
    if usr[0] == 'write':
        if fname in files:
            print('Writing in: %s' % fname)
            read(fname)
            write(fname)
        else:
            print('File not found, creating file: %s' % fname)
            write(fname)
    elif usr[0] == 'help':
        print('commands:\n write [file]\tread [file]\nlist')
    elif usr[0] == 'read':
        if fname in files:
            dcd = decoded(fname[:-4])
            print('Now Reading %s' % dcd)
            read(fname)
        else:
            print('File not found')
    elif usr[0] == 'clear':
        if fname in files:
            w = open(fname, 'w')
            w.write('')
            w.close()
        else:
            print('File not found')
    elif usr[0] == 'list':
        y = 1
        files = [f for f in glob.glob('*.txt', recursive=True)]
        print('Files:')
        for f in files:
            dcd = decoded(f[:-4])
            print('%d) %s.txt' % (y, dcd))
