import random
import string

note = input("Enter Note: ").strip()
prefix = "".join(random.choices(string.ascii_uppercase,k = 5))
suffix = "".join(random.choices(string.ascii_lowercase,k = 6))

sub_note = prefix + note + suffix
format_n = sub_note[::-1]
print(format_n)

sub_format_n = format_n[::-1]
sub_sub_format_n = sub_format_n[len(prefix):-len(suffix)]
print(sub_sub_format_n)