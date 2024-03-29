# Sortowania

## Sortowanie - definiuje się następująco:
Dana jest ciąg elementów a1, a2,...,an
elementów zbioru liniowo uporządkowanego.
Trzeba dokonać permutacji ustawiającej
elementy w porządku rosnącym


# Metody Sortowania:
| algorymt                          | zlożonosc optymistyczna | złożoność pesymistyczna | złożonośc średnia |  
|-----------------------------------|-------------------------|-------------------------|-------------------|
| [Selection Sort](#selection-sort) | O(n^2)                  | O(n^2)                  | O(n^2)            |  
| [Insertion Sort](#insertion-sort) | O(n)                    | O(n^2)                  | O(n^2)            |  
| Bubble Sort                       | O(n)                    | O(n^2)                  | O(n^2)            |   
| [Merge Sort](#merge-sort)         | O(n log n)              | O(n log n)              | O(n log n)        |   
| [Quick Sort](#quick-sort)         | O(n log n)              | O(n^2)                  | O(n log n)        |
| [Heap Sort](#heap-sort)           | O(n log n)              | O(n log n)              | O(n log n)        |   
   

---
# Stabliność sortowanie
* Algorytm sortowania jest stabilny, gdy zachowuje kolejność elementów o tej samej wartości. Oznacza to, że jeśli mamy dwa lub więcej elementów o tej samej wartości, to po posortowaniu ich za pomocą stabilnego algorytmu sortowania, ich względna kolejność względem siebie pozostaje niezmieniona.

* Na przykład, rozważmy listę osób zawierającą imię i wiek. Chcemy posortować tę listę względem wieku, ale jeśli dwie osoby mają ten sam wiek, chcemy, aby pozostały w kolejności, w jakiej zostali pierwotnie wprowadzeni.

* Stabilny algorytm sortowania będzie utrzymywał tę kolejność. Jeśli zastosujemy stabilny algorytm sortowania do tej listy, to po posortowaniu osoby o tym samym wieku pozostaną w tej samej kolejności, w jakiej były pierwotnie.

>Przykład:
Mamy listę osób: [(Anna, 25), (Jan, 30), (Maria, 25), (Piotr, 30)]

>Po zastosowaniu stabilnego algorytmu sortowania względem wieku, lista zostanie posortowana tak: [(Anna, 25), (Maria, 25), (Jan, 30), (Piotr, 30)]

__NOTE__: Możemy zauważyć, że osoby o wieku 25 (Anna i Maria) zachowują swoją względną kolejność, nawet po posortowaniu. To właśnie cecha stabilności w algorytmie sortowania.

`Stabilne algorytmy sortowanie:`
* InsertionSort (przez proste wstawianie)
* BubbleSort (przez prostą zamianę)
* MergeSort (przez scalanie)
* SelectionSort (przez wybieranie)

`Niestabline algorytmy sortowania:`
* QuickSort (szybkie)
* Heapsort (stogowe)


---
### Dlaczego warto sortować zbiory?
Sortowanie
Aby łatwiejsze było wyszukiwanie danego elementu
w zbiorze
Aby łatwiejsze było sprawdzenie, czy dany element
znajduje się w zbiorze

---

## Insertion Sort
1. Dla każdego indeksu i od 1 do długość(listy):
2. Przechowujemy wartość elementu o indeksie i jako klucz.
3. Przechowujemy indeks poprzedniego elementu jako j.
4. Dopóki j >= 0 i lista[j] > klucz:
    1. Przesuwamy element o indeksie j o jedno miejsce w prawo.
    2. Zmniejszamy j o 1.
5. Umieszczamy klucz na pozycji j+1.
6. Zwracamy posortowaną listę.

>pseudo kod

    Funkcja insertion_sort(lista):
        Dla każdego indeksu i od 1 do długość(lista):
            Przechowaj wartość elementu o indeksie i jako klucz
            Przechowaj indeks poprzedniego elementu jako j

            Dopóki j >= 0 i lista[j] > klucz:
                Przesuń element o indeksie j o jedno miejsce w prawo
                Zmniejsz j o 1

            Umieść klucz na pozycji j+1

        Zwróć posortowaną listę

---

## Selection Sort
1. Dla każdego indeksu i od 0 do długość(listy) - 1:
2. Znajdujemy indeks najmniejszego elementu w podliście od i do długość(listy) - 1.
4. Zamieniamy miejscami najmniejszy element z elementem o indeksie i.
5. Zwracamy posortowaną listę.

> pseudo kod

    Funkcja selection_sort(lista):
        Dla każdego indeksu i od 0 do długość(lista) - 1:
            Znajdź indeks najmniejszego elementu w podlisty od i do długość(lista) - 1
            Zamień miejscami najmniejszy element z elementem o indeksie i

        Zwróć posortowaną listę


---
## Quick Sort

* Jest to jeden z najczęściej używanych algorytmów sortowania.
* Jest uważany za najszybszy algorytm sortowania dla "losowych" danych wejściowych


1. Jeśli lista ma długość 1 lub mniejszą, to zwracamy tę listę, ponieważ jest już posortowana.
2. Wybieramy jeden element z listy jako punkt odniesienia (zwykle jest to element środkowy).
3. Tworzymy dwie puste listy: mniejszych_elementów i większych_elementów.
4. Dla każdego elementu w liście (oprócz punktu odniesienia) sprawdzamy, czy jest mniejszy czy większy od punktu odniesienia i umieszczamy go w odpowiedniej liście.
5. Rekurencyjnie sortujemy mniejsze_elementy i większe_elementy, używając algorytmu QuickSort.
6. Łączymy posortowane mniejsze_elementy, punkt odniesienia i posortowane większe_elementy w jedną listę i zwracamy ją jako wynik.


>Peusod kod

    Funkcja quicksort(lista):
        Jeśli długość(listy) <= 1:
            Zwróć listę

        Wybierz element o indeksie środkowym z listy jako punkt odniesienia
        Utwórz pustą listę mniejszych_elementów
        Utwórz pustą listę większych_elementów

        Dla każdego elementu w liście (oprócz punktu odniesienia):
            Jeśli element < punkt_odniesienia:
                Dodaj element do mniejszych_elementów
            W przeciwnym razie:
                Dodaj element do większych_elementów

        Posortuj mniejsze_elementy za pomocą rekurencyjnego quicksort(mniejsze_elementy)
        Posortuj większe_elementy za pomocą rekurencyjnego quicksort(większe_elementy)

        Zwróć połączoną listę: quicksort(mniejsze_elementy) + [punkt_odniesienia] + quicksort(większe_elementy)

---

## Merge Sort
1. Jeśli lista ma długość 1 lub mniejszą, to zwracamy tę listę, ponieważ jest już posortowana.
2. Dzielimy listę na dwie połowy, znajdując środek listy.
3. Rekurencyjnie sortujemy lewą połowę i prawą połowę, używając algorytmu Merge Sort.
4. Scalamy posortowane lewą_połowę i prawą_połowę, korzystając z funkcji scalanie.
5. Funkcja scalanie porównuje pierwsze elementy lewej_połowy i prawej_połowy, dodaje mniejszy z nich do listy wynikowej, a następnie usuwa ten element z odpowiedniej połowy.
6. Jeśli jedna z połówek nie jest pusta, dodajemy jej pozostałe elementy do listy wynikowej.
7. Zwracamy posortowaną listę wynikową.

>Psuedo kod:

    Funkcja merge_sort(lista):
        Jeśli długość(listy) <= 1:
            Zwróć listę

        Podziel listę na dwie połowy:
        Środek = długość(listy) / 2
        Lewa_połowa = lista[0:Środek]
        Prawa_połowa = lista[Środek:długość(listy)]

        Posortuj lewą_połowę, wywołując rekurencyjnie merge_sort(lewa_połowa)
        Posortuj prawą_połowę, wywołując rekurencyjnie merge_sort(prawa_połowa)

        Zwróć scaloną listę: scalanie(lewa_połowa, prawa_połowa)


    Funkcja scalanie(lewa, prawa):
        Utwórz pustą listę wynikową

        Dopóki lewa i prawa nie są puste:
            Jeśli pierwszy element lewej_połowy <= pierwszy element prawej_połowy:
                Dodaj pierwszy element lewej_połowy do listy wynikowej
                Usuń pierwszy element lewej_połowy
            W przeciwnym razie:
                Dodaj pierwszy element prawej_połowy do listy wynikowej
                Usuń pierwszy element prawej_połowy

        Jeśli lewa_połowa nie jest pusta:
            Dodaj pozostałe elementy lewej_połowy do listy wynikowej

        Jeśli prawa_połowa nie jest pusta:
            Dodaj pozostałe elementy prawej_połowy do listy wynikowej

        Zwróć listę wynikową

---


## Heap sort

1. Budujemy maksymalny kopiec z listy.
2. Dla i od długość(listy) - 1 do 1:
    1. Zamieniamy miejscami pierwszy element z elementem o indeksie i.
    2. Zachowujemy własność kopca, wywołując procedurę 
    3. naprawy_kopca dla skróconej listy.
3. Zwracamy odwróconą listę, aby uzyskać posortowane elementy w kolejności rosnącej.

Procedura naprawy_kopca służy do naprawiania kopca, aby zachować jego własność. Przechodzimy przez rodzica, lewe dziecko i prawe dziecko w danym węźle kopca, a następnie zamieniamy miejscami rodzica z największym z dzieci, jeśli jest to konieczne. Kontynuujemy naprawę kopca rekurencyjnie w dół, jeśli zamiana została dokonana.

> pseudo kod

    Funkcja heap_sort(lista):
        Zbuduj maksymalny kopiec z listy
        Dla i od długość(lista) - 1 do 1:
            Zamień miejscami pierwszy element z elementem o indeksie i 
            Zachowaj własność kopca, wywołując procedurę naprawy_kopca(lista, 0, i)

        Zwróć odwróconą listę (aby uzyskać wynik w kolejności rosnącej)


    Procedura naprawy_kopca(lista, rodzic, rozmiar):
        Ustaw indeks największego elementu na rodzica
        Ustaw indeks lewego dziecka na 2 * rodzic + 1
        Ustaw indeks prawego dziecka na 2 * rodzic + 2

        Jeśli lewe_dziecko < rozmiar i lista[lewe_dziecko] > lista[największy_element]:
            Ustaw indeks lewego_dziecka jako największy_element

        Jeśli prawe_dziecko < rozmiar i lista[prawe_dziecko] > lista[największy_element]:
            Ustaw indeks prawego_dziecka jako największy_element

        Jeśli największy_element != rodzic:
            Zamień miejscami rodzic z największym_elementem
            Wywołaj rekurencyjnie procedurę naprawy_kopca(lista, największy_element, rozmiar