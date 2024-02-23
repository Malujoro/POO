def media(vetor, horas):
    
    media = 0

    for num in vetor:
        media += num

    media /= len(vetor)
    return media * horas

periodo1 = media([10, 10, 9, 9], 90) + media([8.7, 9.5, 8.8], 60) + media([10, 10, 10], 60) + media([9.2, 9.5, 10], 60) + media([10], 15) + media([7.5, 10, 10], 60)

periodo2 = media([10, 8.5, 8.5, 10], 90) + media([10, 10, 10], 60) + media([10, 9.5, 9.7], 60) + media([8.3, 9.4, 8.8], 60) + media([8.3, 9.1, 9], 60) + media([10, 8.5], 30) + media([9.2, 10, 10], 60)

IRA = periodo1 + periodo2

periodo1 /= sum([90, 60, 60, 60, 15, 60])
periodo2 /= sum([90, 60, 60, 60, 60, 30, 60])

IRA /= sum([90, 60, 60, 60, 15, 60]) + sum([90, 60, 60, 60, 60, 30, 60])

print(periodo1)
print(periodo2)
print(IRA)