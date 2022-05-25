n_e = int(input())
e_s = input()
e_s = list(e_s.split(" "))

n_f = int(input())
f_s = input()
f_s = set(list(f_s.split(" ")))

print(len(f_s.intersection(set(e_s))))