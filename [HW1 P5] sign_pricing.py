sPrice = 3
setUpFee = 10
sText = input('Sign text? ')
nCopies = int(input('How many copies? '))

print(f"That will cost ${sPrice * len(sText) * nCopies + 10}.")