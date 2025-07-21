
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 17:01:07 2017

@author: Miguel
"""
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
   
import glob
from xml.dom import minidom
   
if __name__ == "__main__":
    #ruta = 'C:/Users/Miguel/Documents/sat/facturas electronicas/'
    ruta = 'D:/invoiceDownload/'
    #ruta = 'C:/Users/Miguel/Documents/trabajo/Black Owl/contabilidad/facturas/'    
    conjuntoDeXmls = ruta + '*.xml'
    archivoSalida = ruta + 'salidaFacturas'
    archivoLog = ruta + 'cfdiparser.log'

    files = glob.glob(conjuntoDeXmls)
    
    #salida = io.open(archivoSalida, 'w', encoding='utf8')
    salida = open(archivoSalida, 'w')
    logfile = open(archivoLog, 'w')
    

    for archivo in files:
        
        nomArchivo = archivo[len(ruta)-1+1:len(archivo)]
        logfile.write(nomArchivo + '\n')
          
        xmldoc = minidom.parse(archivo)

        #print('primer canalla')
        itemlist = xmldoc.getElementsByTagName('cfdi:Emisor')
        try:
          nombre = itemlist[0].attributes['nombre'].value
        except:
            nombre = itemlist[0].attributes['Nombre'].value
        
        
        try:
            rfc =    itemlist[0].attributes['rfc'].value
        except:
            rfc =    itemlist[0].attributes['Rfc'].value


        itemlist = xmldoc.getElementsByTagName('cfdi:Comprobante')
        try:
            subtotal = itemlist[0].attributes['subTotal'].value
        except:
            subtotal = itemlist[0].attributes['SubTotal'].value
        
        try:
            descuento = itemlist[0].attributes['Descuento'].value
        except:
            descuento = '0'
        
        try:
            total = itemlist[0].attributes['Total'].value
        except:
            total = itemlist[0].attributes['total'].value
        
        
        subtotalOutput = str(float(subtotal) - float(descuento))
        iva = str(float(total) - float(subtotalOutput))
        
        
        #cadenaSalida = nomArchivo + '\nnombre' + nombre + '\nRFC:' + rfc + '\nSubtotal:' + subtotal + '\niva:' + iva + '\ndescuento:' + descuento + '\ntotal' + total + '\n\n'
        cadenaSalida = nomArchivo + '@' +nombre + '@' + rfc + '@' + subtotalOutput + '@' + iva + '@' + total + '\n'
        
        
        #print(archivo + '\n')        
        #print(cadenaSalida)
        #salida.write(archivo + '\n')
        #salida.write(archivo + '@')
        cadenaSalidaUTF = cadenaSalida.encode('utf-8')
        #salida.write(cadenaSalidaUTF)
        salida.write(cadenaSalida)
    logfile.close()
    salida.close()   
    

'''
ESTO ERA PARA LA VERSIÓN ANTERIOR DEL CFDI   
     itemlist = xmldoc.getElementsByTagName('cfdi:Traslado')
        #iva = itemlist[0].attributes['totalImpuestosTrasladados'].value
        contadorIva = 0        
        for impuesto in itemlist:
            
            if (impuesto.attributes['impuesto'].value == 'IVA'):
                if (int(float(impuesto.attributes['tasa'].value)) == 16):
         #           if (contadorIva == 0):
                      iva = impuesto.attributes['importe'].value
                      contadorIva = 1
                else:
                    if (contadorIva == 0):
                      iva = '0'
                    
         #         xmldoc = minidom.parse('C:/Users/Miguel/Documents/sat/facturas electronicas/SECFD_20170417_043241.xml')      
'''      
                  







