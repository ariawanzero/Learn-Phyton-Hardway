import first_test
first_test.apple()
print first_test.tangerine

import second_test
thing = second_test.MyClassy()
thing.apple()
print thing.tangerine

import main_class

happy_bday = main_class.Song(["Happy birthday to you","I don't want to get sued", "So I'll stop right there"])

bulls_on_parade = main_class.Song(["They rally around that family","With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
