from fpdf import FPDF

title = 'Maintanance report'

address = 'P.O Box: 14045, Ajman, U.A.E \n Tel:+971 6 7411426 \n Fax: +971 6 7411427 \n Mail: info@mastersystems-intl.com \n Web: www.mastersystems.org'

job_no = 'JB01220508284'
job_txt = 'Job no: ' + job_no

WO_PO_no = ''
WO_PO_txt = 'WO/PO No: ' + str(WO_PO_no)

uniq_id = 116998
id_txt = 'S. No: ' + str(uniq_id)

user_data = (
    ('VESSEL NAME', 'SAGAR VIOLET', 'LOCATION', 'KORFAKKAN ANCH', 'ENGINEER', 'NAME'),
    ('PIC', 'JERIL', 'IMO', '9292981', 'DATE', '06/05/2022'),
    ('EQPT', 'INSPECTION', 'MAKE/MODEL', 'IT AND V SAT', 'SL NO', str(uniq_id))
)

# template
class PDF(FPDF):
    def header(self):
        #image
        self.image('logo.png', x = 10,y = 10, w = report_pdf.epw / 4)
        self.ln(5)
        # font
        self.set_font('helvetica', 'B', 10)
        self.set_x(120)
        title_w = 0
        title_line_h = 4
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
    
    # Report data in table
    def table_data(self, data):
        self.set_font("Times",'B', size=9)
        line_height = (self.font_size * 2.5) + 1
        col_width = self.epw / 6  # distribute content evenly
        for row in data:
            for datum in row:
                self.multi_cell(col_width, line_height, datum, border=1,
                        new_x="RIGHT", new_y="TOP", max_line_height=report_pdf.font_size, align='C')
            self.ln(line_height)
        self.ln(10)
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
report_pdf.set_font('times', '', 12)
report_pdf.cell(80, 8, job_txt, border=1)
report_pdf.ln()
report_pdf.cell(80, 8, WO_PO_txt, border=1)
report_pdf.ln(20)

report_pdf.set_y(50)
report_pdf.set_font('times', '', 14)
report_pdf.cell(0, 8, 'S. No:             ', align='R')
report_pdf.set_text_color(255,0,0)
report_pdf.cell(0, 8, str(uniq_id), align='R')
report_pdf.set_text_color(0,0,0)
report_pdf.ln(20)


# report title
report_pdf.page_title('SERVICE REPORT')

# Data on box
report_pdf.table_data(user_data)

#report body
report_pdf.report_body('chp1.txt')

# end each chapter
report_pdf.set_font('times', 'I', 12)
report_pdf.cell(0, 5, 'END OF CHAPTER',border=1)


# creating pdf
report_pdf.output('report.pdf')