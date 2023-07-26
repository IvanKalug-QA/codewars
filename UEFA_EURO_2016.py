# DESCRIPTION:
# Finish the uefaEuro2016() function so it return string just like in the examples below:
#
# uefa_euro_2016(['Germany', 'Ukraine'],[2, 0]) # "At match Germany - Ukraine, Germany won!"
# uefa_euro_2016(['Belgium', 'Italy'],[0, 2]) # "At match Belgium - Italy, Italy won!"
# uefa_euro_2016(['Portugal', 'Iceland'],[1, 1]) # "At match Portugal - Iceland, teams played draw."

def uefa_euro_2016(teams, scores):
    t1,t2 = teams
    s1,s2 = scores
    if s1 > s2:
        return f'At match {t1} - {t2}, {t1} won!'
    if s1 < s2:
        return f"At match {t1} - {t2}, {t2} won!"
    return f'At match {t1} - {t2}, teams played draw.'