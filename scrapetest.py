#from bs4 import BeautifulSoup
import urllib.request as urllib2
import re
import zipfile
    
# получение контента страницы
req = urllib2.Request('https://www.ozon.ru/product/kurtka-outventure-1108129843/')
req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8')
req.add_header('Accept-Encoding', 'deflate, br')
req.add_header('Accept-Language', 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3')
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0')
req.add_header('Host', 'www.ozon.ru')
req.add_header('Cookie', 'cf_clearance=8o8vnhRfneON3v8BrkxwJhjJvkw2uJQevfGaD2g0edk-1706806331-1-AcOW2WGjZ+O3DxIPdwpmuxHAFwTdF+Jsi/zEUJNMgjiFFFRLhJyqtorwDjbKOjbP5at5bZYsje0ESHqqujBxrOI=; abt_data=b19a8bbf747e7978ccffa5df7e96ed74:2436cfdeb640d0f2369b0f5b654057da5c3e65ea417e3d19bdcfd50d1e10d68ed2d220accc3b6e1e8c704cc1d580f1c30af89b8bb07704d140bd69b9030f0435d4fb7499543c66514af79dd996290ad3a383cac26905cc661c80f96f378f8905dcc54af03abd516e274c8e50290195158c25ded80f60e95d663336367390c1e2e47ea09a008851d9694847a21c653cd40b515e7ea4b12c6552eeb6ce63bf4d891f84709db964b5d286114bedf280b2be0eef616fcd0074d5b42dcce00b5fff10; __Secure-ext_xcid=0b7adc1cfba4cbab75b84b84c15ea664; __Secure-refresh-token=4.0.osEq-RpPRC66wfmlCBX29A.36.Af-FNm28ksKjwJp7g08QSuWGG0uRUeMt4MnYIcCEqHYIFZ82vAjz1e7JdGxgCc_blw..20240205150439.d06Uk3mUvuiPU6GtxdZLj98P2nNdu_2fQeucWpnnffw; __Secure-access-token=4.0.osEq-RpPRC66wfmlCBX29A.36.Af-FNm28ksKjwJp7g08QSuWGG0uRUeMt4MnYIcCEqHYIFZ82vAjz1e7JdGxgCc_blw..20240205150439.FXtHq0W9asKmrvA1VZUOTR3ZLQC6iwc1nWq-lvgIlSk; __Secure-ab-group=36; __Secure-user-id=0; is_cookies_accepted=1; xcid=0b7adc1cfba4cbab75b84b84c15ea664; guest=true; ADDRESSBOOKBAR_WEB_CLARIFICATION=1707142374; rfuid=LTE5NTAyNjU0NzAsMzUuNzQ5OTY4MjIzMjczNzU0LDEzNzAwNjM5MTUsTGludXggeDg2XzY0LDE2ODg4NzQ2NjcsVzNzaWJtRnRaU0k2SWxCRVJpQldhV1YzWlhJaUxDSmtaWE5qY21sd2RHbHZiaUk2SWxCdmNuUmhZbXhsSUVSdlkzVnRaVzUwSUVadmNtMWhkQ0lzSW0xcGJXVlVlWEJsY3lJNlczc2lkSGx3WlNJNkltRndjR3hwWTJGMGFXOXVMM0JrWmlJc0luTjFabVpwZUdWeklqb2ljR1JtSW4wc2V5SjBlWEJsSWpvaWRHVjRkQzl3WkdZaUxDSnpkV1ptYVhobGN5STZJbkJrWmlKOVhYMHNleUp1WVcxbElqb2lRMmh5YjIxbElGQkVSaUJXYVdWM1pYSWlMQ0prWlhOamNtbHdkR2x2YmlJNklsQnZjblJoWW14bElFUnZZM1Z0Wlc1MElFWnZjbTFoZENJc0ltMXBiV1ZVZVhCbGN5STZXM3NpZEhsd1pTSTZJbUZ3Y0d4cFkyRjBhVzl1TDNCa1ppSXNJbk4xWm1acGVHVnpJam9pY0dSbUluMHNleUowZVhCbElqb2lkR1Y0ZEM5d1pHWWlMQ0p6ZFdabWFYaGxjeUk2SW5Ca1ppSjlYWDBzZXlKdVlXMWxJam9pUTJoeWIyMXBkVzBnVUVSR0lGWnBaWGRsY2lJc0ltUmxjMk55YVhCMGFXOXVJam9pVUc5eWRHRmliR1VnUkc5amRXMWxiblFnUm05eWJXRjBJaXdpYldsdFpWUjVjR1Z6SWpwYmV5SjBlWEJsSWpvaVlYQndiR2xqWVhScGIyNHZjR1JtSWl3aWMzVm1abWw0WlhNaU9pSndaR1lpZlN4N0luUjVjR1VpT2lKMFpYaDBMM0JrWmlJc0luTjFabVpwZUdWeklqb2ljR1JtSW4xZGZTeDdJbTVoYldVaU9pSk5hV055YjNOdlpuUWdSV1JuWlNCUVJFWWdWbWxsZDJWeUlpd2laR1Z6WTNKcGNIUnBiMjRpT2lKUWIzSjBZV0pzWlNCRWIyTjFiV1Z1ZENCR2IzSnRZWFFpTENKdGFXMWxWSGx3WlhNaU9sdDdJblI1Y0dVaU9pSmhjSEJzYVdOaGRHbHZiaTl3WkdZaUxDSnpkV1ptYVhobGN5STZJbkJrWmlKOUxIc2lkSGx3WlNJNkluUmxlSFF2Y0dSbUlpd2ljM1ZtWm1sNFpYTWlPaUp3WkdZaWZWMTlMSHNpYm1GdFpTSTZJbGRsWWt0cGRDQmlkV2xzZEMxcGJpQlFSRVlpTENKa1pYTmpjbWx3ZEdsdmJpSTZJbEJ2Y25SaFlteGxJRVJ2WTNWdFpXNTBJRVp2Y20xaGRDSXNJbTFwYldWVWVYQmxjeUk2VzNzaWRIbHdaU0k2SW1Gd2NHeHBZMkYwYVc5dUwzQmtaaUlzSW5OMVptWnBlR1Z6SWpvaWNHUm1JbjBzZXlKMGVYQmxJam9pZEdWNGRDOXdaR1lpTENKemRXWm1hWGhsY3lJNkluQmtaaUo5WFgxZCxXeUp5ZFMxU1ZTSXNJbkoxTFZKVklpd2ljblVpTENKbGJpMVZVeUlzSW1WdUlsMD0sMCwxLDAsMjQsMjM3NDE1OTMwLC0xLDIyNzEyNjUyMCwwLDEsMCwtNDkxMjc1NTIzLElFNWxkSE5qWVhCbElFZGxZMnR2SUV4cGJuVjRJSGc0Tmw4Mk5DQTFMakFnS0ZneE1Ta2dNakF4TURBeE1ERWdUVzk2YVd4c1lRPT0sZTMwPSw2NSwtMTI4NTU1MTMsMSwxLC0xLDE2OTk5NTQ4ODcsMTY5OTk1NDg4NywyOTI0MzUzODMsNA==')

#response = urllib2.urlopen(req)
#zip_data = response.read()

# распаковываем архив в переменную
#with zipfile._ZipStream(zip_data) as zip_ref:
 #   content = zip_ref.extract()

f = open('temp.txt', 'r')
content = f.read()

# парсим контент страницы
prices = re.findall(r'price":"([0-9\u2009]{3,})\u2009₽', str(content))
for p in prices:
    print(p.replace('\u2009',''))
print(prices)

price_block = re.findall(r'"(originalPrice|price)":"(.*?)"', content)
print(price_block)


#print(content)

#price_block = re.search(r'data-widget=\"webPrice\"', str(content))
#print(price_block)

exit

test_data = '<div params="[object Object]" class="lo4" data-widget="webPrice"><!----> <div class="lo3"><div class="lo a2435-a a2435-a3"><button tabindex="0" type="button" class="a2435-a4 a2435-a3" style="border-radius:8px;"><span class="a2435-b1 a2435-d6 a2435-f0 a2435-a3" style="border-radius:8px;"><div class="n0j"><div class="jn1 j1n"><div class="ol"><div class="lo0 n9l"><span class="ol2 o0l">2 483 ₽</span> <!----></div> <span class="ol0 n9l">c Ozon Картой</span></div></div><div class="n1j jn2"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" class="j2n"><path fill="currentColor" d="M5.293 12.293a1 1 0 1 0 1.414 1.414l5-5a1 1 0 0 0 0-1.414l-5-5a1 1 0 0 0-1.414 1.414L9.586 8l-4.293 4.293Z"></path></svg></div></div></span></button></div> <!----> <div class="lo6 pl0"><div class="lo9"><div class="l9o"><span class="l7o ol7 p0l">2 560 ₽</span> <!----> <span class="o6l o7l o5l lo7">6 299 ₽</span> <!----></div> <div class="ol8"><span class="o6l lo7">без Ozon Карты</span></div></div> <!----></div> <!----></div> <!----> <!----> <div><!----></div> <!----></div>'

#prices = re.findall(r'([0-9\u2009]{3,})\u2009₽', test_data)
#for p in prices:
#    print(p.replace('\u2009',''))
#print(prices)

#price_block = re.search(r'<div(.*?) data-widget="webPrice">(.*?)</div>', test_data)
#print(price_block)

#matches = re.findall(r'<span class="ol2 o0l">(.*?)</span>', test_data)

#print(matches)

#html = urlopen('https://yandex.com/', )
#bs= BeautifulSoup(html, 'html.parser')
#print(bs.h1)



#<div params="[object Object]" class="lo4" data-widget="webPrice"><!----> <div class="lo3"><div class="lo a2435-a a2435-a3"><button tabindex="0" type="button" class="a2435-a4 a2435-a3" style="border-radius:8px;"><span class="a2435-b1 a2435-d6 a2435-f0 a2435-a3" style="border-radius:8px;"><div class="n0j"><div class="jn1 j1n"><div class="ol"><div class="lo0 n9l"><span class="ol2 o0l">2 483 ₽</span> <!----></div> <span class="ol0 n9l">c Ozon Картой</span></div></div><div class="n1j jn2"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" class="j2n"><path fill="currentColor" d="M5.293 12.293a1 1 0 1 0 1.414 1.414l5-5a1 1 0 0 0 0-1.414l-5-5a1 1 0 0 0-1.414 1.414L9.586 8l-4.293 4.293Z"></path></svg></div></div></span></button></div> <!----> <div class="lo6 pl0"><div class="lo9"><div class="l9o"><span class="l7o ol7 p0l">2 560 ₽</span> <!----> <span class="o6l o7l o5l lo7">6 299 ₽</span> <!----></div> <div class="ol8"><span class="o6l lo7">без Ozon Карты</span></div></div> <!----></div> <!----></div> <!----> <!----> <div><!----></div> <!----></div>
