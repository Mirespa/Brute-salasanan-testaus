def generate_all(m, p, osa_salasanasta):
    if p == 0:
        print(osa_salasanasta)
        return
    
    for kirjain in m:
        generate_all(m, p - 1, osa_salasanasta + kirjain)

generate_all("abcdefg", 7, "")