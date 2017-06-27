import difflib

albums = ['Enter The Wu-Tang (36 Chambers) (LP, Album)',
          'Enter The Wu-Tang (36 Chambers) (Clean) (CD, Album, Cle)',
          'Enter The Wu-Tang (36 Chambers) (CD, Album)',
          'Enter The Wu-Tang (36 Chambers) (Cass, Album)',
          'Enter The Wu-Tang Clan (36 Chambers) (12", Promo, Smplr)',
          'Enter The Wu-Tang (36 Chambers) (CD, Album, RE, RM)',
          'Test (Clean) (CD)']

search_term = 'enter the wu tang (36 chambers)'

found = difflib.get_close_matches(search_term,
                                  albums,
                                  n=10,
                                  cutoff=0.5)

for title in found:
    print(title)
