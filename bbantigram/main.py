import bbantigram.helpers as helpers
from copy import deepcopy
import pandas as pd
 
#constants
DOUBLE_DOSE = [('C', 'c'), ('E', 'e'), ('Fya', 'Fyb'), ('Jka', 'Jkb'), ('M', 'N'), ('S', 's')]
SCREEN_CELL_SIZE = 3
PANEL_SIZE = 11
ANTIGENS = ['D', 'C', 'E', 'c', 'e', 'f', 'Cw', 'V', 'K', 'k', 'Kpa', 'Kpb', 'Jsa', 'Jsb', 'Fya', 'Fyb', 'Jka', 'Jkb', 'P1', 'Lua', 'Lub', 'M', 'N', 'S', 's', 'Lea', 'Leb']
STRENGHTS = ['0', 'w', '1+', '2+', '3+', '4+']

# variable definitions
cross_count = {'D': 0, 'C': 0, 'E': 0, 'c': 0, 'e': 0, 'f': 0, 'Cw': 0, 'V': 0, 'K': 0, 'k': 0, 'Kpa': 0, 'Kpb': 0, 'Jsa': 0, 'Jsb': 0, 'Fya': 0, 'Fyb': 0, 'Jka': 0, 'Jkb': 0, 'P1': 0, 'Lua': 0, 'Lub': 0, 'M': 0, 'N': 0, 'S': 0, 's': 0, 'Lea': 0, 'Leb': 0}
ab_to_eliminate = deepcopy(ANTIGENS)
panel = [[0] * len(ANTIGENS)] * PANEL_SIZE
panel_results = ['3+', '3+', '0', '0', '0', '1+', '0', '1+', '3+', '1+', '0']
autocontrol = None

# checks if antigen is heterozygous or homozygous
def is_double_dose(antigen, row):
    for pair in DOUBLE_DOSE:
        if antigen in pair:
            if pair[0] == antigen:
                other = pair[1]
            else:
                other = pair[1]
            break
    i1 = ANTIGENS.index[antigen]
    i2 = ANTIGENS.index[other]

    global panel
    if panel[row][i1] == '+' and panel[row][i2] == '+':
        return True
    return False
    
        

def initialize_panel():
    df = pd.read_excel("Panel1.xlsx")
    print(df)
    global panel 
    panel = [[str(x) for x in l] for l in df.to_numpy()]
    print(panel)

def rule_out():
    # for each donor cell
    for i in range(PANEL_SIZE):
        # only check for antigens to rule out for cells with negative reaction
        if panel_results[i] == '0':
            # for each antigen
            for j in range(len(ANTIGENS)):
                antigen = ANTIGENS[j]
                # only consider antigens not ruled out yet and not present in double dose 
                if antigen in ab_to_eliminate and (antigen not in DOUBLE_DOSE or not is_double_dose(antigen, i)):
                    if panel[i][j] == '+':
                        cross_count[antigen] += 1
                        if cross_count[antigen] >= 2:
                            ab_to_eliminate.remove(antigen)
    print(cross_count)
    print(ab_to_eliminate)


def find_best_fit():
    return

def main():
    initialize_panel()
    print(panel)
    rule_out()
    return 

if __name__ == "__main__":
    main()
