* Jest to jeden z najczęściej używanych algorytmów sortowania.
* Jest uważany za najszybszy algorytm sortowania dla "losowych" danych wejściowych


1. Jeśli lista ma długość 1 lub mniejszą, to zwracamy tę listę, ponieważ jest już posortowana.
2. Wybieramy jeden element z listy jako punkt odniesienia (zwykle jest to element środkowy).
3. Tworzymy dwie puste listy: mniejszych_elementów i większych_elementów.
4. Dla każdego elementu w liście (oprócz punktu odniesienia) sprawdzamy, czy jest mniejszy czy większy od punktu odniesienia i umieszczamy go w odpowiedniej liście.
5. Rekurencyjnie sortujemy mniejsze_elementy i większe_elementy, używając algorytmu QuickSort.
6. Łączymy posortowane mniejsze_elementy, punkt odniesienia i posortowane większe_elementy w jedną listę i zwracamy ją jako wynik.

---
Peusod kod

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
