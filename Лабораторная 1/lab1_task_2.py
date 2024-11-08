# TODO Найдите количество книг, которое можно разместить на дискете

memory_Mb = 1.44
stranicy = 100
stroki = 50
simvoly = 25
memory_for_one_simvol_bait = 4
memory_bait = 1.44 * 1024 * 1024
memory_for_one_book_bait = stranicy * stroki * simvoly * memory_for_one_simvol_bait
count_book = int(memory_bait // memory_for_one_book_bait)

print("Количество книг, помещающихся на дискету:", count_book)
