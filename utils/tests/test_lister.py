from utils.lister import Lister


def test_format_duration():
    assert Lister.format_duration(12.3812) == "0:12"
    assert Lister.format_duration(185.4432) == "3:05"
    assert Lister.format_duration(212.6367) == "3:32"
    assert Lister.format_duration(212.6367) == "3:32"


def test_max_tags_width():
    files = [
        {
            'name': '01 - The Moor.mp3',
            'ext': 'mp3',
            'tags': {
                'TPE1': 'Opeth',
                'TDRC': '1999',
                'TALB': 'Still Life',
                'TCON': 'Progressive Metal',
                'TRCK': '1',
                'TIT2': 'The Moor',
                'duration': '11:24'
            }
        },
        {
            'name': '10 - From So Far Away.mp3',
            'ext': 'mp3',
            'tags': {
                'TPE1': 'All Shall Perish',
                'TDRC': '2008',
                'TALB': 'Awaken the Dreamers',
                'TCON': 'Deathcore',
                'TRCK': '10',
                'TIT2': 'From So Far Away',
                'duration': '2:38'
            }
        }
    ]

    assert Lister.max_tags_width(files) == {
        'TPE1': 16,
        'TDRC': 4,
        'TALB': 19,
        'TCON': 17,
        'TRCK': 2,
        'TIT2': 16,
        'duration': 5
    }
