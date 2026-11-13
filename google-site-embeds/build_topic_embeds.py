import html,sys
CSS='<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;700;800&display=swap" rel="stylesheet"><style>body{margin:0;font-family:Manrope,Arial,sans-serif;color:#0b1330;background:#fff}h2{font-size:15px;letter-spacing:.08em;text-transform:uppercase;color:%(c)s;margin:22px 4px 10px;border-bottom:2px solid %(c)s;padding-bottom:6px}h2:first-child{margin-top:4px}.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:10px}a{display:block;text-decoration:none;background:#f3f5fa;border:1px solid #c9d2e4;border-left:6px solid %(c)s;border-radius:10px;padding:11px 14px}a.t{border-left-color:#ffd24a}a:hover,a:focus{background:#e3eafb;border-color:#1c3fb0}b{display:block;font-size:15px;font-weight:800;color:#0b1330}i{display:block;font-style:normal;font-size:12px;font-weight:700;color:%(c)s;text-transform:uppercase;letter-spacing:.06em}a.t i{color:#8a6a00}</style>'
def page(colour,sections):
    o=[CSS%{'c':colour}]
    for title,cards in sections:
        o.append('<h2>%s</h2><div class="g">'%html.escape(title))
        for kind,label,url in cards:
            cls=' class="t"' if kind=='Tool' else ''
            if not url.startswith('http'): url='https://drive.google.com/file/d/%s/view'%url
            o.append('<a%s target="_blank" href="%s"><i>%s</i><b>%s</b></a>'%(cls,url,kind,html.escape(label)))
        o.append('</div>')
    return ''.join(o)
G='https://phillippain.github.io/HSC-Economics/'
t2=page('#0e8a8a',[
 ('Whole topic',[('Slides','Topic 2 slides 2026','1HPpjkN5gi1n8hmtCkxmlMXvHsk8cUNoV'),('Practice','Past HSC questions: Topic 2 booklet','14hfU1CKiN-r0X0OYx9iznaBwDD_5KeDd'),('Tool','Question Finder',G+'hsc-question-finder-site/'),('Tool','Glossary',G+'glossary/')]),
 ('Trade and financial flows',[('Worksheet','Trade and financial flows worksheet','1-0PILlyynTVNmiJjfQR2csZTRNbyY1dD'),('Tool','Economy at a Glance',G+'economy-at-a-glance/')]),
 ('Balance of payments',[('Tool','Balance of Payments Explorer',G+'bop-explorer/'),('Notes','Balance of payments class summary','1aek6aiT8QglOBDf51nWKKOPvj5oD-pW0'),('Notes','Structure of the BOP and its transactions','1WBGuI5SH2b0XieK10iBQpfhVYWhogaF9'),('Activity','BOP classification activity','1I8XJht3zAR0WlE30qlEav2SASD2AYO_O'),('Diagram','Trends in the balance of payments','1E3ZB9s6r_TglS3u-ZwTePeH_1wH22pn7'),('Diagram','The CAD continuum','1eXzWhszzq0OAU5ASN1Q_vS5KsTa3gPGt'),('Diagram','The BOP and the exchange rate','1Zubc1iE-j7pxDq2PYZEo-oerUsXK_vF6')]),
 ('Exchange rates',[('Tool','Exchange Rate Explorer',G+'exchange-rate-explorer/'),('Tool','Macro Diagram Lab',G+'macro-diagram-lab/'),('Slides','Exchange rates slides 2026','1qiJKH61hJITXafmMgsg58QJDXo7G8A66'),('Diagram','Floating exchange rate','14Te1Bz7jTxwxo0LtwoANlvL0xj-4ud7t'),('Diagram','Fixed exchange rate','1V-8JEnAPPlCuqoGjD-Q9mS3ZYr8aE8HB'),('Diagram','RBA dirty float','1xa4qc4_6FFkSOX1duaFiKPY-ILhR4AeO'),('Diagram','RBA intervention: appreciation','1dl396zTdJlAvouNDUVDRkDit0hy3Svux'),('Diagram','Currency appreciation','1QlsoetGjh0uCcq_8TG6IDPwAgk6aYOE5'),('Diagram','Currency depreciation','1Uq48izCLo8ijMIfa3-JIPd3QusSt9BZf')]),
 ('Free trade and protection',[('Tool','Protection Diagram Lab',G+'diagram-lab/'),('Tool','Who Wins from Protection',G+'protection-explainer/'),('Slides','Protection slides 2026','1CiEDHfYCdcAHhylErzne_gMzfE1SUubR'),('Worksheet','Free trade and protection worksheet','1dbxoDfuHhY-a87hdnXBO58oMQFc-9Az_'),('Practice','Protection: past HSC questions','1AHS60m7bPJGTELwI1Kaq4bHXOewZXMNz'),('Diagram','Effect of a tariff reduction','1MDRNC0GIB_p0MvW0oYWdiL_CzAj2CeVt')]),
])
open('topic-2.html','w').write(t2); print(len(t2))
