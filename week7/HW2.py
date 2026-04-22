import keyword

var = input("")

if not var or var[0].isdigit() or (not var[0].isalnum() and var[0] != "_") or var in keyword.kwlist:
    print("Illegal! - 1")
else:
    if (var.replace('_','') != "") and not var.replace('_','').isalnum():
        print("Illegal! - 2")
    else:
        print("Legal!")