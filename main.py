import PyPDF4

# abrir el archivo PDF
pdf_file = open('nombre_archivo.pdf', 'rb')

# crear un objeto PyPDF4 PdfReader
pdf_reader = PyPDF4.PdfFileReader(pdf_file)

# crear un objeto PyPDF4 PdfWriter
pdf_writer = PyPDF4.PdfFileWriter()

# agregar contraseñas para proteger el archivo. 
# la contraseña_usuario es la que pedirá cualquier programa al querer abrir el archivo PDF, 
# la contraseña_admin es opcional (dejar en blanco para no asignar, ejemplo: '')
pdf_writer.encrypt('contraseña_usuario', 'contraseña_admin')

# copiar las páginas del archivo original al archivo protegido
for page in pdf_reader.pages:
    pdf_writer.addPage(page)

# guardar el archivo protegido
result_pdf = open('nombre_archivo_final.pdf', 'wb')
pdf_writer.write(result_pdf)

# cerrar los archivos
result_pdf.close()
pdf_file.close()
