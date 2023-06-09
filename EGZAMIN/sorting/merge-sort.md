* Jeśli l jest mniejsze niż r, wykonaj następujące kroki:
    Oblicz m jako środkowy indeks: m = (l + r) / 2.
    Wywołaj rekurencyjnie mergesort(arr, l, m) dla lewej części tablicy.
    Wywołaj rekurencyjnie mergesort(arr, m + 1, r) dla prawej części tablicy.
    Wywołaj procedurę merge(arr, l, m, r) dla scalenia dwóch posortowanych części.

* Procedura merge(arr, l, m, r) wykonuje następujące kroki:
    Oblicz długości dwóch podtablic: n1 = m - l + 1 i n2 = r - m.
    Utwórz dwie tymczasowe tablice: L o rozmiarze n1 i R o rozmiarze n2.
    Skopiuj elementy z lewej części tablicy arr do tablicy L.
    Skopiuj elementy z prawej części tablicy arr do tablicy R.
    Zainicjalizuj zmienne: i = 0, j = 0, k = l (indeksy dla L, R i arr).

* Wykonuj poniższe kroki, dopóki i jest mniejsze niż n1 i j jest mniejsze niż n2:
    Porównaj elementy L[i] i R[j].
    Jeśli L[i] jest mniejsze lub równe R[j], przypisz L[i] do arr[k] i zwiększ i o 1.
    W przeciwnym razie przypisz R[j] do arr[k] i zwiększ j o 1.
    Zwiększ k o 1.

* Skopiuj pozostałe elementy z tablicy L, jeśli istnieją, do tablicy arr zaczynając od indeksu k.
    Wykonuj poniższe kroki, dopóki i jest mniejsze niż n1:
        Przypisz L[i] do arr[k] i zwiększ i i k o 1.

* Skopiuj pozostałe elementy z tablicy R, jeśli istnieją, do tablicy arr zaczynając od indeksu k.
    Wykonuj poniższe kroki, dopóki j jest mniejsze niż n2:
        Przypisz R[j] do arr[k] i zwiększ j i k o 1.

* Po wykonaniu powyższych kroków, tablica arr będzie posortowana w porządku rosnącym.

Psuedo kod:

    procedure mergesort(arr, lewy, prawy)
        if lewy < prawy then
            srodek = (lewy + prawy) / 2
            mergesort(arr, lewy, srodek)
            mergesort(arr, srodek + 1, prawy)
            scal(arr, lewy, srodek, prawy)

    procedure scal(arr, lewy, srodek, prawy)
        rozmiar_lewej = srodek - lewy + 1
        rozmiar_prawej = prawy - srodek
        lewa_czesc = new array of size rozmiar_lewej
        prawa_czesc = new array of size rozmiar_prawej

        for i = 0 to rozmiar_lewej - 1 do
            lewa_czesc[i] = arr[lewy + i]
        for j = 0 to rozmiar_prawej - 1 do
            prawa_czesc[j] = arr[srodek + 1 + j]

        i = 0
        j = 0
        k = lewy

        while i < rozmiar_lewej and j < rozmiar_prawej do
            if lewa_czesc[i] <= prawa_czesc[j] then
                arr[k] = lewa_czesc[i]
                i = i + 1
            else
                arr[k] = prawa_czesc[j]
                j = j + 1
            k = k + 1

        while i < rozmiar_lewej do
            arr[k] = lewa_czesc[i]
            i = i + 1
            k = k + 1

        while j < rozmiar_prawej do
            arr[k] = prawa_czesc[j]
            j = j + 1
            k = k + 1

    # Wywołanie procedury sortowania przez scalanie
    arr = [5, 2, 8, 3, 1]
    mergesort(arr, 0, len(arr) - 1)
    print(arr)