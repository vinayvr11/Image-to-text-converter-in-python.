from PIL import Image
from pytesseract import image_to_string
from skimage import io
import pytesseract
import pandas as pd
import re
import glob,os

#os.chdir('D:\image_extract_text\images\image_folder')




pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'



namex1 = 45
namex2 = 420
namey1 = 140
namey2 = 275

c = 375   
name = []
pita = []
house_no = []
age = []
gender = []

take_file = []

for files in glob.glob('*.jpg'):
    
    take_file.append(files)    


for kl in take_file:
    
    
    d = io.imread(kl)
    
    for n in range(0,10):
        
        for m in range(0,3):
        
            cro2 = d[namey1:namey2,namex1:namex2-82]
    
            io.imsave('D:/image_extract_text/glo/crop/v3.jpg',cro2)


            im1 = image_to_string(Image.open('D:/image_extract_text/glo/crop/v3.jpg'), lang='hin', config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')

            with open('v.txt', 'w', encoding='utf-8') as l:
            
                l.write(im1)
                
            fil = open('v.txt', encoding='utf-8')
        
            for take in fil:
                st = str(take)
            
                if re.findall('^नाम', st):
                    if ':' in st:
                        
                        name.append(st.split(':')[-1])
                    else:
                        name.append(st.split('-')[-1])
                            
                elif re.findall('^प्रति',st):
                    pita.append(st)
                
                elif re.findall('^पति', st):
                    pita.append(st)
                elif re.findall('^पिता',st):
                    pita.append(st)
                    
                elif re.findall('^मकान', st):
                    
                    house_no.append(st.split(':')[-1])
            
                elif re.findall('^आ', st):
                    gender.append(st.split()[-1])
                    age.append(st)



            #main part starts of calculations- 
            
            namex1 = namex2
            namex2 = namex1 + c
        namex1 = 45
        namex2 = 420
        namey1 += 145
        namey2 += 149
    
    namey1 = 140
    namey2 = 275

    
s1 = pd.Series(name)
s2 = pd.Series(pita)
s3 = pd.Series(house_no)
s4 = pd.Series(age)
s5 = pd.Series(gender)


data = pd.DataFrame({'Name':s1,'Spouse':s2,'House_no':s3,'Age':s4,'Gender':s5})
write = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
data.to_excel(write, sheet_name='sheet1', index=False)
write.save()


