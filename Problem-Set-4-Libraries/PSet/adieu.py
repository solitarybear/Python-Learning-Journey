import resource
resource.setrlimit(resource.RLIMIT_AS, (2 * 1024 * 1024 * 1024, resource.RLIM_INFINITY))
sentence =["Adieu", "adieu", "to"]
# something = ""
something = input("Name: ")
# sentence.append(something = input("Name: "))

try:
    while True :
        sentence.append(something)
except EOFError:
    print()


if len(sentence) == 4:
    result = f"{', '.join(sentence[:1])} {sentence[2]} {sentence[3]}"
elif len(sentence) == 5:
    result =f"{', '.join(sentence[:1])} {sentence[2]} {', and'.join(sentence[3:-1])}"
else:
    result = f"{', '.join(sentence[:1])} {sentence[2]} {', '.join(sentence[3:-2])} and {sentence[-1]}"

print(result)

# in above i made correction to mine code and did much changes wherever it's needed other wise i just try to correct that in the way i thought
