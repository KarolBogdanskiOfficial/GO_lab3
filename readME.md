Program został podzielony na 4 pliki źródłowe. 

W PointMenagment.py znajdują się funkcje zajmujące się obsługą chmury punktów - 
ładowaniem jej z pliku oraz obliczniem odległości. Jest tam również zdefiniowany sposób w 
jaki w programie zapisywane są punkty i ich współrzędne.

W Tree.py znajdują się funkcje obsługujące drzewo KD - budująca je z załadowanej chmury,
oraz znajdująca z jego pomocą punkt najbliższy podanemu.

W GUI.py znajdują się wszystkie funkcje konieczne do graficznego pokazania działania 
programu. Do stworzenia interfejsu użyłem pakietu Tkinter.

W main.py znajduje się główny skrypt programu. Prezentuje on jego działanie zarówno w GUI jak
i w terminalu.

                            INSTRUKCJA URUCHOMIENIA

1. Konieczny jest oczywiście interpreter Pythona
2. Należy uruchomić plik main.py
3. W GUI kliknięcie przycisku "rysuj punkty", prezentuje graficznie załadowaną chmurę
4. Przycisk "najbliższy punkt" rysuje na zielono punkt testowy i koloruje na fiołkowo
    wynik działania programu - najbliższy punkt
5. Współrzędne punktu testowego można zmienić w dwóch miejscach
    a) main.py linia 14 (dla prezentacji w terminalu)
    b) GUI.py linia 6 (dla prezentacji okienkowej)
6. Chmura punktów ładowana jest z pliku dane.txt i w nim można ją dowolnie modyfikować

Przepraszam za opóźnienie jak i wszelkie błędy.