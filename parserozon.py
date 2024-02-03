import requests


#params = { "q" : "funny cats" }

#response = requests.get("https://www.google.com/search", params=params)
#response = requests.get("https://www.google.com/search?client=firefox-b-lm&q=parsing")
response = requests.get("https://www.ozon.ru/product/xiaomi-smartfon-redmi-12c-4-128-gb-temno-seryy-1051011868/?advert=h3w98OkIKBJ8jvf_qYugd10ek0nZG4QAG7Qz7LakskhvpJSbXgcO19h295bY9Ft4CWsVR5SLRcDjIl3h0vksa2_Mu40gZj-larMPBFnByP0Kp8Vuls9UsBwGfv4eZXu_m0rz7QyavvLaDUY33Nd--AoF5lCR2c-ynyVJ2Ts9eDzi4DTiTh0Xbs3f2I89tWAEKK0zsnwmmkTE3MEt-vTso3rfDd1geyXm_wf4GKK3jDn4A5wfG8jKzU6NFYv2EyGTOKxfem8&avtc=1&avte=2&avts=1706803573")


#print(response.status_code)
#print(response.headers)
print(response.text)
