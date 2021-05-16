

flub = ["£","£","£","£","£","£","£","£","£","£"]


the_array = ["i", "!", "u", "k", "h", "¿", "q","j","?","e","y","o","a","z",
"r","s","l","g","d","?", "w","f","z","m","t", "(", ")", "g","p",":", "n", " "]





ctb = []
ctb.append(the_array[12])
ctb.append(the_array[16])
ctb.append(the_array[len(flub) - 10])
ctb.append(the_array[len(the_array) - 2])
ctb.append(the_array[(2*2*2)+1])
ctb.append(the_array[len(the_array) - 1])
ctb.append(the_array[15])
ctb.append(the_array[23])
ctb.append(the_array[(2*2*2)+1])
ctb.append(the_array[16])
ctb.append(the_array[16])
ctb.append(the_array[15])
ctb.append(the_array[len(the_array) - 1])
ctb.append(the_array[29])
ctb.append(the_array[26])

ctb_final="".join(ctb)
print(ctb_final.capitalize())


