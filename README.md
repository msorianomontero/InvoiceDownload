# InvoiceDownload
Two simple Python scripts for downloading Mexican invoices from Gmail and retrieve invoice info. Great for accountants.

In Mexico, legal invoices are digital. They consist of an XML file that has all the info regarding the purchase as well as a visual PDF representation of the invoice. They must be sealed by the Internal Revenue Secretary (Secretaría de Hacienda y Crédito Público), and are usually delivered via e-mail. In order for accountants to keep track of the invoices, they must download both files and usually they register by hand all the relevant information:
1) RFC of the issuer (the unique identifier for any person or company)
2) Invoice ID
3) Products / Services
4) Sales Tax per item (in Mexico the majority of the products incorporate a 16% sales tax, while some products and services, such as medicine and medical consultations have a 0% sales tax).

I wrote these two scripts to drastically reduce the time consumed by downloading and logging my invoices on an Excel file by hand.
