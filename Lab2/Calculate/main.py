from function import func1

s = "Hello! How are you? I'm fine. Thank you... A.S. Pushkin is was. I love you!"
s_split = []
s_split_ = []
counter = 0
counter_ = 0
separators = ['.', '!', '?', '...']
separators_non_declarative = ['!', '?']

for i in range(len(s)):
    if s[i] in separators and s[i-1].islower():
        s_split.append(s[counter:i+1])
        counter = i + 1

a = list(map(lambda s: s.strip(), s_split))
print(a)

for i in range(len(a)):
    s_split_.append(a[i])

print(s_split_)