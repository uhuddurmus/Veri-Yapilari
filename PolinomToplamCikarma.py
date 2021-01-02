px = {}
qx = {}
result = {}
while True: 
    entry = input("Px Elamanlarını önce katsayı ardından üst gelcek şekilde tek tek yazıp her elamanın sonunda entera basınız. En son bitirmek için end yazınız:")
    if entry != 'end': 
        px[int(entry.split()[1])] = int(entry.split()[0]) # bir dictionary tutuyorum. key: üs, value: katsayı
    else: 
        break
while True: 
    entry = input("Qx Elamanlarını önce katsayı ardından üst gelcek şekilde tek tek yazıp her elamanın sonunda entera basınız. En son bitirmek için end yazınız:")
    if entry != 'end': 
        qx[int(entry.split()[1])] = int(entry.split()[0]) # bir dictionary tutuyorum. key: üs, value: katsayı
    else: 
        break
        
operation = input("Toplama için + çıkarma için - yazınız  : ")
if operation == "+":  
    for key in px: # 1. polinomdaki bütün elemanlara bakıyorum
        if key in qx: # eğer 1. polinomdaki bir "üs" 2. polinomda da varsa, onların katsayılarını toplayıp sonuca yazıyorum. 
            result[key] = px[key] + qx[key]
        else: # eğer üs 1. polinomda var ama 2. polinomda yoksa, toplamadan direk sonuca yazıyorum. 
            result[key] = px[key]
    for key in qx: # 2. polinomdaki bütün elemanlara bakıyorum
        if key not in px: # ortak elemanlara zaten bir önceki dömgüde bakmıştım. burada sadece 2. polinomda olup 1.sinde olmayan "üs"lere bakmam yeterli
            result[key] = qx[key]   
    for key in result: 
        print (str(result[key]) + "x" + str(key), end=" ")

if operation == "-": 
    for key in px: # 1. polinomdaki bütün elemanlara bakıyorum
        if key in qx: # eğer 1. polinomdaki bir "üs" 2. polinomda da varsa, onların katsayılarını çıkarıp sonuca yazıyorum. 
            result[key] = px[key] - qx[key]
        else: # eğer üs 1. polinomda var ama 2. polinomda yoksa, çıkarmadan direk sonuca yazıyorum. 
            result[key] = px[key]
    for key in qx: # 2. polinomdaki bütün elemanlara bakıyorum
        if key not in px: # ortak elemanlara zaten bir önceki dömgüde bakmıştım. burada sadece 2. polinomda olup 1.sinde olmayan "üs"lere bakmam yeterli
            result[key] = qx[key] * -1       
    for key in result: 
        print (str(result[key]) + "x" + str(key), end=" ")
