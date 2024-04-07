from kalam_data import *

with ui.Blocks(title='Kalam AI', theme=thx, css=css, analytics_enabled=False) as kalam:
    ui.HTML(value='''
            <center>
                <h2>📖 Kalam AI Web App 🤲</h2>
                <p>Sebuah aplikasi web menghasilkan poster ayat Al-Quran beserta terjemahan menggunakan AI</p>
            </center>
            ''')
    
    with ui.Row(equal_height=True):
        with ui.Column(min_width=512, variant='panel') as step_1:
            pict = ui.Gallery(type='pil', label='Hasil Janaan', show_share_button=False, height='50vh', columns=2, rows=2, object_fit='contain')
            them = ui.Dropdown(label='Tema / Topik', choices=theme_list, value='Manfaat Kebaikan')
            sura = ui.Dropdown(label='Nama Surah', choices=surah_list, value='Surah Hud, Ayat 114')
            disp = ui.Dropdown(label='Jenis Paparan', choices=layer_list, value='Gelap')
            with ui.Group():
                with ui.Row():
                    stop = ui.Button('Batal')
                    init = ui.Button('Hantar', variant='primary')
    
    proc = init.click(fn=queue, inputs=[them, disp], outputs=[pict])
    stop.click(fn=None, inputs=None, outputs=None, cancels=proc)
    them.select(fn=theme_change, inputs=[them], outputs=[sura])
    
    ui.HTML(value='''
            <center>
                <h2>Dibangunkan oleh Ikmal Said (<a href='https://twitter.com/ikmalsaid'>@ikmalsaid</a>) untuk #GodamSahur 2024</h2>
            </center>
            ''')

if __name__ == "__main__":
    kalam.queue(default_concurrency_limit=100).launch(inbrowser=True, favicon_path="favicon.ico")

