rName = input('Restaurant name? ')
fEntree = input('First entree? ')
fEntreePrice = input('First entree price? ')
sEntree = input('Second entree? ')
sEntreePrice = (input('Second entree price? '))
tEntree = input('Third entree? ')
tEntreePrice = (input('Third entree price? '))

space1 = max(len(fEntree), len(sEntree), len(tEntree)) + 2
dots = (('.') * space1)

lfmenus = (len(dots) - len(fEntree))
dlfmenus = (('.') * lfmenus)
lsmenus = (len(dots) - len(sEntree))
dlsmenus = (('.') * lsmenus)
ltmenus = (len(dots) - len(tEntree))
dltmenus = (('.') * ltmenus)

space2 = ((' ') * (3-len(fEntreePrice))) + fEntreePrice
space3 = ((' ') * (3-len(sEntreePrice))) + sEntreePrice
space4 = ((' ') * (3-len(tEntreePrice))) + tEntreePrice

ftotalmenu = f"{fEntree}{dlfmenus}${space2}"
stotalmenu = f"{sEntree}{dlsmenus}${space3}"
ttotalmenu = f"{tEntree}{dltmenus}${space4}"


dash = f'{rName} Entrees'
print()
print(f'{rName} Entrees')
print(('-') * len(dash))
print(ftotalmenu)
print(stotalmenu)
print(ttotalmenu) 