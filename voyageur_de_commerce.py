import random
import matplotlib.pyplot as plt
from random import randint, sample
import time

# déclaration des variables
villes = ['Paris', 'Marseille', 'Lyon', 'Toulouse', 'Nice', 'Nantes', 'Montpellier', 'Strasbourg', 'Bordeaux', 'Lille', 'Reims',
          'Toulon', 'Saint-etienne', 'Le havre', 'Grenoble', 'Dijon', 'Angers', 'Clermont-ferrand', 'Orléans', 'Brest', 'Pau', 'Limoges']
X = [651458, 893357, 840962, 573373, 1040456, 357203, 770133, 1050073, 418003, 705698, 775588,
     936365, 799062, 493529, 913610, 853351, 433631, 708479, 618795, 146587, 423398, 564846]
Y = [6863437, 6249711, 6522215, 6277648, 6296766, 6682237, 6278840, 6841937, 6417338, 7062301, 6906298,
     6234065, 6483699, 6937291, 6453203, 6693438, 6714185, 6520601, 6757932, 6838157, 6247970, 6526612]
Matrice_adj = [[0.0, 774.9, 465.5, 678.0, 931.9, 384.5, 747.6, 491.3, 584.2, 225.3, 144.1, 838.8, 523.4, 197.2, 575.3, 314.5, 296.0, 424.5, 132.6, 590.9, 794.5, 392.0], [774.9, 0.0, 313.7, 403.7, 198.9, 985.7, 170.0, 801.4, 645.4, 999.8, 798.0, 66.5, 332.6, 965.5, 305.6, 505.5, 905.5, 476.8, 757.8, 1282.6, 593.6, 591.3], [465.5, 313.7, 0.0, 537.9, 471.2, 685.5, 304.2, 492.5, 552.9, 690.9, 489.1, 378.2, 62.8, 656.6, 111.4, 196.6, 597.0, 168.3, 449.2, 971.3, 727.8, 410.5], [678.0, 403.7, 537.9, 0.0, 560.8, 585.2, 242.9, 942.5, 244.9, 894.6, 812.9, 467.7, 535.3, 848.1, 529.8, 646.6, 634.7, 375.9, 555.1, 882.0, 196.8, 290.1], [931.9, 198.9, 471.2, 560.8, 0.0, 1143.9, 330.1, 784.6, 803.5, 1158.0, 956.1, 150.5, 490.8, 1123.6, 463.7, 663.7, 1063.6, 634.9, 915.9, 1440.7, 751.7, 848.7], [384.5, 985.7, 685.5, 585.2, 1143.9, 0.0, 825.3, 865.5, 346.9, 600.0, 518.3, 1050.1, 663.8, 384.6, 793.3, 639.0, 91.5, 535.9, 335.0, 297.2, 557.2, 319.7], [747.6, 170.0, 304.2, 242.9, 330.1, 825.3, 0.0, 790.6, 484.5, 963.6, 787.3, 232.8, 321.9, 917.0, 294.9, 494.8, 771.8, 332.4, 624.0, 1121.7, 432.7, 423.8], [491.3, 801.4, 492.5, 942.5, 784.6, 865.5, 790.6, 0.0, 939.1, 524.7, 350.5, 866.1, 550.7, 698.9, 529.3, 330.3, 776.8, 631.1, 587.3, 1071.7, 1147.0, 726.6], [584.2, 645.4, 552.9, 244.9, 803.5, 346.9, 484.5, 939.1, 0.0, 806.0, 724.3, 709.7, 534.7, 658.1, 664.3, 646.0, 403.0, 375.4, 468.0, 650.3, 216.9, 227.2], [225.3, 999.8, 690.9, 894.6, 1158.0, 600.0, 963.6, 524.7, 806.0, 0.0, 206.5, 1064.9, 749.5, 316.5, 801.4, 501.4, 511.8, 640.3, 348.4, 758.5, 1010.3, 607.8], [144.1, 798.0, 489.1, 812.9, 956.1, 518.3, 787.3, 350.5, 724.3, 206.5, 0.0, 862.6, 547.2, 351.3, 599.1, 299.1, 429.8, 558.3, 266.4, 724.8, 928.4, 525.9], [
    838.8, 66.5, 378.2, 467.7, 150.5, 1050.1, 232.8, 866.1, 709.7, 1064.9, 862.6, 0.0, 397.1, 1029.9, 370.0, 569.9, 969.9, 541.2, 822.2, 1347.0, 658.0, 655.7], [523.4, 332.6, 62.8, 535.3, 490.8, 663.8, 321.9, 550.7, 534.7, 749.5, 547.2, 397.1, 0.0, 714.5, 152.5, 254.6, 575.4, 146.7, 427.6, 949.7, 739.2, 388.9], [197.2, 965.5, 656.6, 848.1, 1123.6, 384.6, 917.0, 698.9, 658.1, 316.5, 351.3, 1029.9, 714.5, 0.0, 765.3, 504.5, 297.7, 593.6, 301.7, 466.3, 864.7, 561.1], [575.3, 305.6, 111.4, 529.8, 463.7, 793.3, 294.9, 529.3, 664.3, 801.4, 599.1, 370.0, 152.5, 765.3, 0.0, 305.6, 704.7, 276.0, 575.1, 1079.1, 719.9, 518.3], [314.5, 505.5, 196.6, 646.6, 663.7, 639.0, 494.8, 330.3, 646.0, 501.4, 299.1, 569.9, 254.6, 504.5, 305.6, 0.0, 550.8, 333.4, 314.6, 860.0, 849.3, 429.0], [296.0, 905.5, 597.0, 634.7, 1063.6, 91.5, 771.8, 776.8, 403.0, 511.8, 429.8, 969.9, 575.4, 297.7, 704.7, 550.8, 0.0, 447.2, 246.4, 376.8, 607.2, 265.0], [424.5, 476.8, 168.3, 375.9, 634.9, 535.9, 332.4, 631.1, 375.4, 640.3, 558.3, 541.2, 146.7, 593.6, 276.0, 333.4, 447.2, 0.0, 299.8, 821.9, 569.6, 230.2], [132.6, 757.8, 449.2, 555.1, 915.9, 335.0, 624.0, 587.3, 468.0, 348.4, 266.4, 822.2, 427.6, 301.7, 575.1, 314.6, 246.4, 299.8, 0.0, 543.8, 672.9, 268.0], [590.9, 1282.6, 971.3, 882.0, 1440.7, 297.2, 1121.7, 1071.7, 650.3, 758.5, 724.8, 1347.0, 949.7, 466.3, 1079.1, 860.0, 376.8, 821.9, 543.8, 0.0, 853.8, 616.3], [794.5, 593.6, 727.8, 196.8, 751.7, 557.2, 432.7, 1147.0, 216.9, 1010.3, 928.4, 658.0, 739.2, 864.7, 719.9, 849.3, 607.2, 569.6, 672.9, 853.8, 0.0, 431.2], [392.0, 591.3, 410.5, 290.1, 848.7, 319.7, 423.8, 726.6, 227.2, 607.8, 525.9, 655.7, 388.9, 561.1, 518.3, 429.0, 265.0, 230.2, 268.0, 616.3, 431.2, 0.0]]

# fonctions de base
def creer_individu():
    l = len(Matrice_adj)
    return random.sample(range(l), k=l)


def creer_population(n):
    return [creer_individu() for i in range(n)]


def distance(ville1, ville2):
    ville1, ville2 = int(ville1), int(ville2)
    return Matrice_adj[ville1][ville2]

# distance total du trajet
def fitness(individu):
    individu1 = individu+[individu[0]]
    s = 0
    for i in range(len(individu1)-1):
        s += distance(individu1[i], individu1[i+1])
    return s

# opérateurs génétiques
def selection(population):
    population_s = sorted([(fitness(population[i]), i)
                          for i in range(len(population))])
    return [population[p[1]] for p in population_s[:2]]

# fusion de deux trajets
def cross_over(population):
    population1 = population[0]
    taille_pop = len(population1)
    moitie = taille_pop//2
    population1_2 = population1[moitie:]
    for i in range(1, len(population)):
        population2_2 = population[i][moitie:]
        population1_1 = population1[:moitie]
        for k in range(len(population2_2)):
            if population2_2[k] not in population1_1:
                population1_1 += [population2_2[k]]
            else:
                i = 0
                while population1_2[i] in population1_1:
                    i += 1
                population1_1 += [population1_2[i]]
        population.append(population1_1)


def mutation(population):
    for i in range(len(population)):
        individu = population[i]
        gene_aletoire1 = randint(0, len(individu)-1)
        gene_aletoire2 = randint(0, len(individu)-1)
        individu[gene_aletoire1], individu[gene_aletoire2] = individu[gene_aletoire2], individu[gene_aletoire1]
        population[i] = individu


# fonction génétique
test = []


def genetique():
    n = 16 # nombre d'individus
    population = creer_population(n)
    meilleur = (fitness(population[0]), population[0])
    population_copie = []
    distance_min = meilleur[0]
    stop = 0
    population = selection(population_copie+population)
    while stop < 200:
        meilleur1 = (fitness(population[0]), [i for i in population[0]])
        population_copie = [[i for i in population[0]]]
        if meilleur1[0] < meilleur[0]:
            meilleur = meilleur1
        cross_over(population)
        mutation(population)
        population = selection(population_copie+population)
        distance_min1 = fitness(population[0])
        if distance_min1 == distance_min:
            stop += 1
        else:
            distance_min = distance_min1
            stop = 0
    test.append(meilleur)


for i in range(200):
    genetique()

# Affichage des résultats
# Iterations
n = 200
iterations = [i for i in range(n)]
fig, ax1 = plt.subplots()
distances = [test[i][0] for i in range(n)]
plt.plot(iterations, distances)
plt.xlabel('Itérations')
plt.ylabel('Distance totale en km')
plt.plot(iterations, distances, 'bo-')
ax1.set_ylim([2000, max(distances)+2000])
ax1.set_xlabel('iterations', fontweight='bold')
ax1.set_ylabel('Distance totale en km', fontweight='bold')
plt.show()

# Meilleur trajet
meilleur = min(test)
o = meilleur[1][0]
meilleur_trajet = meilleur[1]+[o]

print("distance total du plus court trajet : ", meilleur[0])

X1 = [X[int(i)] for i in meilleur_trajet]
Y1 = [Y[int(i)] for i in meilleur_trajet]
for i in range(len(X)):
    plt.annotate(villes[i], (X[i], Y[i]))
plt.plot(X1, Y1, 'ro-')
plt.title("Le plus court trajet")
plt.ylabel("Ordonnés")
plt.xlabel("Abscisses")
plt.plot(X[0], Y[0], 'go')
plt.show()
