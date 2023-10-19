from bs4 import BeautifulSoup


def ekstraksi_data():

    """
    Tanggal : 15 Oktober 2023
    Waktu : 22:24:44 WIB
    Magnitudo : 4.4
    Kedalaman : 15 km
    Lokasi : LS=8.20 BT=118.09
    Pusat Gempa : Pusat gempa berada di darat 55 km barat laut Dompu
    Dirasakan : Dirasakan (Skala MMI): III Dompu, III Kab. Bima
    """

    soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
    print(soup.prettify())

    hasil = dict()
    hasil['tanggal'] = '15 Oktober 2023'
    hasil['waktu'] = '22:24:44 WIB'
    hasil['magnitudo'] = 4.4
    hasil['kedalaman'] = '15 km'
    hasil['lokasi'] = {'ls': 8.20, 'bt': 118.09}
    hasil['pusat'] = 'Pusat gempa berada di darat 55 km barat laut Dompu'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): III Dompu, III Kab. Bima'

    return hasil

def tampilkan_data(result):
    print('Gempa Terkini Berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")

if __name__ == '__main__':
    print ('ini adalah package gempa terkini')
    print('hai')
