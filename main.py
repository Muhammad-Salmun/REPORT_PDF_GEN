from fpdf import FPDF

title = 'Maintanance report'

address = 'P.O Box: 14045, Ajman, U.A.E \n Tel:+971 6 7411426 \n Fax: +971 6 7411427 \n Mail: info@mastersystems-intl.com \n Web: www.mastersystems.org'

job_txt = 'Job no: '

# template
class PDF(FPDF):
    def header(self):
        #image
        self.image('logo.png', x = 10,y = 10, w = report_pdf.w / 4)
        # font
        self.set_font('helvetica', 'B', 10)
        self.set_x(120)
        title_w = 0
        title_line_h = 5.5
        # Title
        self.multi_cell(title_w, title_line_h, address, align='R')
        # Line break
        self.ln(10)

    # Page footer
    def footer(self):
        # Set position of the footer
        self.set_y(-15)
        # set font
        self.set_font('helvetica', 'I', 8)
        # Set font color grey
        self.set_text_color(169,169,169)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    # Adding page title to start of each page
    def page_title(self, ch_title):
        # set font
        self.set_font('helvetica', 'B', 14)
        # Chapter title
        self.cell(0, 5, ch_title,align='C', ln=1)
        # line break
        self.ln()

    # Chapter content
    def report_body(self, name):
        # read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # set font
        self.set_font('times', '', 12)
        # insert text
        self.multi_cell(0, 5, txt)
        # line break
        self.ln()

# start a pdf element
report_pdf = PDF('P', 'mm', 'A4')

# metadata
report_pdf.set_title(title)
report_pdf.set_author('Muhammad Salmun')

# Set auto page break
report_pdf.set_auto_page_break(auto = True, margin = 25)

# Add Page
report_pdf.add_page()


## content of page
# data with border
report_pdf.set_font('times', '', 16)
report_pdf.cell(80, 8, job_txt, border=1)
report_pdf.ln(20)

# report title
report_pdf.page_title('SERVICE REPORT')

#report body
report_pdf.report_body('chp1.txt')

# end each chapter
report_pdf.set_font('times', 'I', 12)
report_pdf.cell(0, 5, 'END OF CHAPTER',border=1)


# creating pdf
report_pdf.output('report.pdf')