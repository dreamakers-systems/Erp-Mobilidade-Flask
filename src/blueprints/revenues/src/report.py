"""Create images with pillow. This images are a report for the drive's."""


from PIL import Image, ImageDraw, ImageFont

font_path = './src/static/dist/fonts/Roboto-Regular.ttf'
logo_path = './src/static/dist/img/logo.png'


def save_report(name, date_one, date_two, data_frame, motorist_id='000'):
    # Configs
    width = 595
    height = 842

    # Page
    img = Image.new('RGBA', (width, height), color='#E5E5E5')

    # Top Retangle
    top_retangle = ImageDraw.Draw(img)
    top_retangle.rectangle([(0, 0), (595, 86)], fill='#1A336B')
    top_retangle.text(
        (40, 27),
        'Fatura Semanal - G4 Mobile',
        (255, 255, 255),
        font=ImageFont.truetype(font_path, 24),
    )

    # Content Retangle
    content_retangle = ImageDraw.Draw(img)
    content_retangle.rectangle([(596, 86), (595, 86)], fill='#E5E5E5')

    table_retangle = ImageDraw.Draw(img)
    table_retangle.rectangle(
        [(40, 260), (550, 630)], fill='#E5E5E5', outline='#000000'
    )

    content_retangle.text(
        (40, 110), 'Nome:', (0, 0, 0), font=ImageFont.truetype(font_path, 14)
    )
    name_retangle = ImageDraw.Draw(img)
    name_retangle.rectangle(
        [(40, 130), (550, 160)], fill='#E5E5E5', outline='#000000'
    )

    content_retangle.text(
        (40, 180), 'ID:', (0, 0, 0), font=ImageFont.truetype(font_path, 14)
    )
    id_retangle = ImageDraw.Draw(img)
    id_retangle.rectangle(
        [(40, 200), (180, 230)], fill='#E5E5E5', outline='#000000'
    )

    content_retangle.text(
        (250, 180),
        'Data Inicial:',
        (0, 0, 0),
        font=ImageFont.truetype(font_path, 14),
    )

    data_one_retangle = ImageDraw.Draw(img)
    data_one_retangle.rectangle(
        [(250, 200), (380, 230)], fill='#E5E5E5', outline='#000000'
    )

    content_retangle.text(
        (420, 180),
        'Data Final:',
        (0, 0, 0),
        font=ImageFont.truetype(font_path, 14),
    )

    data_two_retangle = ImageDraw.Draw(img)
    data_two_retangle.rectangle(
        [(420, 200), (550, 230)], fill='#E5E5E5', outline='#000000'
    )

    content_retangle.text(
        (85, 270), 'Valor:', (0, 0, 0), font=ImageFont.truetype(font_path, 14)
    )

    content_retangle.text(
        (180, 270),
        'Quantidade:',
        (0, 0, 0),
        font=ImageFont.truetype(font_path, 14),
    )

    content_retangle.text(
        (300, 270),
        'Recebido:',
        (0, 0, 0),
        font=ImageFont.truetype(font_path, 14),
    )

    content_retangle.text(
        (420, 270),
        'A Pagar:',
        (0, 0, 0),
        font=ImageFont.truetype(font_path, 14),
    )

    content_retangle.text(
        (50, 660),
        'Total de Corridas',
        (0, 0, 0),
        font=ImageFont.truetype(font_path, 14),
    )

    total_runs_retangle = ImageDraw.Draw(img)
    total_runs_retangle.rectangle(
        [(48, 680), (189, 720)], fill='#E5E5E5', outline='#000000'
    )

    content_retangle.text(
        (232, 660),
        'Total Recebido',
        (0, 0, 0),
        font=ImageFont.truetype(font_path, 14),
    )

    total_recived_retangle = ImageDraw.Draw(img)
    total_recived_retangle.rectangle(
        [(230, 680), (370, 720)], fill='#E5E5E5', outline='#000000'
    )

    content_retangle.text(
        (400, 660),
        'Total a Pagar',
        (0, 0, 0),
        font=ImageFont.truetype(font_path, 14),
    )

    total_to_pay_retangle = ImageDraw.Draw(img)
    total_to_pay_retangle.rectangle(
        [(400, 680), (530, 720)], fill='#E5E5E5', outline='#000000'
    )

    # Footer Retangle
    footer_retangle = ImageDraw.Draw(img)
    footer_retangle.rectangle([(0, 742), (595, 842)], fill='#1A336B')

    content_retangle.text(
        (150, 755),
        'Muito Obrigado pela sua Colaboração! \n'
        'A Forma de Pagamento estará no Grupo da Diretória \n'
        '',
        (255, 255, 255),
        font=ImageFont.truetype(font_path, 15),
        align='center',
    )

    valor = 290
    total = data_frame.pop(-1)

    content_retangle.text(
        (95, 689),
        '{:03}'.format(total[1]),
        (0, 0, 0),
        font=ImageFont.truetype(font_path, 20),
    )

    content_retangle.text(
        (245, 689),
        '{}'.format(total[2]),
        (0, 0, 0),
        font=ImageFont.truetype(font_path, 18),
    )

    content_retangle.text(
        (415, 689),
        '{}'.format(total[3]),
        (0, 0, 0),
        font=ImageFont.truetype(font_path, 18),
    )

    content_retangle.text(
        (55, 137),
        '{}'.format(name),
        (0, 0, 0),
        font=ImageFont.truetype(font_path, 18),
    )

    content_retangle.text(
        (55, 205),
        '{}'.format(motorist_id),
        (0, 0, 0),
        font=ImageFont.truetype(font_path, 18),
    )

    content_retangle.text(
        (260, 205),
        '{}'.format(date_one),
        (0, 0, 0),
        font=ImageFont.truetype(font_path, 18),
    )

    content_retangle.text(
        (430, 205),
        '{}'.format(date_two),
        (0, 0, 0),
        font=ImageFont.truetype(font_path, 18),
    )

    for row in data_frame:
        content_retangle.text(
            (80, valor),
            '{}'.format(row[0]),
            (0, 0, 0),
            font=ImageFont.truetype(font_path, 12),
        )

        content_retangle.text(
            (200, valor),
            '{}'.format(row[1]),
            (0, 0, 0),
            font=ImageFont.truetype(font_path, 12),
        )

        content_retangle.text(
            (300, valor),
            '{}'.format(row[2]),
            (0, 0, 0),
            font=ImageFont.truetype(font_path, 12),
        )

        content_retangle.text(
            (420, valor),
            '{}'.format(row[3]),
            (0, 0, 0),
            font=ImageFont.truetype(font_path, 12),
        )
        valor = valor + 20
        logo = Image.open(logo_path)
        img.alpha_composite(logo, (370, 16))
        img.convert('RGB')

    return img
