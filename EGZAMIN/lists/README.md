# Typ danych 
* zbiór wartości, które mogę przyjmować zmienne
# Abstrakcyjny typ danych

* model matematyczny wraz ze zbiorem operacji zdefiniowanych na tym modelu
>np.. zbiór liczb całkowitych z operacjami  sumy, iloczynu i różnicy mnogościowej, graf  z operacjami dodawania i usuwania
wierzchołków oraz krawędzi)
---

> # Proces rozwiązywania problemu

1. Opracowanie modelu matematycznego: Definiujemy model matematyczny, który opisuje problem, uwzględniając zbiór wartości, jakie mogą przyjąć zmienne oraz operacje na tych wartościach.

2. Opracowanie nieformalnego algorytmu: Na podstawie modelu matematycznego tworzymy nieformalny algorytm, czyli sekwencję kroków, które prowadzą do rozwiązania problemu.

3. Abstrakcyjne typy danych (ADT): Abstrakcyjne typy danych są matematycznymi modelami wraz z zestawem operacji zdefiniowanych na tych modelach.

4. Programowanie w pseudojęzyku: Na podstawie ADT i nieformalnego algorytmu tworzymy program w pseudojęzyku, który jest uproszczonym językiem programowania, umożliwiającym bardziej formalne zapisanie algorytmu.

5. Struktury danych i program w języku programowania: Reprezentujemy ADT za pomocą struktur danych, które składają się z zmiennych o różnych typach. Następnie implementujemy program w konkretnym języku programowania, wykorzystując dostępne typy danych i operatory.

6. Implementacja konkretnego programu: Przechodzimy do implementacji programu, tłumacząc go z pseudojęzyka na wybrany język programowania i korzystając z funkcji i bibliotek dostępnych w tym języku.


---
## Wskazniki vs kursory 
1. `Wskaźniki:` Wskaźnik jest komórką, która przechowuje adres (wskaźnik) innej komórki w pamięci. Może być traktowany jako pośrednik między różnymi elementami struktury danych. Wskaźniki są szczególnie przydatne w dynamicznie alokowanych strukturach danych, takich jak listy czy drzewa, gdzie elementy mogą być dowolnie dodawane i usuwane w trakcie działania programu. Przy użyciu wskaźników można tworzyć powiązania między elementami struktury, umożliwiając skomplikowane struktury danych.

2. `Kursory:` Kursor jest komórką przechowującą wartość typu int, która służy do wskazywania elementów tablicy. Kursory są szczególnie użyteczne w kontekście tablic, gdzie elementy są przechowywane w sekwencyjnym układzie w pamięci. Kursor wskazuje na indeks elementu tablicy, umożliwiając dostęp do jego wartości. Kursory są wykorzystywane do nawigacji po tablicach, iteracji przez ich elementy i wykonywania operacji na poszczególnych elementach.

>Wskaźniki i kursory są narzędziami, które umożliwiają tworzenie złożonych struktur danych i operowanie na nich w sposób efektywny i elastyczny. Ich zastosowanie zależy od konkretnego problemu i języka programowania, w którym jest implementowany program.


### ADT LIST - reprezentacja tablicowa listy

Tablicowa implementacja listy:

```c
Const int maxlength=10;
struct list
{
    elementtype elements[maxlength];
    int last; // indeks ostatniego elementu listy
}
int position; // indeks danego elementu listy, pozycja elementu
```

Funkcje pomocnicze:

    Position END(List l): Zwraca pozycję za ostatnim elementem listy.
    Position First(List l): Zwraca pozycję pierwszego elementu listy.

Operacje na listy:

    Position Next(position p, List l): Zwraca pozycję elementu następującego po elemencie o pozycji p w liście.
    Position Previous(position p, List l): Zwraca pozycję elementu poprzedzającego element o pozycji p w liście.

Operacje wyszukiwania i pobierania elementów:

    Position Locate(elementtype x, List l): Zwraca pozycję elementu x w liście l. Jeśli element nie występuje w liście, zwraca END(l).
    Elementtype Retrieve(position p, List l): Zwraca wartość elementu o pozycji p w liście l.

Operacje dodawania i usuwania elementów:

    bool Insert(int x, position p, List l): Wstawia element x na pozycję p w liście l. Zwraca true, jeśli operacja się powiedzie, a false w przeciwnym przypadku.
    bool Delete(position p, List l): Usuwa element o pozycji p z listy l. Zwraca true, jeśli operacja się powiedzie, a false w przeciwnym przypadku.

### Przykład działania operacji Insert:

Załóżmy, mamy tablicę czteroelementową (maxlength=4) i nasza lista składa się z elementów 10, 20, 30.
Wywołujemy procedurę Insert(50, 1, l) - chcemy wstawić element 50 na pozycję 1.
Operacja Insert przesuwa element 30 z pozycji 2 na pozycję 3 oraz element 20 z pozycji 1 na pozycję 2, aby zrobić miejsce na element 50 na pozycji 1.

### Przykład działania operacji Delete:

Załóżmy, mamy tablicę czteroelementową (maxlength=4) i nasza lista składa się z elementów 10, 20, 30, 40.
Wywołujemy procedurę Delete(1, l) - chcemy usunąć element z pozycji 1.
Operacja Delete przesuwa element 20 z pozycji 2 na pozycję 1 oraz element 30 z pozycji 3 na pozycję 2.