x = "We are now the Knights who say...'Ekki-Ekki-Ekki-Ekki-PTANG. Zoom-Boing. Znourrwringmm'."

x = x.lower()
count = 0

for ch in x:
    if ch == "k":
        count += 1

print(count)