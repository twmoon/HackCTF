# -*- coding: utf-8 -*-
import urllib.request

url_start = "http://ctf.j0n9hyun.xyz:2025/" + '?'
idx = 1

while True:
    try:
        while 1:
            url = url_start + 'page=' + str(idx)
            print(url)

            req = urllib.request.Request(url)

            res = urllib.request.urlopen(req)
            data = res.read().decode('utf-8')

            if data.find('HackCTF{') != -1:
                print('\n\nDATA FOUND!!\n\n')
                answer = data[data.find('HackCTF'):(data.find('}</p>'))+1]
                print(answer)
                quit()
            idx += 1

    except Exception as e:
        continue
