theme = {
    'Manfaat Kebaikan'          : {'surah': 'Surah Hud, Ayat 114',          'dark': 'resources/surah/hud_114_dark.png',     'light': 'resources/surah/hud_114_light.png',       'prompt': 'A diverse group of individuals from various backgrounds engage in acts of kindness, such as feeding the hungry, helping the elderly, or planting trees. Each person is depicted with distinct features, clothing, and expressions, reflecting the unity and compassion found in Islamic teachings. The setting may include a bustling city street, a tranquil park, or a rural community, emphasizing that kindness knows no boundaries.'},
    'Allah Tempat Berlindung'   : {'surah': 'Surah Al-Ahzab, Ayat 3',       'dark': 'resources/surah/ahzab_3_dark.png',     'light': 'resources/surah/ahzab_3_light.png',       'prompt': 'An image portraying a serene natural landscape, such as a lush forest, a calm ocean shore, or a majestic mountain range, evoking feelings of peace and tranquility. In the foreground, a lone muslim figure sits in contemplation or prayer, seeking solace and protection in the beauty of the surroundings. The scene is bathed in warm sunlight or soft moonlight, suggesting a sense of divine presence and comfort without explicitly depicting it.'},
    'Allah Maha Melihat'        : {'surah': 'Surah Al-Furqan, Ayat 20',     'dark': 'resources/surah/furqan_20_dark.png',   'light': 'resources/surah/furqan_20_light.png',     'prompt': 'A scene depicting everyday life, such as a bustling marketplace or a quiet street corner, with subtle visual cues suggesting a higher power observation. This could include a flock of birds soaring overhead, casting fleeting shadows on the ground, or beams of sunlight filtering through clouds, creating patterns reminiscent of watchful eyes. The focus is on the ordinary moments of human existence, with an underlying sense of divine awareness.'},
    'Memohon Keampunan'         : {'surah': 'Surah Hud, Ayat 90',           'dark': 'resources/surah/hud_90_dark.png',      'light': 'resources/surah/hud_90_light.png',        'prompt': 'An image of a solitary figure kneeling in muslim prayer or contemplation, surrounded by symbols of repentance and forgiveness. This could include an empty chair beside them, symbolizing the presence of the divine, or a serene natural setting conducive to introspection. The atmosphere is one of humility and sincerity, with the individual body language conveying a heartfelt plea for mercy and absolution.'},
    'Kesenangan Yang Menipu'    : {'surah': 'Surah Ali Imran, Ayat 185',    'dark': 'resources/surah/imran_185_dark.png',   'light': 'resources/surah/imran_185_light.png',     'prompt': 'A visual juxtaposition of temporary pleasures and their eventual consequences, portrayed through contrasting images. For example, one side of the image may depict lavish banquets, extravagant parties, or material possessions, while the other side shows scenes of disillusionment, loneliness, or regret. The overall tone is one of caution and reflection, highlighting the fleeting nature of worldly delights.'},
    'Mati Itu Pasti'            : {'surah': 'Surah Al-Jumuah, Ayat 8',      'dark': 'resources/surah/jumuah_8_dark.png',    'light': 'resources/surah/jumuah_8_light.png',      'prompt': 'An evocative portrayal of the cycle of muslim life and death, captured through imagery of nature rhythms and transformations. This could include scenes of wilting flowers, fallen leaves, or the changing seasons, symbolizing the inevitability of mortality. The mood is contemplative yet accepting, with an emphasis on the interconnectedness of all living things.'},
    'Bersyukur'                 : {'surah': 'Surah Ibrahim, Ayat 7',        'dark': 'resources/surah/ibrahim_7_dark.png',   'light': 'resources/surah/ibrahim_7_light.png',     'prompt': 'An image depicting expression of gratitude and contentment in muslim life situations. This could include individuals sharing meals with loved ones, helping those in need, or simply enjoying the beauty of nature. Each scene radiates warmth and positivity, with smiles, gestures, and small acts of kindness conveying a sense of thankfulness and appreciation.'},
    'Tabah Menghadapi Ujian'    : {'surah': 'Surah Al-Baqarah, Ayat 286',   'dark': 'resources/surah/baqarah_286_dark.png', 'light': 'resources/surah/baqarah_286_light.png',   'prompt': 'A scene portraying resilience and perseverance in the face of adversity, such as individuals overcoming obstacles, supporting each other through difficult times, or finding strength in faith. This could include images of muslim people rebuilding homes after an incident, comforting one another during times of grief, or standing firm in the face of injustice. The emphasis is on endurance, solidarity, and hope.'},
    'Kata-Kata Yang Baik'       : {'surah': 'Surah Al-Baqarah, Ayat 83',    'dark': 'resources/surah/baqarah_83_dark.png',  'light': 'resources/surah/baqarah_83_light.png',    'prompt': 'An image featuring uplifting and positiveness in everyday muslim community with natural landscapes that resonates with themes of kindness, love, and optimism inspiring viewers to embrace goodness in their own lives. festivities at night'},
    'Kewajipan Solat'           : {'surah': 'Surah Al-Ankabut, Ayat 45',    'dark': 'resources/surah/ankabut_45_dark.png',  'light': 'resources/surah/ankabut_45_light.png',    'prompt': 'Scenes of devotion and spiritual practice within Malaysian contexts (individuals praying in mosques, suraus, or praying spaces at home, performing ablutions with Malaysian cultural elements, reading religious texts with respect to Malaysian customs and values). beautiful moonlight'}
}

layer = {
    'Gelap' : 'resources/layers/dark.png',
    'Terang': 'resources/layers/light.png'
}

theme_list = theme.keys()
layer_list = layer.keys()
surah_list = [theme[key]['surah'] for key in theme]

import gradio as ui; import requests, logging, os; from io import BytesIO
from PIL import Image, ImageEnhance; from requests.exceptions import *; import concurrent.futures
logging.basicConfig(level=logging.DEBUG)

def theme_change(a, i: ui.SelectData):
    print(f"Theme changed -> {a}")
    return ui.Dropdown(value=theme[a]['surah'])

def stella(surah, mode):
    data = {
        'model_version': (None, '1'),
        'prompt': (None, theme[surah]['prompt']),
        'style_id': (None, '128'),
        'negative_prompt': (None, 'hands, face, eyes, legs'),
        'aspect_ratio': (None, '1:1'),
        'high_res_results': (None, '1'),
        'cfg': (None, '9.5'),
        'priority': (None, '1')
    }
    
    key = {
        'bearer': os.getenv('bearer')
    }
    
    try:
        print(f'Processing -> {expanded}')
        response = requests.post(os.getenv('generate'), headers=key, files=data, timeout=(60, 60))
        layer0 = enhance_img(Image.open(BytesIO(response.content)))
        
        if mode == 'Terang':
            layer1 = Image.open(layer['Terang'])
            layer2 = Image.open(theme[surah]['light'])
        else:
            layer1 = Image.open(layer['Gelap'])
            layer2 = Image.open(theme[surah]['dark'])

        layer0.paste(layer1, (0, 0), layer1)
        layer0.paste(layer2, (0, 0), layer2)

        return layer0
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def queue(a, b):
    quantities = 4
    result_list = [None] * quantities
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i in range(quantities):
            future = executor.submit(lambda x: stella(a, b), i)
            futures.append(future)

    for i, future in enumerate(futures):
        result = future.result()
        result_list[i] = result

    successful_results = [result for result in result_list if result is not None]
    return successful_results

def enhance_img(image):
    return ImageEnhance.Contrast(ImageEnhance.Color(ImageEnhance.Brightness(ImageEnhance.Sharpness(image).enhance(2.00)).enhance(1.05)).enhance(1.05)).enhance(1.05)

thx = ui.themes.Default(
    font=[ui.themes.GoogleFont('Myriad Pro')], font_mono=[ui.themes.GoogleFont('Myriad Pro')],
    text_size=ui.themes.Size(lg="18px", md="18px", sm="18px", xl="18px", xs="18px", xxl="18px", xxs="18px"),
    primary_hue='rose', secondary_hue='rose', neutral_hue='zinc')
    
css = '''
footer {display: none !important;}
.app.svelte-182fdeq.svelte-182fdeq {padding: 12px;}
.unpadded_box.svelte-1oiin9d {min-height: 50vh;}
.icon-buttons.svelte-hpz95u.svelte-hpz95u {scale: 2; padding-top: 8px; padding-right: 15px;}
.grid-wrap.svelte-hpz95u.svelte-hpz95u {overflow-y: auto;}
::-webkit-scrollbar {display: none;}
::-webkit-scrollbar-button {display: none;}
'''