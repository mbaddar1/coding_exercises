
s = "abcbbbbcccbdddadacb"
chr_dict = {}
i =0
j=0
chr_dict[s[j]]=1

i_max = i
j_max  =j

max_len = 1
while (i<len(s)) & (j < len(s)):

    j = j + 1
    if j >= len(s):
        break
    if s[j] in chr_dict.keys():
        cnt = chr_dict[s[j]]
        chr_dict[s[j]] = cnt+1
    else:
        chr_dict[s[j]] = 1

    if len(chr_dict.keys())<=2:
        if j-i+1 > max_len:
            i_max = i
            j_max = j
            max_len = max_len + 1

    else:
        condition = False
        while (not condition) & (i<j):
            cnt = chr_dict[s[i]]
            if cnt==1:
                del chr_dict[s[i]]
            else:
                chr_dict[s[i]] = cnt -1

            if len(chr_dict.keys())<=2:
                condition = True
            i = i+1


print(f'i_max = {i_max}, j_max = {j_max} , max_len = {max_len}')
print(f'substr = {s[i_max:j_max]}')