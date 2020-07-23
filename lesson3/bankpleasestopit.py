nominals = [5, 10, 20, 50, 100, 200, 500, 1000]
amount = int(input('Enter the amount here: '))
if amount % 5 != 0:
    print('The amount should be a multiple of 5, please try again')
max_outcome = sum([nom * 10 for nom in nominals])
if amount > max_outcome:
    print("Please enter a smaller amount.")
outcome = {}
for id, nom in enumerate(nominals):
    if not amount:
        break
    if id == len(nominals) - 1:
        outcome[nom] = amount // nom
        break
    for i in range(10, 0, -1):
        if (amount - nom * i) < 0:
            continue
        if not (amount - nom * i) % nominals[id + 1]:
                outcome[nom] = i
                amount -= nom * i
                break
    if outcome:
        check_sum = sum([i * outcome[i] for i in outcome])
        outcome_string = ' + '.join([str(n) + '×' + str(outcome[n]) for n in outcome])
        print(outcome_string, check_sum, sep=' = ')

