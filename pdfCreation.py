from fpdf import FPDF

pdf = FPDF(orientation = 'L', unit = 'mm',format = 'A4')
pdf.add_page()

#TEXTO
pdf.set_font('Arial','',12)

#Image
name = 'datyra-logo.png'
pdf.image(name,10,10,60,20)

#Salto de linea
pdf.ln(30)

pdf.multi_cell(0,10,'The next table shows the results obtained after performing tests with Selenium. \nCell values = Has permissions : Test result ')
pdf.ln(5)

width = 40
users = ['','SysAdmin','UserAdmin','Field Service ','EOL Tech','Engineering','Customer']
descriptions = ['Add Unit','Update Unit','Add Unit Notes','View Unit Notes','Delete Unit']

permission = [
    [True, True, True, True, True],
    [False, False, False, False, False],
    [False, True, False, True, True],
    [True, True, True, True, True],
    [False, True, False, True, True],
    [False, False, False, False, False]
]
resultList = [
    [True, True, True, True, False], 
    [False, True, True, True, True], 
    [False, True, True, True, True], 
    [False, True, True, True, True], 
    [False, True, True, True, True], 
    [False, True, True, True, True]
]

pdf.cell(w=280,h=15,txt='Test Report',ln=1,border = 1 ,align='C',fill=0)
pdf.set_font('Arial','B',12)
for user in users:
    pdf.cell(w=width,h=15,txt=user,border = 1 ,align='C',fill=0)
pdf.set_font('Arial','',12)
#Salto de linea
pdf.ln(15)
text = ''
for i in range(len(descriptions)):
    pdf.set_text_color(0,0,0)
    pdf.set_font('Arial','B',12)
    pdf.cell(w=width,h=15,txt=descriptions[i],border = 1 ,align='C',fill=0)
    
    pdf.set_font('Arial','',12)
    for j in range(len(users)-1):
        result = permission[j][i]
        if result == True:    
            text = 'Yes'
        else:
            text = 'No'

        if result == resultList[j][i]:
            pdf.set_text_color(8,130,21)
            text += ' / Succesful'        
        else:
            pdf.set_text_color(255,0,0)
            text += ' / Failure'        
        pdf.cell(w=width,h=15,txt=text,border = 1 ,align='C',fill=0)
    #Salto de linea
    pdf.ln(15)

pdf.output('testResults.pdf')